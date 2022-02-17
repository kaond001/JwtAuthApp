from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view ,permission_classes
from  .serializers import NoteSerializer , ContactSerializer
from Auth.models import Note , Contact
from rest_framework.pagination import PageNumberPagination
# import logging
# from .pagnation import  LargeResultsSetPagination

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoutes(request):
    routes =[
        'api/token',
        'api/token/refresh'
    ]

    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNote(request):
    user =request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return  Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Contact_list(request):
    if request.method == 'GET':
        user =request.user
        paginator = PageNumberPagination()
        query_set = Contact.objects.filter(userId=user.id)
        # contact = Contact.objects.filter(userId=user.id)
        context = paginator.paginate_queryset(query_set, request)
        Contact_serializer = ContactSerializer(context, many=True)
        # ContactSerializer(contact, many=True)
        return paginator.get_paginated_response(Contact_serializer.data)

    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def my_function_based_list_view(request):
#     paginator = PageNumberPagination()
#     query_set = MyModel.objects.all()
#     context = paginator.paginate_queryset(query_set, request)
#     serializer = MyModelSerializer(context, many=True)
#     return paginator.get_paginated_response(serializer.data)
