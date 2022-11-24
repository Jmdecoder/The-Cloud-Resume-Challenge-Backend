"""
Visitor count
"""

from flask import jsonify
from google.cloud import firestore
import functions_framework
import os


def get_visitor_count():
	"""
    Get the number of visitors

    :return: the number of visitor
    """
	database = firestore.Client()
	current_count = 0
	
	# Get the document
	visitor_doc = database.collection(u'cloudresume').document(u'visitor_count')
	
	doc = visitor_doc.get()
	# If the documents exists
	if doc.exists:
		# Get the last number of visitor
		current_count = int(doc.to_dict()['count'])
	
	return current_count


def save_visitor_data(visitor_nb):
	"""
    Save the number of visitors to Firestore

    :param visitor_nb: number of visitor
    """
	database = firestore.Client()
	visitor_ref = database.collection(u'cloudresume').document(u'visitor_count')
	
	# Write the new number of visitors
	visitor_ref.set({'count': visitor_nb})


@functions_framework.http
def visitor_count(request):  # pylint: disable=unused-argument
	"""

    :param request: the client request
    :return: the current visitor number
    """
	visitor_number = get_visitor_count()
	current_visitor = str(visitor_number + 1)
	save_visitor_data(current_visitor)
	response_data = {
		'currentVisitor': current_visitor
	}
	headers = {
		'Access-Control-Allow-Origin': 'https://vmtech.info'
	}
	
	return jsonify(response_data), 200, headers
