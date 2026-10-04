#!/usr/bin/env bash

set -euo pipefail

BACKUP="${1:-}"

CONTAINER="open-webui"
VOLUME="open-webui-data"

if [ -z "$BACKUP" ]; then
    echo "Usage:"
    echo
    echo "  $0 /path/to/backup-directory"
    echo
    exit 1
fi

if [ ! -f "$BACKUP/openwebui-data.tar.gz" ]; then
    echo "ERROR: Backup archive not found:"
    echo "$BACKUP/openwebui-data.tar.gz"
    exit 1
fi

echo "======================================"
echo "Stargate Open WebUI Restore"
echo "======================================"

echo
echo "WARNING:"
echo "This will replace the contents of:"
echo "$VOLUME"

read -r -p "Continue? Type RESTORE: " CONFIRM

if [ "$CONFIRM" != "RESTORE" ]; then
    echo "Restore cancelled."
    exit 1
fi

echo
echo "[1] Stopping Open WebUI..."

docker stop "$CONTAINER" 2>/dev/null || true

echo
echo "[2] Restoring volume..."

docker run --rm \
    -v "${VOLUME}:/data" \
    -v "${BACKUP}:/backup:ro" \
    alpine \
    sh -c 'rm -rf /data/* /data/.[!.]* /data/..?* 2>/dev/null || true;
           tar xzf /backup/openwebui-data.tar.gz -C /data'

echo
echo "[3] Starting Open WebUI..."

docker start "$CONTAINER"

echo
echo "[4] Checking container..."

docker ps \
    --filter "name=${CONTAINER}"

echo
echo "Restore completed."