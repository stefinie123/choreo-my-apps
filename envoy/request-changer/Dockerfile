FROM envoyproxy/envoy:v1.30-latest
COPY envoy.yaml /etc/envoy/envoy.yaml
USER 10014
CMD /usr/local/bin/envoy -c /etc/envoy/envoy.yaml
