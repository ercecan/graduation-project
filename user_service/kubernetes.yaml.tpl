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
  type: LoadBalancer
  selector:
    app: user
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-configmap
data:
  RABBITMQ_HOST: rabbitmq
  REDIS_HOST: redis

---

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: grad-ingress
  annotations:
    kubernetes.io/ingress.global-static-ip-name: user-svc-static
  labels:
    app: user
spec:
  defaultBackend:
    service:
      name: user
      port:
        number: 8000