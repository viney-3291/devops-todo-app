# DevOps To-Do App — End-to-End CI/CD on AWS

[![CI Pipeline](https://github.com/viney-3291/devops-todo-app/actions/workflows/ci.yml/badge.svg)](https://github.com/viney-3291/devops-todo-app/actions/workflows/ci.yml)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-ECS%20%7C%20RDS%20%7C%20ALB-FF9900?logo=amazonaws&logoColor=white)

A production-style DevOps project demonstrating a complete CI/CD pipeline — from a Flask REST API to a fully automated deployment on AWS, provisioned entirely with Infrastructure as Code and monitored in real time.

This project was built to practice the full DevOps lifecycle hands-on: containerization, CI/CD automation, cloud infrastructure provisioning, and observability.

---

## Architecture

```
Developer
    │
    │ git push
    ▼
GitHub  ──────────────►  GitHub Actions (CI/CD)
                              │
                  ┌───────────┴───────────┐
                  │                       │
            Run pytest tests       Build Docker image
                  │                       │
                  └───────────┬───────────┘
                              ▼
                       Push to Amazon ECR
                              │
                              ▼
              ┌───────────────────────────────┐
              │           AWS (Terraform)      │
              │                                 │
              │   ALB → ECS Fargate → RDS       │
              │   (public URL)   (Flask app)  (PostgreSQL) │
              └───────────────────────────────┘
                              │
                              ▼
                Prometheus + Grafana (monitoring)
```

---

## Tech stack

| Layer | Technology |
|---|---|
| Application | Python, Flask, SQLAlchemy |
| Testing | pytest |
| Containerization | Docker, Docker Compose |
| Database | PostgreSQL |
| CI/CD | GitHub Actions |
| Container Registry | Amazon ECR |
| Infrastructure as Code | Terraform |
| Cloud Compute | AWS ECS Fargate |
| Managed Database | AWS RDS |
| Load Balancing | AWS Application Load Balancer |
| Monitoring | Prometheus, Grafana |

---

## Features

- REST API with full CRUD for task management
- Automated test suite run on every push
- Multi-stage CI/CD pipeline (test → build → push → deploy)
- Infrastructure fully defined as code — reproducible in one command
- Zero-downtime container orchestration via ECS Fargate
- Real-time metrics and dashboards via Prometheus/Grafana
- Database persistence via Docker volumes (local) and RDS (cloud)

---

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/tasks` | List all tasks |
| `POST` | `/tasks` | Create a new task |
| `DELETE` | `/tasks/<id>` | Delete a task by ID |
| `GET` | `/metrics` | Prometheus metrics endpoint |

---

## Running locally

**Prerequisites:** Docker Desktop, Python 3.11+

```bash
# Clone the repo
git clone https://github.com/viney-3291/devops-todo-app.git
cd devops-todo-app

# Run the full stack (Flask app + PostgreSQL) with Docker Compose
docker-compose up --build
```

The API will be available at `http://localhost:5000`.

```bash
# Test it
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn DevOps"}'

curl http://localhost:5000/tasks
```

### Run the test suite

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest test_app.py -v
```

---

## Deploying to AWS

Infrastructure is fully defined in `terraform/`. This provisions a VPC, ECS Fargate cluster, RDS PostgreSQL instance, and an Application Load Balancer.

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

On completion, Terraform outputs the public app URL:

```
app_url = "http://<your-alb-dns-name>"
```

To tear down all AWS resources and avoid ongoing charges:

```bash
terraform destroy
```

---

## CI/CD pipeline

Defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml). On every push to `main`:

1. **Test** — installs dependencies and runs the `pytest` suite
2. **Build & push** — builds the Docker image and pushes it to Amazon ECR (only if tests pass)

---

## Monitoring

Prometheus and Grafana run via `monitoring/docker-compose.monitoring.yml`, scraping metrics from the app's `/metrics` endpoint.

```bash
cd monitoring
docker-compose -f docker-compose.monitoring.yml up
```

- Prometheus UI: `http://localhost:9090`
- Grafana dashboards: `http://localhost:3000`

Tracked metrics: request count, request latency, and request rate per endpoint.

---

## Project structure

```
devops-todo-app/
├── app.py                          # Flask REST API with Prometheus metrics
├── test_app.py                     # pytest test suite
├── requirements.txt
├── Dockerfile
├── docker-compose.yml               # Local app + PostgreSQL
├── .github/workflows/ci.yml         # CI/CD pipeline
├── terraform/
│   ├── main.tf                      # AWS infrastructure
│   ├── variables.tf
│   └── outputs.tf
└── monitoring/
    ├── prometheus.yml
    └── docker-compose.monitoring.yml
```

---

## What this project demonstrates

- Writing and testing a REST API
- Containerizing applications with Docker
- Building multi-stage CI/CD pipelines
- Provisioning cloud infrastructure with Terraform (Infrastructure as Code)
- Deploying containerized applications on AWS ECS Fargate
- Managing secrets securely using GitHub Actions secrets and IAM
- Setting up application monitoring with Prometheus and Grafana

---

## Author

**Vinay** — [GitHub](https://github.com/viney-3291)
