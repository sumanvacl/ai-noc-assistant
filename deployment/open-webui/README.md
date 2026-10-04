# Open WebUI Deployment

Open WebUI provides the web interface for the
Stargate AI/NOC Engineering Platform.

## Architecture

Open WebUI runs inside Docker.

Ollama runs directly on the Linux host.

```text
Docker Container
      |
      | HTTP
      v
host.docker.internal:11434
      |
      v
Ollama