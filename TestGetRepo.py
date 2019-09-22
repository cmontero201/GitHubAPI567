import unittest
import get_repo


class TestGetRepo(unittest.TestCase):
    def testConnection(self):
        self.assertTrue(get_repo.connect("cmontero201"))
    
    def testConnection2(self):
        self.assertTrue(get_repo.connect("richkempinski"))
    
    def testConnection_Fail(self):
        self.assertTrue(get_repo.connect(""))

if __name__ == '__main__':
    print('Running unit tests')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetRepo)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    
    
