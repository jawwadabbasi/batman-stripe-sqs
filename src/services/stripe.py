import requests

class Stripe:

	api_endpoint = 'http://batman-ms-stripe'

	def Webhook(data):

		try:
			result = requests.post(f'{Stripe.api_endpoint}/api/v1/Stripe/Webhook',json = data,stream = True)

			return True if result.ok else False

		except:
			return False