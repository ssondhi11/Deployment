import jinja2

# Define your template file (deployment-template.yaml)
template_file = 'deployment-template.yaml'

# Load the template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(template_file)

# Define variables from Jenkins environment


# Render the template with variables
rendered_template = template.render(
    DEPLOYMENT_NAME=deployment_name,
    REPLICAS=replica_count,
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


