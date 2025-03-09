repo="307946653835.dkr.ecr.us-east-2.amazonaws.com"
build:
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin ${repo}
	docker build --platform=linux/amd64 -t 307946653835.dkr.ecr.us-east-2.amazonaws.com/hello-python:v2 .
	docker push 307946653835.dkr.ecr.us-east-2.amazonaws.com/hello-python:v1
