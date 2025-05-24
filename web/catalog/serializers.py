from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime
from catalog.models import Artist, Album, Song


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class ArtistSerializer(serializers.ModelSerializer):
    """
    Automatically created PK field (ex: id: 1)
    """
    class Meta:
        model = Artist
        fields = '__all__'
        
class ArtistHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    """
    Set a url field instead of a pk field (ex: url: 'http://api.example.com')
    """

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        
class Song(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__ ' 