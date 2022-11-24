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


class testGetVisitorNumber(unittest.TestCase):
	
	
	
	'''def test_get_visitor_by_mocking_id(self):
        
        visitor_doc = database.collection(u'cloudresume')
        visitor_ref = visitor_doc.document(u'visitor_count')
        
        doc = visitor_ref.get()
        
        {'currentVisitor': '35'}
        firestore = Mock(Client=Mock(return_value=mock_database))
        self.assertTrue()'''
	
	def test_get_visitor_count(self):
		mock_db = MockFirestore()
		mock_db._data = {'cloudresume': {
			'visitor_count': {'count': 1}
		}}
		# mock_db.collection('cloudresume').document('visitor_count').set({'count': '32'})
		
		docs = list(mock_db.collection('cloudresume').stream())
		
		self.assertEqual({'count': 1}, docs[0].to_dict())
		
		visitor_nb = int(docs[0].to_dict()['count'])
		print(visitor_nb)
		self.assertEqual(visitor_nb, 1)
		# self.assertEqual(visitor_nb, 32)
		return visitor_nb
	
	def test_visitor_count(self):
		mock_db = MockFirestore()
		mock_db._data = {'cloudresume': {
			'visitor_count': {'count': 1}
		}}
		# mock_db.collection('cloudresume').document('visitor_count').set({'count': '32'})
		
		docs = list(mock_db.collection('cloudresume').stream())
		
		self.assertEqual({'count': 1}, docs[0].to_dict())
		
		visitor_nb = int(docs[0].to_dict()['count'])
		current_visitor = str(visitor_nb + 1)
		client_data = {
			'currentVisitor': current_visitor
		}
		expected_data = json.dumps(client_data)
		print(expected_data)
		actual_data = '{"currentVisitor": "2"}'
		self.assertEquals(expected_data, actual_data)


if __name__ == '__main__':
	unittest.main()
