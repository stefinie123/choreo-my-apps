### Build and Run

docker build -t envoy-req-changer . && docker run --rm --name envoy-req-changer -p 8000:8000 envoy-req-changer

### Curl

curl -v localhost:8000/multiple/lua/scripts
