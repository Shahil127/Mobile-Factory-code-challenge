

import unittest
import json
from app import app

class OrderAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_order_success(self):
        payload = {
            "components": ["I", "A", "D", "F", "K"]
        }
        response = self.app.post('/orders', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['total'], 142.3)
        self.assertEqual(data['parts'], [
            'LED Screen',
            'Wide-Angle Camera',
            'USB-C Port',
            'Android OS',
            'Metallic Body'
        ])

    def test_create_order_invalid(self):
        payload = {
            "components": ["I", "A", "D", "F"]
        }
        response = self.app.post('/orders', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid order')

if __name__ == '__main__':
    unittest.main()
