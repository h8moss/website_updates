# website updates
A python script that sends you an email if a website changes.

Whenever this script is run, it will compare the specified website to a cached version of said website and it will send an email if it can find any changes.

Currently the file will send at most one mail a day, but I am planning to allow that to be customizable as well.

## How it works

This script will open the specified domain, fetch the text of said domain, and cache it, if it already has a cached response, it will also compare the previous cache to the current response and send an email if they are different. Currently the app will send at most 1 mail per day, after that it will stop checking for updates.

## Installation

Installation is relatively simple, but it is necessary to make a new mail account for the script to use (you could use your own account, but I can't recommend it)

Once you have created a new mail account, it is also important to allow python to access it, this is done differently depending on your provider, so you will have to do some research.
For gmail, you need to set "allow less secure apps" to ON in order to use this service.

![image](https://user-images.githubusercontent.com/43828996/157164093-fe4b6ccd-d8ca-44b3-81ce-1b084f822efc.png)

Once this is done, you should clone this repository into a machine, and edit the `conf.txt` file

On the first line of the conf file, write the URL you want to check for changes

Then, on the next line, the mail account you created

Then the password of said mail account, this is why we recommend you use an account separate from your own, although as long as you don't show this file to anyone you should be safe

Then every line onwards should contain a destination email, to forward the data towards.

Here is an example:

```
https://youtube.com/channel/ludwig/videos
myRobotAccount@gmail.com
password12345
myPersonalMail@gmail.com
myFriendsPersonalMail@gmail.com
SomeOtherMail@gmail.com
```

## Setting up a cron job

This script will only check for a website update when run manually, making the script about as good as just accessing the page itself.
In order to avoid this, you should set up this script to run automatically every certain time, this section explains how to do so

### Windows

In windows, we can set up a scheduled task using the schtasks command, which takes a few important parameters:
```ps
schtasks /create /sc HOURLY /tn <SOME NAME> /tr "C:\full\path\to\python.exe C:\full\path\to\project\main.py" 
```
This will make the check run every hour.

I also recommend you make the command available even if the user is not logged in, this will prevent a command line window to appear when the command runs. To do this, open the task scheduler app, find the task, and mark the correct option.

![image](https://user-images.githubusercontent.com/43828996/157281253-e2962ed8-308d-45db-b44f-364e9283e9c7.png)


### Linux and Mac OS

Setting up a cron job on Linux and mac is similarly quite easy, we just need to open the cron tab by running the following command:
```
crontab -e
```
This will open the crontab, which is where your cron jobs are stored, to add a new one, go to the last line and add the following (for an hourly check)
```
0 * * * * python /path/to/project/dir/main.py
```
