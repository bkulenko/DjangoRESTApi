import unittest
import requests


class TestViews(unittest.TestCase):

    def test_movie_post(self):
        #self.maxDiff=None
        r = requests.post('http://localhost:8000/movies/', json = {"name": "Christopher Robin"})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json(), {})
        r2 = requests.post('http://localhost:8000/movies/', json={"name": "Gone With The Wind"})
        self.assertEqual(r2.status_code, 201)

    def test_movie_get(self):
        r = requests.get('http://localhost:8000/movies/')
        self.assertEqual(r.status_code, 200)

    def test_comment_post(self):
        r = requests.post('http://localhost:8000/comments/', json={"Movie": "tt0031381", "Comment": "This movie really good"})



    def test_comment_get(self):
        r = requests.get('http://localhost:8000/comments/')
        self.assertEqual(r.status_code, 200)
        r2 = requests.get('http://localhost:8000/comments/tt0031381')
        self.assertEqual(r2.status_code, 200)


if __name__ == '__main__':  
    unittest.main()