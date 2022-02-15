from operator import mod
from pyexpat import model
from attr import field, fields
from rest_framework.serializers import ModelSerializer
from base.models import Note


class NoteSerializer(ModelSerializer):
  class Meta:
    model =Note
    fields='__all__'