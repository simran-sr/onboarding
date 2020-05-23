from django.urls.conf import path
from onboarding.apps.employee.views.home import ViewHome
# from onboarding.apps.employee.views.login import ViewAutoLoginOnboard

urlpatterns = [
    
    # path('onboard-login/<uuid:id>', 
    #      ViewAutoLoginOnboard.as_view(), 
    #      name='login'
    # ),

    path('', 
         ViewHome.as_view(), 
         name='home'
    ),
]