# Create AWS instances kubernetes node with python
This script use to create EC2 instances add add them into existing Kubernetes cluster using Python.<br>
**Requirement:**
1. AWS CLI - Please follow this [link](https://aws.amazon.com/cli/) for installation and information about AWS CLI
1. AWS SDK for Python (boto3) - Please follow this [link](https://aws.amazon.com/sdk-for-python/) for installtion and information about AWS SDK for Python
1. AWS account with access key to your EC2 - You can use an existing account or create a new one with AWS IAM console then go to manage access key and generate 
a new key. This account must have IAM role which have minimum policy to create instances in EC2 and attach IAM role to instance. You also need a 
role that has read only policy to S3 for the new create instance. Please follow this [link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
for information how to create IAM role. <br> 

**How to use**
1. Setup environment
   1. Create virtual env and install requirement packages
      ```
      python3 -m venv aws-env
      cd aws-env
      source bin/activate
      pip3 install awscli boto3
      ```
   

1. Configure AWS credential: 
   1. Invoke credential configuration with AWS CLI and follow on screen instruction enter aws_access_key_id, aws_secret_access_key, region, output (json) <br>
      ```
      aws configure
      AWS Access Key ID [None]:Your AWS Access Key
      AWS Secret Access Key [None]: Your AWS Secret Access Key 
      Default region name [None]: us-east-1
      Default output format [None]: json
      ```
1. To run script in your virtual env run:
      ```python3 create_instance_nodes.py```
