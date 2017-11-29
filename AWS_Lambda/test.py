import boto3

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
