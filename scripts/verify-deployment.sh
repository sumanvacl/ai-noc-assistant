#!/usr/bin/env bash

set -euo pipefail

echo "======================================"
echo "Stargate AI/NOC Deployment Verification"
echo "======================================"

echo
echo "[1] Operating System"
cat /etc/os-release | grep PRETTY_NAME || true

echo
echo "[2] Docker"
docker --version

echo
echo "[3] Ollama"
ollama --version

echo
echo "[4] Ollama Service"
systemctl is-active ollama

echo
echo "[5] Ollama API"
curl -fsS http://127.0.0.1:11434/api/tags

echo
echo
echo "[6] Ollama Models"
ollama list

echo
echo "[7] Open WebUI Container"

docker inspect open-webui \
    --format \
    'Image={{.Config.Image}}
Status={{.State.Status}}
Restart={{.HostConfig.RestartPolicy.Name}}'

echo
echo "[8] Open WebUI Image"

docker image inspect stargate-open-webui:latest \
    --format \
    'Image={{.RepoTags}}
ID={{.Id}}'

echo
echo "[9] Open WebUI HTTP"

curl -I --max-time 10 \
    http://127.0.0.1:8080

echo
echo "[10] Container Network Utilities"

docker exec open-webui \
    which ping

docker exec open-webui \
    which traceroute

docker exec open-webui \
    which nslookup

echo
echo "======================================"
echo "Deployment verification completed."
echo "======================================"