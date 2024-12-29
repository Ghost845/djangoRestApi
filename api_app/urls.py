from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from api_app.views import *

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='notes-list'),
    path('notes/<int:pk>/', NotesDetailView.as_view(), name='notes-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)