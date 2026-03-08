# 🚀 Enterprise CI/CD Pipeline: Python Logistics API

[![CI/CD Pipeline](https://github.com/Parthyyyy/logistics-python-cicd/actions/workflows/ci.yml/badge.svg)](https://github.com/Parthyyyy/logistics-python-cicd/actions)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-blue)

## 📋 Project Overview
This project demonstrates a modern, fully automated DevOps lifecycle for a Python-based Logistics microservice. It features a robust REST API built with FastAPI, containerized using Docker, and deployed to a Kubernetes cluster. 

The core of this project is the **GitHub Actions CI/CD pipeline**, which strictly enforces code quality, runs automated tests, builds the artifact, and delivers it to a global container registry upon every commit.

## 🏗️ Architecture & CI/CD Flow

1. **Local Development:** Python 3.12 + FastAPI + Pytest.
2. **Continuous Integration (CI):** GitHub Actions triggers on push/PR, sets up the environment, and runs `pytest`. Code cannot be merged if tests fail.
3. **Continuous Delivery (CD):** Upon successful tests, GitHub Actions builds a multi-stage Docker image and pushes it to Docker Hub.
4. **Deployment:** Kubernetes pulls the latest image and deploys it across highly available, self-healing Pods exposed via a LoadBalancer.

*(Note to self: Add an Architecture Diagram image here using Draw.io or Excalidraw!)*

## 🛡️ Enterprise DevOps Practices Implemented

* **Automated Testing Gates:** Pipeline strictly blocks unverified code from reaching the registry.
* **Minimal Base Images:** Utilized `python:3.12-slim` to significantly reduce the container footprint and attack surface.
* **Non-Root Containers:** Configured Dockerfile to run the application as a non-root user (`myuser`) for enhanced security.
* **High Availability & Self-Healing:** Kubernetes `Deployment` configured with multiple replicas and Liveness/Readiness probes (`/health`) to automatically restart crashed containers.
* **Secrets Management:** Docker Hub credentials managed securely via GitHub Secrets.

## 🚀 How to Run Locally

### 1. Run via Docker
```bash
docker run -d -p 8000:8000 parth1717/logistics-app:latest