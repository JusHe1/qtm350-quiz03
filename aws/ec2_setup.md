# EC2 Setup Notes — QTM350 Quiz 03 (Activity 2)

## Instance
- Region: us-east-2 (Ohio)
- AMI: Ubuntu Server 24.04 LTS (x86_64)
- Type: t3.micro (Free tier)
- Security Group: SSH (22) from my IP
- Key Pair: qtm350-key.pem

## Connect
```bash
chmod 400 ~/Downloads/qtm350-key.pem
ssh -i ~/Downloads/qtm350-key.pem ubuntu@ec2-18-188-251-182.us-east-2.compute.amazonaws.com

