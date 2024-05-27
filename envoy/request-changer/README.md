### Build and Run

docker build -t envoy-req-changer . && docker run --rm --name envoy-req-changer -p 8000:8000 envoy-req-changer

### Curl

curl -v localhost:8000/multiple/lua/scripts

curl localhost:8000/2 -X POST -v

### Stop

docker kill envoy-req-changer


Right now this calls pipedream endpoint and gets the instructions to modify the upstream request.
(https://eosm2szibnsw86b.m.pipedream.net/extcall)

Inspect:
https://pipedream.com/@malithiim/projects/proj_24sAnZq/envoymediation-p_OKCQJ9R/inspect/2h1mRBg1EA7HvLdBzct2Ka2TBca