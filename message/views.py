from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from message.models import Messages, Conversations
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from rest_framework import serializers
from users.views import UserSerializer
from message.serializers import ConversationSerializer, AddMessageSerializer, RequestGetMessageSerializer, MessageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MessageView(APIView):
    # authentication_classes = []
    def get(self, request):
        s = RequestGetMessageSerializer(data = request.GET)
        if s.is_valid():
            c = Conversation.objects.get(
                id = request.GET['conversation'])
            messages = Messages.objects.filter(conversation = c)
            s = MessageSerializer(messages, many = True)
            return Response({s.data})
        else:
            return Response(
                s.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def post(self, request):
        s = AddMessageSerializer(
            data = request.POST,
            context = {
                'user': request.user
            }) 
        if s.is_valid():  
            s.save() 
            r = {
                'message': 'Message saved!'
            }
            return Response(r)
        else:
            print(s.errors)
            return Response({
                'message': 'Your request is invalid!',
                'errors': s.errors
            }, status = status.HTTP_400_BAD_REQUEST)



def login_required(function):
    def wrapper(r):
        if not r.user.is_authenticated:
            return JsonResponse({
             'message': 'Send login request'
            }, status = 401)
        else:
            return function(r)
    return wrapper

@login_required
def add_message(request):
    s = AddMessageSerializer(
        data = request.POST,
        context = {
            'user': request.user
        }) 
    if s.is_valid():  
        s.save() 
        r = {
            'message': 'Message saved!'
        }
        return JsonResponse(r)
    else:
        print(s.errors)
        return JsonResponse({
            'message': 'Your request is invalid!',
            'errors': s.errors
        }, status = 400)

def message_list(request):
    if request.method != 'GET':
        return JsonResponse({
            'message': 'Method not allowed!'
        }, status=405)
    if 'conversation' not in request.GET:
        return JsonResponse({
            'message': 'please send conversation id'
        }, status=400)
    c = Conversation.objects.get(
        id=request.GET['conversation']
    )
    messages = Messages.objects.filter(
        conversation=c
    )
    s = MessageSerializer(messages, many = True)
    # messages_list = []
    # for m in messages:
    #     messages_list.append(
    #         {
    #             'text': m.text,
    #             'sender': {
    #                 'first_name': m.sender.first_name,
    #                 'last_name': m.sender.last_name,
    #                 'id': m.sender.id
    #             },
    #             'date': m.date,
    #         }
    #     )

    d = {
        'messages': s.data
    }
    return JsonResponse(d)


def conversation_list(request):
    s = ConversationSerializer(Conversation.objects.all(), many = True)
    return JsonResponse({'conversations': s.data})