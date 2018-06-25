

class BaseConfig(object):
    """common configurations that are common across all environments"""
    CSRF_ENABLED =True
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    """development configurations
       setting Testing to True activates the testing mode of Flask extensions. """

    Testing = True
    """setting this to True activates the debug mode on the app"""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    Production configurations

    """

    Debug =False
    Testing =False

app_config= {
    'development':DevelopmentConfig,
    'production':ProductionConfig

    }