from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request=request, template_name='core/index.html', context={
        "title": "Home",
    })


@csrf_exempt
def send_file(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)

        return JsonResponse(data={'key': 'value'}, safe=False)
