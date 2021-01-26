"""
Waffle flags and switches to change user API functionality.
"""


from django.utils.translation import ugettext_lazy as _

from edx_toggles.toggles import LegacyWaffleSwitchNamespace

SYSTEM_MAINTENANCE_MSG = _(u'System maintenance in progress. Please try again later.')
WAFFLE_NAMESPACE = u'user_api'

# Switches
ENABLE_MULTIPLE_USER_ENTERPRISES_FEATURE = u'enable_multiple_user_enterprises_feature'
ENABLE_MULTIPLE_SSO_ACCOUNTS_ASSOCIATION_TO_SAML_USER = u'enable_multiple_sso_accounts_association_to_saml_user'


def waffle():
    """
    Returns the namespaced, cached, audited Waffle class for user_api.
    """
    return LegacyWaffleSwitchNamespace(name=WAFFLE_NAMESPACE, log_prefix=u'UserAPI: ')
