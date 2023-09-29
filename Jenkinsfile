pipeline {
    agent any

    parameters {
        string(name: 'DEPLOYMENT_NAME', description: 'Deployment Name')
        string(name: 'REPLICA_COUNT', description: 'Number of Replicas')
        string(name: 'APP_NAME', description: 'Application Name')
        string(name: 'CONTAINER_NAME', description: 'Container Name')
        string(name: 'DOCKER_IMAGE', description: 'Container Image Name')
        string(name: 'IMAGE_TAG', description: 'Container Image Tag')
        string(name: 'CONTAINER_PORT', description: 'Container Port')
        string(name: 'CPU_LIMIT', description: 'CPU Limit')
        string(name: 'MEMORY_LIMIT', description: 'Memory Limit')
        string(name: 'ENV_VARIABLE_NAME', description: 'Environment Variable Name')
        string(name: 'ENV_VARIABLE_VALUE', description: 'Environment Variable Value')
    }

    stages {
        stage('Generate Kubernetes YAML') {
            steps {
                script {
                    // Use Jinja or any templating engine to generate Kubernetes YAML
                
                    bat "python generate_k8s_yaml.py" 
                }
            }
        }
    }
}
