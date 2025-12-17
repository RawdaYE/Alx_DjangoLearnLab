from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.



@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
        return HttpResponse("Books list page")

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
        return HttpResponse("Add book page")
    

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
        return HttpResponse("Edit book page")
    

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
        return HttpResponse("Delete book page")


def example_form_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        # You could process the data here
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        # Example: just render back a success message
        return render(request, 'bookshelf/form_example.html', {'form': form, 'success': True})

    return render(request, 'bookshelf/form_example.html', {'form': form})