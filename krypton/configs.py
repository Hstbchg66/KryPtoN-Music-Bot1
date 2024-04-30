HEROKU = False # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = environ["SUDO_CHAT_ID"]
    SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 20212768
    API_HASH = "763f10232d31864558eebb107630b9e1"
    SUDO_CHAT_ID = "2084002979"


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
