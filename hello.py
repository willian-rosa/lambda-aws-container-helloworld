import sys

print('Run file Test')


def world(event, context):
    print('Run Hello World')
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
