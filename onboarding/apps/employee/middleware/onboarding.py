import logging

from django.shortcuts import redirect, HttpResponseRedirect
from django.urls.base import reverse
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------
# BaseMiddlewareOnboarding
# -------------------------------------------------------------------------------
class MiddlewareOnboarding:

    # ---------------------------------------------------------------------------
    # __init__
    # ---------------------------------------------------------------------------
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    # ---------------------------------------------------------------------------
    # __call__
    # ---------------------------------------------------------------------------
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        self.request = request
        self.user = request.user

        logger.debug('Requested path: %s', self.request.path)

        # we want superuser and staff to bypass onboarding
        if self.user.is_staff:
            logger.debug('User %s is staff. Skipping onboarding.', self.user)
            return self.get_response(request)


        # only authenticated users can onboard
        if self.user.is_authenticated:
            # ModelEmployee.
            if
            url = self.request.path.split('/')[1]
            uuid = self.request.path.split('/')[2]
            user = self.user

            # onboarding can only be performed by users who have not yet onboarded
            # if url == 'onboarding-login':

            # data = ModelEmployee.objects.get(user=self.user)
            # slug = data.slug

            d = self.process_onboarding()
            print('=======================', d)
            return d
            '''
            if slug == 'welcome':
                return redirect(reverse('employee:login', kwargs={'id': uuid}))

            if slug == 'role':
                return redirect(reverse('employee:roles-and-responsiblity', kwargs={'id': uuid}))

            if slug == 'personal':
                return redirect(reverse('employee:personal-info', kwargs={'id': uuid}))

            if slug == 'family':
                return redirect(reverse('employee:family-infoity', kwargs={'id': uuid}))

            if slug == 'emergency':
                return redirect(reverse('employee:emergency-contact', kwargs={'id': uuid}))

            if slug == 'document':
                return redirect(reverse('employee:document-info', kwargs={'id': uuid}))

            if slug == 'drug-declaration':
                return redirect(reverse('employee:drug-declaration', kwargs={'id': uuid}))
            '''


            # if slug == 'role':
            #     response = HttpResponseRedirect('/bank-details')
                # return redirect(reverse('employee:bank-details', kwargs={'id': uuid}))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    # ---------------------------------------------------------------------------
    # process_onboarding
    # ---------------------------------------------------------------------------
    def process_onboarding(self):
        """
        Continue onboarding.
        """
        redirect_url = '/'
        page = 'home'
        data = ModelRedirectUrl.objects.get(user=self.user.id)
        print('..../././...................', data.personal_info, self.user.id)
        uuid = self.request.path.split('/')[2]
        if data.roles_responsibility == False:
            return redirect(reverse('employee:roles-and-responsiblity', kwargs={'id': uuid}))

        if data.personal_info == False:
            return redirect(reverse('employee:personal-info', kwargs={'id': uuid}))

        if data.family_info == False:
            return redirect(reverse('employee:family-info', kwargs={'id': uuid}))

        if data.emergency_contact == False:
            return redirect(reverse('employee:emergency-contact', kwargs={'id': uuid}))

        if data.document_gathering == False:
            return redirect(reverse('employee:document-info', kwargs={'id': uuid}))

        if data.drug_declaration == False:
            return redirect(reverse('employee:drug-declaration', kwargs={'id': uuid}))

        if data.bank_detail == False:
            return redirect(reverse('employee:bank-details', kwargs={'id': uuid}))

        logger.debug(
            'Onboarding incomplete. Redirecting to %s page.', page
        )

        return redirect(redirect_url)
