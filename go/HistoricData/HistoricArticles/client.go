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

	historicClient := types.NewHistoricDataClient(conn)

	// create time frame
	now := time.Now()
	twoHoursAgo := now.Add(-2 * time.Hour)
	timestampNow, _ := ptypes.TimestampProto(now)
	timestamp2HAgo, _ := ptypes.TimestampProto(twoHoursAgo)

	historicRequest := &types.HistoricRequest{From: timestamp2HAgo, To: timestampNow, Filter: &types.AssetsFilter{Assets: []string{"BTC", "ETH"}, AllAssets: false}}
	sub, err := historicClient.HistoricArticles(context.Background(), historicRequest)
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
