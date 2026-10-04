#!/usr/bin/env bash

set -u

echo "======================================"
echo "Stargate AI/NOC Health Check"
echo "======================================"

FAILED=0

check() {
    local NAME="$1"
    shift

    echo -n "[CHECK] $NAME ... "

    if "$@" >/dev/null 2>&1; then
        echo "OK"
    else
        echo "FAILED"
        FAILED=1
    fi
}

check "Docker" systemctl is-active --quiet docker
check "Ollama" systemctl is-active --quiet ollama

check "Ollama API" \
    curl -fsS http://127.0.0.1:11434/api/tags

check "Open WebUI container" \
    docker inspect open-webui

check "Open WebUI running" \
    docker inspect \
        --format '{{.State.Running}}' \
        open-webui

check "Open WebUI HTTP" \
    curl -fsS http://127.0.0.1:8080

check "Ollama model available" \
    ollama list

echo

if [ "$FAILED" -eq 0 ]; then
    echo "RESULT: HEALTHY"
    exit 0
else
    echo "RESULT: PROBLEMS DETECTED"
    exit 1
fi