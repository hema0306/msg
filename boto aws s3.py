import boto3
import sys


class AWS:

    def __init__(self, bucket_name, bucket_region):

        self.bucket_name = bucket_name
        self.bucket_region = bucket_region
        self.file_name = file_name
        self.key key

    def create_user_bucket(self, bucket_name, bucket_region):

        client = boto3.client('s3', aws_access_key_id='AKIATC6DXP3TY5LMMBC7', aws_secret_access_key='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')
        buckets = client.create_bucket(Bucket = self.bucket_name, CreateBucketConfiguration={'LocationConstraint': self. bucket_region})

        print("Created bucket {}.".format(bucket_name))
        return buckets

    def upload_file_into_bucket(self, file_name, bucket_name, key):

        resource = boto3.client('s3', aws_access_key_id='AKIATC6DXP3TY5LMMBC7', aws_secret_access_key='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')
        file_upload = resource.meta.client.upload_file(Filename = self.file_name, Bucket = self.bucket_name, Key = self.key)

        print("{} with {} is successfully uploaded into {} of S3".format(file_name, key, bucket_name))

    def download_file_from_bucket(self, file_name, bucket_name, key):

        resource = boto3.client('s3', aws_access_key_id='AKIATC6DXP3TY5LMMBC7', aws_secret_access_key='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')
        download_file = resource.meta.client.download_file(Filename = self.file_name, Bucket = self.bucket_name, Key = self.key)

        print("{} with {} is successfully downloaded from {} of S3".format(file_name, key, bucket_name))

            
            
if __name__ == '__main__':

    print("AWS S2 services")
    print("Choose from the following services 1.create bucket 2.upload a file 3.delete a file")

    user_response = int(input("Enter the option number"))
    response_check = [1,2,3]

    if user_response not in response_check:
        print("Enter the valid option")
        sys.exit()

    if user_response == 1:
        bucket_name = input("Enter the bucket name")
        bucket_region = input("Enter the region for the bucket")

        bucket_obj = AWS(bucket_name)
        bucket_obj.create_bucket(bucket_name,bucket_region)

    elif user_response == 2:
        bucket_name = input("Enter the bucket name in which you wish to upload file")
        file_name = input("Enter the file name")
        key = input("Enter the name of the file to upload")

        bucket_obj = AWS(bucket_name)
        bucket_obj.upload_file_into_bucket(file_name, bucket_name, key)

    elif user_response == 3:
        bucket_name = input("Enter the bucket name in which you wish to upload file")
        file_name = input("Enter the file name")
        key = input("Enter the name of the file to download")

        if s3.bucket_name.creation_date is None:
            return True
        else:
            print("Bucket already exists")

        bucket_obj = AWS(bucket_name)
        bucket_obj.download_file_from_bucket(file_name, bucket_name, key)

    else:
        print("Exit")
        sys.exit()





