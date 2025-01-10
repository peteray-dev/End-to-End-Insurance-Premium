# ML-wine-project-End-to-end

# Health Insurance Premium Prediction App

## Introduction
Determining health insurance premiums is often a complex and opaque process, influenced by various demographic, lifestyle, and financial factors. Customers frequently struggle to understand how their premiums are calculated, leading to dissatisfaction and suboptimal policy choices. Similarly, insurance providers face challenges in pricing policies accurately and competitively.

This project aims to develop a **Health Insurance Premium Prediction App** using machine learning techniques. By leveraging a rich dataset and advanced analytics, the app provides personalized premium predictions, improving transparency and empowering users to make informed decisions.

---

## Problem Statement
The current health insurance premium determination process presents significant challenges:
- **Lack of Transparency:** Customers are unaware of how premiums are calculated.
- **Inequitable Pricing:** Overcharging or underinsuring due to non-personalized premium structures.
- **Provider Challenges:** Difficulty in balancing profitability with competitive pricing.

This project addresses these issues by building an app that predicts health insurance premiums using features such as:
- Demographics (e.g., age, gender, marital status)
- Financial indicators (e.g., income, credit score)
- Lifestyle habits (e.g., smoking status, exercise frequency)
- Policy details (e.g., type, duration, previous claims)

---

## Scope of the Project

### For Customers:
- Personalized premium predictions based on individual profiles.
- Transparent breakdown of contributing factors.
- Actionable insights to optimize policy selection.

### For Insurance Providers:
- Improved accuracy in premium pricing.
- Enhanced ability to identify key customer segments and risk factors.
- Data-driven strategies for policy design and competitiveness.

### Features of the App:
- Intuitive interface for user data input.
- Instant premium predictions using machine learning models.
- Visual explanations of premium calculations.
- Policy optimization recommendations.

---

## Dataset Description
The dataset used in this project includes the following features:
- **Demographics:** Age, gender, marital status, number of dependents, location.
- **Financial Indicators:** Annual income, credit score, occupation.
- **Health and Lifestyle:** Health score, smoking status, exercise frequency.
- **Policy Details:** Policy type, previous claims, insurance duration, property/vehicle details.
- **Other Information:** Education level, customer feedback.


---

## Technology Stack
- **Programming Language:** Python
- **Libraries and Frameworks:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Modeling Techniques:**  Random Forest, Gradient Boosting
- **Deployment:** Flask for backend API; HTML, CSS and JavaScript for front-end (optional)

---




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
uri: 084828601471.dkr.ecr.eu-north-1.amazonaws.com/insureproject

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
