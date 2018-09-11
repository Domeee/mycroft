import mycroft
import mycroft_config
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class TestMycroft(unittest.TestCase):
    def test_get_random_summary(self):
        summary = mycroft._get_random_summary(mycroft_config.summaries_dir)
        self.assertIsNotNone(summary)

    def test_get_random_summary_is_none(self):
        summary = mycroft._get_random_summary('./.vscode')
        self.assertIsNone(summary)

    def test_get_random_summary_throws_FileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            mycroft._get_random_summary('./invalid/path')

    def test_compose_email_msg(self):
        html = '<h1>test</h1>'
        msg = mycroft._compose_email_msg(html)

        self.assertEqual(mycroft_config.email_subject, msg['Subject'])
        self.assertEqual(mycroft_config.email_from, msg['From'])
        self.assertEqual(mycroft_config.email_to, msg['To'])

        part = msg.get_payload()[0]
        self.assertEqual(html, part._payload)


if __name__ == '__main__':
    unittest.main()
