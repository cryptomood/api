package main

import (
	types "../.."
	"fmt"
	"github.com/golang/protobuf/ptypes"
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
	conn, err := grpc.Dial(Server,grpc.WithTransportCredentials(creds), grpc.WithTimeout(15*time.Second), grpc.WithBlock())
	if err != nil {
		panic(fmt.Sprintf("did not connect: %v", err))
	}
	fmt.Println("Connected")

	historicClient := types.NewHistoricDataClient(conn)

	// create time frame
	now := time.Now()
	twoHoursAgo := now.Add(-2 * time.Hour)
	timestampNow, _ := ptypes.TimestampProto(now)
	timestamp2HAgo, _ := ptypes.TimestampProto(twoHoursAgo)

	historicRequest := &types.HistoricRequest{From: timestamp2HAgo, To: timestampNow, Filter: &types.AssetsFilter{Assets: []string{"BTC"}, AllAssets: false}}
	sub, err := historicClient.HistoricTransactions(context.Background(), historicRequest)
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
