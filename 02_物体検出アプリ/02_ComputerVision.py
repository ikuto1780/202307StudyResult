from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

import streamlit as st
from PIL import ImageDraw
from PIL import ImageFont


KEY = "4d24e50f06bf4dd9a1334092a7b948a3"
ENDPOINT = "https://udemy-20230716.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def get_tags(filepath):
    local_image = open(filepath, "rb")

    tags_result = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
        
    return tags_name

def detect_objects(filepath):
    local_image = open(filepath, "rb")

    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    return objects

st.title('物体検出アプリ')

uploaded_file = st.file_uploader('Choose an image...', type = ['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)
    
    # 描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

        font = ImageFint.truetype(font = './Helvetica 400.ttf', size = 50)

        draw.rectangle([(x, y), (x + w, y + h)], fill = None, outline = 'green', width = 5)
    
    st.image(img)





    st.markdown('**認識されたコンテンツタグ**')
    st.markdown('> apple, tree, building, green')










