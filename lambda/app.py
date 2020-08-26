import boto3
import json
import requests

def secrets_handler(event, context):
  ssmClient = boto3.client("ssm")
  print(event)
  value = ssmClient.get_parameter(Name=event["SSMKey"], WithDecryption=True)

  data = json.dumps({
    "Value": value["Parameter"]["Value"]
  })

  return data