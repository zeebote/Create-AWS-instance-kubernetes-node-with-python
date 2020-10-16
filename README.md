# Create AWS instances kubernetes node with python
This script use to create EC2 instances add add them into existing Kubernetes cluster using Python.<br>
**Requirements:**
1. AWS CLI - Please follow this [link](https://aws.amazon.com/cli/) for installation and information about AWS CLI
1. AWS SDK for Python (boto3) - Please follow this [link](https://aws.amazon.com/sdk-for-python/) for installation and information about AWS SDK for Python
1. AWS account with access key to your EC2 - You can use an existing account or create a new one with AWS IAM console then go to manage access key and generate 
a new key. This account must have IAM role which have minimum policy to create instances in EC2 and attach IAM role to instance. You also need a 
role that has read only policy to S3 for the new create instance. Please follow this [link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
for information how to create IAM role. <br> 

**How to use**
1. Setup environment
   - Create virtual env and install requirement packages
      ```
      python3 -m venv aws-env
      cd aws-env
      source bin/activate
      pip3 install awscli boto3
      ```
   

1. Configure AWS credential: 
   - Invoke credential configuration with AWS CLI and follow on screen instruction enter aws_access_key_id, aws_secret_access_key, region, output (json) <br>
      ```
      aws configure
      AWS Access Key ID [None]:Your AWS Access Key
      AWS Secret Access Key [None]: Your AWS Secret Access Key 
      Default region name [None]: us-east-1
      Default output format [None]: json
      ```
1. To run script in your virtual env run: <br>
      `python3 create_instance_nodes.py `
1. You should see the newly create instances info <br>       
      ```
      Instance is ready 
      Instance ID: i-0b9a858234adab63a
      Private IP: 172.31.25.79
   -----------------------------------------
      Instance is ready 
      Instance ID: i-0174d153868a58e8b
      Private IP: 172.31.29.187
   -----------------------------------------
      Instance is ready 
      Instance ID: i-011617f0e79c33a8f
      Private IP: 172.31.23.94
   -----------------------------------------
      ```
 1. From your Kubernetes master, check if new nodes show up and ready <br>
     ```
     ubuntu@ip-172-31-30-106:~$ kubectl get node
      NAME               STATUS   ROLES    AGE     VERSION
      ip-172-31-22-170   Ready    <none>   2d1h    v1.19.2
      ip-172-31-23-94    Ready    <none>   5m42s   v1.19.3
      ip-172-31-25-79    Ready    <none>   5m37s   v1.19.3
      ip-172-31-29-187   Ready    <none>   5m19s   v1.19.3
      ip-172-31-30-106   Ready    master   2d11h   v1.19.2
     ```
        
