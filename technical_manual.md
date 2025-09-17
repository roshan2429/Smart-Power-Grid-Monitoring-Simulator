# Technical Manual - Smart Power Grid Monitoring Simulator

## Overview
This manual explains the architecture, components, and working of the Smart Power Grid Monitoring Simulator. It is intended for developers, engineers, and users who want to deploy or extend the system.

## Project Objective
Simulate a **real-time distributed power grid monitoring system** to visualize load, detect outages, and analyze anomalies using virtual sensors.

## Components

### 1. Sensors
- Simulate power readings (voltage, current, load) across a distributed grid.
- Publish data via **MQTT** topics.
- Configurable frequency and parameters for realistic simulation.

### 2. MQTT Broker
- Handles communication between sensors and collector.
- Supports multiple subscribers for scalability.

### 3. Collector Service
- Subscribes to MQTT topics to receive sensor data.
- Processes and stores readings.
- Provides endpoints for Grafana dashboards to query metrics.

### 4. Dashboards
- Grafana dashboards visualize:
  - Real-time load and power consumption
  - Outage detection
  - Anomaly alerts
- Configurable alerts for threshold breaches.

### 5. Deployment
- Docker Compose and Kubernetes manifests are provided.
- Services are containerized for reproducible and scalable deployments.

## Architecture Diagram
```
[ Sensors ] ---> MQTT Broker ---> Collector ---> Grafana Dashboards
```

## Data Flow
1. Sensors generate and publish readings to MQTT Broker.
2. Collector subscribes, processes, and stores data.
3. Grafana queries the collector to render dashboards and alerts.


## Configuration
- Adjust sensor parameters in `sensors/sensor_simulator.py`.
- Configure MQTT topics in `broker/docker-compose.yml`.
- Update Grafana dashboard JSONs in `dashboards/`.

## Fault Detection & Recovery
- Detect abnormal sensor readings or missing data.
- Generate alerts in Grafana for anomalies.
- Collector automatically reconnects to MQTT broker if disconnected.



