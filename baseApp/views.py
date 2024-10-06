from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Developers, Company
from .serializers import DevelopersSerializers, CompanySerializers
from django.db.models import Q # Q for complex Queries

# Create your views here.

# this function create the APIs urls
@api_view(['GET'])
def endpoints(request):
    data = ['/developers', 'developers/username']
    return Response(data) # safe = False means it disables dictionaries

@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def developers_list(request):

    # handling GET requests
    if request.method == 'GET':
        query = request.GET.get('query') # creating a query search to show data that contains the entered string
        # print('Query:', query)

        if query == None:
            query = ''

        # use Q to check whether the entered query is contained in the username or bio
        developers = Developers.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = DevelopersSerializers(developers, many=True) # many=True mean we are converting many fields
        return Response(serializer.data)

    if request.method == 'POST':
        developer = Developers.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = DevelopersSerializers(developer, many=False)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def developer_details(request, username):

    developer = Developers.objects.get(username=username)

    if request.method == 'GET':
        serializer = DevelopersSerializers(developer, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        developer.username = request.data['username']
        developer.bio = request.data['bio']

        developer.save()
        serializer = DevelopersSerializers(developer, many=False)

        return Response(serializer.data)

    if request.method == 'DELETE':
        developer.delete()
        return Response('User was deleted!!')



##### company view api functions ####
@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializers(companies, many=True)
    return Response(serializer.data)