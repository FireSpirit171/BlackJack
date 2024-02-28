import unittest
from unittest.mock import patch
from read import read_singletone
from config_path import STAT_PATH

class TestReadSingletone(unittest.TestCase):
    @patch('builtins.open', unittest.mock.mock_open(read_data="Games: 0\nWons: 0\nDraws: 0\nLoses: 0\nPercant: 0.00"))
    def test_read_file(self):
        reader = read_singletone(STAT_PATH)
        games, wons, draws, loses, percent = reader.read_file()
        self.assertEqual(games, 0)
        self.assertEqual(wons, 0)
        self.assertEqual(draws, 0)
        self.assertEqual(loses, 0)
        self.assertEqual(percent, 0.00)

if __name__ == '__main__':
    unittest.main()