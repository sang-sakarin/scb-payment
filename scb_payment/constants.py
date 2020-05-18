"""
A libraly that provides a python interface to SCB Payment API
"""

ENDPOINTS = {
    "API_ROOT": "https://api-sandbox.partners.scb/partners/sandbox",
    "OAUTH_AUTHORIZE_PATH": "/v2/oauth/authorize",
    "OAUTH_TOKEN_PATH": "/v1/oauth/token",
    "OAUTH_TOKEN_REFRESH_PATH": "/v2/oauth/authorize",
    "PAYMENT_QRCODE_PATH": "/v1/payment/qrcode/create",
    "BILLPAYMENT_TRANSACTION_PATH": "/v1/payment/billpayment/transactions/{transaction}?sendingBank=014",
    "QRCODE_CREDITCARD_PATH": "/v1/payment/qrcode/creditcard/{qr}"
}
