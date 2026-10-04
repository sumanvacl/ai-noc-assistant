```dockerfile
FROM ghcr.io/open-webui/open-webui:main

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        iputils-ping \
        traceroute \
        dnsutils \
    && rm -rf /var/lib/apt/lists/*

USER root
