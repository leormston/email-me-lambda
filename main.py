import json
import boto3

def lambda_handler(event, context):
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Credentials': True,
            'mode': 'cors'
        }
    print(event)
    if event['requestContext']['http']['method'] == 'POST':
        try:
            client = boto3.client('ses')
            body = json.loads(event['body'])
            print(body)
            client.send_email(
                Source='l.e.ormston@gmail.com',
                Destination={'ToAddresses': [
                        'l.e.ormston@gmail.com',
                    ]
                },
                Message={
                    'Subject': {
                        'Data': f'You have a new message from { body["sender_name"] } on you\'re site [{body["sender_email"]}]'
                    },
                    'Body': {
                        'Text': {
                            'Data': f' You have an email from: { body["sender_name"] } [{body["sender_email"]}]. \n \n \n{body["message"]}'
                        },
                        'Html': {
                            'Data': f'<h1> You have an email from: { body["sender_name"] } [{body["sender_email"]}].</h1> <hr/> <h2>{body["message"]} </h2>'
                        }
                    }
                }
            )
            # TODO implement
            return {
                'statusCode': 200,
                'body': json.dumps('Email Sent!'),
                'headers': headers,
            }
        except Exception as err:
            print(err)
    return {
        'statusCode': 404,
        'body': json.dumps('Something went wrong.'),
        'headers': headers,
    }
        
