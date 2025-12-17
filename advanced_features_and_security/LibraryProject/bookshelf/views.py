from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

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