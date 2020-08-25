from django.shortcuts import render
from cowsay_app.models import CowsayModel
from cowsay_app.forms import TextForm
import subprocess



def index(request):
    cowsay_text = ""
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowsayModel.objects.create(
                text=data.get("text")
            )
            text = data.get("text")
            cowsay_text = subprocess.check_output(["cowsay", text], universal_newlines=True, text = True)
            form = TextForm()
            return render(request, "index.html", {"form": form, "cowsay_text": cowsay_text})
    form = TextForm()
    return render(request, "index.html", {"form": form})

def history_view(request):
    cowsay_text = CowsayModel.objects.order_by("-id")[:10]
    return render(request, "history.html", {"data": cowsay_text})

    
