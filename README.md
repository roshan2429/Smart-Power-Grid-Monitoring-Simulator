### Kubernetes Deployment (Minikube or any cluster)

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap-code.yaml
kubectl apply -f k8s/influxdb.yaml
kubectl apply -f k8s/mosquitto.yaml
kubectl apply -f k8s/grafana.yaml
kubectl apply -f k8s/collector.yaml
kubectl apply -f k8s/sensor.yaml
```

Access Grafana by port-forwarding:

```
kubectl -n smart-grid port-forward deploy/grafana 3000:3000
# then open http://localhost:3000 (admin/admin)
```
