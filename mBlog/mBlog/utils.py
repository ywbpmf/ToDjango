from django.core.cache import cache
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from hashlib import md5
import logging
import _thread

logger = logging.getLogger('mBlog')

def get_max_articleid_commentid():
