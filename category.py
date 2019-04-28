__author__ = 'mohit'

import sys
import urlparse
from pprint import pprint
from google.protobuf import text_format

SEPARATOR = " :"
from login import *
from googleplay import GooglePlayAPI

api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD)
response = api.browse()

print SEPARATOR.join(["ID", "Name"])
for c in response.category:
   print SEPARATOR.join(i.encode('utf8') for i in [urlparse.parse_qs(c.dataUrl)['cat'][0], c.name])
