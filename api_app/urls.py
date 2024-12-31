from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from api_app.views import NoteViewSet

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
urlpatterns = router.urls

# urlpatterns = [
#     path('notes/', NoteListView.as_view(), name='notes-list'),
#     path('notes/<int:pk>/', NotesDetailView.as_view(), name='notes-detail'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
