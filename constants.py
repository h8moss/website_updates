import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
CONF_PATH = CURRENT_DIR + '\\conf.txt'
LAST_DAY_PATH = CURRENT_DIR + '\\last_day.txt'
LAST_RESPONSE_PATH = CURRENT_DIR + '\\last_response.txt'
LOG_PATH = CURRENT_DIR + '\\.log'

with open(CONF_PATH, 'r') as f:
    global WEBSITE
    global USERNAME
    global PASSWORD
    global TARGET_MAILS

    text = f.read()
    text = text.split('\n')
    WEBSITE = text[0]
    USERNAME = text[1]
    PASSWORD = text[2]
    TARGET_MAILS = text[3:]
