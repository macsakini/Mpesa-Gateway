# Mpesa Gateway

This is the mpesa gateway repo.

# Instructions on running the application

Currently there exists no user interface for the application. Fork the application to a folder on your desired location.

The main.py file requires inputs from the terminal. Thus use the following steps:

1. Run __python main.py__ on your terminal/command prompt.

2. Upon running it will require the first input, this is the amount...i.e 70 
*press enter*

3. The next input is the phone number to make request from i.e 254700000000
*press enter*

4. Check your mobile phone for the request. __DO NOT ENTER YOUR PIN__

5. Cancel the request.


# Specifications

This code will work with any app provided amount and phone number are sent to the api url. It will also send responses to set urls in the env file.

You can connect this said url to a bulk messaging provider which will then maybe push custom messages to your clients.