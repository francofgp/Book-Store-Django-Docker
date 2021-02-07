from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),

    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    # no usamos esto porque en lugar usamos el UUID
    # path('<int:pk>', BookDetailView.as_view(), name='book_detail'),  # new
]
