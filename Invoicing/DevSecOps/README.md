# DevSecops

** Requried Tools in Master Server:- **
        OWASP       # dependency Check
        Trivy       # Image Scan
        Docker      # Contaier
        Jenkins     # CI/CD
        SonarQube   # Code Scan 
        GitHub/Git  # code

# Create a Ec2 

    sudo apt update -y
    sudo apt upgrade -y

# SonarQube Server installed

    docker run -itd --name sonarqube-server -p 9000:9000 sonarqube:lts-community

# Installed Trivy 

    sudo apt-get install wget apt-transport-https gnupg lsb-release
    wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null
    echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
    sudo apt-get update -y
    sudo apt-get install trivy -y
    sudo apt-get upgrade -y

# Trivy Commands:- 

    trivy image imagename

    trivy fs --security-checks vuln,config  Folder_name_OR_Path

    trivy image --severity HIGH,CRITICAL image_name

    trivy image -f json -o results.json image_name

    trivy repo repo-url

# Installed Jenkins 

     sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
     https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

    echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null

    sudo apt-get update -y
    sudo apt-get install fontconfig openjdk-17-jre -y
    sudo apt-get install jenkins -y
    sudo apt-get upgrade -y

# Plugins Installation :

    * SonarQube Scanner (Version 2.16.1)
    * Sonar Quality Gates(Version 1.3.1)
    * OWASP Dependency-Check (version 5.5.0)
    * Docker (Version 1.5)