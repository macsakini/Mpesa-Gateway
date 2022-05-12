import os
from dotenv import load_dotenv
import base64
import time
import requests

class Express():
    def __init__(self, auth_details, amount, phone):
        #get url
        self.process_url = os.getenv("TRANSACTION_URL")

        #get auth details
        self.auth_details = auth_details

        # transaction parameters
        self.BusinessShortCode = os.getenv("TILL")
        self.TransactionType = "CustomerPayBillOnline"
        self.Amount =  amount
        self.PartyA = phone
        self.PartyB = os.getenv("TILL")
        self.PhoneNumber = phone
        self.CallbackURL = os.getenv("CALLBACK_URL")
        self.AccountReference = "CustomerPayBillOnline"
        self.TransactionDesc = "TestTest"

        #get till passkey
        self.Passkey = os.getenv("PASSKEY")

    #YYYYMMDDHHmmss
    def gettime(self):
        return time.time

    def create_password(self):
        time  = self.gettime

        pass_str = self.BusinessShortCode + self.Passkey + str(time)

        password = base64.b64encode(pass_str)

        return password, time

    #initiate transaction
    def initiate(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.auth_details["access_token"]}'
        }

        body = {
            "BusinessShortCode":self.BusinessShortCode,
            "Password":self.create_password[0],
            "Timestamp":self.create_password[1],
            "TransactionType":self.TransactionType,
            "Amount":self.Amount,
            "PartyA":self.PartyA,
            "PartyB":self.PartyB,
            "PhoneNumber":self.PhoneNumber,
            "CallbackURL":self.CallbackURL,
            "AccountReference":self.AccountReference,
            "TransactionDesc":self.TransactionDesc,
        }

        response = requests.request("POST", self.process_url, headers = headers, data = body)
        
        if response.status_code == 200:
            return 'success'
        else:
            print("request failed")