import os
class Config (object):
    """define app configurations"""
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard-to-guess'