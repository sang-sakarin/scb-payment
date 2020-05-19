# QR Code Payment SCB - Python

A Python library for [QR Code Payment](https://developer.scb/#/documents/documentation/qr-payment/thai-qr.html)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Initial SCB Object](#initialobj)
  - [Generate QR 30](#gemerateqr30)
  - [Generate QR CS](#gemerateqrcs)
  - [Generate QR 30 QR CS](#gemerateqr30qrcs)
  - [Slip Verification](#slipverification)
  - [Payment Inquiry](#paymentinquiry)


## Installation <a name="installation"></a>

    pip install scb-payment

## Usage <a name="usage"></a>

    from scb_payment import QRCodePayment

### Initial SCB Object <a name="initialobj"></a>

#### Parameter:

  * ```API_KEY``` <b>string</b> API authorization key respective to each partner obtained from partner onboarding process. ```required```
  * ```API_SECRET``` <b>string</b> API authorization secret obtained from partner onboarding process. ```required```
  * ```BILLER``` <b>string</b> Biller ID. ```required```
  * ```MERCHANT``` <b>string</b> Merchant ID for QR CS. ```required```
  * ```TERMINAL``` <b>string</b> Terminal ID for QR CS. ```required```


#### Function:

    from scb_payment import QRCodePayment

    API_KEY = 'YOUT_API_KEY'
    API_SECRET = 'YOUR_API_SECRET'
    MERCHANT = 'YOUR_MERCHANT'
    TERMINAL = 'YOUR_TERMINAL'
    BILLER = 'YOUR_BILLER'

    # initial object
    qr_payment = QRCodePayment(API_KEY, API_SECRET, MERCHANT, TERMINAL, BILLER)


### Generate QR 30 <a name="gemerateqr30"></a>

#### Parameter:

  * ```amount``` <b>number</b> Amount of transaction with the length up to 13 characters including "." e.g. 100, 100.00 ```required```
  * ```ref1``` <b>string</b> Reference number required for the relevant payment methods. ```required```
  * ```ref2``` <b>string</b> Reference number required for the relevant payment methods.
Required if: Supporting Reference field under merchant profile of application is set to Two references. ```required```
  * ```ref3``` <b>string</b> Reference number required for the relevant payment methods to identify endpoint for receiving payment confirmation.
Format: Reference 3 Prefix + (value), example: SCB1234 ```required```


#### Function:

    qr_payment.gererate_qr_30(amount=100.00, ref1="TH1234", ref2="THG456", ref3="SCB0987")

#### Response:

    {
      'status': {
        'code': 1000,
        'description': 'Success'
      },
      'data': {
        'qrRawData': '000201010212303901155833191498329610206TH12340306THG45652047011530376454031005802TH5922TestMerchant15879948176007BANGKOK62380523202005190933460930000000707SCB09876304D4BA',
        'qrImage': 'R0lGODdh9AH0AYAAAAAAAP///ywAAAAA9AH0AQAC/4yPqcvtD6OctNqLs968+w+G4kiW5omm6sq27gvH8kzX9o3n+s73/g8MCofEovGITCqXzKbzCY1Kp9Sq9YrNarfcrvcLDovH5LL5jE6r1+wb4A2Py+f0uv1eb+DpFrt+Dxgo9ycIQDh3GJgYt1ioyOBoWBEZ+UF5iQm...'
      }
    }

### Generate QR CS <a name="gemerateqrcs"></a>

#### Parameter:

  * ```amount``` <b>number</b> Amount of transaction with the length up to 13 characters including "." e.g. 100, 100.00 ```required```
  * ```invoice``` <b>string</b> Invoice number as unique ID per transaction for QR CS. It must be English uppercase letters and numbers only. ```required```

#### Function:

    qr_payment.gererate_qr_cs(amount=100.00, invoice="AA115294912")

#### Response:

    {
      'status': {
        'code': 1000,
        'description': 'Success'
      },
      'data': {
        'qrRawData': '0002010102120216453927496092340052047011530376...',
        'qrImage': 'R0lGODdh9AH0AYAAAAAAAP///ywAAAAA9AH0AQAC/4yPqcvtD6OctNqLs968+w+G4kiW5omm6sq27gvH8kzX9o3n+s73/...',
        'csExtExpiryTime': '2020-05-19 22:49:23',
        'qrcodeId': '20200519094923139000000',
        'merchantId': '058041048495401',
        'merchantName': 'TestMerchant1587994817',
        'amount': '100',
        'currencyCode': '764',
        'csNote': '',
        'csUserDefined': '',
        'invoice': 'AA1111B',
        'channels': [
          {
            'seqNo': '1',
            'channelName': 'VISA',
            'channelCode': 'VISA'
          }
        ],
        'terminalId': '933271425507787',
        'qrCodeType': 'EM',
        'poi': '12',
        'currencyName': 'Baht',
        'terminalName': 'Sandbox Terminal',
        'responseCode': '000'
      }
    }

### Generate QR 30 QR CS <a name="gemerateqr30qrcs"></a>

#### Parameter:

  * ```amount``` <b>number</b> Amount of transaction with the length up to 13 characters including "." e.g. 100, 100.00 ```required```
  * ```invoice``` <b>string</b> Invoice number as unique ID per transaction for QR CS. It must be English uppercase letters and numbers only. ```required```
  * ```ref1``` <b>string</b> Reference number required for the relevant payment methods. ```required```
  * ```ref2``` <b>string</b> Reference number required for the relevant payment methods.
Required if: Supporting Reference field under merchant profile of application is set to Two references. ```required```
  * ```ref3``` <b>string</b> Reference number required for the relevant payment methods to identify endpoint for receiving payment confirmation.
Format: Reference 3 Prefix + (value), example: SCB1234 ```required```


#### Function:

    qr_payment.gererate_qr_30_qr_cs(amount=100.00, invoice="TH0872312", ref1="TH1234", ref2="OG44", ref3="KKK")

#### Response:

    {
      'status': {
        'code': 1000,
        'description': 'Success'
      },
      'data': {
        'qrRawData': '00020101021202164539274960923400303701155833191498329610206TH12340304OG44...', 'qrImage': 'R0lGODdh9AH0AYAAAAAAAP///ywAAAAA9AH0AQAC/4yPqcvtD6OctNqLs968+w+G4kiW5omm6sq27gvH8kzX9o3n+s73/g8MCofEovGITCqXzKbzCY0eANSq9YrNardcAKN75YCt37GZvNKWsRT1xK04e9...',
        'csExtExpiryTime': '2020-05-19 22:55:02',
        'qrcodeId': '20200519095502798000000',
        'merchantId': '058041048495401',
        'merchantName': 'TestMerchant1587994817',
        'amount': '100',
        'currencyCode': '764',
        'csNote': '',
        'csUserDefined': '',
        'invoice': 'TH0872312',
        'channels': [
          {
            'seqNo': '1',
            'channelName': 'VISA',
            'channelCode': 'VISA'
          }
        ],
        'terminalId': '933271425507787',
        'qrCodeType': 'EM',
        'poi': '12',
        'currencyName': 'Baht',
        'terminalName': 'Sandbox Terminal',
        'responseCode': '000'
      }
    }

### Slip Verification <a name="slipverification"></a>

#### Parameter:

  * ```transaction``` <b>number</b> Transaction Slip ID ```required```


#### Function:

    qr_payment.slip_verification(transaction="202005184XOpuqz4T8KoRWt")

#### Response:

    {
      'status': {
        'code': 1000,
        'description': 'Success'
      },
      'data': {
        'transRef': '202005184XOpuqz4T8KoRWt',
        'sendingBank': '014',
        'receivingBank': '014',
        'transDate': '20200518',
        'transTime': '20:05:28',
        'sender': {
          'displayName': 'Kullawat Changenai',
          'name': 'Kullawat Changenai',
          'proxy': {
            'type': 'ACCOUNT',
            'value': '6543740001'
          },
          'account': {
            'type': 'BANKAC',
            'value': '6543740001'
          }
        },
        'receiver': {
          'displayName': 'TestBiller1587994817',
          'name': 'TestBiller1587994817',
          'proxy': {
            'type': 'BILLERID',
            'value': '583319149832961'
          },
          'account': {
            'type': 'BANKAC',
            'value': '0987654321'
          }
        },
        'amount': '100',
        'paidLocalAmount': '100',
        'paidLocalCurrency': '764',
        'countryCode': 'TH',
        'ref1': 'TH1234',
        'ref2': 'OG44',
        'ref3': 'KKK'
      }
    }


### Payment Inquiry <a name="paymentinquiry"></a>

#### Parameter:

  * ```qr``` <b>number</b> Unique identifier of QR code. ```required```


#### Function:

    qr_payment.payment_inquiry(qr="20200518090809857000000")

#### Response:

    {
      'status': {
        'code': 1000,
        'description': 'Success'
      },
      'data': {
        'transactionId': '20200518090809857000000',
        'qrId': '20200518090809857000000',
        'transactionDateandTime': '2020-05-18T21:09:58+07:00',
        'merchantId': '058041048495401',
        'terminalId': '933271425507787',
        'traceNo': '000002',
        'authorizeCode': '524711',
        'amount': '100.00',
        'merchantPAN': '4539274960923400',
        'consumerPAN': '9999994008730001',
        'currencyCode': '764',
        'paymentMethod': 'QRCS',
        'transactionType': 'SETTLED',
        'channelCode': 'VISA',
        'invoice': 'AA1111B',
        'note': ''
      }
    }
