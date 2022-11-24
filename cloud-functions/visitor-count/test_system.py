#!/usr/bin/env python3
from unittest.mock import Mock

from google.cloud import firestore
import json
import requests
import unittest
import main
from mockfirestore import MockFirestore, DocumentReference, DocumentSnapshot, AlreadyExists

import mockfirestore
from mockfirestore import client
import json


class testgetCount(unittest.TestCase):
	
	def test_get_visitor_number_response_is_dict(self):
		response = requests.get("https://us-east1-ivory-duality-360002.cloudfunctions.net/function-2/visitor_count")
		data = json.loads(response.content)
		print(data)
		self.assertIs(type(data), dict)
		self.assertIn('currentVisitor', data)


if __name__ == '__main__':
	unittest.main()
