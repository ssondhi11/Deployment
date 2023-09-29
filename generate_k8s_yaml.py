import jinja2

# Define your template file (deployment-template.yaml)
template_file = 'deployment-template.yaml'

# Load the template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(template_file)

# Define variables from Jenkins environment
import sys

# Check if the script received the expected number of arguments (14 including script name)
if len(sys.argv) != 15:
    print("Usage: generate_k8s_yaml.py --deployment_name <name> --replica_count <count> --app-name <name> --container_name <name> --docker_image <image> --image_tag <tag> --container_port <port> --env_variable_name <name> --env_variable_value <value>")
    sys.exit(1)

# Parse command-line arguments
args = sys.argv[1:]

# Define variables based on command-line arguments
deployment_name = args[args.index("--deployment_name") + 1]
replica_count = args[args.index("--replica_count") + 1]
app_name = args[args.index("--app-name") + 1]
container_name = args[args.index("--container_name") + 1]
docker_image = args[args.index("--docker_image") + 1]
image_tag = args[args.index("--image_tag") + 1]
container_port = args[args.index("--container_port") + 1]
env_variable_name = args[args.index("--env_variable_name") + 1]
env_variable_value = args[args.index("--env_variable_value") + 1]

# Use the variables in your script as needed
# ...

# Continue with your script logic


# Use the variables in your script as needed


# Render the template with variables
rendered_template = template.render(
    DEPLOYMENT_NAME=deployment_name,
    IMAGE_TAG=image_tag,
    DOCKER_IMAGE=docker_image,
    ENV_VARIABLE_NAME=env_variable_name,
    CPU_LIMIT=cpu_limit,
    MEMORY_LIMIT=memory_limit,
    REPLICAS=replica_count,
    DOCKER_ARGS=docker_args,
    CONTAINER_NAME=container_name,
    CONTAINER_PORT=container_port,
    PVC_VOLUME=pvc_volume,
)

# Write the rendered template to deployment.yaml
with open('k8s-deployment.yaml', 'w') as deployment_file:
    deployment_file.write(rendered_template)


