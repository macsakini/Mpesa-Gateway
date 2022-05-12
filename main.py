from authorize import Authorize
from express import Express

#get client credentials via app/flask/terminal
print("Enter the amount to request")
amount = int(input())
print("\n")

print("Enter your phone number")
phone = int(input())


if __name__ == "__main__":
    auth = Authorize()
    try:
        access = auth.auth()
    except:
        print("Authorization failed")

    transact = Express(access, amount, phone)
    transact.initiate()


