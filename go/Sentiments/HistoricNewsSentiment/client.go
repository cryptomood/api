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

const CertFile = "../../../certs/cert.pem"
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

	historicClient := types.NewSentimentsClient(conn)

	// create time frame
	now := time.Now()
	twoHoursAgo := now.Add(-2 * time.Hour)
	timestampNow, _ := ptypes.TimestampProto(now)
	timestamp2HAgo, _ := ptypes.TimestampProto(twoHoursAgo)

	historicRequest := &types.SentimentHistoricRequest{From: timestamp2HAgo, To: timestampNow, Resolution: "M1", Asset: "BTC"}
	sub, err := historicClient.HistoricNewsSentiment(context.Background(), historicRequest)
	if err != nil {
		panic(err)
	}
	for {
		candle, err := sub.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			panic(err)
		}

		fmt.Println(candle)
	}
}
