import os
import shutil
import subprocess

# Define the paths and commands
frontend_repo_path = "/home/azureuser/expression_of_interest"
backend_repo_path = "/home/azureuser/EOI_Backend"
base_path = "/home/azureuser"
destination_path = "/var/www/html"
nginx_service_name = "nginx"
build_command = "npm run build"
install_command = "npm install"
dist_folder = os.path.join(frontend_repo_path, "dist")

# Function to run shell commands
def run_command(command, cwd=None):
    try:
        subprocess.run(command, check=True, shell=True, cwd=cwd)
        print(f"Command '{command}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute '{command}': {e}")

# Pull the latest code and stash any local changes
def update_code(repo_path):
    os.chdir(repo_path)
    run_command("git stash")
    run_command("git pull")

# Run npm install and build commands
def build_project(repo_path):
    run_command(install_command, cwd=repo_path)
    run_command(build_command, cwd=repo_path)

# Copy the contents of the dist folder to the destination path
def copy_dist(src_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
    print(f"Contents of {src_path} copied to {dest_path}.")

# Restart the Nginx service
def restart_service(service_name):
    run_command(f"sudo systemctl restart {service_name}")
    print(f"{service_name} service restarted.")

# Main function for the backend operations
def handle_backend():
    run_command("docker compose down", cwd=backend_repo_path)
    update_code(backend_repo_path)
    run_command("docker compose up -d --build", cwd=base_path)

# Main function
def main():
    update_code(frontend_repo_path)
    build_project(frontend_repo_path)
    copy_dist(dist_folder, destination_path)
    restart_service(nginx_service_name)
    handle_backend()

if __name__ == "__main__":
    main()
