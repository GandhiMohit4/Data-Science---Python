__author__ = 'mohit'

import sys
from login import *
from googleplay import GooglePlayAPI
from information import *
from list_apps import *

#if (len(sys.argv) < 2):
 #   print "Usage: %s packagename [filename]"
  #  print " Download information not available"
   # sys.exit(0)

#packagename = sys.argv[1]

#if (len(sys.argv) == 3):
 #   filename = sys.argv[2]
#else:
 #   filename = packagename + ".apk"

# Connect
api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD)
for packagename in package:
    #packagename=package[c]
 #   print(packagename)
    file=packagename + ".apk"
# Get the version code and the offer type from the app details
    m = api.details(packagename)
    doc = m.docV2
    vc = doc.details.appDetails.versionCode
    ot = doc.offer[0].offerType

#for c in packag

# Download
    print "Downloading %s..." % size_app(doc.details.appDetails.installationSize),
    data = api.download(packagename, vc, ot)
    open(file, "wb").write(data)
    print "Done"
