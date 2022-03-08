import datetime
import requests
import smtplib
import ssl
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


def generate_log(old_data, new_data, equal):
    target = ''
    if (len(TARGET_MAILS) > 3):
        for _target in TARGET_MAILS[:3]:
            target += str(_target) + ' ,'
        target = target[:-1]
        target += f'and {len(TARGET_MAILS) - 3} more'
    else:
        for _target in TARGET_MAILS:
            target += str(_target) + ' ,'
        target = target[:-1]

    date = str(datetime.datetime.today())
    textA = f'''\

{date}
SENT UPDATE TO {target} FROM {USERNAME}

OLD DATA:
{old_data}

NEW DATA:
{new_data}

--------------------------------------------------------------------------------
'''
    textB = f'''\

{date}
DATA DID NOT CHANGE; DID NOT SEND MAIL

--------------------------------------------------------------------------------
'''

    with open(LOG_PATH, 'a') as f:
        if (not equal):
            f.write(textA)
        else:
            f.write(textB)


def get_data():
    r = requests.get(WEBSITE)
    return r.text


def get_old_data():
    data = ''
    with open(LAST_RESPONSE_PATH, 'r') as f:
        data = f.read()
    return data


def update_data(data):
    current_day = datetime.datetime.today().day
    with open(LAST_DAY_PATH, 'w+') as f:
        f.write(str(current_day))

    with open(LAST_RESPONSE_PATH, 'w+') as f:
        f.write(str(data))


def compare_day():
    current_day = datetime.datetime.today().day
    last_day = 0
    with open(LAST_DAY_PATH, 'r') as f:
        text = f.read()
        if (text != ''):
            last_day = int(f.read())

    return last_day != current_day


def send_mail():
    port = 465

    message = f'''\
Subject: Website updated

I am your website update checker, here to tell you that {WEBSITE} has been updated

This message was sent by the website checker, TODO: put the github link here
If you don't know why you received this mail, please ignore the mail and add this account to your spam folder
'''

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, TARGET_MAILS, message)


def main():
    if compare_day():
        data = get_data()
        old_data = get_old_data()
        is_data_equal = str(data) == str(old_data)
        generate_log(old_data, data, is_data_equal)
        if not is_data_equal:
            update_data(data)
            send_mail()


if __name__ == '__main__':
    main()
