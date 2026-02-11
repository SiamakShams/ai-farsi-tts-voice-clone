# Docker Setup Instructions for farsi-tts-voice-clone

This document provides complete instructions for setting up, using, and troubleshooting Docker for the farsi-tts-voice-clone project.

## Prerequisites
- Ensure that Docker is installed on your machine. You can download it from the [official Docker website](https://www.docker.com/get-started).
- Verify the installation by running:
  ```bash
  docker --version
  ```

## Docker Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/SiamakShams/farsi-tts-voice-clone.git
   cd farsi-tts-voice-clone
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t farsi-tts-voice-clone .
   ```

3. **Run the Docker container**:
   ```bash
   docker run -it --rm farsi-tts-voice-clone
   ```

## Commands
- To list running containers:
  ```bash
  docker ps
  ```
- To stop a running container:
  ```bash
  docker stop <container_id>
  ```
- To remove unused Docker images:
  ```bash
  docker image prune
  ```

## Troubleshooting
- **Common Issues**:
  - If you encounter a permissions error, ensure that you have adequate permissions for Docker.
  - If the container fails to start, check the logs by running:
    ```bash
    docker logs <container_id>
    ```

- **Rebuilding the Image**:
  If you make changes to the Dockerfile or the application code, rebuild the image with:
  ```bash
  docker build -t farsi-tts-voice-clone .
  ```

## Workflow Examples
### Example 1: Basic Usage
1. Build the image:
   ```bash
   docker build -t farsi-tts-voice-clone .
   ```
2. Run the container with mounted volume:
   ```bash
   docker run -it --rm -v $(pwd)/data:/app/data farsi-tts-voice-clone
   ```

### Example 2: Running with Environment Variables
   ```bash
   docker run -it --rm -e "ENV_VAR=value" farsi-tts-voice-clone
   ```

## Conclusion
For further details and updates, refer to the official GitHub repository [farsi-tts-voice-clone](https://github.com/SiamakShams/farsi-tts-voice-clone).  
