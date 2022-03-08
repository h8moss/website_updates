import datetime
import requests
import smtplib
import ssl
import constants


def generate_log(old_data, new_data, equal):
    target = ''
    if (len(constants.TARGET_MAILS) > 3):
        for _target in constants.TARGET_MAILS[:3]:
            target += str(_target) + ' ,'
        target = target[:-1]
        target += f'and {len(constants.TARGET_MAILS) - 3} more'
    else:
        for _target in constants.TARGET_MAILS:
            target += str(_target) + ' ,'
        target = target[:-1]

    date = str(datetime.datetime.today())
    textA = f'''\

{date}
SENT UPDATE TO {target} FROM {constants.USERNAME}

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

    with open(constants.LOG_PATH, 'a') as f:
        if (not equal):
            f.write(textA)
        else:
            f.write(textB)


def get_data():
    r = requests.get(constants.WEBSITE)
    return r.text


def get_old_data():
    data = ''
    with open(constants.LAST_RESPONSE_PATH, 'r') as f:
        data = f.read()
    return data


def update_data(data):
    current_day = datetime.datetime.today().day
    with open(constants.LAST_DAY_PATH, 'w+') as f:
        f.write(str(current_day))

    with open(constants.LAST_RESPONSE_PATH, 'w+') as f:
        f.write(str(data))


def compare_day():
    current_day = datetime.datetime.today().day
    last_day = 0
    with open(constants.LAST_DAY_PATH, 'r') as f:
        try:
            last_day = int(f.read())
        except:
            last_day = 0

    return last_day != current_day


def send_mail():
    port = 465

    message = f'''\
Subject: Website updated

I am your website update checker, here to tell you that {constants.WEBSITE} has been updated

This message was sent by the website checker, TODO: put the github link here
If you don't know why you received this mail, please ignore the mail and add this account to your spam folder
'''

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(constants.USERNAME, constants.PASSWORD)
        server.sendmail(constants.USERNAME, constants.TARGET_MAILS, message)


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
