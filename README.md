# website updates
A python script that sends you an email if a website changes.

Whenever this script is run, it will compare the specified website to a cached version of said website and it will send desktop notification if it can find any changes.

Currently the file will send at most one notification per day, but I am planning to allow that to be customizable as well.

## How it works

This script will open the specified domain, fetch the text of said domain, and cache it, if it already has a cached response, it will also compare the previous cache to the current response and send an notification if they are different. Currently the app will send at most 1 notification per day, after that it will stop checking for updates.

## Installation

Installation is relatively simple

all you have to do is clone this repository into a machine, and edit the `conf.txt` file

The first and only line of said file should have the url of the desired website

You should also have python installed in the machine, create and activate a new virtual environment and run the following command:

```
python -r ./requirements.txt
```
inside of this repository.

Now you should be able to run this script by running `python ./main.py`

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
