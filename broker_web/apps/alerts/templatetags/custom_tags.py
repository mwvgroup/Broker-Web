from base64 import b64encode
from warnings import warn

from django import template

register = template.Library()


@register.filter
def bin_2_utf8(_bin):
    """Convert binary data to UTF8"""

    try:
        if _bin is not None:
            return b64encode(_bin).decode('utf-8')

    except Exception as e:
        warn(str(e))
