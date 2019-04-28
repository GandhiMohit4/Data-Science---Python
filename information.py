__author__ = 'mohit'

separator = ':'
def size_app(s):
    for unit in ['Bytes', 'KB', 'MB', 'GB']:
        if s>=1024 :
            s/=1024
        return "%3.1f%s" % (s, unit)

def topline():
    l =  ["Title",
         "Package",
         "Price",
         "Size" ]
    print separator.join(l)

def app_info(c):
    info = [c.title, c.docid,c.offer[0]. formattedAmount,size_app(c.details.appDetails.installationSize)]
    print separator.join(unicode(i).encode('utf8') for i in info)
    return info[1] ;



