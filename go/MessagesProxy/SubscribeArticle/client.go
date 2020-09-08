package main

import (
	"fmt"
	"io"
	"time"

	types "../.."
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

const CertFile = "../../../certs/cert.pem"
const Server = "apiv1.cryptomood.com:443"
const Token = "" // put your token here (if you don't have token please visit https://cryptomood.com/business/products/sentiment-analysis-api/

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
	if Token == "" {
		panic("You need to set Token. To obtain your token visit https://cryptomood.com/business/products/sentiment-analysis-api/.")
	}
	creds, err := credentials.NewClientTLSFromFile(CertFile, "")
	if err != nil {
		panic(err)
	}
	conn, err := grpc.Dial(Server, grpc.WithTransportCredentials(creds), grpc.WithPerRPCCredentials(tokenAuth{Token}), grpc.WithTimeout(5*time.Second), grpc.WithBlock())
	if err != nil {
		panic(fmt.Sprintf("did not connect: %v", err))
	}
	fmt.Println("Connected")

	proxyClient := types.NewMessagesProxyClient(conn)

	filter := &types.AssetsFilter{Assets: []string{"BTC", "ETH"}, AllAssets: false}
	sub, err := proxyClient.SubscribeArticle(context.Background(), filter)
	if err != nil {
		panic(err)
	}
	for {
		article, err := sub.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			panic(err)
		}
		fmt.Println(article)
	}
}
