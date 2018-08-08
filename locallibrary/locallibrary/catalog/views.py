from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views import generic

# Create your views here.

def index(request):
    """View function for home page of site"""

    #Generate counts of some of main objects
    num_books = Book.objects.all().count();
    num_instances = BookInstance.objects.all().count();

    #Available books(status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count();

    #The 'all()' is implied by default.
    num_authors = Author.objects.count();

    #Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0);
    request.session['num_visits'] = num_visits + 1;

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    #Render the HTML template index index.html with the data in the context variable
    return render(request, 'index.html', context = context)

class BookListView(generic.ListView):
    model = Book;
    # paginate_by = 1;

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs);
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data';
        return context;


class BookDetailView(generic.DetailView):
    model = Book;

    def book_detail_view(request):
        try:
            book = Book.objects.get(pk = primary_key);
        except Book.DoesNotExist:
            raise Http404('Book does not exist.');
        return render(request, 'catalog/book_detail.html', context = {'book': book});

class AuthorListView(generic.ListView):
    model = Author;

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs);
        context['some_data'] = 'This is just some date';
        return context;

class AuthorDetailView(generic.DetailView):
    model = Author;

    def author_detail_view(request):
        try:
            author = Author.objects.get(pk = primary_key);
        except Book.DoesNotExist:
            raise Http404('Book does not exist.');
        return render(request, 'catalog/author_detail.html', context = {'author': author});
