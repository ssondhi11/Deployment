pipeline {
    agent any

    parameters {
        string(name: 'DEPLOYMENT_NAME', defaultValue: 'nginx-deployment', description: 'Deployment Name')
        string(name: 'REPLICA_COUNT', defaultValue: '3', description: 'Number of Replicas')
        string(name: 'APP_NAME', defaultValue: 'web', description: 'Application Name')
        string(name: 'CONTAINER_NAME', defaultValue: 'nginx', description: 'Container Name')
        string(name: 'IMAGE_NAME', defaultValue: 'nginx', description: 'Container Image Name')
        string(name: 'IMAGE_TAG', defaultValue: 'latest', description: 'Container Image Tag')
        string(name: 'CONTAINER_PORT', defaultValue: '80', description: 'Container Port')
        string(name: 'ENV_VARIABLE_NAME', defaultValue: 'version', description: 'Environment Variable Name')
        string(name: 'ENV_VARIABLE_VALUE', defaultValue: '1.0', description: 'Environment Variable Value')
    }

    stages {
        stage('Generate Kubernetes YAML') {
            steps {
                script {
                    // Use Jinja or any templating engine to generate Kubernetes YAML
                    def deployment_name = params.DEPLOYMENT_NAME
                    bat "python generate_k8s_yaml.py --deployment-name ${deployment_name}"
                }
            }
        }
    }
}
