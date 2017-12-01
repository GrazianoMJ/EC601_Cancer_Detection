""" test.py
    Author: Michael Graziano
    This code exists on the EC2 Instance of our AWS  account. It acts
    as a quick test of our communication between services by doing the
    following:
    1.) Accessing our sqs queue and retrieving a single message
    2.) printing out the body of the message as well as any attributes
    3.) Deleting the message after it has been processed
    4.) Performing steps 1-3 until the queue is empty
"""

import boto3

# boto3.Session allows us to access our AWS Services as if we are a user
session = boto3.Session(
        aws_access_key_id = "AKIAIEBEC5MT3VR725SA",
        aws_secret_access_key = "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",
        region_name = "us-east-2"
)
sqs = session.resource('sqs')
queue = sqs.get_queue_by_name(QueueName="cancerdetect.fifo")
for message in queue.receive_messages(MaxNumberOfMessages=1, MessageAttributeNames=["All"]):
    print("Body:", message.body)
    print("Attributes:", message.message_attributes)
    message.delete()
print("Test complete!")
