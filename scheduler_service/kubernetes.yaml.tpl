apiVersion: apps/v1
kind: Deployment
metadata:
  name: scheduler
  labels:
    app: scheduler
spec:
  replicas: 1
  selector:
    matchLabels:
      app: scheduler
  template:
    metadata:
      labels:
        app: scheduler
    spec:
      nodeSelector:
        cloud.google.com/gke-nodepool: "default-pool"
      containers:
        - name: scheduler
          image: europe-west3-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/grad/scheduler:COMMIT_SHA

---
apiVersion: v1
kind: Service
metadata:
  name: scheduler
spec:
  type: LoadBalancer
  selector:
    app: scheduler

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: scheduler-configmap
data:
  RABBITMQ_HOST: rabbitmq
  REDIS_HOST: redis