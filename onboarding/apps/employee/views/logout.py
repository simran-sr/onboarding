from django.contrib.auth import logout
from django.views.generic import RedirectView

class ViewLogout(RedirectView):
    """
    A view that logout user and redirect to homepage.
    """
    permanent = False
    query_string = True
    pattern_name = '/'

    def get_redirect_url(self, *args, **kwargs):
        """
        Logout user and redirect to target url.
        """
        print("ssss-- ", self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(ViewLogout, self).get_redirect_url(*args, **kwargs)