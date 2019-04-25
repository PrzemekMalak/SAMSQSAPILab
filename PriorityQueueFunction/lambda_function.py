import json

def lambda_handler(event, context):
    # TODO implement
    print(json.dumps(event))
    x = 2 / 0
    return {
        "statusCode": 200,
        "body": json.dumps('Priority')
    }