### Build and Run

docker build -t envoy-lua . && docker run --rm --name envoy-lua -p 8000:8000 envoy-lua

### Curl

curl -v localhost:8000/multiple/lua/scripts
