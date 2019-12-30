from datetime import datetime
import json
import pytz
from unittest import mock
from django.test import TestCase
from django.utils import timezone
from .models import Message


class ModelTests(TestCase):
    def test_get_message(self):
        first_message = Message.objects.create(text="Hello, World!")
        second_message = Message.objects.create(text="Привет, Мир!")
        message_list = Message.objects.get_messages()
        self.assertDictEqual(message_list, {'success': 'ok', 'data': [
            {'date': timezone.localtime(first_message.date).strftime("%d.%m.%Y %H:%M"), 'text': first_message.text},
            {'date': timezone.localtime(second_message.date).strftime("%d.%m.%Y %H:%M"), 'text': second_message.text}
        ]})

    def test_add_message(self):
        message_count = Message.objects.count()
        temp_datetime = timezone.now()
        result = Message.objects.add_message(text="Hello, World!")
        self.assertDictEqual(result, {"success": "ok"})
        self.assertEqual(Message.objects.count(), message_count + 1)
        message = Message.objects.first()
        self.assertEqual(message.text, "Hello, World!")
        self.assertEqual(message.date, timezone.localtime(temp_datetime))


class ViewsTests(TestCase):
    def test_main_view(self):
        result = self.client.get('')
        self.assertEqual(result.status_code, 200)

    def test_get_message(self):
        message = Message.objects.create(text="Hello, World!")
        result = self.client.get("/messages/")
        self.assertEqual(result.status_code, 200)
        self.assertDictEqual(json.loads(result.content.decode("utf-8")),
                             {"success": "ok", "data": [
                                 {"date": timezone.localtime(message.date).strftime("%d.%m.%Y %H:%M"),
                                  "text": message.text}]})

    def test_add_message(self):
        result = self.client.post('/messages/', {"message": "Hello, World!"}, content_type="application/json")
        self.assertEqual(result.status_code, 200)
        self.assertDictEqual(json.loads(result.content.decode("utf-8")), {"success": "ok"})
