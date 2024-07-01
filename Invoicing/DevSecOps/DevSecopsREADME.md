# DevSecOps Using Jenkins :
### Requried Tools in Master Server:- **
* OWASP       # dependency Check
* Trivy       # Image Scan
* Docker      # Contaier
* Jenkins     # CI/CD
* SonarQube   # Code Scan 
* GitHub/Git  # code

# Create a Ec2  
#####  https://aws.amazon.com

    sudo apt update -y
    sudo apt upgrade -y

# Installation Docker Engine
##### https://www.docker.com/

    sudo apt-get install docker, docker-compose -y
    docker --version
    docker-compose --version
    sudo systemctl status docker
    sudo chmod 777 /var/run/docker.sock
    sudo systemctl restart docker

# SonarQube Server installed
##### https://www.sonarsource.com/products/sonarqube/

    docker run -itd --name sonarqube-server -p 9000:9000 sonarqube:lts-community
#
1. After Configuration SonarQube Create jenkins-webhook, ex:- 
        http://localhost:8080/jenkins-webhook/      
2. Create secret for SonarQube Projects    



# Installed Trivy 
##### https://www.cyberithub.com/how-to-install-trivy-vulnerability-scanner-on-ubuntu-22-04/
#### 1.
    sudo apt-get install wget apt-transport-https gnupg lsb-release
    wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null
#### 2.
    echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
#### 3.
    sudo apt-get update -y
    sudo apt-get install trivy -y
    sudo apt-get upgrade -y
# Trivy Commands:- 
    trivy image imagename
####
    trivy fs --security-checks vuln,config  Folder_name_OR_Path
####
    trivy image --severity HIGH,CRITICAL image_name
####
    trivy image -f json -o results.json image_name
####
    trivy repo repo-url

# Installed Jenkins  
##### https://www.jenkins.io/
###### 1.
     sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
     https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
###### 2.
    echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null
###### 3.
    sudo apt-get update -y
    sudo apt-get install fontconfig openjdk-17-jre -y
    sudo apt-get install jenkins -y
    sudo apt-get upgrade -y
# Plugins Installation :
###### 4.
* SonarQube Scanner (Version 2.16.1)
* Sonar Quality Gates(Version 1.3.1)
* OWASP Dependency-Check (version 5.5.0)
* Docker (Version 1.5)

### To obtain an NVD API key, you need to register and request the key from the National Vulnerability Database (NVD). Here are the steps:

##### https://nvd.nist.gov/developers/request-an-api-key

1.  Visit the NVD API Key Request Page:
    Go to the NVD API Key Request Page.

2.  Fill Out the Request Form:
    Provide your email address and any other required information.

3.  Submit the Request:
    Click on the submit button to send your request.

4.  Receive the API Key:
    You will receive your NVD API key via email.

5.  Once you have the API key, you can add it to Jenkins as a credential and use it in your        pipeline script as shown earlier.

# To install OWASP ZAP (Zed Attack Proxy) on Ubuntu, follow these steps:
###### https://software.opensuse.org/download.html?project=home%3Acabelo&package=owasp-zap
###### https://www.zaproxy.org/download/
### 1. Install Java Development Kit (JDK):
##### OWASP ZAP requires Java to run. If you don't already have Java installed, you can install the default JDK package.

    sudo apt install default-jre -y
    sudo apt install snapd -y
    sudo snap install zaproxy --classic

### 2. For xUbuntu 23.04 run the following:

    echo 'deb http://download.opensuse.org/repositories/home:/cabelo/xUbuntu_23.04/ /' | sudo tee /etc/apt/sources.list.d/home:cabelo.list

    curl -fsSL https://download.opensuse.org/repositories/home:cabelo/xUbuntu_23.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_cabelo.gpg > /dev/null

    sudo apt update
    sudo apt install owasp-zap -y

## Please Configure all tools and Credentials in Jenkins which is required in to create Pipeline 


# Create CICD Pipeline
1. Create new project with pipeline option 
    
2. Configure Source 
3. Configure Build Triggers
4. Write Pipeline script 
###
    pipeline {
    agent any

    stages {
        stage("Start") {
            steps {
                echo "Start pipeline"
            }
        }

        stage("Checkout ") {
            steps {
                echo "copy code from GitHub"
            }
        }

        stage("Build") {
            steps {
                echo "copy code Build"
                    }
                }

        stage("Test") {
            steps {
               echo "Build Code Test   "
            }
        }

        stage("Deploy") {
            steps {
                echo "Test Code  Deploy"
            }
        }
    }
    }

5. save 
6. Build 
     

##