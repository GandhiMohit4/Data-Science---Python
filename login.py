__author__ = 'mohit'

print("Please provide your google account details")

LANG = "en-US"
ANDROID_ID = "33649F125C7E151D"
GOOGLE_LOGIN = "mohit411993@gmail.com"
GOOGLE_PASSWORD = "sachidanand"
if any([tout == None for tout in[ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("Login details are missing in login.py")
else:
    print ("Login Successful")

