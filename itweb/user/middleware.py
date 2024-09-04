from django.shortcuts import redirect

class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            path = request.path
            if path == '/news/':
                return redirect('usernews')
            elif path == '/authors/':
                return redirect('usereauthors')
            elif path == '/quotes/':
                return redirect('userquotes')
        
        return response