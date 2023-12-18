# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# import os
#
# def read_html_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.read()
#
# def send_image_email(to_email, subject, image_path, html_file_path):
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
#
#     smtp_username = 'pashkevich.anton.v@gmail.com'
#     smtp_password = 'ntqirrxdqkknvcxr'
#
#     from_email = 'pashkevich.anton.v@gmail.com'
#
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#
#     body = ""
#     msg.attach(MIMEText(body, 'plain'))
#
#     with open(image_path, 'rb') as image_file:
#         img = MIMEImage(image_file.read())
#         img.add_header('Content-Disposition', 'attachment', filename='image.jpg')
#         msg.attach(img)
#
#     html_content = read_html_file(html_file_path)
#     msg.attach(MIMEText(html_content, 'html'))
#
#     try:
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(smtp_username, smtp_password)
#         server.sendmail(from_email, to_email, msg.as_string())
#         server.quit()
#         print("Сообщение успешно отправлено!")
#     except Exception as e:
#         print("Ошибка при отправке сообщения:", str(e))
#
# to_email = 'kubik19891502@gmail.com'
# subject = 'kartinka'
# html_file_path = r'E:\TMS\NewCARS\NewCARS\email_template.html'
# image_path = r'E:\1.jpg'
# send_image_email(to_email, subject, image_path, html_file_path)
#
#
#
#
# login = 'pashkevich.anton.v@gmail.com'
# password = 'ntqirrxdqkknvcxr'

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.header import Header
# import base64
#
# login = 'pashkevich.anton.v@gmail.com'
# password = 'ntqirrxdqkknvcxr'  # App Password or regular Gmail password
#
# try:
#     # Connect to the SMTP server
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(login, password)
#
#     subject = 'normal`no HTML?'
#
#     # Указываем путь до файла с HTML-контентом и изображением
#     html_file_path = r'E:\TMS\NewCARS\NewCARS\email_template.html'
#     image_path = r'E:\1.jpg'
#
#     # Читаем содержимое HTML-файла
#     with open(html_file_path, 'r', encoding='utf-8') as html_file:
#         html_content = html_file.read()
#
#     # Создаем MIMEMultipart object
#     msg = MIMEMultipart()
#     msg['Subject'] = Header(subject, 'utf-8')
#
#     # Attach HTML content to the email
#     msg.attach(MIMEText(html_content, 'html'))
#
#     # Читаем содержимое изображения и кодируем в base64
#     with open(image_path, 'rb') as image_file:
#         image_data = image_file.read()
#         image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#     # Вставляем изображение в HTML как встроенное (inline) base64
#     img_tag = f'<img src="data:image/jpg;base64,{image_base64}" alt="Image">'
#     html_content_with_image = html_content.replace('<!-- INSERT_IMAGE_HERE -->', img_tag)
#
#     # Attach image to the email
#     image_attachment = MIMEImage(image_data, name='image.jpg')
#     msg.attach(image_attachment)
#
#     # Send the email
#     server.sendmail(login, 'kubik19891502@gmail.com', msg.as_string())
#
# finally:
#     # Ensure the connection is closed
#     server.quit()
# В этом примере, в HTML-шаблоне вы должны использовать комментарий <!-- INSERT_IMAGE_HERE --> в месте, где вы хотите вставить изображение.
# Затем, код заменит этот комментарий на тег <img> с base64-кодированным изображением.
# Отправлять изображение в виде встроенного (inline) base64 может быть удобным для электронной почты, но помните, что это может увеличить размер вашего письма.
#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.header import Header
# import base64
#
# login = 'pashkevich.anton.v@gmail.com'
# password = 'ntqirrxdqkknvcxr'  # Ваш App Password или обычный пароль Gmail
#
# try:
#     # Соединяемся с SMTP-сервером
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(login, password)
#
#     subject = 'HTML с изображением'
#
#     # Указываем путь до файла с HTML-контентом и изображением
#     html_file_path = r'E:\TMS\NewCARS\NewCARS\email_template.html'
#     image_path = r'E:\TMS\NewCARS\NewCARS\1.jpg'
#
#     # Читаем содержимое HTML-файла
#     with open(html_file_path, 'r', encoding='utf-8') as html_file:
#         html_content = html_file.read()
#
#     # Создаем MIMEMultipart object
#     msg = MIMEMultipart()
#     msg['Subject'] = Header(subject, 'utf-8')
#
#     # Attach HTML content to the email
#     msg.attach(MIMEText(html_content, 'html'))
#
#     # Читаем содержимое изображения и кодируем в base64
#     with open(image_path, 'rb') as image_file:
#         image_data = image_file.read()
#         image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#     # Вставляем изображение в HTML как встроенное (inline) base64
#     img_tag = f'<img src="data:image/jpg;base64,{image_base64}" alt="Image">'
#     html_content_with_image = html_content.replace('<!-- INSERT_IMAGE_HERE -->', f'<img src="data:image/jpg;base64,{image_base64}" alt="Image" style="max-width: 100%;">')
#
#
#     # Attach image to the email
#     image_attachment = MIMEImage(image_data, name='image.jpg')
#     msg.attach(image_attachment)
#
#     # Send the email
#     server.sendmail(login, 'kubik19891502@gmail.com', msg.as_string())
#
# finally:
#     # Убеждаемся, что соединение закрыто
#     server.quit()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import base64

login = 'pashkevich.anton.v@gmail.com'
password = 'ntqirrxdqkknvcxr'  # App Password or regular Gmail password

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

finally:
    # Ensure the connection is closed
    server.quit()