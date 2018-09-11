# Mycroft - dropping knowledge once a week

Mycroft is a python script that does the following three things in sequental order.

1. Select a random markdown file from a specified folder
2. Convert the markdown to html
3. Send the html as e-mail to a specified address

I run this script with a Cron job once a week on my Syncthing master where it has access to my book summaries. I store my book summaries as markdown. Long story short: **Mycroft delivers a random book summary to my e-mail inbox every week.**

## Installation

The script was tested on Linux with Python 3.7 targeting a Gmail e-mail server.

## Running unit tests

```bash
python -m unittest mycroft_test
```
