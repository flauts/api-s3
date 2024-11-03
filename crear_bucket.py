import boto3

def lambda_handler(event, context):
    # Obtener el nombre del bucket del evento
    bucket_name = event['body']['bucket_name']

    # Cliente de S3
    s3_client = boto3.client('s3')
        # Crear el bucket
    s3_client.create_bucket(Bucket=bucket_name)
    return {
        'statusCode': 200
    }
