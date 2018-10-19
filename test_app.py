import unittest
import json
from api.v1.app import app

class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_sales(self):
        request = self.client.get('/store/api/v1/sales', headers={"content-type": "application/json"})
        self.assertEqual(request.status_code, 200)

    def test_get_product(self):
        request = self.client.get('/store/api/v1/products/1', headers={"content-type": "application/json"})
        self.assertEqual(request.status_code, 200)

    def test_get_sale(self):
        request = self.client.get('/store/api/v1/sales/1', headers={"content-type": "application/json"})
        self.assertEqual(request.status_code, 200)

    def test_create_product(self):
        data = {
            'description': 'Whats up Doc!'
        }
        request = self.client.post('/store/api/v1/products/', data=json.dumps(data), headers={"content-type": "application/json"})
        self.assertEqual(['product'],['product'])
        self.assertEqual(request.status_code, 201)

    def test_get_products(self):
        request = self.client.get('/store/api/v1/products', headers={"content-type": "application/json"})
        self.assertEqual(request.status_code, 200)
        self.assertEqual('products', 'products')

    def test_create_sale(self):
        data = {
            'attendant' : 'Bugs Bunny',
            'description': 'Whats up Doc!'}
        request = self.client.post('/store/api/v1/sales/', data=json.dumps(data), headers={"content-type": "application/json"})
        print(request.data)
        self.assertEqual(request.status_code, 201)

    def test_update_sale(self):
        data = {
            'description': 'Khaleds another one!'
                }
        request = self.client.put('/store/api/v1/sales/2', data=json.dumps(data), headers={"content-type": "application/json"})
        self.assertTrue(request.status_code, 201)

    def test_update_product(self):
        data = {
            'description': 'Khaleds another one!'
        }
        request = self.client.put('/store/api/v1/products/2', data=json.dumps(data),
                                  headers={"content-type": "application/json"})
        self.assertTrue(request.status_code, 201)

    def test_delete_sale(self):
        request = self.client.delete('/store/api/v1/sales/2')
        self.assertTrue(request.status_code, 200)

    def test_delete_product(self):
        request = self.client.delete('/store/api/v1/products/2')
        self.assertTrue(request.status_code, 200)


if __name__ == '__main__':
    unittest.main
