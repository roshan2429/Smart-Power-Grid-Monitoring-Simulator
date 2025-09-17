# Smart Power Grid Monitoring Simulator

A full-stack simulator for real-time power grid monitoring, built with Python, MQTT, Docker, Kubernetes, and Grafana.

## Overview
This project simulates a distributed power grid monitoring system using virtual sensors. It collects, visualizes, and analyzes grid data in real-time.
- Sensors publish data via **MQTT**
- Collector service gathers data and stores it
- **Grafana** dashboards visualize load, outages, and anomalies
- Designed with **fault detection and recovery** inspired by real-world power system protection engineering
- Fully deployable with **Docker Compose** or **Kubernetes**

## Features
- Simulated distributed sensors with configurable frequency and parameters  
- Real-time load visualization and outage detection  
- Alerting for anomalies and failures  
- Scalable deployment using Docker and Kubernetes  
- Technical manual and operator guide included for reproducibility

## Setup Instructions

### Option 1: Using Docker Compose
1. Navigate to the project root:
   ```bash
   cd smart-grid-monitoring-complete
   ```
2. Start all services:
   ```bash
   docker-compose up --build
   ```
3. Access Grafana dashboards at `http://localhost:3000`  
   - Default login: `admin` / `admin`

### Option 2: Using Kubernetes
1. Apply all Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/namespace.yaml
   kubectl apply -f k8s/
   ```
2. Port-forward Grafana and MQTT services for local access:
   ```bash
   kubectl port-forward svc/grafana 3000:3000
   kubectl port-forward svc/mosquitto 1883:1883
   ```
3. Access Grafana at `http://localhost:3000`

## Project Structure

```
smart-grid-monitoring-complete/
│
├── broker/                 # MQTT broker Docker setup
├── collector/              # Data collector service
├── dashboards/             # Grafana dashboard JSON
├── k8s/                    # Kubernetes manifests
├── sensors/                # Sensor simulation scripts
├── README.md
```

## Usage
1. Start either **Docker Compose** or **Kubernetes** deployment  
2. Sensors publish simulated power readings  
3. Collector gathers data, Grafana visualizes load, outages, and anomalies  
4. Monitor and analyze the simulated grid in real-time

## Technologies
- **Programming & Simulation**: Python, MQTT  
- **Visualization**: Grafana, JSON dashboards  
- **Deployment**: Docker, Docker Compose, Kubernetes  
- **Cloud-Native Concepts**: Namespaces, ConfigMaps, Services

## Author
Roshan Hyalij  
MS in Computer Science (2025)

