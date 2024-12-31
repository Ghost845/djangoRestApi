from django.contrib.auth import get_user_model
from permissions import IsAuthorOrReadOnly
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api_app.serializers import NoteSerializer, ThinSerializer, UserSerializer
from notes.models import Note


class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def list(self, request, *args, **kwargs):
        notes = Note.objects.all()
        context = {'request': request}
        serializer = ThinSerializer(notes, many=True, context=context)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# CBV APIView
# class NoteListView(APIView):
#     def get(self, request, format=None):
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThinSerializer(notes, many=True, context=context)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class NotesDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Note.objects.get(pk=pk)
#         except Note.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         note = self.get_object(pk)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# FBV:
# @api_view(['GET', 'POST'])
# def notes_list(request, format=None):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def notes_detail(request, pk=None, format=None):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = NoteSerializer(note, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
