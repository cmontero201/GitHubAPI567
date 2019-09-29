import unittest
import json
import get_repo
from unittest.mock import MagicMock as Mock
from unittest.mock import patch

class TestGetRepo(unittest.TestCase):

    @patch("get_repo.connect")
    def testConnection(self, mock_connect):
        mock_connect.return_value = [200, {"CS-523-Web-Programming-1": "1",
                                     "CS555---GEDCOM-Project": "13",
                                     "GitHubAPI567": "12",
                                     "HelloWorldRepo": "3",
                                     "Triangle567": "8"}]
        self.assertTrue(get_repo.connect("cmontero201")[0])

    @patch("get_repo.connect")
    def test_repos1(self, mock_connect):
        mock_connect.return_value = [200, {"CS-523-Web-Programming-1": "1",
                                     "CS555---GEDCOM-Project": "13",
                                     "GitHubAPI567": "12",
                                     "HelloWorldRepo": "3",
                                     "Triangle567": "8"}]
        self.assertIs(mock_connect()[1], get_repo.connect("cmontero201")[1])
    
    @patch("get_repo.connect")
    def testConnection2(self, mock_connect):
        mock_connect.return_value = [200, {"helloworld": "6",
                                     "Mocks": "10",
                                     "Project1": "2",
                                     "threads-of-life": "1"}]
        self.assertTrue(get_repo.connect("richkempinski")[0])

    @patch("get_repo.connect")
    def test_repos2(self, mock_connect):
        mock_connect.return_value = [200, {"helloworld": "6",
                                     "Mocks": "10",
                                     "Project1": "2",
                                     "threads-of-life": "1"}]
        self.assertIs(mock_connect()[1], get_repo.connect("richkempinski")[1])

if __name__ == '__main__':
    print('Running unit tests')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetRepo)
    unittest.TextTestRunner(verbosity = 2).run(suite)
