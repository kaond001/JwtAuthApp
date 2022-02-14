from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view ,permission_classes
from  .serializers import NoteSerializer
from Auth.models import Note
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
