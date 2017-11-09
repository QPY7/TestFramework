import  unittest

class Test_case(unittest.TestCase):


    def setUp(self):
        print('set up')

    def test_case_one(self):
        print('test_case_one')

    def test_case_two(self):
        print('test_case_two')

    def tearDown(self):
        print('tesar down')

if __name__ == '__main__':
    unittest.main()