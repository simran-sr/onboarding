from django.apps.config import AppConfig


#-------------------------------------------------------------------------------
# ConfigEmployee
#-------------------------------------------------------------------------------
class ConfigAccount(AppConfig):

    name = 'onboarding.apps.employee'
    label = 'employee'
    verbose_name = 'Employee Management'
    verbose_name_plural = 'Employee Management'
    