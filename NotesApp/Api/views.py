from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from Api import serializers
# Create your views here.

@api_view(['GET'])
def getRouters(request):
    
    #here, routes are defined and their urls by endpoints and method
    #description tells us for what pupose the route is used
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]


  #  return JsonResponse(routes,safe=False)

    return Response(routes)


# for getting notes from database admin
#it will take notes and serialize them then send data as response

@api_view(['GET','POST'])
def getNotes(request):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('-updated')
        seralizer = NoteSerializer(notes,many=True)
        return Response(seralizer.data)
    
    if request.method == 'POST':
        data =request.data
        note = Note.objects.create(
            body = data['body']
        )
        serializer = NoteSerializer(note,many=False)
        return Response(serializer.data)


# it will just get specific note, not all as we have specified cond.
@api_view(['GET','PUT','DELETE'])
def getNote(request,pk):
    
    if request.method == 'GET':
        note = Note.objects.get(id=pk)
        seralizer = NoteSerializer(note,many=False)
        return Response(seralizer.data)

    if request.method == 'PUT':
        data = request.data
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note,data=data)
    
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    if request.method == 'DELETE':
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('Note was deleted')



#create new note
# @api_view(['POST'])
# def createNote(request):
#     data =request.data
#     note = Note.objects.create(
#         body = data['body']
#     )
#     serializer = NoteSerializer(note,many=False)
#     return Response(serializer.data)
#here we find obj and then take new data and pass it and update it
#with Serializer and save it
# @api_view(['PUT'])
# def updateNote(request,pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note,data=data)
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# #it will delete note
# @api_view(['DELETE'])
# def deleteNote(request,pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted')


