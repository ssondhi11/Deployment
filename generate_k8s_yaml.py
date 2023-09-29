import jinja2

# Define your template file (deployment-template.yaml)
template_file = 'deployment-template.yaml'

# Load the template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(template_file)

# Define variables from Jenkins environment
import sys

# Check if the script received the expected number of arguments
if len(sys.argv) != 15:
    print("Usage: generate_k8s_yaml.py --deployment_name <name> --replica_count <count> --app-name <name> --container_name <name> --docker_image <image> --image_tag <tag> --container_port <port> --env_variable_name <name> --env_variable_value <value>")
    sys.exit(1)

# Parse command-line arguments
args = sys.argv[1:]

# Define variables based on command-line arguments
deployment_name_index = args.index("--deployment_name")
deployment_name = args[deployment_name_index + 1]
replica_count_index = args.index("--replica_count")
replica_count = args[replica_count_index + 1]
app_name_index = args.index("--app-name")
app_name = args[app_name_index + 1]
container_name_index = args.index("--container_name")
container_name = args[container_name_index + 1]
docker_image_index = args.index("--docker_image")
docker_image = args[docker_image_index + 1]
image_tag_index = args.index("--image_tag")
image_tag = args[image_tag_index + 1]
container_port_index = args.index("--container_port")
container_port = args[container_port_index + 1]
env_variable_name_index = args.index("--env_variable_name")
env_variable_name = args[env_variable_name_index + 1]
env_variable_value_index = args.index("--env_variable_value")
env_variable_value = args[env_variable_value_index + 1]

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


