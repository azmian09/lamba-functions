import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the source bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    
    print(f"Source Bucket: {source_bucket}")
    print(f"Source Key: {source_key}")

    # Remove the subfolder and only copies the files from the source_key if it exists. Example: s3://pocbucket/outbound/. You only want the files in outbound not the whole subfolder copes. Add outbound/ below to remove the subfolder
    if source_key.startswith("specify the subfolder path that needs to be removed "):
        source_key_without_prefix = source_key[len("specify the subfolder path that needs to be removed"):]
    else:
        source_key_without_prefix = source_key
    
    # Define the destination bucket and key (subfolder structure)
    destination_bucket = 'bucket_name enter here'
    destination_key = f"place subfolder path for bucket/{source_key_without_prefix}"

    # Copy the object
    copy_source = {
        'Bucket': source_bucket,
        'Key': source_key
    }
    
    s3.copy_object(
        CopySource=copy_source,
        Bucket=destination_bucket,
        Key=destination_key
    )

    return {
        'statusCode': 200,
        'body': json.dumps('File copied successfully!')
    }
