""" New_Data_Process.py - AWS Lambda Code

    This program is designed to receive an event from Amazon AWS S3
    service and then perform the following tasks:

    * Pass important information about the S3 bucket and file to the
      Amazon AWS SQS queue.
    * Pass commands to the EC2 Instance Service Manager to execute our
      learning model.
"""
import boto3


def queue_update(event):

    """ Sends a message to the queue based on the event json message.
        Information includes the following:
        * eventtime, bucketname, bucketarn & filename
    """

    sqs = boto3.resource("sqs")
    queue = sqs.get_queue_by_name(QueueName="cancerdetect.fifo")
    eventtime = event["Records"][0]["eventTime"]
    bucketname = event["Records"][0]["s3"]["bucket"]["name"]
    bucketarn = event["Records"][0]["s3"]["bucket"]["arn"]
    filename = event["Records"][0]["s3"]["object"]["key"]
    message = ("New File Received @ " + eventtime + "\n" +
               "Bucket Name = " + bucketname + "\n" +
               "Bucket ARN = " + bucketarn + "\n" +
               "Target File = " + filename + "\n")
    queue.send_message(MessageBody=message, MessageGroupId="Classify")


def run_ec2_command():

    """ Sends a command to the System Service Manager of EC2. This
        command will execute the following functions on our EC2
        instance:
        1.) Update the shell's PATH varibale to include the appropriate
            path for our Python 3.6.3 (Anaconda)
        2.) Change the directory to the home directory of the "ubuntu"
            user
        3.) Execute the test.py code
    """

    ssm = boto3.client("ssm")
    ssm.send_command(
        InstanceIds=["i-0209de525bf9cc235"],
        DocumentName="AWS-RunShellScript",
        TimeoutSeconds=240,
        Comment="Classification Request",
        Parameters={
            "commands":["export PATH='/home/ubuntu/anaconda3/bin:$PATH'",
                        "cd /home/ubuntu/", "python test.py"]})


def handler(event, context):

    """ Function called by lambda once it receives the appropriate
        S3 trigger information
    """

    queue_update(event)
    run_ec2_command()
