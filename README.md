# Airflow instalation

## Prerequisites

Before proceeding, ensure the following requirements are met:

- Docker and Docker Compose are installed on your system. If not, follow the installation guides for [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).
- Docker is configured with at least 4 GB of memory. Adjust your Docker settings to allocate more memory, if necessary.

## Quick Start

Follow these steps for a quick setup:

1. **Download the `docker-compose.yaml` File**

   Fetch the official Docker Compose file from the Airflow documentation:

   ```bash
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'

2. **Create Directories for DAGs, Logs, and Plugins**
   ```bash
   mkdir -p ./dags ./logs ./plugins

3. **Set the AIRFLOW_UID Environment Variable**
   ```bash
   echo -e "AIRFLOW_UID=$(id -u)" > .env

4. **Initialize the Database and Start Services**

   Before using Apache Airflow, initialize its database and start all required services:
  
   ```bash
   docker-compose up airflow-init
   docker-compose up

5. **Accessing the Web Interface**

   - **Username:** airflow
   - **Password:** airflow

