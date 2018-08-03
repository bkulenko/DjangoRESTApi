from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest.models import Movie, Comment
from rest.serializers import MovieSerializer, CommentSerializer
import requests, json

@csrf_exempt
def movie_controller(req):

    if req.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    if req.method == "POST":
        reqbody = json.loads(req.body.decode('utf-8'))
        response = (requests.get('http://omdbapi.com/?t={}&apikey={}'.format(reqbody['name'], settings.OMDBKEY))).json()
        print(type(response))
        #data = JSONParser().parse(json.load(response))
        serializer = MovieSerializer(data=response)
        if serializer.is_valid() and Movie.objects.filter(imdbID=response['imdbID']).count()==0:
            serializer.save()
            return JsonResponse(serializer.validated_data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def comment_controller(req):

    if req.method=='POST':
        reqbody = json.loads(req.body.decode('utf-8'))
        serializer = CommentSerializer(data=reqbody)
        if serializer.is_valid() and Movie.objects.filter(imdbID=reqbody['Movie']).count()!=0:
            serializer.save()
            return JsonResponse(serializer.validated_data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    if req.method=='GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def comment_detail(req, movieid):
    if req.method == 'GET':
        comments = Comment.objects.filter(Movie=movieid)
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
