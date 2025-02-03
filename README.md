# batman-ms-sqs

## Overview

**batman-ms-sqs** is a microservice responsible for polling AWS SQS for Stripe event notifications and forwarding them to the **batman-ms-stripe** webhook endpoint for processing. This service ensures efficient handling of asynchronous Stripe events, allowing real-time updates to customer subscriptions, payments, and invoices.

## How It Works

1. **Polling AWS SQS**: The service continuously listens to a dedicated AWS SQS queue where Stripe webhook events are stored.
2. **Event Filtering & Processing**: It retrieves event messages, validates them, and ensures no duplicate processing.
3. **Forwarding to Batman-MS-Stripe**: Once an event is processed, it is sent to the `/api/v1/Stripe/Webhook` endpoint of **batman-ms-stripe** for further handling.
4. **Error Handling & Retry Mechanism**: Failed messages are retried, and unprocessed events are logged for debugging.

## Key Features

- **AWS SQS Integration**: Efficient polling of Stripe events from a managed queue.
- **Event Deduplication**: Ensures each event is processed only once.
- **Webhook Forwarding**: Sends valid Stripe events to **batman-ms-stripe**.
- **Retry Mechanism**: Handles failed requests and retries when needed.
- **Scalable**: Can be deployed as a serverless function or a containerized service.

## Integration with Batman-MS-Stripe

- This service is designed to work alongside **batman-ms-stripe**, which processes the Stripe events received via its webhook.
- **Workflow Example:**
  1. A Stripe event (e.g., `invoice.paid`) is generated.
  2. AWS SQS receives and stores the event.
  3. **batman-ms-sqs** polls the queue, retrieves the event, and forwards it to **batman-ms-stripe**.
  4. **Batman-MS-Stripe** processes the event, updating customer data accordingly.

## API Endpoints

This service primarily interacts with AWS SQS and does not expose public API endpoints. However, it pushes processed events to:

```
POST /api/v1/Stripe/Webhook
```

on **batman-ms-stripe**.

## Deployment & Scaling

- Can be deployed as a background worker, AWS Lambda function, or containerized service.
- Uses AWS IAM roles for secure access to SQS.
- Logging and monitoring via AWS CloudWatch or an external observability stack.

## Final Thoughts

Batman never lets crime—or unprocessed events—slip through the cracks. With **batman-ms-sqs**, your Stripe events will always reach their final destination. 🦇

