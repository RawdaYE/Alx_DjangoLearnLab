from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

#implementing role-based views
def is_librarian(user):
    return user.userprofile.role == "librarian"

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')



