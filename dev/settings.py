# Include all global variables in this file.
# These are used across different modules/packages
# where required.

# Service Name
SVC_NAME = 'batman-stripe-sqs'

# AWS Settings
AWS_REGION_NAME = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# SQS Settings
AWS_SQS_QUEUE_URL = ''
AWS_SQS_MAX_MESSAGES = 10
AWS_SQS_VISIBILITY_TIMEOUT = 30 #seconds
AWS_SQS_WAIT_TIME = 20 #seconds