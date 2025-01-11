import paramiko
import subprocess

# Define the new user details
NEW_USER = "newuser"
NEW_UID = 1001
NEW_GID = 1001
USER_PASSWORD = "securepassword"

# Define the containers and their SSH details
CONTAINERS = [
    {"name": "slurm-controller", "port": 2222},
    {"name": "slurm-node", "port": 2223},
    {"name": "slurm-node2", "port": 2224},
]


# Function to execute a command via SSH
def ssh_execute_command(host, port, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=port, username=username, password=password)

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        ssh.close()
        return output, error
    except Exception as e:
        return None, str(e)


# Add user to the container
def add_user_to_container(container_name, ssh_port):
    print(f"Adding user '{NEW_USER}' to container '{container_name}'...")
    command = (
        f"groupadd -g {NEW_GID} {NEW_USER} && "
        f"useradd -m -u {NEW_UID} -g {NEW_GID} {NEW_USER} && "
        f"echo '{NEW_USER}:{USER_PASSWORD}' | chpasswd"
    )
    output, error = ssh_execute_command(
        host="localhost",
        port=ssh_port,
        username="root",
        password="password",  # Replace with the root password of the container
        command=command,
    )
    if error:
        print(f"Error adding user to {container_name}: {error}")
    else:
        print(f"User added successfully to {container_name}. Output: {output}")


if __name__ == "__main__":
    # Add user to each container
    for container in CONTAINERS:
        add_user_to_container(container["name"], container["port"])
