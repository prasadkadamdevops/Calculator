# Calculator
this is calculator app using andriod

#Projct structure


calculator_app/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── docker-compose.yml          # optional: local compose
└── k8s/
    ├── namespace.yaml
    ├── deployment.yaml
    ├── service.yaml
    └── ingress.yaml            # optional - if you have an ingress controller

#🧑‍💼 DevOps responsibility-


| File / Folder         | Purpose                                                         | Owner      |
| --------------------- | --------------------------------------------------------------- | ---------- |
| `Dockerfile`          | Containerizes the app; defines build and runtime environment    | **DevOps** |
| `docker-compose.yml`  | Local orchestration/testing (optional but common for DevOps)    | **DevOps** |
| `k8s/namespace.yaml`  | Creates Kubernetes namespace for app isolation                  | **DevOps** |
| `k8s/deployment.yaml` | Defines pod spec, replicas, and container image                 | **DevOps** |
| `k8s/service.yaml`    | Exposes the deployment as a service (ClusterIP, NodePort, etc.) | **DevOps** |
| `k8s/ingress.yaml`    | (Optional) Provides external access through Ingress             | **DevOps** |
