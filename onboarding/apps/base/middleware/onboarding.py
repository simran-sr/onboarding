import logging

from django.shortcuts import redirect
from django.urls.base import reverse


logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
# BaseMiddlewareOnboarding
#-------------------------------------------------------------------------------
class BaseMiddlewareOnboarding:
    """
    Handles onboarding checks for all types of entities, like company, fund,
    etc. If an entity fails an entity check, then it must be redirected
    to the appropriate url.
    """
    
    #---------------------------------------------------------------------------
    # __init__
    #---------------------------------------------------------------------------
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    #---------------------------------------------------------------------------
    # __call__
    #---------------------------------------------------------------------------
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
        
        # Check if the url path needs to be ignored
        if any([self.path_in_exempt_urls, self.path_in_exempt_url_patterns]):
            
            logger.debug(
                (
                    'Requested path: %s is exempt from onboarding '
                    'checks. Skipping...'
                ), 
                self.request.path
            )
            
            return self.get_response(request)
        
        # only authenticated users can onboard
        if self.user.is_authenticated:
            
            self.entity = self.request.user.active_entity
            
            # onboarding can only be performed by users who have not yet onboarded
            if not self.user.has_onboarded:
                
                if not self.user.is_email_verified:
                    logger.debug('Email not verified for %s', self.user)
                    return redirect(
                        reverse('account:resend-email-verification')
                    )

                if self.user.is_member:
                    return self.process_member_onboarding()
                
                # continue onboarding if the user is part of a fund
                if self.entity.entity_type == 'fund':
                    
                    # redirect only if the investor has started the onboarding
                    # process
                    if not self.entity.onboarding_started:
                        return self.get_response(request)
                        
                    return self.process_fund_onboarding()
                
                # continue onboarding if the user is part of a company
                if self.entity.entity_type == 'company':
                    return self.process_company_onboarding()
        
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    #---------------------------------------------------------------------------
    # path_in_exempt_urls
    #---------------------------------------------------------------------------
    @property
    def path_in_exempt_urls(self):
        """
        Tests if a path is in the list of urls that are exempt from onboaring
        checks. Returns True if the url is an exempt url else return False.
        """
        

        return self.request.path in exempt_urls
        exempt_urls = [
            reverse('logout'),
            reverse('account:login'),
            reverse('account:onboarding-roles-and-responsiblity'),
            reverse('account:onboarding-personal-info'),
            reverse('account:onboarding-family-info'),
            reverse('account:onboarding-document-info'),
            reverse('account:onboarding-drug-declaration'),
            reverse('account:onboarding-banking-info'),
        ]

    #---------------------------------------------------------------------------
    # path_in_exempt_url_patterns
    #---------------------------------------------------------------------------
    @property
    def path_in_exempt_url_patterns(self):
        """
        Tests if a path matches url patterns that are exempt from onboaring
        checks. Returns True if the url is an exempt pattern else return False.        
        """
        
        ignore_patterns = [
            '/favicon.ico', '/media/', '/static/', '/api/', '/connect-request/', 
            '/connect-invite/', '/confirm-payment-method/',
            '/update-payment-method/', 
        ]
        
        for pattern in ignore_patterns:
            if self.request.path.startswith(pattern):
                return True
    
        return False        
    
    #---------------------------------------------------------------------------
    # process_member_onboarding
    #---------------------------------------------------------------------------
    def process_member_onboarding(self):
        """
        Continue onboarding for a member.
        """
        
        redirect_url = '/'
        page = 'home'        
        
        if not self.user.is_profile_complete:
            page = 'create profile'
            redirect_url = reverse('account:onboarding-create-member-profile')
            
        logger.debug(
            'Onboarding incomplete. Redirecting to %s page.', page
        )
        
        return redirect(redirect_url)    
    
    #---------------------------------------------------------------------------
    # process_company_onboarding
    #---------------------------------------------------------------------------
    def process_company_onboarding(self):
        """
        Continue onboarding for a company.
        
        1. Profile should be complete.
        2. Must have uploaded a presentation deck.
        3. Must have completed billboard.
        4. The presentation deck must have completed converting.
        5. Must have completed outpost.
        """
        
        redirect_url = '/'
        page = 'home'
        
        if not self.entity.is_profile_complete:
            page = 'create profile'
            redirect_url = reverse('account:onboarding-create-profile')
        
        elif not self.entity.is_deck_uploaded:
            page = 'upload deck'
            redirect_url = reverse('account:onboarding-upload-deck')

        elif not self.entity.is_billboard_complete:
            page = 'create billboard'
            redirect_url = reverse('account:onboarding-create-billboard')
        
        elif not self.entity.is_outpost_complete:
            
            if not self.entity.is_deck_converted:
                page = 'deck conversion status'
                redirect_url = reverse(
                    'account:onboarding-deck-conversion-status'
                )
            else:
                page = 'deck conversion status'
                redirect_url = reverse('account:onboarding-create-outpost')
        
        logger.debug(
            'Onboarding incomplete. Redirecting company to %s page.', page
        )
        
        return redirect(redirect_url)
    
    #---------------------------------------------------------------------------
    # process_fund_onboarding
    #---------------------------------------------------------------------------
    def process_fund_onboarding(self):
        """
        Continue onboarding for a Fund.
        
        1. Must have completed profile.
        2. Must have completed billboard.
        3. Must have completed triggers, if required.
        4. Must have completed introductions.
        5. Must have completed team members.

        """
        
        redirect_url = reverse('account:onboarding-completed')
        page = 'home'
        
        if not self.entity.is_profile_complete:
            page = 'create profile'
            redirect_url = reverse('account:onboarding-create-profile')
         
        elif not self.entity.is_billboard_complete:
            page = 'create billboard'
            redirect_url = reverse('account:onboarding-create-billboard')

        elif not self.entity.is_bypass_triggers and not self.entity.is_triggers_complete:
            page = 'create triggers'
            redirect_url = reverse('account:onboarding-create-triggers')
            
        elif not self.entity.is_bypass_introductions and not self.entity.is_introductions_complete:
            page = 'create introductions'
            redirect_url = reverse('account:onboarding-create-introductions')

        elif not self.entity.is_team_complete:
            page = 'create team'
            redirect_url = reverse('account:onboarding-create-team')
            
        
        logger.debug(
            'Onboarding incomplete. Redirecting fund to %s page.', page
        )
        
        return redirect(redirect_url)
    
    