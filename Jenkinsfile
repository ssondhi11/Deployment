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
        CONTAINER_NAME = 'nginx'
        CONTAINER_PORT = '80'
        PVC_VOLUME = '1Gi'
    }

    stages {
        stage('Generate Kubernetes YAML') {
            steps {
                script {
                    // Use Jinja or any templating engine to generate Kubernetes YAML
                    bat 'python generate_k8s_yaml.py'
                }
            }
        }
    }
}
