#!/usr/bin/env bash

set -euo pipefail

echo "======================================"
echo "Stargate Ollama Update Check"
echo "======================================"

echo
echo "Current Ollama version:"
ollama --version

echo
echo "Current models:"
ollama list

echo
echo "Ollama service:"
systemctl status ollama --no-pager

echo
echo "API status:"
curl -fsS http://127.0.0.1:11434/api/tags

echo
echo "======================================"
echo "Update check completed."
echo "======================================"
echo
echo "Review the official Ollama release"
echo "before performing a production upgrade."