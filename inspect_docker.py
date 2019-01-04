import docker


client = docker.from_env()

print(client.containers.run("ubuntu:16.04", "echo hello world"))
print(client.containers.list())
print(client.images.list())
