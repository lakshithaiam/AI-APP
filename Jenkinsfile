pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.12-alpine
    command:
    - cat
    tty: true
  - name: sonar-scanner
    image: sonarsource/sonar-scanner-cli
    command:
    - cat
    tty: true
  - name: kubectl
    image: bitnami/kubectl:latest
    command:
    - cat
    tty: true
    securityContext:
      runAsUser: 0
      readOnlyRootFilesystem: false
    env:
    - name: KUBECONFIG
      value: /kube/config        
    volumeMounts:
    - name: kubeconfig-secret
      mountPath: /kube/config
      subPath: kubeconfig
  - name: dind
    image: docker:dind
    args: ["--registry-mirror=https://mirror.gcr.io", "--storage-driver=overlay2"]
    securityContext:
      privileged: true  # Needed to run Docker daemon
    env:
    - name: DOCKER_TLS_CERTDIR
      value: ""  # Disable TLS for simplicity
    volumeMounts:
    - name: docker-config
      mountPath: /etc/docker/daemon.json
      subPath: daemon.json  # Mount the file directly here
  volumes:
  - name: docker-config
    configMap:
      name: docker-daemon-config
  - name: kubeconfig-secret
    secret:
      secretName: kubeconfig-secret
'''
        }
    }
    
    
    stages {
        stage('Run Tests') {
            steps {
                container('python') {
                    sh '''
                        python -m venv venv
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install pytest pytest-cov
                        pytest my_tests.py --cov=. --cov-report=xml
                    '''
                }
            }
            
        }
        stage('SonarQube Analysis') {
            steps {
                container('sonar-scanner') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=my-python-project \
                          -Dsonar.host.url=http://my-sonarqube-sonarqube.sonarqube.svc.cluster.local:9000 \
                          -Dsonar.login=sqp_386737361b3175c17288b144365b494da11fbe34 \
                          -Dsonar.python.coverage.reportPaths=coverage.xml
                    '''
                }
            }
        }
        stage('Login to Docker Registry') {
            steps {
                container('dind') {
                    sh 'docker --version'
                    sh 'sleep 10'
                    sh 'docker login nexus-service-for-docker-hosted-registry.nexus.svc.cluster.local:8085 -u admin -p Changeme@2025'
                }
            }
        }
        stage('Build - Tag - Push') {
            steps {
                container('dind') {
                    sh 'docker build -t nexus-service-for-docker-hosted-registry.nexus.svc.cluster.local:8085/my-repository/my-new-ai-assistant:v3 .'
                    sh 'docker push nexus-service-for-docker-hosted-registry.nexus.svc.cluster.local:8085/my-repository/my-new-ai-assistant:v3'
                    sh 'docker pull nexus-service-for-docker-hosted-registry.nexus.svc.cluster.local:8085/my-repository/my-new-ai-assistant:v3'
                    sh 'docker image ls'
                }
            }
        }
        stage('Deploy AI Application') {
            steps {
                container('kubectl') {
                    script {
                        dir('ai-app-deployment') {
                            sh 'kubectl get node'
                            sh 'kubectl apply -f ai-assistant-deployment.yaml'
                            sh 'sleep 99999'
                        }
                    }
                }
            }
        }
    }
}
