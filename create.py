import boto3
import json

def lambda_handler(input, context):
    """
    API Endpoint for creating Ingredients.
    """
    client = boto3.client('lambda')

    input_json = input['body-json']

    # Create the create object we'll pass to the lambda endpoint
    create = {
        "table_name": "Ingredients",
        "item": input_json
    }

    response = client.invoke(
        FunctionName='DALCreate',
        InvocationType='RequestResponse',
        Payload=json.dumps(create)
    )

    return '/ingredients/' + input_json['name']
