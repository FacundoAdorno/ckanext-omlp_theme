import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from pylons import config


def getGoogleAnalyticsID():
    ##Load GoogleAnalytics ID into config
    return config.get('omlp_theme.googleanalytics.id', '')

class Omlp_ThemePlugin(plugins.SingletonPlugin):
    # IConfigurer
    plugins.implements(plugins.IConfigurer)
    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'omlp_theme')

    def get_helpers(self):
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'omlp_theme_googleanalytics_id': getGoogleAnalyticsID}

