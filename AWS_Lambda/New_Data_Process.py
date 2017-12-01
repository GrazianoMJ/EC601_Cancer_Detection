""" New_Data_Process.py - AWS Lambda Code

    This program is designed to receive an event from Amazon AWS S3
    service and then perform the following tasks:

    * Pass important information about the S3 bucket and file to the
      Amazon AWS SQS queue.
    * Pass commands to the EC2 Instance Service Manager to execute our 
      learning model.
"""

import boto3
import json

def handler(event, context):
    ssm = boto3.client("ssm")
    sqs = boto3.resource("sqs")
    queue = sqs.get_queue_by_name(QueueName="cancerdetect.fifo")
    response = queue.send_message(MessageBody=json.dumps(event),
                                  MessageGroupId="Test"
    )
    
    ssmCommand = ssm.send_command(
        InstanceIds = ["i-0209de525bf9cc235"],
        DocumentName = "AWS-RunShellScript",
        TimeoutSeconds = 240,
        Comment = "CancerDetectExample",
        Parameters = {
            "commands":["export PATH='/home/ubuntu/anaconda3/bin:$PATH'",
                        "cd /home/ubuntu/", "python test.py"
            ]
        }
    )
