from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
 
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
 
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return
 
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'https://sarumen.com/callback'
    client_class = OAuth2Client
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)