import boto3
import cfnresponse
import json

def secrets_handler(event, context):
  ssmClient = boto3.client("ssm")
  # Retrieving from resource properties since this is the format
  # from a custom resource in a CloudFormation template
  requestedSSMParameter = event["ResourceProperties"]["SSMKey"]
  value = ssmClient.get_parameter(Name=requestedSSMParameter, WithDecryption=True)

  # Raw Data for CFN Response
  cfnRespData = {
    "Value": value["Parameter"]["Value"]
  }
  cfnresponse.send(event, context, cfnresponse.SUCCESS, cfnRespData)

  # Data to return if avoiding the CFN response
  data = json.dumps({
    "Value": value["Parameter"]["Value"]
  })

  return data