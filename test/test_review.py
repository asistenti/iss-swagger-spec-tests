import unittest
import json

from deepdiff import DeepDiff
from .request_sending import send_post_request, send_get_request, send_put_request, send_delete_request
from .server_port import PORT


def load_json_from_file(file_path):
    f = open(file_path, encoding='utf-8')
    data = json.load(f)
    f.close()
    return data


class ReviewTest(unittest.TestCase):
    def setUp(self):
        self.base_path = f'http://localhost:{PORT}/api/review'

    def test_post_api_review_id_vehicle_id(self):
        request_data = load_json_from_file('request_bodies/post_api_review_id_vehicle_id_request_body.json')
        response_data = load_json_from_file('response_bodies/post_api_review_id_vehicle_id_response_body.json')
        response = send_post_request(data=request_data, url=f'{self.base_path}/1/vehicle/1')
        self.assertEqual(response.status_code, 200)
        ddiff = DeepDiff(response_data, response.json())
        self.assertEqual(ddiff.get('dictionary_item_removed', None), None)

    def test_get_api_review_vehicle_id(self):
        response_data = load_json_from_file('response_bodies/get_api_review_vehicle_id_response_body.json')
        response = send_get_request(url=f'{self.base_path}/vehicle/1')
        self.assertEqual(response.status_code, 200)
        ddiff = DeepDiff(response_data, response.json())
        self.assertEqual(ddiff.get('dictionary_item_removed', None), None)

    def test_post_api_review_id_driver_id(self):
        request_data = load_json_from_file('request_bodies/post_api_review_id_driver_id_request_body.json')
        response_data = load_json_from_file('response_bodies/post_api_review_id_driver_id_response_body.json')
        response = send_post_request(data=request_data, url=f'{self.base_path}/1/driver/1')
        self.assertEqual(response.status_code, 200)
        ddiff = DeepDiff(response_data, response.json())
        self.assertEqual(ddiff.get('dictionary_item_removed', None), None)

    def test_get_api_review_driver_id(self):
        response_data = load_json_from_file('response_bodies/get_api_review_driver_id_response_body.json')
        response = send_get_request(url=f'{self.base_path}/driver/1')
        self.assertEqual(response.status_code, 200)
        ddiff = DeepDiff(response_data, response.json())
        self.assertEqual(ddiff.get('dictionary_item_removed', None), None)

    def test_get_api_review_id(self):
        response_data = load_json_from_file('response_bodies/get_api_review_id_response_body.json')
        response = send_get_request(url=f'{self.base_path}/1')
        self.assertEqual(response.status_code, 200)
        ddiff = DeepDiff(response_data, response.json())
        self.assertEqual(ddiff.get('dictionary_item_removed', None), None)