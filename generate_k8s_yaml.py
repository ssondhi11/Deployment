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
    deployment_name=deployment_name,
    replica_count=replica_count,
    app_name=app_name,
    container_name=container_name,
    docker_image=docker_image,
    image_tag=image_tag,
    container_port=container_port,
    cpu_limit=cpu_limit,
    memory_limit=memory_limit,
    env_variable_name=env_variable_name,
    env_variable_value=env_variable_value,
)

# Write the rendered template to deployment.yaml
with open('k8s-deployment.yaml', 'w') as deployment_file:
    deployment_file.write(rendered_template)


