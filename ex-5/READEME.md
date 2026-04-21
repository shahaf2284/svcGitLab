# Nexus3 Private Docker Registry – Steps 5–8

## Overview

In this section, we set up a **private Docker registry** using Nexus Repository Manager 3.  
This allows us to store and manage Docker images in a centralized and persistent way instead of keeping them only locally.

---

## What is Nexus?

**Nexus Repository Manager 3 (Nexus3)** is a tool used to manage and store artifacts such as:

- Docker images
- Maven dependencies
- npm packages

In this task, Nexus is used as a **Private Docker Registry**, which means:

- We can push Docker images to it
- Other machines/services can pull images from it
- We can manage versions and repositories centrally

---

## What is a Docker Volume?

A **Docker Volume** is used to persist data outside the container.

Without a volume:

- All data inside the container is lost when it is removed ❌

With a volume:

- Data is stored persistently and survives container restarts/deletions ✔️

Nexus stores all its important data in: /nexus-data: 

Therefore, attaching a volume is critical.

---

## Step 5 – Run Nexus3 Container (Basic Run)

### Goal

Start Nexus3 using Docker.

### Command

```bash
docker run -d --name nexus3 -p 8081:8081 -p 8082:8082 sonatype/nexus3  
```

Explanation

- -d → Run in background
- --name nexus3 → Container name
- -p 8081:8081 → Web UI access
- -p 8082:8082 → Docker registry port
sonatype/nexus3 → Nexus image from Docker Hub



####Notes: 

- Docker will automatically pull the image if it does not exist locally.
- Nexus may take 1–2 minutes to fully start.

#### Verify container is running:

```bash
docker ps
```

#### Check logs (optional):

```bash
docker logs -f nexus3
```

## Step 6 – Add Volume for Persistent Data

Goal - Ensure Nexus data is saved permanently.
Important Note
Volumes cannot be added to an existing container. Therefore, we must:

1.  Stop the container
2.  Remove the container
3.  Re-run it with a volume

#### Stop the container and remove it

```bash
docker stop nexus3
docker rm nexus3
```

- No need to remove the Docker image.

#### Run Nexus again WITH a volume

```bash
docker run -d --name nexus3 -p 8081:8081 -p 8082:8082 -v nexus-data:/nexus-data sonatype/nexus3
```

Explanation
- -v nexus-data:/nexus-data → attaches a persistent volume

#### Verify volume exists

```bash
docker volume ls
```

## Step 7 – Login to Nexus Admin Panel

Goal - Access Nexus Web UI.

#### Open in browser [ http://localhost:8081 ] 

```bash
docker exec nexus3 cat /nexus-data/admin.password 
```

get the password from the nexus3 image first time

|    Default login          |
|---------------------------|
|    Username: admin        |
|    Get initial password   |

Change the admin password
Complete initial setup

## Step 8 – Create Docker Repository

Goal - Create a private Docker repository inside Nexus.

Steps 
1. Go to: Settings → Repositories
2. Click: Create repository
3. Select: docker (hosted)

Configuration
  Name: my-private-hub
  HTTP Port: 8082
  
#### Why this is important
    This repository will act as your private Docker registry.


#### Pushing Docker Image to Nexus

Check if the web work on port 8082 docker connected to nexus
    
    curl -v http://localhost:8082/v2/

After creating the repository, push your image.
    
    docker login localhost:8082

Push image and change tag befor 

    docker tag python_health_check:v0.1 localhost:8082/python_health_check:v0.1
    docker push localhost:8082/python_health_check:v0.1


## Step 9 - 11

remove the continer and image

    docker rm localhost:8082/python_health_check:v0.1
    docker rmi localhost:8082/python_health_check:v0.1

then need to run the image from the nexus 

    docker run -d -p 5000:5000 --name python-health-from-nexus localhost:8082/my-private-hub/python_health_check:v0.1

