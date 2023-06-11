apiVersion: apps/v1
kind: Deployment
metadata:
  name: recommendation
  labels:
    app: recommendation
spec:
  replicas: 1
  selector:
    matchLabels:
      app: recommendation
  template:
    metadata:
      labels:
        app: recommendation
    spec:
      nodeSelector:
        cloud.google.com/gke-nodepool: "production-pool"
      containers:
        - name: recommendation
          image: europe-west3-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/grad/recommendation:COMMIT_SHA
          env:
          ports:
            - containerPort: 8002
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              cpu: "2000m"
              memory: "4Gi"

---
apiVersion: v1
kind: Service
metadata:
  name: recommendation
spec:
  type: LoadBalancer
  selector:
    app: recommendation
  ports:
    - protocol: TCP
      port: 8002
      targetPort: 8002

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: recommendation-configmap
data:
  RABBITMQ_HOST: rabbitmq
  REDIS_HOST: redis