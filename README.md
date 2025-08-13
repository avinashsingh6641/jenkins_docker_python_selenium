docker pull jenkins/jenkins:lts
getent group docker
docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --user root --group-add 103 --name jenkins jenkins/jenkins:lts
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword 
docker exec -u 0 -it jenkins bash
docker exec -it jenkins bash
apt-get update && apt-get install -y docker.io
docker exec -it jenkins-docker sh



docker-compose up -d
docker compose down

[ Azure VM (host for Codespace) ]
    └─ [ Codespace container environment ]
          ├─ /workspaces/<repo>        <-- Your repo files
          ├─ /var/lib/docker/volumes/  <-- Docker named volumes (jenkins_home)
          ├─ Docker daemon (dockerd)
          │
          ├─ Jenkins container
          │     ├─ Mount: /var/jenkins_home -> jenkins_home volume
          │     ├─ Mount: /var/run/docker.sock -> Host Docker socket
          │     └─ Controls host Docker
          │
          ├─ Ephemeral Python test containers
          │     └─ Run from Jenkins, execute tests, then removed
          │
          └─ Port forwarding for Jenkins UI
