# Built with ingenuity,
# by Jawwad Abbasi (jawwad@omnitryx.ca)

# Initiates a AWS SQS consumer to long poll a designated queue
# and process accordingly.

import sys
import inspect
import json
import time
import concurrent.futures
import boto3
import settings

from services.logger import Logger
from services.stripe import Stripe

class Consumer:

	def ReceiveMessages(self):

		try:
			return self.client.receive_message(
				QueueUrl = settings.AWS_SQS_QUEUE_URL,
				MaxNumberOfMessages = settings.AWS_SQS_MAX_MESSAGES,
				VisibilityTimeout = settings.AWS_SQS_VISIBILITY_TIMEOUT,
				WaitTimeSeconds = settings.AWS_SQS_WAIT_TIME
			)

		except:
			return False

	def DeleteMessage(self,receipt_handle):

		try:
			return self.client.delete_message(
				QueueUrl = settings.AWS_SQS_QUEUE_URL,
				ReceiptHandle = receipt_handle
			)

		except:
			return False

	def ProcessMessage(self,message):

		try:
			data = json.loads(message['Body'])

		except:
			return False

		if Stripe.Webhook(data):
			self.DeleteMessage(message['ReceiptHandle'])

			return True

		return False

	def __init__(self):

		try:
			self.client = boto3.client(
				'sqs',
				region_name = settings.AWS_REGION_NAME,
				aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
				aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
			)

		except Exception as e:
			Logger.CreateExceptionLog(inspect.stack()[0][3],e)

			sys.exit('ERROR - Could not connect with AWS')

		while True:
			messages = self.ReceiveMessages()

			if not messages or 'Messages' not in messages:
				time.sleep(2)
				
				continue

			with concurrent.futures.ThreadPoolExecutor() as executor:
				for x in messages['Messages']:
					executor.submit(self.ProcessMessage,x)

####################################
# Initiate AWS SQS consumer
####################################
Consumer()