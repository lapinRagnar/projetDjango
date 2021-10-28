# urls.py
from django.urls import path
from books.views import PublisherListView, PublisherBookListView

urlpatterns = [
    path('publishers/', PublisherListView.as_view()),
    path('books/<publisher>/', PublisherBookListView.as_view()),
]

