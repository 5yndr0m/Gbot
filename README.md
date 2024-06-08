# Gbot
Trying to build a bot to manage google drive using google api and python

# .env file
SERVICE_ACCOUNT_FILE = place the path to google service_account_details.json here
PARENT_FOLDER_ID = google drive folder this acount can operate. obtain from url

# fyi
this does not use 0auth from google. instead it use an service account which we have to give
permission to work in our drive space.
decided to resort to this method for now because authentication kept trowing errors at me.

* will update on how to create service account and other requirements
