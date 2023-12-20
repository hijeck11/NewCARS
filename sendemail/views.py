from rest_framework import generics
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import Message
from django.core.mail import send_mail

class SendMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        send_mail(
            instance.subject,
            instance.body,
            instance.sender_email,
            ['pashkevich.anton.v@gmail.com'],
            fail_silently=False,
        )

        return Response({"message": "Message sent successfully"})