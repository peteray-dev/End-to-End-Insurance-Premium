# ML-wine-project-End-to-end

<!-- conda create -n mlproj python=3.8 -->

<!-- conda activate mlproj -->

<!-- pip install -r requirements.txt -->
# workflow
Update config.yaml

Update schema.yaml

Update params.yaml

Update the entity

Update the configuration manager in src config

Update the components

Update the pipeline

Update the main.py

Update the app.py

# create iam user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess


# Create ECR repo to store docker image
uri: 084828601471.dkr.ecr.eu-north-1.amazonaws.com/insuranceproject

# Create an EC2 virtual machine (Ubuntu)
mainly used for deployment, other can be selected based on request

# open EC2 and install doocker

#optinal

sudo apt-get update -y  #update all necessary packages

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

# configure EC2 as a self hosted runner 
setting>actions>runner>new self hosted runner> choose os> then run command one by one
this ensures that github is connected to the ec2 machine

# setting up Github secerets
this ensure that the github is connected to aws using keys
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
