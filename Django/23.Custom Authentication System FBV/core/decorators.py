from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden

def login_and_role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # First check login
            if not request.user.is_authenticated:
                return login_required(view_func)(request, *args, **kwargs)
            # Then check role
            user = request.user
            if required_role == "customer" and not getattr(user, "is_customer", False):
                return HttpResponseForbidden("Not accessible")
            if required_role == "seller" and not getattr(user, "is_seller", False):
                return HttpResponseForbidden("Not accessible")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator