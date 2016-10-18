import os

app_config = {
    'DEBUG': bool(os.getenv('DEBUG', True)),
    'REDIS_DB': int(os.getenv('REDIS_DB', 1)),
    'REDIS_HOST': os.getenv('REDIS_HOST', '127.0.0.1'),
    'REDIS_PORT': int(os.getenv('REDIS_PORT', 6379)),
    'REDIS_PW': os.getenv('REDIS_PW', None),
    'SERVER_HOST': os.getenv('SERVER_HOST', '0.0.0.0'),
    'SERVER_PORT': int(os.getenv('SERVER_PORT', 5000))
}
