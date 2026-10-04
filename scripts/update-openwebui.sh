#!/usr/bin/env bash

set -euo pipefail

IMAGE="stargate-open-webui:latest"
CONTAINER="open-webui"

echo "======================================"
echo "Stargate Open WebUI Update"
echo "======================================"

echo "[1] Current container configuration..."

docker inspect "$CONTAINER" \
    > "/root/openwebui-before-update-$(date +%Y%m%d-%H%M%S).json"

echo "[2] Current image:"
docker inspect "$IMAGE" \
    --format '{{.Id}}' || true

echo
echo "[3] Building updated image..."

docker build \
    -t "$IMAGE" \
    .

echo
echo "[4] New image:"
docker inspect "$IMAGE" \
    --format '{{.Id}}'

echo
echo "IMPORTANT:"
echo "The existing container has NOT been replaced."
echo
echo "Review the image and recreate the container manually"
echo "after confirming the new version."