__author__ = 'mohit'
SEPARATOR= ':'
import sys

from login import *
from googleplay import GooglePlayAPI
from information import *
#from download import *
package = [];
i = 0
if len(sys.argv) < 2:
    print "Usage: %s category [subcategory] [nb_results] [offset]" % sys.argv[0]
    print "List subcategories and apps within them."
    print "category: To obtain a list of supported catagories, use categories.py"
    print "subcategory: You can get a list of all subcategories available, by supplying a valid category"
    sys.exit(0)

packagename = sys.argv[1]
filename = None
nb_results = None
offset = None

if (len(sys.argv) >= 3):
    filename = sys.argv[2]
if (len(sys.argv) >= 4):
    nb_results = sys.argv[3]
if (len(sys.argv) == 5):
    offset = sys.argv[4]

api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD)
try:
    message = api.list(packagename, filename, nb_results, offset)
except:
    print "Error: HTTP 500 - one of the provided parameters is invalid"

if (filename is None):
    print SEPARATOR.join(["Subcategory ID", "Name"])
    for doc in message.doc:
        print SEPARATOR.join([doc.docid.encode('utf8'), doc.title.encode('utf8')])
else:
    topline()
    doc = message.doc[0]
    i=0
    for c in doc.child:
         ia = app_info(c);
         package.append(ia);