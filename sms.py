import requests
# Sending sms message via SMSGateWay24
class SMSGateWay24(object):

    url = "https://smsgateway24.com/getdata/addsms" # compy from the website
    token = "your token" # put your own token
    device_id = "your device id" # put your device id here
    
    headers = {
        'apikey': "api key",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
        }
        
    def __init__(self, dstNumber, msg):
        self.dstNumber = dstNumber
        self.msg = msg
    
       
    def sendSMS(self):

        payload = "token="+self.token+"&sendto="+self.dstNumber+"&body="+self.msg+"&device_id="+self.device_id
        response = requests.request("POST", self.url, data=payload, headers=self.headers)
        return response.text

#Testing Code
number = "destination phone number" # destination phone number
text = "Test 1 2 3" # text message
smsGate = SMSGateWay24(number, text)

print(smsGate.sendSMS())
