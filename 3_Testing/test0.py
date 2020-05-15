import unittest
import main0

class TestMain(unittest.TestCase):
    def setUp(self):                #runs after each function call
        print("About to run a function")

    def test_do_stuff1(self):
        """lala"""
        test_param=10
        result=main0.do_stuff(test_param)
        self.assertEqual(result,15) 

    def test_do_stuff2(self):
        test_param='str'
        result = main0.do_stuff(test_param) 
        self.assertIsInstance(result,ValueError)

    def test_do_stuff3(self):
        test_param=None
        result = main0.do_stuff(test_param) 
        self.assertEqual(result, 'enter a no')
    
    def test_do_stuff4(self):
        test_param=''
        result = main0.do_stuff(test_param) 
        self.assertEqual(result, 'enter a no')

    def test_do_stuff5(self):
        test_param=0
        result=main0.do_stuff(test_param)
        self.assertEqual(result,5)     

    def tearDown(self):             #clears var after each fun
        print("Cleaning up")    

if __name__=="__main__":
    unittest.main()        