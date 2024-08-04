# from django.utils.deprecation import MiddlewareMixin
# from rest_framework.authtoken.models import Token
#
#
# class TokenAuthMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         print("Processing request in middleware.")
#         auth_token = request.COOKIES.get("authtoken")
#
#         if auth_token:
#             try:
#                 token = Token.objects.get(key=auth_token)
#
#                 request.user = token.user
#                 request.auth = token
#
#                 print(f"Authenticated user -> {request.user}")
#
#             except Token.DoesNotExist:
#                 print("Token does not exists.")
#                 request.user = None
#
#         else:
#             print("No authtoken in cookies.")
#             request.user = None
