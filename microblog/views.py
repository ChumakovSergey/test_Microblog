import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Message


class ApiView(View):
    def get(self, request):
        messages = Message.objects.get_messages()
        return HttpResponse(json.dumps(messages, ensure_ascii=False), content_type="application/json")

    def post(self, request):
        data = json.loads(request.body)
        print(data)
        result = Message.objects.add_message(data["message"])
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")


class PageView(View):
    def get(self, request):
        messages = Message.objects.get_messages()
        return render(request, "microblog/index.html", context={"messages": messages})
