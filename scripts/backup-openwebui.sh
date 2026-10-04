#!/usr/bin/env bash

set -euo pipefail

BACKUP_DIR="${BACKUP_DIR:-/root/openwebui-backup}"
CONTAINER="${CONTAINER:-open-webui}"
VOLUME="${VOLUME:-open-webui-data}"

DATE="$(date +%Y%m%d-%H%M%S)"
DEST="${BACKUP_DIR}/${DATE}"

echo "======================================"
echo "Stargate Open WebUI Backup"
echo "======================================"

mkdir -p "$DEST"

echo "[1/5] Checking container..."
docker inspect "$CONTAINER" >/dev/null

echo "[2/5] Backing up Open WebUI volume..."

docker run --rm \
    -v "${VOLUME}:/data:ro" \
    -v "${DEST}:/backup" \
    alpine \
    tar czf /backup/openwebui-data.tar.gz -C /data .

echo "[3/5] Saving container configuration..."

docker inspect "$CONTAINER" \
    > "${DEST}/docker-inspect.json"

echo "[4/5] Saving image information..."

docker inspect stargate-open-webui:latest \
    > "${DEST}/image-inspect.json"

docker image ls \
    > "${DEST}/docker-images.txt"

echo "[5/5] Creating checksums..."

cd "$DEST"

sha256sum * > SHA256SUMS

echo
echo "Backup completed:"
echo "$DEST"
echo
echo "Files:"
ls -lh "$DEST"