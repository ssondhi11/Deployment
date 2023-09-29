import jinja2

# Define your template file (deployment-template.yaml)
template_file = 'deployment-template.yaml'

# Load the template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(template_file)

# Define variables from Jenkins environment
docker_image = "${DOCKER_IMAGE}"
env_variable = "${ENV_VARIABLE}"
env_value = "${ENV_VALUE}"
cpu_limit = "${CPU_LIMIT}"
memory_limit = "${MEMORY_LIMIT}"
replicas = "${REPLICAS}"
docker_args = "${DOCKER_ARGS}"
container_port = "${CONTAINER_PORT}"
pvc_volume = "${PVC_VOLUME}"

# Render the template with variables
rendered_template = template.render(
    DOCKER_IMAGE=docker_image,
    ENV_VARIABLE=env_variable,
    CPU_LIMIT=cpu_limit,
    MEMORY_LIMIT=memory_limit,
    REPLICAS=replicas,
    DOCKER_ARGS=docker_args,
    CONTAINER_PORT=container_port,
    PVC_VOLUME=pvc_volume,
)

# Write the rendered template to deployment.yaml
with open('k8s-deployment.yaml', 'w') as deployment_file:
    deployment_file.write(rendered_template)


