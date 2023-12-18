import pandas as pd
import os
from django.shortcuts import render, redirect
from rest_framework import generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django import forms
from .models import AutohausREST
from .forms import AutohausRESTForm
from .models import AutohausREST
from .serializers import MyModelSerializer

from rest_framework.generics import ListAPIView


class AutohausRESTForm(forms.ModelForm):
    class Meta:
        model = AutohausREST
        fields = '__all__'


class AutohausCreateView(generics.CreateAPIView):
    queryset = AutohausREST.objects.all()
    serializer_class = MyModelSerializer
    #
    # def get(self, request, *args, **kwargs):
    #     form = AutohausRESTForm()
    #     return render(request, 'autohaus_create.html', {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = AutohausRESTForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('mymodel-list-create')
    #     return render(request, 'autohaus_create.html', {'form': form})



class MyModelListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        cars_list = self.get_queryset()
        return render(request, 'cars_list.html', {'cars_list': cars_list})

    def get_queryset(self):
        queryset = AutohausREST.objects.all()
        q = self.request.query_params.get('q', None)
        if q:
            queryset = queryset.filter(brand_auto__icontains=q)
        return queryset

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Ошибка':'Не указан id объекта'})
        instance = AutohausREST.objects.get(pk=pk)
        instance.delete()
        return Response({'Deleted AutohausREST': 'deliting_AutohausREST'})

class AutohausListViews(generics.ListAPIView):
    queryset = AutohausREST.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = (IsAuthenticated, )
    # filter_backends = [filters.SearchFilter]
    # filter_backends = [filters.SearchFilter]
    filter_backends = [filters.OrderingFilter]
    # filterset_fields = ['price']
    # search_fields = ['brand_auto', 'model_auto', 'engine_fuel']
    ordering_fields = ['price']


class PurchaseList(generics.ListAPIView):
    serializer_class = MyModelSerializer

    def get_queryset(self):
        name_1 = self.kwargs['price']
        return AutohausREST.objects.filter(price=name_1)


class WonderDestroy(generics.DestroyAPIView):
    queryset = AutohausREST.objects.all()
    serializer_class = MyModelSerializer

class ExportAPIViews(APIView):
    def post(self, request):
        try:
            queryset = AutohausREST.objects.all()
            df = pd.DataFrame.from_records(queryset.values(), exclude=['brand_auto'])
            df.to_excel('AutoHaus.xlsx', index=False)
            return Response({
                'status': True,
                'message': 'Export successfully'
            },status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': False,
                'message': 'Export not complete'
            },status=status.HTTP_400_BAD_REQUEST)

# class ExportAPIViews(APIView):
#     def post(self, request):
#         try:
#             queryset = AutohausREST.objects.all()
#             df = pd.DataFrame.from_records(queryset.values(), exclude=['brand_auto'])
#
#             # Specify the absolute path to the file
#             file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'AutoHaus.xlsx')
#             df.to_excel(file_path, index=False)
#
#             return Response({
#                 'status': True,
#                 'message': 'Export successfully',
#                 'file_path': file_path,
#             }, status=status.HTTP_200_OK)
#
#         except PermissionError as pe:
#             return Response({
#                 'status': False,
#                 'message': f'PermissionError: {str(pe)}',
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         except FileNotFoundError as fe:
#             return Response({
#                 'status': False,
#                 'message': f'FileNotFoundError: {str(fe)}',
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         except Exception as e:
#             return Response({
#                 'status': False,
#                 'message': f'Export failed: {str(e)}',
#             }, status=status.HTTP_400_BAD_REQUEST)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import base64

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def send_message(request):
    if request.method == 'POST':
        # Получаем сообщение из POST-запроса
        message = request.data.get('message', '')

        # Подготавливаем и отправляем электронное письмо
        login = 'ваш_email@gmail.com'
        password = 'ваш_пароль'

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(login, password)

            subject = 'Тема вашего HTML-письма'

            # Указываем путь до файла с HTML-контентом и изображением
            html_file_path = r'E:\TMS\NewCARS\NewCARS\email_template.html'
            image_path = r'E:\TMS\NewCARS\NewCARS\1.jpg'

            # Читаем содержимое HTML-файла
            with open(html_file_path, 'r', encoding='utf-8') as html_file:
                html_content = html_file.read()

            # Создаем MIMEMultipart object
            msg = MIMEMultipart()
            msg['Subject'] = Header(subject, 'utf-8')

            # Читаем содержимое изображения и кодируем в base64
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
                image_base64 = base64.b64encode(image_data).decode('utf-8')

            # Attach HTML content with image to the email
            msg.attach(MIMEText(html_content, 'html'))

            # Attach image to the email as inline
            image_attachment = MIMEImage(image_data, name='image.jpg')
            image_attachment.add_header('Content-ID', '<image>')
            msg.attach(image_attachment)

            # Send the email
            server.sendmail(login, 'kubik19891502@gmail.com', msg.as_string())
            print("Email sent successfully!")

            # Возвращаем успешный ответ
            return Response({'status': 'success'}, status=status.HTTP_200_OK)

        except Exception as e:
            # Возвращаем ошибку в случае неудачи
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        finally:
            # Ensure the connection is closed
            server.quit()

    # Если запрос не POST, возвращаем ошибку
    return Response({'status': 'error', 'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)