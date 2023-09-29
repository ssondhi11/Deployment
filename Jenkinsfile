pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'nginx:latest'
        ENV_VARIABLE = 'Version'
        ENV_VALUE = '1.0'
        CPU_LIMIT = '0.5'
        MEMORY_LIMIT = '256Mi'
        REPLICAS = '3'
        DOCKER_ARGS = 'app_version'
        PORT_NUMBER = '80'
        PVC_VOLUME = '1Gi'
    }

    stages {
        stage('Generate Kubernetes YAML') {
            steps {
                script {
                    // Use Jinja or any templating engine to generate Kubernetes YAML
                    sh 'python generate_k8s_yaml.py'
                }
            }
        }

        stage('Apply Kubernetes Manifests') {
            steps {
                script {
                    // Apply the generated YAML files to your Kubernetes cluster
                    sh 'kubectl apply -f k8s-deployment.yaml -f k8s-service.yaml'
                }
            }
        }
    }
}
