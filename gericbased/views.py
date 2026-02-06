from django.urls import reverse_lazy
from classbased.models import Book
from django.views import generic

class BookCreateView(generic.CreateView):
    model = Book
    fields = ['order','title', 'author', 'price']
    template_name = "classbased/book_form.html"
    success_url = reverse_lazy('book_list')


class BookListView(generic.ListView):
    model = Book
    template_name = "classbased/book_list.html"
    context_object_name  = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "classbased/book_detail.html"


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['order','title', 'author', 'price']
    template_name = "classbased/book_form.html"
    success_url = reverse_lazy('book_list')


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'classbased/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
