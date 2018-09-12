from os import listdir
from os.path import isfile, join
from random import randint
from sys import exit
from codecs import open
from markdown import markdown
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mycroft_config
import logging


def drop_knowledge():
    try:
        summary_md = _get_random_summary(mycroft_config.summaries_dir)

        if (summary_md is None):
            logging.info('No markdown files (*.md) found in ' +
                         mycroft_config.summaries_dir + '. Script exited.')
            exit()

        summary_html = markdown(summary_md, extensions=[
                                'markdown.extensions.tables'])
        email_msg = _compose_email_msg(summary_html)
        _send_msg(email_msg)
    except FileNotFoundError:
        logging.error('Summaries directory not found: ' +
                      mycroft_config.summaries_dir + '. Ensure "summaries_dir" in mycroft_config.py points to a valid directory.')
    except:
        logging.error('Unknown error', exc_info=True)


def _get_random_summary(summaries_dir):
    summaries = []
    for f in listdir(summaries_dir):
        file = join(summaries_dir, f)
        if (isfile(file) and file.lower().endswith('.md')):
            summaries.append(join(file))

    summaries_count = len(summaries)

    if (summaries_count > 0):
        random_summary_index = randint(0, summaries_count - 1)
        summary_path = summaries[random_summary_index]
        summary_file = open(summary_path, mode='r', encoding='utf-8')
        return summary_file.read()


def _compose_email_msg(html):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = mycroft_config.email_subject
    msg['From'] = mycroft_config.email_from
    msg['To'] = mycroft_config.email_to
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    return msg


def _send_msg(msg):
    server = smtplib.SMTP(mycroft_config.email_host, mycroft_config.email_port)
    server.ehlo()
    server.starttls()
    server.login(mycroft_config.email_user_name,
                 mycroft_config.email_user_password)
    server.sendmail(mycroft_config.email_from,
                    mycroft_config.email_to, msg.as_string())
    server.close()


if __name__ == '__main__':
    drop_knowledge()
