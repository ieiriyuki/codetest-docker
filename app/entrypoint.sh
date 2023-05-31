#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Number of workers is necessary"
    exit 1
fi

N_WORKER=$1

uvicorn main:app \
    --host 0.0.0.0 \
    --port $PORT \
    --workers $N_WORKER
