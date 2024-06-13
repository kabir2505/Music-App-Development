

class Config(object):
    DEBUG = False
    TESTING = False
    CACHE_TYPE="RedisCache"
    CACHE_DEFAULT_TIMEOUT=300


class DevelopmentConfig(Config):
    DB_NAME="database.db"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=f'sqlite:///{DB_NAME}'
    SECURITY_PASSWORD_SALT = "thisissaltt"
    SECRET_KEY='sjfkjsdfkjsdf'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    WTF_CSRF_ENABLED=False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    CACHE_REDIS_HOST="localhost"
    CACHE_REDIS_PORT=6379
    CACHE_REDIS_DB=3
    WHOOSH_BASE='whoosh'
  
    