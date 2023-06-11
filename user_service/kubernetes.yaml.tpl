apiVersion: apps/v1
kind: Deployment
metadata:
  name: user
  labels:
    app: user
spec:
  replicas: 1
  selector:
    matchLabels:
      app: user
  template:
    metadata:
      labels:
        app: user
    spec:
      nodeSelector:
        cloud.google.com/gke-nodepool: "default-pool"
      containers:
        - name: user
          image: europe-west3-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/grad/user:COMMIT_SHA
          env:
          ports:
            - containerPort: 8000

---
apiVersion: v1
kind: Service
metadata:
  name: user
spec:
  selector:
    app: user
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
  type: LoadBalancer
  loadBalancerIP: 34.107.96.1

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-configmap
data:
  RABBITMQ_HOST: rabbitmq
  REDIS_HOST: redis