FROM envoyproxy/envoy:v1.30-latest
RUN     apt update && apt install -y \
            luarocks
RUN    luarocks install lua-cjson
COPY envoy.yaml /etc/envoy/envoy.yaml
COPY lib /home/wso2/lib
USER 10014
CMD /usr/local/bin/envoy -c /etc/envoy/envoy.yaml
