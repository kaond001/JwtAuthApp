from rest_framework.serializers import ModelSerializer
from Auth.models import Note ,Contact



class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields ='__all__'


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact

        fields = ['id', 'userId', 'area', 'city', 'email', 'country', 'phone', 'created_on', 'status']



 