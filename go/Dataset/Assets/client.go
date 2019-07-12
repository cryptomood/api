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
	conn, err := grpc.Dial(Server, grpc.WithTransportCredentials(creds), grpc.WithTimeout(5*time.Second), grpc.WithBlock())
	if err != nil {
		panic(fmt.Sprintf("did not connect: %v", err))
	}
	fmt.Println("Connected")

	datasetClient := types.NewDatasetClient(conn)
	assetItems, err := datasetClient.Assets(context.Background(), &empty.Empty{})
	if err != nil {
		panic(err)
	}

	fmt.Println(len(assetItems.Assets))
	for _, asset := range assetItems.Assets[0:19] {
		println(asset.Symbol)
	}
}
