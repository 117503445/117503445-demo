package main

import (
	"math/rand"
	"time"

	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

func main() {

	cfg := zap.NewProductionConfig()
	cfg.OutputPaths = []string{
		"./log.jsonl",
	}

	logger, _ := cfg.Build(zap.AddStacktrace(zapcore.DebugLevel))

	defer logger.Sync() // flushes buffer, if any

	for {
		logger.Info("get rand number",
			zap.Int("rand", rand.Intn(100)),
		)
		time.Sleep(time.Second)
	}

}
