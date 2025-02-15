pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: kubectl
    image: bitnami/kubectl:latest
    command:
    - cat
    tty: true
    securityContext:
      runAsUser: 1000
    volumeMounts:
    - name: kubeconfig-secret
      mountPath: /root/.kube
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
    environment {
        registryCredentials = "nexus-docker-creds"
        registry = "nexus-service-for-docker-hosted-registry.nexus-ns.svc.cluster.local:8085"
        KUBECONFIG_DATA = credentials('KUBECONFIG_DATA')
    }
    stages {
        stage('Configure Insecure Registry') {
            steps {
                container('dind') {
                    sh "whoami"
                }
            }
        }
        stage('Login to Docker Registry') {
            steps {
                container('dind') {
                    sh 'docker login nexus-service-for-docker-hosted-registry.nexus-ns.svc.cluster.local:8085 -u admin -p Devops@1252429'
                }
            }
        }
        stage('Build - Tag - Push') {
            steps {
                container('dind') {
                    sh 'docker build -t nexus-service-for-docker-hosted-registry.nexus-ns.svc.cluster.local:8085/my-new-ai-assistant .'
                    sh 'docker image ls'
                    sh 'docker push nexus-service-for-docker-hosted-registry.nexus-ns.svc.cluster.local:8085/my-new-ai-assistant'
                }
            }
        }
        stage('test kubectl') {
            steps {
                container('kubectl') {
                    sh 'pwd'
                    sh 'ls -a'
                    sh 'ls'
                    sh 'kubectl version'
                    sh 'kubectl cluster-info dump'
                    sh 'kubectl cluster-info'
                    sh 'kubectl get nodes'
                    sh 'kubectl create ns testthree'
                }
            }
        }
    }
}
