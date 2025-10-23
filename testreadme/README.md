
# .NET Application – IMCC Kubernetes Deployment

This repository contains the **.NET application** containerized with **Docker** and deployed on the **IMCC Kubernetes cluster** through a fully automated **Jenkins CI/CD pipeline**.  
It demonstrates a complete end-to-end workflow — from code build to container deployment — following internal DevOps standards.

---
## Project Structure

```
.
├── app/
├── Dockerfile
├── Jenkinsfile
└── hello-dotnet-deployment/
    ├── hello-dotnet-deployment.yaml
    └── hello-dotnet-namespace.yaml
```

---
## Overview

| Component            | Description               |
| -------------------- | ------------------------- |
| **Language**         | .NET 8 (ASP.NET Core)     |
| **Orchestration**    | Kubernetes (IMCC Cluster) |
| **CI/CD**            | Jenkins Pipeline          |
| **Containerization** | Docker                    |
| **Namespace**        | `hello-dotnet`            |

---

## 🐳 Docker Build & Run

_(For local build and testing)_

### **Build Docker Image**

```bash
docker build -t hello-dotnet .
```

### **Run Container**

```bash
docker run -p 8083:8083 hello-dotnet
```

Access locally at:  
👉 **[http://localhost:8083](http://localhost:8083/)**

---

##  Kubernetes Deployment (IMCC Cluster)

### **Apply Manifests**

```bash
kubectl apply -f hello-dotnet-namespace.yaml
kubectl apply -f hello-dotnet-deployment.yaml
```

### **Verify Deployment**

```bash
kubectl get pods -n hello-dotnet
kubectl get svc -n hello-dotnet
```

### **Access Application (via Port Forward)**

```bash
kubectl port-forward svc/hello-dotnet-service 8083:8083 -n hello-dotnet
```

Then open:  
👉 **[http://localhost:8083](http://localhost:8083/)**

---

## 🧠 Jenkins CI/CD Pipeline

All build, quality analysis, and deployment stages are fully automated through **Jenkins**.

### **Pipeline Stages (Jenkinsfile)**

1. **Checkout Code**  
    Pulls the latest code from the Git repository.
    
2. **SonarQube Analysis**  
    Performs static code analysis and quality checks.
    
3. **Authenticate with Nexus Registry**  
    Logs into the **self-hosted Nexus Docker Registry**.
    
4. **Build and Tag Docker Image**  
    Builds the .NET Docker image using the provided `Dockerfile` and tags it for the registry.
    
5. **Push to Nexus Registry**  
    Publishes the built image to the internal **Nexus Docker Registry**.
    
6. **Deploy to IMCC Kubernetes Cluster**  
    Deploys the **hello-dotnet** application using manifests from the `hello-dotnet-deployment/` directory via `kubectl`.
    

---

**

# Express Application – IMCC Kubernetes Deployment

This repository contains the **express application** containerized with **Docker** and deployed on the **IMCC Kubernetes cluster** through a fully automated **Jenkins CI/CD pipeline**.
It demonstrates a complete end-to-end workflow — from code build to container deployment — following internal DevOps standards.

---
## Project Structure

```
.
├── app.js
├── package.json
├── Dockerfile
├── Jenkinsfile
└── hello-express-deployment/
	├── hello-express-deployment.yaml
	└── hello-express-namespace.yaml
```

---
## Overview

| Component | Description |
| -------------------- | ------------------------- |
| **Language** | Node.js 20 (Express) |
| **Orchestration** | Kubernetes (IMCC Cluster) |
| **CI/CD** | Jenkins Pipeline |
| **Containerization** | Docker |
| **Namespace** | `hello-express` |

---
## 🐳 Docker Build & Run

_(For local build and testing)_
### **Build Docker Image**

```bash
docker build -t hello-express .
```
### **Run Container**

```bash
docker run -p 3000:3000 hello-express
```

Access locally at:

👉 **[http://localhost:3000](http://localhost:3000/)**

---
## Kubernetes Deployment (IMCC Cluster)

### **Apply Manifests**

```bash
kubectl apply -f hello-express-namespace.yaml

kubectl apply -f hello-express-deployment.yaml
```

### **Verify Deployment**

```bash
kubectl get pods -n hello-express

kubectl get svc -n hello-express
```

### **Access Application (via Port Forward)**

```bash
kubectl port-forward svc/hello-express-service 3000:3000 -n hello-express
```

Then open:

👉 **[http://localhost:3000](http://localhost:3000/)**

---
## 🧠 Jenkins CI/CD Pipeline

All build, quality analysis, and deployment stages are fully automated through **Jenkins**.

### **Pipeline Stages (Jenkinsfile)**

1. **Checkout Code**
	Pulls the latest code from the Git repository.

2. **SonarQube Analysis**
	Performs static code analysis and quality checks.

3. **Authenticate with Nexus Registry**
	Logs into the **self-hosted Nexus Docker Registry**.

4. **Build and Tag Docker Image**
	Builds the express Docker image using the provided `Dockerfile` and tags it for the registry.

5. **Push to Nexus Registry**
	Publishes the built image to the internal **Nexus Docker Registry**.

6. **Deploy to IMCC Kubernetes Cluster**
	Deploys the **hello-express** application using manifests from the `hello-express-deployment/` directory via `kubectl`.

---

**
  
# Go Application – IMCC Kubernetes Deployment

This repository contains the **go application** containerized with **Docker** and deployed on the **IMCC Kubernetes cluster** through a fully automated **Jenkins CI/CD pipeline**.
It demonstrates a complete end-to-end workflow — from code build to container deployment — following internal DevOps standards.

---
## Project Structure

```
.
├── main.go
├── Dockerfile
├── Jenkinsfile
├── README.md
└── hello-go-deployment/
	├── hello-go-deployment.yaml
	└── hello-go-namespace.yaml
```

---
## Overview

| Component | Description |
| -------------------- | ------------------------- |
| **Language** | Go 1.21 |
| **Orchestration** | Kubernetes (IMCC Cluster) |
| **CI/CD** | Jenkins Pipeline |
| **Containerization** | Docker |
| **Namespace** | `hello-go` |

---
## 🐳 Docker Build & Run

_(For local build and testing)_
### **Build Docker Image**

```bash
docker build -t hello-go .
```
### **Run Container**

```bash
docker run -p 8099:8099 hello-go
```

Access locally at:

👉 **[http://localhost:8099](http://localhost:8099/)**

---
## Kubernetes Deployment (IMCC Cluster)

### **Apply Manifests**

```bash
kubectl apply -f hello-go-namespace.yaml

kubectl apply -f hello-go-deployment.yaml
```

### **Verify Deployment**

```bash
kubectl get pods -n hello-go

kubectl get svc -n hello-go
```

### **Access Application (via Port Forward)**

```bash
kubectl port-forward svc/hello-go-service 8099:8099 -n hello-go
```

Then open:

👉 **[http://localhost:8099](http://localhost:8099/)**

---
## 🧠 Jenkins CI/CD Pipeline

All build, quality analysis, and deployment stages are fully automated through **Jenkins**.
### **Pipeline Stages (Jenkinsfile)**

1. **Checkout Code**
	Pulls the latest code from the Git repository.

2. **SonarQube Analysis**
	Performs static code analysis and quality checks.

3. **Authenticate with Nexus Registry**
	Logs into the **self-hosted Nexus Docker Registry**.

4. **Build and Tag Docker Image**
	Builds the go Docker image using the provided `Dockerfile` and tags it for the registry.

5. **Push to Nexus Registry**	
	Publishes the built image to the internal **Nexus Docker Registry**.

6. **Deploy to IMCC Kubernetes Cluster**
	Deploys the **hello-go** application using manifests from the `hello-go-deployment/` directory via `kubectl`.

---

**
  
# Java Application – IMCC Kubernetes Deployment

This repository contains the **java application** containerized with **Docker** and deployed on the **IMCC Kubernetes cluster** through a fully automated **Jenkins CI/CD pipeline**.
It demonstrates a complete end-to-end workflow — from code build to container deployment — following internal DevOps standards.

---
## Project Structure

```
.
├── src/
├── target/
├── pom.xml
├── Dockerfile
├── Jenkinsfile
└── hello-java-deployment/
	├── hello-java-deployment.yaml
	└── hello-java-namespace.yaml
```

---
## Overview

| Component | Description |
| -------------------- | ------------------------- |
| **Language** | Java 17 (Spring Boot) |
| **Build Tool** | Maven (`pom.xml`) |
| **Orchestration** | Kubernetes (IMCC Cluster) |
| **CI/CD** | Jenkins Pipeline |
| **Containerization** | Docker |
| **Namespace** | `hello-java` |

---
## 🐳 Docker Build & Run

_(For local build and testing)_
### **Build Docker Image**

```bash
docker build -t hello-java .
```
### **Run Container**

```bash
docker run -p 8080:8080 hello-java
```

Access locally at:

👉 **[http://localhost:8080](http://localhost:8080/)**

---
## Kubernetes Deployment (IMCC Cluster)
### **Apply Manifests**

```bash
kubectl apply -f hello-java-namespace.yaml

kubectl apply -f hello-java-deployment.yaml
```

### **Verify Deployment**

```bash
kubectl get pods -n hello-java

kubectl get svc -n hello-java
```
### **Access Application (via Port Forward)**

```bash
kubectl port-forward svc/hello-java-service 8080:8080 -n hello-java
```

Then open:

👉 **[http://localhost:8080](http://localhost:8080/)**

---
## 🧠 Jenkins CI/CD Pipeline

All build, quality analysis, and deployment stages are fully automated through **Jenkins**.
### **Pipeline Stages (Jenkinsfile)**

1. **Checkout Code**
	Pulls the latest code from the Git repository.

2. **SonarQube Analysis**
	Performs static code analysis and quality checks.

3. **Authenticate with Nexus Registry**
	Logs into the **self-hosted Nexus Docker Registry**.

4. **Build and Tag Docker Image**
	Builds the java Docker image using the provided `Dockerfile` and tags it for the registry.

5. **Push to Nexus Registry**
	Publishes the built image to the internal **Nexus Docker Registry**.

6. **Deploy to IMCC Kubernetes Cluster**
	Deploys the **hello-java** application using manifests from the `hello-java-deployment/` directory via `kubectl`.

  
---
**

# PHP Application – IMCC Kubernetes Deployment

This repository contains the **PHP application** containerized with **Docker** and deployed on the **IMCC Kubernetes cluster** through a fully automated **Jenkins CI/CD pipeline**.  
It demonstrates a complete end-to-end workflow — from code build to container deployment — following internal DevOps standards.

---
## Project Structure

```
.
├── Dockerfile
├── index.php
├── Jenkinsfile
└── hello-php-deployment/
    ├── hello-php-deployment.yaml
    ├── hello-php-namespace.yaml
```

---
##  Overview

|Component|Description|
|---|---|
|**Language**|PHP 8.x|
|**Orchestration**|Kubernetes (IMCC Cluster)|
|**CI/CD**|Jenkins Pipeline|
|**Containerization**|Docker|
|**Namespace**|`hello-php`|

---
## 🐳 Docker Build & Run

_(For local build and testing)_

### **Build Docker Image**

```bash
docker build -t hello-php .
```

### **Run Container**

```bash
docker run -p 8000:8000 hello-php
```

Access locally at:  
👉 **[http://localhost:8000](http://localhost:8000/)**

---

##  Kubernetes Deployment (IMCC Cluster)

### **Apply Manifests**

```bash
kubectl apply -f hello-php-namespace.yaml
kubectl apply -f hello-php-deployment.yaml
```

### **Verify Deployment**

```bash
kubectl get pods -n hello-php
kubectl get svc -n hello-php
```

### **Access Application (via Port Forward)**

```bash
kubectl port-forward svc/hello-php-service 8000:8000 -n hello-php
```

Then open:  
👉 **[http://localhost:8000](http://localhost:8000/)**

---

## 🧠 Jenkins CI/CD Pipeline

All build, quality analysis, and deployment stages are fully automated through **Jenkins**.

### **Pipeline Stages (Jenkinsfile)**

1. **Checkout Code**  
    Pulls the latest code from the Git repository.
    
2. **SonarQube Analysis**  
    Performs static code analysis and quality checks.
    
3. **Authenticate with Nexus Registry**  
    Logs into the **self-hosted Nexus Docker Registry**.
    
4. **Build and Tag Docker Image**  
    Builds the PHP Docker image using the provided `Dockerfile` and tags it for the registry.
    
5. **Push to Nexus Registry**  
    Publishes the built image to the internal **Nexus Docker Registry**.
    
6. **Deploy to IMCC Kubernetes Cluster**  
    Deploys the **hello-php** application using manifests from the `hello-php-deployment/` directory via `kubectl`.
    

---

**
  
# Ai-app Application – IMCC Kubernetes Deployment

This repository contains the **ai-app application** containerized with **Docker** and deployed on the **IMCC Kubernetes cluster** through a fully automated **Jenkins CI/CD pipeline**.
It demonstrates a complete end-to-end workflow — from code build to container deployment — following internal DevOps standards.

---
## Project Structure

```
.
├── main.py
├── Dockerfile
├── requirements.txt
├── Jenkinsfile
└── ai-app-deployment/
	├── ai-assistant-deployment.yaml
	└── ai-app-namespace.yaml
```

---
## Overview

| Component | Description |
| -------------------- | ----------------------------- |
| **Language** | Python 3.11 (Flask / FastAPI) |
| **Orchestration** | Kubernetes (IMCC Cluster) |
| **CI/CD** | Jenkins Pipeline |
| **Containerization** | Docker |
| **Namespace** | `ai-ns` |

---
## 🐳 Docker Build & Run

_(For local build and testing)_
### **Build Docker Image**

```bash
docker build -t ai-app .
```
### **Run Container**

```bash
docker run -p 8501:8501 ai-app
```

Access locally at:

👉 **[http://localhost:8501](http://localhost:8501/)**

---
## Kubernetes Deployment (IMCC Cluster)

### **Apply Manifests**

```bash
kubectl apply -f ai-app-namespace.yaml

kubectl apply -f ai-assistant-deployment.yaml
```

### **Verify Deployment**

```bash
kubectl get pods -n ai-app

kubectl get svc -n ai-app
```

### **Access Application (via Port Forward)**


```bash
kubectl port-forward svc/ai-app-service 8501:8501 -n ai-app
```

Then open:

👉 **[http://localhost:8501](http://localhost:8501/)**

---
## 🧠 Jenkins CI/CD Pipeline

All build, quality analysis, and deployment stages are fully automated through **Jenkins**.
### **Pipeline Stages (Jenkinsfile)**

1. **Checkout Code**

Pulls the latest code from the Git repository.

2. **SonarQube Analysis**

Performs static code analysis and quality checks.

3. **Authenticate with Nexus Registry**

Logs into the **self-hosted Nexus Docker Registry**.

4. **Build and Tag Docker Image**

Builds the ai-app Docker image using the provided `Dockerfile` and tags it for the registry.

5. **Push to Nexus Registry**

Publishes the built image to the internal **Nexus Docker Registry**.

6. **Deploy to IMCC Kubernetes Cluster**

Deploys the **ai-app** application using manifests from the `ai-app-deployment/` directory via `kubectl`.

---
******************************
## AI Assistant

**AI Assistant** is a generative AI project built using **Langchain**. It provides a variety of features to assist users in various tasks, including chatbot interactions, text translation, code assistance, grammar checking and exam tutoring. The assistant leverages state-of-the-art AI models to deliver intelligent and helpful responses in each of these areas.

## Features

1. **Chatbot**

Engage in interactive conversations with the AI to answer questions, provide recommendations, or have casual discussions.

  
2. **Text Translator**

Translate text between multiple languages seamlessly.

3. **Code Assistant**

Get help with coding tasks, including writing, debugging, and explaining code in various programming languages.

4. **Grammar Check**

Analyze and improve your text by identifying and correcting grammar, spelling, and punctuation errors.

5. **Exam Tutor**

Prepare for exams with personalized tutoring. The AI can help you with practice questions, explanations, and study strategies.

## Technologies Used

- **Python**: Core programming language for the application.

- **Langchain**: Framework for building applications with large language models (LLMs), enabling reasoning, memory, and tool integration.

- **Langsmith**: Platform for debugging, testing, monitoring, and improving LLM-powered applications.

- **Streamlit**: Framework for deploying the web application.

## How to Deploy

- Clone the repository by the following command: `git clone https://github.com/pratyush770/AI_Assistant.git`

- Create a **virtual environment** (venv) first and install all the packages using `pip install requirements.txt`.

- Create your **GroqCloud** account by visiting the following link: https://console.groq.com

- Click on the **API Keys** section and generate an API key by giving a name to it.

- Create a secret_key.py file and add `sec_key = "Your generated secret key"`.

- Create your **Langsmith** account by visiting the following link: https://www.langchain.com/langsmith

- Click on the **Settings** section and generate an API key by giving a description to it.

- In the secret_key.py add `langsmith_sec_key = "Your generated secret key"`.

- Create a github repository and make sure to add **secret_key.py** in .gitignore for security reasons.

- Create your **Streamlit** account by visiting the following link: https://streamlit.io/cloud

- Click on **Create app** button on the top right and then select **Deploy a public app from Github**.

- Select your **created repository, branch, main file path** and give **app url** if needed.

- Click on the **Advanced settings** and add the following configurations.

- `GROQ_API_KEY = "Your groqcloud secret key"`

- `LANGCHAIN_API_KEY = "Your langsmith secret key"`

- Click on the **Deploy** button and you're done!

## Deployment

The application is deployed on **Streamlit** and is accessible via the following link:

[Live Demo] https://ai-assistant-python.streamlit.app/

**
  
# Ruby Application – IMCC Kubernetes Deployment


This repository contains the **ruby application** containerized with **Docker** and deployed on the **IMCC Kubernetes cluster** through a fully automated **Jenkins CI/CD pipeline**.
It demonstrates a complete end-to-end workflow — from code build to container deployment — following internal DevOps standards.

---
## Project Structure

```
.
├── app.rb
├── Gemfile
├── Dockerfile
├── Jenkinsfile
└── hello-ruby-deployment/
	├── hello-ruby-deployment.yaml
	└── hello-ruby-namespace.yaml
```

---
## Overview

| Component | Description |
| -------------------- | ------------------------- |
| **Language** | Ruby 3.x (Sinatra) |
| **Orchestration** | Kubernetes (IMCC Cluster) |
| **CI/CD** | Jenkins Pipeline |
| **Containerization** | Docker |
| **Namespace** | `hello-ruby` |

---
## 🐳 Docker Build & Run

_(For local build and testing)_
### **Build Docker Image**

```bash
docker build -t hello-ruby .
```
### **Run Container**

```bash
docker run -p 4567:4567 hello-ruby
```

Access locally at:

👉 **[http://localhost:4567](http://localhost:4567/)**

---
## Kubernetes Deployment (IMCC Cluster)

### **Apply Manifests**

```bash
kubectl apply -f hello-ruby-namespace.yaml

kubectl apply -f hello-ruby-deployment.yaml
```

### **Verify Deployment**


```bash
kubectl get pods -n hello-ruby

kubectl get svc -n hello-ruby
```

### **Access Application (via Port Forward)**

```bash
kubectl port-forward svc/hello-ruby-service 4567:4567 -n hello-ruby
```

Then open:

👉 **[http://localhost:4567](http://localhost:4567/)**

---

## 🧠 Jenkins CI/CD Pipeline

All build, quality analysis, and deployment stages are fully automated through **Jenkins**.
### **Pipeline Stages (Jenkinsfile)**

1. **Checkout Code**
	Pulls the latest code from the Git repository.

2. **SonarQube Analysis**
	Performs static code analysis and quality checks.

3. **Authenticate with Nexus Registry**
	Logs into the **self-hosted Nexus Docker Registry**.

4. **Build and Tag Docker Image**
	Builds the ruby Docker image using the provided `Dockerfile` and tags it for the registry.

5. **Push to Nexus Registry**
	Publishes the built image to the internal **Nexus Docker Registry**.

6. **Deploy to IMCC Kubernetes Cluster**
	Deploys the **hello-ruby** application using manifests from the `hello-ruby-deployment/` directory via `kubectl`.

---
