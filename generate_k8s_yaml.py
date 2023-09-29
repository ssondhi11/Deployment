import jinja2

# Define your template file (deployment-template.yaml)
template_file = 'deployment-template.yaml'

# Load the template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(template_file)

# Define variables from Jenkins environment
deployment_name = "${DEPLOYMENT_NAME}"
docker_image = "nginx"
env_variable = "Version"
env_value = "1.0"
cpu_limit = "0.5"
memory_limit = "256Mi"
replicas = "3"
docker_args = "app_version"
container_name = "nginx"
container_port = "80"
pvc_volume = "1Gi"

# Render the template with variables
rendered_template = template.render(
    DEPLOYMENT_NAME=deployment_name,
    DOCKER_IMAGE=docker_image,
    ENV_VARIABLE=env_variable,
    CPU_LIMIT=cpu_limit,
    MEMORY_LIMIT=memory_limit,
    REPLICAS=replicas,
    DOCKER_ARGS=docker_args,
    CONTAINER_NAME=container_name,
    CONTAINER_PORT=container_port,
    PVC_VOLUME=pvc_volume,
)

# Write the rendered template to deployment.yaml
with open('k8s-deployment.yaml', 'w') as deployment_file:
    deployment_file.write(rendered_template)


