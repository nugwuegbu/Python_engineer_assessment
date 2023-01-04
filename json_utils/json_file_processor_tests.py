import unittest

from json_file_processor import ProcessJson


class TestProcessJson(unittest.TestCase, ProcessJson):

    def setUp(self):
        self.json_file = '../data/data_1.json'

    def test_read_file_when_file_exists(self):
        result = self.read_file()
        self.assertEqual(type(result), str)

    def test_file_isjson(self):
        self.assertEqual(type(self.sniff_schema()), dict)

    def test_output_format(self):
        expected_keys = ['type', 'tag', 'description', 'required']
        output = self.capture_attributes()
        for key, data in output.items():
            self.assertEqual(list(data.keys()), expected_keys)
        # self.assertEqual(2,2)
