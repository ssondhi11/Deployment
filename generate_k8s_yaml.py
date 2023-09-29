import jinja2

# Define your template file (deployment-template.yaml)
template_file = 'deployment-template.yaml'

# Load the template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(template_file)

# Define variables from Jenkins environment
deployment_name = "nginx-deployment"
replica_count = "3"
app_name = "web"
container_name = "nginx"
docker_image = "nginx"
image_tag = "latest"
container_port =  "80"
cpu_limit = "0.5"
memory_limit = "256Mi"
env_variable_name = "version"
env_variable_value = "1.0"

# Render the template with variables
rendered_template = template.render(
    DEPLOYMENT_NAME=deployment_name,
    REPLICA_COUNT=replica_count,
    APP_NAME=app_name,
    CONTAINER_NAME=container_name,
    DOCKER_IMAGE=docker_image,
    IMAGE_TAG=image_tag,
    CONTAINER_PORT=container_port,
    CPU_LIMIT=cpu_limit,
    MEMORY_LIMIT=memory_limit,
    ENV_VARIABLE_NAME=env_variable_name,
    ENV_VARIABLE_VALUE=env_variable_value,
)

# Write the rendered template to deployment.yaml
with open('k8s-deployment.yaml', 'w') as deployment_file:
    deployment_file.write(rendered_template)


