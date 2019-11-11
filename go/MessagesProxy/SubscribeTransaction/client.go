package main

import (
	types "../.."
	"fmt"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"io"
	"time"
)

const CertFile = "./cert.pem"
const Server = "SERVER"

type tokenAuth struct {
	token string
}

func (t tokenAuth) GetRequestMetadata(ctx context.Context, in ...string) (map[string]string, error) {
	return map[string]string{
		"authorization": "Bearer " + t.token,
	}, nil
}

func (tokenAuth) RequireTransportSecurity() bool {
	return true
}

func main() {
	creds, err := credentials.NewClientTLSFromFile(CertFile, "")
	if err != nil {
		panic(err)
	}
	// in case you need token auth use command below
	// conn, err := grpc.Dial(Server, grpc.WithTransportCredentials(creds), grpc.WithPerRPCCredentials(tokenAuth{"YOUR_TOKEN"}), grpc.WithTimeout(5*time.Second), grpc.WithBlock())
	conn, err := grpc.Dial(Server, grpc.WithTransportCredentials(creds), grpc.WithTimeout(5*time.Second), grpc.WithBlock())
	if err != nil {
		panic(fmt.Sprintf("did not connect: %v", err))
	}
	fmt.Println("Connected")

	proxyClient := types.NewMessagesProxyClient(conn)

	filter := &types.AssetsFilter{Assets: []string{"BTC", "ETH"}, AllAssets: false}
	sub, err := proxyClient.SubscribeTransaction(context.Background(), filter)
	if err != nil {
		panic(err)
	}
	for {
		transaction, err := sub.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			panic(err)
		}
		fmt.Println(transaction)
	}
}
