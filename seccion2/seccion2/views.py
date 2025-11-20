from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    """Redirect root URL to the productos app 'inicio' view.

    This keeps a single canonical landing page at /productos/ while
    keeping the project root available.
    """
    return redirect('inicio')