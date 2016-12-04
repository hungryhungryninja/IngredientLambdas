import boto3
import json

def lambda_handler(input, context):
    """
    API Endpoint for creating Ingredients.
    """
    client = boto3.client('lambda')

    # Create the search object we'll pass to the lambda endpoint
    search = {}
    if "name" in input:
        search = {
            "table_name": "Ingredients",
            "type": "get_id",
            "id_keys": input
        }
    else:
        search = {
            "table_name": "Ingredients",
            "type": "query",
            "match_attributes": input
        }

    response = client.invoke(
        FunctionName='DALSearch',
        InvocationType='RequestResponse',
        Payload=json.dumps(search)
    )

    ingredients = json.loads(response['Payload'].read())

    if isinstance(ingredients, list):
        for idx, ingredient in enumerate(ingredients):
            ingredients[idx] = {
                'name': ingredient['name']['S']
            }

    return ingredients
