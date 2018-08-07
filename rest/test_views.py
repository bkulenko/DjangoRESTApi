import unittest
import requests
import logging

logging.basicConfig(level=0,filename='testlog.txt', filemode='w')

class TestViews(unittest.TestCase):

    def test_base_seed(self):
        r = requests.post('http://localhost:8000/movies/', json={"name": "Gone With The Wind"})
        r2 = requests.post('http://localhost:8000/comments/', json={"Movie": "tt0031381", "Comment": "This movie really good"})

    def test_movie_post_empty(self):
        log = logging.getLogger('Test movie POST: Adding new entity\n')
        r = requests.post('http://localhost:8000/movies/', json = {"name": "Christopher Robin"})
        self.assertEqual(r.status_code, 201)
        #with open('testlog.txt', 'w') as testlog:
        log.info('Status:' + str(r.status_code))
        log.info('Response:' + str(r.json()))

    def test_movie_post_existing(self):
        log = logging.getLogger('Test movie POST: Trying to add entity present in db\n')
        r = requests.post('http://localhost:8000/movies/', json={"name": "Christopher Robin"})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json(), {})
        log.info('Status:' + str(r.status_code))
        log.info('Response:' + str(r.json()))

    def test_movie_get(self):
        log = logging.getLogger('Test movie GET\n')
        r = requests.get('http://localhost:8000/movies/')
        self.assertEqual(r.status_code, 200)
        log.info('Status:' + str(r.status_code))
        log.info('Response:' + str(r.json()))

    def test_comment_post(self):
        log = logging.getLogger('Test Comment POST\n')
        r = requests.post('http://localhost:8000/comments/', json={"Movie": "tt0031381", "Comment": "This movie really good"})
        self.assertEqual(r.status_code, 201)
        log.info('Status:' + str(r.status_code))
        log.info('Response:' + str(r.json()))

    def test_comment_get_all(self):
        log = logging.getLogger('Test comment GET: All comments\n')
        r = requests.get('http://localhost:8000/comments/')
        self.assertEqual(r.status_code, 200)
        log.info('Status:' + str(r.status_code))
        log.info('Response:' + str(r.json()))

    def test_comment_get_detail(self):
        log = logging.getLogger('Test comment GET: Speciffic movie\n')
        r = requests.get('http://localhost:8000/comments/tt0031381')
        self.assertEqual(r.status_code, 200)
        log.info('Status:' + str(r.status_code))
        log.info('Response:' + str(r.json()))


if __name__ == '__main__':
    unittest.main()
