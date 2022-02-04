from os import stat
from django.shortcuts import render
from .serializers import NewsletterSerializer, CreateNewsletterSerializer
from .models import Newsletter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status, permissions
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
# Create your views here.

class NewsLetterViewSet(ModelViewSet):
    permissions_classes = (IsAdminOrReadOnly,)
    # permissions_classes = (permissions.IsAuthenticated,)
    # permissions.DjangoModelPermissions
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return CreateNewsletterSerializer
        return NewsletterSerializer

    def get_queryset(self):
        filter = self.request.query_params.get('tag')
        if filter:
            newsletters = self.queryset.filter(
                tags__slug__contains=filter
            )
            return newsletters
        return self.queryset

    @action(methods=['PATCH'], detail=True)
    def vote(self, request, pk=None):
        user = request.user
        id = user.id
        newsletter = self.get_object()
        votes = newsletter.voters.all()
        if user in votes:
            newsletter.voters.remove(id)
            return Response(status=status.HTTP_200_OK, data={
                'vote': 'The vote was remove'
            })
        newsletter.voters.add(id)
        return Response(status=status.HTTP_200_OK, data = {
            'vote': 'The vote was add'
        })
    
    @action(methods=["PATCH"], detail=True)
    def subscribe(self, request, pk=None):
        user = request.user
        id = user.id
        newslettter = self.get_object()
        users = newslettter.members.all()
        if newslettter.target <=  len(newslettter.voters.all()):
            if user in users:
                newslettter.members.remove(id)
                return Response(status=status.HTTP_200_OK, data={
                    "subscibre": "The subscribe was removed"
                })
            newslettter.members.add(id)
            return Response(status=status.HTTP_200_OK, data={
                    "subscibre": "The subscribe was add"
                })
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={
            "message": "El boletin no ha alcanzado lso votos suicientes"
        })