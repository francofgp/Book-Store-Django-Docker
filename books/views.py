from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView

from .models import Book
from django.db.models import Q


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):  # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    #queryset = Book.objects.filter(title__icontains='dracula')
    # Asi sobreescribimos el queryset para tener mas flexibilidad
    # "|" significa OR"
    def get_queryset(self):
        # Esa "q" esta en el HTML  y es el name del input
        # de la busqueda
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
