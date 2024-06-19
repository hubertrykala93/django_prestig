from django.middleware.csrf import get_token


def generate_token(request) -> dict:
    """
    Generating CSRF middleware tokens for all forms in the project.

    Parameters
    ----------
        request: django.core.handlers.wsgi.WSGIRequest

    Returns
    ----------
        dict
    """
    return {
        "csrf_token": get_token(request=request)
    }
