from django.shortcuts import render, redirect

from .models import Images
from .tasks import generate_image


def index(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        print(prompt)

        generate_image.delay(prompt)

        return redirect("index")
    print(Images.objects.order_by("-create_date"))
    return render(
        request,
        "index.html",
        {
            "images": Images.objects.order_by("-create_date")
        },
    )