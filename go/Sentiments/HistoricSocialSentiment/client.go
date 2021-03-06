package main

import (
	"fmt"
	"io"
	"time"

	types "../.."
	"github.com/golang/protobuf/ptypes"
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

	historicClient := types.NewSentimentsClient(conn)

	// create time frame
	now := time.Now()
	twoDaysAgo := now.Add(-48 * time.Hour)
	timestampNow, _ := ptypes.TimestampProto(now.Add(-4 * time.Hour))
	timestamp2DAgo, _ := ptypes.TimestampProto(twoDaysAgo)

	historicRequest := &types.SentimentHistoricRequest{From: timestamp2DAgo, To: timestampNow, Resolution: "D1", Asset: "BTC"}
	sub, err := historicClient.HistoricSocialSentiment(context.Background(), historicRequest)
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
