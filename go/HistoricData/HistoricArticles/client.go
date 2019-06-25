package main

import (
	types "../.."
	"fmt"
	"github.com/golang/protobuf/ptypes/timestamp"
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

	historicClient := types.NewHistoricDataClient(conn)
	historicRequest := &types.HistoricRequest{From: &timestamp.Timestamp{Seconds: 1561400800}, To: &timestamp.Timestamp{Seconds: 1561428800}}
	sub, err := historicClient.HistoricArticles(context.Background(), historicRequest)
	if err != nil {
		panic(err)
	}
	fmt.Println(len(sub.Items))
}
