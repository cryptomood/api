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

func main() {
	creds, err := credentials.NewClientTLSFromFile(CertFile, "")
	if err != nil {
		panic(err)
	}
	conn, err := grpc.Dial(Server, grpc.WithTransportCredentials(creds), grpc.WithTimeout(5*time.Second), grpc.WithBlock())
	if err != nil {
		panic(fmt.Sprintf("did not connect: %v", err))
	}
	fmt.Println("Connected")

	proxyClient := types.NewMessagesProxyClient(conn)

	filter := &types.AssetsFilter{Assets: []string{"BTC", "ETH"}, AllAssets: false}
	sub, err := proxyClient.SubscribeTelegram(context.Background(), filter)
	if err != nil {
		panic(err)
	}
	for {
		msg, err := sub.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			panic(err)
		}
		fmt.Println(msg)
	}
}
