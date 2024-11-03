import boto3

def lambda_handler(event, context):
    # Obtener el nombre del bucket y del directorio del evento
    bucket_name = event['body']['bucket_name']
    folder_name = event['body']['folder_name']

    # Cliente de S3
    s3_client = boto3.client('s3')

    # Crear el "directorio" dentro del bucket
    s3_client.put_object(Bucket=bucket_name, Key=folder_name)
    print(f'Directorio "{folder_name}" creado en el bucket "{bucket_name}".')
    return {
        'statusCode': 200,
        'body': f'Directorio "{folder_name}" creado en el bucket "{bucket_name}".'
    }
