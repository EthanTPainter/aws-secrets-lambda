import boto3
import cfnresponse
import json

def secrets_handler(event, context):
  ssmClient = boto3.client("ssm")
  # Retrieving from resource properties since this is the format
  # from a custom resource in a CloudFormation template
  requestedSSMParameter = event["ResourceProperties"]["SSMKey"]
  try:
    value = ssmClient.get_parameter(Name=requestedSSMParameter, WithDecryption=True)
  except:
    badCfnResponseData = {
      "Value": "bad value"
    }
    cfnresponse.send(event, context, cfnresponse.FAILED, badCfnResponseData)
    return json.dumps({
      "Value": "bad value"
    })

  if (value is None or value["Parameter"] is None or value["Parameter"]["Value"] is None):
    badCfnResponseData = {
      "Value": "bad value"
    }
    cfnresponse.send(event, context, cfnresponse.FAILED, badCfnResponseData)
    return json.dumps({
      "Value": "bad value"
    })

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