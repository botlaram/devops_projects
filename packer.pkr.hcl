packer {
  required_plugins {
    docker = {
      version = ">= 1.7.0"
      source  = "github.com/hashicorp/docker"
    }
  }
}

source "docker" "ubuntu" {
  image  = "ubuntu:latest"
  commit = true
}

build {
  name    = "your-image"
  sources = ["source.docker.ubuntu"]

  provisioner "shell" {
    inline=[
      "apt-get update",
      "apt-get install -y python3",
      "apt-get install -y git",
      "apt-get autoremove -y",
      "apt-get clean -y",
      "rm -rf /var/lib/apt/lists/*"
    ]
  }

  post-processor "docker-tag" {
    repository = "imuser/packer"
    tag        = "latest"
  }
}
