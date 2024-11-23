from kavenegar import *

def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('place your api key')
        params = {
            'sender':'Test online shop',
            'receptor':phone_number,
            'message':f'Your otp code: {code}'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)