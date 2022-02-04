from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Newsletter

class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'
    
class CreateNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('name', 'description', 'target', 'tags', 'author')


class ViewNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id', 'name', 'description', 'target', 'tags', 'author')