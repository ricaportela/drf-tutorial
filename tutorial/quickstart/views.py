from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def especies(request, taxon):
    # taxon = "Handroanthus" # parametro de pesquisa
    # url = "http://api.gbif.org/v1/species/search?q=Handroanthus"
    # response = requests.get(url)
    especies = 'Teste1'
    context = {'especies': especies}
    return render(request, 'especies.html', context)
