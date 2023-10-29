from typing import Union

from fastapi import FastAPI

from google.cloud import storage
from fastapi.responses import FileResponse
import os

# Set the path to your GCP service account key JSON file
# key_path = '/home/shalvi27/Downloads/databases-401308-2257e3901842.json'
# key_path = os.environ.get('GCP_SA_KEY')
# print("KEY_PATH")
# print(key_path)
# Initialize the GCS client
# client = storage.Clientfrom_service_account_json(key_path)
client = storage.Client()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/get-file-from-gcs")
def get_file_from_gcs():
    print("line------28")
    file_path = 'decrackle/resnetplusplus/speech_model/finalized_speech_acc_resunet_32480_cv10_05.pth'
    # Fetch the file from GCS
    print("line------31")

    bucket = client.get_bucket("test-bucket-s3")
    print("line------34")
    blob = bucket.blob(file_path)
    print("line------35")
    print(blob.name)
    print(blob.path)
    # file_content = blob.download_as_string()
    # print(file_content)
    # Serve the file as a response
    # response = FileResponse(blob.download_as_bytes(), filename='your-file-name.extension')

    return "ok"
