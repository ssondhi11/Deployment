import jinja2

# Define your template file (deployment-template.yaml)
template_file = 'deployment-template.yaml'

# Load the template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(template_file)



# Render the template with variables
rendered_template = template.render(
    DEPLOYMENT_NAME,
    REPLICA_COUNT,
    APP_NAME,
    CONTAINER_NAME,
    DOCKER_IMAGE,
    IMAGE_TAG,
    CONTAINER_PORT,
    CPU_LIMIT,
    MEMORY_LIMIT,
    ENV_VARIABLE_NAME,
    ENV_VARIABLE_VALUE,
)

# Write the rendered template to deployment.yaml
with open('k8s-deployment.yaml', 'w') as deployment_file:
    deployment_file.write(rendered_template)


