from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from consumables.forms.create import ConsumablesForm
from .models import Consumable

# Create your views here.
class ConsumablesIndexView(View):
    def get(self, request):
        consumables = Consumable.objects.all()
        ctx = {"consumables":consumables}
        return render(request, "consumables/index.html", ctx)


class ConsumablesCreateView(View):
    def get(self, request):
        form = ConsumablesForm()
        ctx = {"form": form}
        return render(request, "consumables/create.html", ctx)

    def post(self, request):
        data = request.POST
        files = request.FILES

        form = ConsumablesForm(data, files)

        if form.is_valid():
            consumable = form.save()
            print("Form is valid and saved")
            return redirect("consumables:admin:home")
        else:
            print("Form is invalid")
            return render(request, "consumables/create.html", {"form": form})
