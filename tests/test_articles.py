import unittest
from  app.models import Articles

class ArticleSourceTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Article Sources
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_article = Articles("Mpasho","Mpasho Gram","Sisi ni wale wabaya","www.href.com","www.href.com", "date 25","Welcome")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
