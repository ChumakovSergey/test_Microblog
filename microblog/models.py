from django.db import models
from django.utils import timezone


class BlogManager(models.Manager):
    def add_message(self, text):
        self.model.objects.create(text=text)
        return {"success": "ok"}

    def get_messages(self):
        data = self.model.objects.all()
        messages = []
        for message in data:
            messages.append({"date": timezone.localtime(message.date).strftime("%d.%m.%Y %H:%M"), "text": message.text})
        return {"success": "ok", "data": messages}


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()

    def __str__(self):
        return "{} {}...".format(timezone.localtime(self.date).strftime('%d.%m.%Y %H:%M'), self.text[:30])
