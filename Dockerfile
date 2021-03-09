FROM amazon/aws-lambda-python:latest
#FROM python:latest

COPY . ./
CMD ["hello.world"]