import unittest
import re
import os
from datetime import datetime
from scripts.apache_log_generator import generate_log_entry, write_log_file

class TestApacheLogGenerator(unittest.TestCase):
    """ Test class for the Apache log generator functions. """

    def setUp(self):
        self.log_file_name = "test_log_mock.log"
        self.generator_config = {
            'ips': ['127.0.0.1'],
            'requests': ['GET /index.html HTTP/1.0'],
            'statuses': [200],
            'min_size': 100,
            'max_size': 5000,
            'max_time_offset_seconds': 86400,
        }
        self.value_catcher = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) \] "(.*?)" (\d{3}) (\d+)$'

    def tearDown(self):
        if os.path.exists(self.log_file_name):
            os.remove(self.log_file_name)

    def test_generate_log_entry(self):
        """Test if `generate_log_entry` generates a valid log entry."""
        now = datetime.now()

        # generate log entry to test
        log_entry = generate_log_entry(**self.generator_config,
                                       now=now)
        self.assertIsInstance(log_entry, str)

        # match the generated log entry and test if it matches the pattern
        match = re.match(self.value_catcher, log_entry)
        self.assertIsNotNone(match)

        if match:
            ip = match.group(1)
            log_time = match.group(2)
            request = match.group(3)
            status = match.group(4)
            size = match.group(5)

        # test if the generated log entry values are valid
        log_time = datetime.strptime(log_time, '%d/%b/%Y:%H:%M:%S')
        diff = (now - log_time).total_seconds()
        self.assertTrue(diff <= self.generator_config['max_time_offset_seconds'])
        self.assertIn(ip, self.generator_config['ips'])
        self.assertIn(request, self.generator_config['requests'])
        self.assertIn(int(status), self.generator_config['statuses'])
        self.assertTrue(
            self.generator_config['min_size'] <= int(size) \
                <= self.generator_config['max_size'])


    def test_write_log_file(self):
        """
        Test if `write_log_file` creates a file with the correct number of
        entries.
        """

        # write log entries to file
        num_entries = 5
        write_log_file(self.log_file_name, num_entries)
        self.assertTrue(os.path.exists(self.log_file_name))

        # read the log file and test if the number of entries is correct
        with open(self.log_file_name, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), num_entries)

        # test if each line in the log file matches the pattern
        for line in lines:
            match = re.match(self.value_catcher, line)
            self.assertIsNotNone(match)

if __name__ == '__main__':
    unittest.main()
