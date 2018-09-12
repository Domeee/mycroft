# Mycroft - dropping knowledge once a week

Mycroft is a python script that does the following three things in sequental order.

1. Select a random markdown file from a specified folder
2. Convert the markdown to html
3. Send the html as e-mail to a specified address

I run this script with a Cron job once a week on my [Syncthing](https://syncthing.net/) server where it has access to my book summaries. I store my book summaries as markdown. Long story short: **Mycroft delivers a random book summary to my e-mail inbox every week.**

## Installation

The script was tested on Linux with Python 3.7 targeting a Gmail e-mail server.

### Prerequisites

1. Python 3 and markdown module

```bash
pip install markdown
```

### Mycroft

1. In the directory of you choice clone the Mycroft git repository:

```git
git clone git@github.com:Domeee/mycroft.git
```

2. Check if everything works so far. Running the unit tests should result in a OK message.

```bash
python -m unittest mycroft_test.py
```

3. Update the configuration in mycroft_config.ps to suit you needs.

4. Test the configuration by running the script once from the console.

```bash
python mycroft.py
```

Congratulations! Mycroft is setup successfully :-) To receive a weekly e-mail configure a Cron task as described next.

## Weekly Cron task

Run the script mycroft.py located at /home/myuser/.bin/mycroft once a week.

```bash
0 0 * * 0 /usr/bin/python /home/myuser/.bin/mycroft/mycroft.py
```

## Running unit tests

```bash
python -m unittest mycroft_test.py
```
