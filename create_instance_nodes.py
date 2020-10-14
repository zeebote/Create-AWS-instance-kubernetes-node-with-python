import boto3
ec2 = boto3.resource('ec2')

# Script launch at instance 1st run
userdata_script = """#!/bin/bash
apt update -y
apt install docker.io -y
systemctl enable docker.service
usermod -aG docker ubuntu
apt install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add
apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
apt update -y
apt install -y kubelet kubeadm kubectl
apt install -y awscli
sysctl -w net.ipv4.ip_forward=1
sed -i 's/net.ipv4.ip_forward=0/net.ipv4.ip_forward=1/Ig' /etc/sysctl.conf
aws s3 cp s3://aa-script/join_command.sh /tmp/
chmod +x /tmp/join_command.sh
/tmp/join_command.sh 
"""
# Create VMs
vm = ec2.create_instances(
  # Using Ubuntu 20.04 id
	ImageId='ami-021809d9177640a20',
	MinCount=1,
  # Create 3 nodes
	MaxCount=3,
  # VM size
	InstanceType='t3.2xlarge',
	KeyName='aa-keypair',
	SubnetId='subnet-0d8e386b',
	UserData=userdata_script,
  # IAM role with read access to S3
	IamInstanceProfile={
        'Name': 's3ReadOnly'
    },
	SecurityGroupIds=[
        	'sg-246d1350',
		'sg-00a3d5e7cd9f5b937',
		'sg-069323c622b6a15c7'
    ],
	TagSpecifications=[
		{
			'ResourceType': 'instance',
			'Tags': [
                {
                    'Key': 'Owner',
                    'Value': 'Engineering'
                },
				{
					'Key': 'Stack',
                    'Value': 'Dev'
				},
				{
					'Key': 'Kubernetes',
                    'Value': 'Node'
				},
            ]
		},
	]
)
for instance in vm:
  # Disable source and destination check for container overlay network (Weave, Flannel...), you don't need this setting if you use AWS PVC-CNI 
	response = instance.modify_attribute(
        SourceDestCheck={
            'Value': False
	    }
	)
  # Wait until instance running and print its ID and IP
	instance.wait_until_running()
	print(
		' Instance is ready \n'
		'   Instance ID: ' + instance.id + '\n'
		'   Private IP: ' + instance.private_ip_address + '\n'
		'-----------------------------------------'
		)