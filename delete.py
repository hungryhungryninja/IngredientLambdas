import boto3
import json

def lambda_handler(input, context):
    """
    API Endpoint for creating Ingredients.
    """
    client = boto3.client('lambda')

    key = {"name" : input['params']['path']['name']}

    # Create the create object we'll pass to the lambda endpoint
    create = {
        "table_name": "Ingredients",
        "key": key
    }

    response = client.invoke(
        FunctionName='DALDelete',
        InvocationType='RequestResponse',
        Payload=json.dumps(create)
    )

    return "deleted"
