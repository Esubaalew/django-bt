import asyncio
import json
from django.http import HttpResponse
from django.shortcuts import render

from .bot import bot_tele


def index(request):
    if request.method == 'POST':
        data = request.body
        res = json.loads(data.decode('utf-8'))
        print(res)
        asyncio.run(bot_tele(res))
        return HttpResponse("ok")
    else:
        return render(request, 'index.html')
