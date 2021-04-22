from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TaskSerializers
from .models import SendMail

from django.core.mail import send_mail
from django.conf import settings

# import smtplib

URL = "http://localhost:8000/apimail"


#
# EMAIL_RECIEVER = "nattapong.jaikla@gmail.com"
# subject = "My Test email"
# body = "my story"
#
#
# def send(subject_d, body_d, email_rec="nattapong.jaikla@gmail.com"):
#     with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#         smtp.starttls()
#         smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
#         msg = f'Subject:{subject_d}\n\n{body_d}'
#         smtp.sendmail(settings.EMAIL_ADDRESS, email_rec, msg)
#         print("Already sent email")
# subject_d='Subject', body_d='FYI', email_rec="nattapong.jaikla@gmail.com"

def send_email_function(subject, message, recipient, name):
    # subject_d
    # message = body_d
    # recipient_list = ['himepe7924@gridmire.com', 'nattapong.jaikla@gmail.com']
    subject = subject
    message = 'ถึงคุณ ' + name + "\n\n" + message + "\n\n\n" + \
              'Best regard,\n' + name
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nattapong.jaikla@gmail.com', recipient]

    send_mail(subject, message, email_from, recipient_list)
    print("Already sent email")


@api_view(['GET'])
def apiListMail(request):
    api_urls = {
        'List': URL + '/email-list/',
        'Detail mail': URL + '/email-detail/<str:pk>',
        'Create': URL + '/email-create/',
        'Update': URL + '/email-updates/<str:pk>',
        'Delete': URL + '/email-delete/<str:pk>',
        # 'Send': URL + '/email-send/<str:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def mailList(request):
    mails = SendMail.objects.all()
    serializer = TaskSerializers(mails, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def mailDetail(request, pk):
    mails = SendMail.objects.get(id=pk)
    serializer = TaskSerializers(mails, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def mailCreate(request):
    print("mailcreate")
    serializer = TaskSerializers(data=request.data)
    print(serializer)
    # print(request.data['subject'])
    # print(request.data['body'])
    # print(request.data['receiver'])
    # send_email(request.data['subject'], request.data['body'], request.data['receiver'])
    send_email_function(request.data['subject'],
                        request.data['body'],
                        request.data['receiver'],
                        request.data['namereceiver'])
    # print(factorial(5))
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def mailUpdate(request, pk):
    mails = SendMail.objects.get(id=pk)
    serializer = TaskSerializers(instance=mails, data=request.data)
    print(serializer)
    send_email_function(request.data['subject'],
                        request.data['body'],
                        request.data['receiver'],
                        request.data['namereceiver'])
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def mailDelete(request, pk):
    mails = SendMail.objects.get(id=pk)
    mails.delete()

    return Response(mails.subject + '  ' + mails.receiver + " successfully delete!")

# @api_view('[POST]')
# def mailSend(request, pk):
#     task = SendMail.objects.get(id=pk)
#     serializer = TaskSerializers(instance=task, data=request.data)
#     print(serializer)
#     send_email_function(request.data['subject'],
#                         request.data['body'],
#                         request.data['receiver'],
#                         request.data['namereceiver'])
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# def factorial(n):
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     return res
