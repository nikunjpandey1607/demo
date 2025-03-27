
import pymongo
import base64
import time
import os
from datetime import datetime
from PIL import Image

# MongoDB Atlas Connection String
MONGO_URI = "mongodb://iamomjoshi:ayll5c93U4nffNNA@cluster0-shard-00-00.sjij0.mongodb.net:27017,cluster0-shard-00-01.sjij0.mongodb.net:27017,cluster0-shard-00-02.sjij0.mongodb.net:27017/?replicaSet=atlas-l5wy6s-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "demo"
COLLECTION_NAME = "ImageData"
IMAGE_PATH = "/home/pi/image.jpg"  # Change this to your actual image path

# Connect to MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def capture_image():
    """ Simulate capturing an image (replace this with actual camera code if needed) """
    if not os.path.exists(IMAGE_PATH):
        print("No image found! Using a test image.")
        img = Image.new("RGB", (100, 100), color="red")
        img.save(IMAGE_PATH)  # Save a test image

def send_image():
    """ Read image, convert to base64, and store in MongoDB """
    capture_image()

    with open(IMAGE_PATH, "rb") as img_file:
        image_data = base64.b64encode(img_file.read()).decode("utf-8")

    # MongoDB Document
    document = {
        "image_data": image_data,
        "timestamp": datetime.utcnow()
    }

    collection.insert_one(document)
    print("Image sent to MongoDB Atlas!")

if __name__ == "__main__":
    while True:
        send_image()
        time.sleep(120)  # Send image every 2 minutes
