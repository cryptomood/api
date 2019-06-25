package main

import (
	types "../.."
	"fmt"
	"github.com/golang/protobuf/ptypes/empty"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"time"
)

const CertFile = "./cert.pem"
const Server = "SERVER"

func main() {
	creds, err := credentials.NewClientTLSFromFile(CertFile, "")
	if err != nil {
		panic(err)
	}
	conn, err := grpc.Dial(Server, grpc.WithDefaultCallOptions(grpc.MaxCallRecvMsgSize(20971520)), grpc.WithTransportCredentials(creds), grpc.WithTimeout(5*time.Second), grpc.WithBlock())
	if err != nil {
		panic(fmt.Sprintf("did not connect: %v", err))
	}
	fmt.Println("Connected")

	proxyClient := types.NewMessagesProxyClient(conn)
	sub, err := proxyClient.SubscribeArticle(context.Background(), &empty.Empty{})
	if err != nil {
		panic(err)
	}
	for {
		msg, _ := sub.Recv()
		fmt.Println(msg)
	}
}
