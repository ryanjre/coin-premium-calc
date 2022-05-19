import requests

print("Precious Metal premium Calculator, by Ryan \nryanre103@gmail.com\n")

#Get info about coin or bar
coinprice = float(input("Enter coin price in USD: "))
metalchoice = input("Gold or silver? ")
weight = input("What is the weight (troy oz) of the coin? ")

#convert weight to decimal
try :
    float(weight)
    weightdec = float(weight)
except:
    
    num,denom = weight.split('/')
    weightdec = int(num) / int(denom)
    
    
#Get price data via GoldAPI for chosen metal
my_headers = {"x-access-token": "PASTE API KEY HERE"}
if metalchoice.lower() == 'gold':
    response = requests.get('https://www.goldapi.io/api/XAU/USD', headers=my_headers)
elif metalchoice.lower() == 'silver':
    response = requests.get('https://www.goldapi.io/api/XAG/USD', headers=my_headers)
else:
    print("Invalid metal choice")
    
#Get spot price
responsedict = response.json()
spot = float(responsedict['ask'])

#calculate premium and display
premium = (( (coinprice / weightdec ) - spot ) / spot ) * 100
print(f"the coin's premium is {premium:.2f}% over spot.")
