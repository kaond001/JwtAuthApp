from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import NoteSerializer, ContactSerializer
from Auth.models import Note, Contact
from rest_framework.pagination import PageNumberPagination
# import logging
# from .pagnation import  LargeResultsSetPagination


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoutes(request):
    routes = ['api/token', 'api/token/refresh']

    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNote(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Contact_list(request):
    if request.method == 'GET':
        user = request.user
        paginator = PageNumberPagination()
        query_set = Contact.objects.filter(userId=user.id)
        context = paginator.paginate_queryset(query_set, request)
        Contact_serializer = ContactSerializer(context, many=True)
        return paginator.get_paginated_response(Contact_serializer.data)

    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(contact_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contact_detail(request, pk):
    try: 
        contact = Contact.objects.get(pk=pk) 
    except Contact.DoesNotExist: 
        return JsonResponse({'message': 'The contact does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        contact_serializer = ContactSerializer(contact) 
        return JsonResponse(contact_serializer.data) 
 
    elif request.method == 'PUT': 
        contact_data = JSONParser().parse(request) 
        contact_serializer = ContactSerializer(contact, data=contact_data) 
        if contact_serializer.is_valid(): 
            contact_serializer.save() 
            return JsonResponse(contact_serializer.data) 
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        contact.delete() 
        return JsonResponse({'message': 'Contact was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
     

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def House_list(request):
#     if request.method == 'GET':
#         paginator = PageNumberPagination()
#         query_set = MyModel.objects.all()
#         context = paginator.paginate_queryset(query_set, request)
#         serializer = MyModelSerializer(context, many=True)
#         return paginator.get_paginated_response(serializer.data)

#     elif request.method == 'POST':
#         contact_data = JSONParser().parse(request)
#         contact_serializer = ContactSerializer(data=contact_data)
#         if contact_serializer.is_valid():
#             contact_serializer.save()
#             return JsonResponse(contact_serializer.data,
#                                 status=status.HTTP_201_CREATED)
#         return JsonResponse(contact_serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
