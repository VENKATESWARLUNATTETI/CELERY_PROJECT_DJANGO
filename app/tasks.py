import base64
import uuid
import os

from celery import shared_task
from django.core.files.base import ContentFile
from openai import OpenAI

from .models import Images


@shared_task
def generate_image(prompt):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024",
    )

    image_data = response.data[0].b64_json

    image = Images(prompt=prompt)

    image.image.save(
        f"{uuid.uuid4()}.png",
        ContentFile(base64.b64decode(image_data)),
        save=True,
    )