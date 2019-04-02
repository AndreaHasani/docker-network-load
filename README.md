# Toxiyproxy example setup with docker containers

Here's a simple example on getting toxiproxy working with docker containers.

## Description 
Toxiproxy is a framework for simulating network conditions. It's made specifically to work in testing, CI and development environments, supporting deterministic tampering with connections, but with support for randomized chaos and customization. Toxiproxy is the tool you need to prove with tests that your application doesn't have single points of failure. 

## Usage

- docker-compose up (on the folder which has docker-compose.yml
- attach to docker-container reciver
- docker attach (container id)
- Run main.py
- Use taxiproxy cli to create proxy and add toxic (read more about toxiproxy commands with --help)


## Toxiproxy cli commands|

**You can download toxiproxy-cli from /Shopify/toxiproxy/releases**

- add proxy -> toxiproxy-cli create inui_api -l 0.0.0.0:22222 -u appsender:5000
- add lentacy -> ./toxiproxy-cli toxic add inui_api -t latency -a latency=5000
- remove lentacy -> ./toxiproxy-cli toxic d inui_api -n latency_downstream  
