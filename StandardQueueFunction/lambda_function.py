import json

def lambda_handler(event, context):
    # TODO implement
    print(json.dumps(event))
    return {
        "statusCode": 200,
        "body": json.dumps('Standard')
    }