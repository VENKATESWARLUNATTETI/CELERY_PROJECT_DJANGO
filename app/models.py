from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to="generated_images/")
    prompt = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt