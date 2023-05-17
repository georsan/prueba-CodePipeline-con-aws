import httpx
import boto3

TOKEN_DEVICE = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJUaGluZ2VyX2F3cyIsInN2ciI6Im1ha2VzZW5zLmF3cy50aGluZ2VyLmlvIiwidXNyIjoiTWFrZVNlbnMifQ.v_3GuNIiLd5Wn14G5GUrxD5XoUowvWoGGudj5WNeI_E"
HEADERS_DEVICES = {"Authorization": "Bearer " + TOKEN_DEVICE}
BUCKET_URL_TEMPLATE = ("https://makesens.aws.thinger.io/v1/users/MakeSens/buckets/B{}/data?items=5")
TOKEN_BUCKET_DEVICES = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJBbGxfYnVja2V0cyIsInN2ciI6Im1ha2VzZW5zLmF3cy50aGluZ2VyLmlvIiwidXNyIjoiTWFrZVNlbnMifQ.Y7iXy0PKxJ0U6LM6tSdxUZVzpmGVjQLG596pjMD0cM4"
HEADERS_BUCKET_DEVICES = {"Authorization": "Bearer " + TOKEN_BUCKET_DEVICES}
sqs = boto3.client('sqs')
