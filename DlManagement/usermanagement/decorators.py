from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def staff_redirect(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return redirect(reverse('admin:index'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view