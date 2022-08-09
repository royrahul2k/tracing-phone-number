import phonenumbers 
from phonenumbers import geocoder,carrier
a=input('ENTER YOUR NUMBER: ')
num= phonenumbers.parse(a)
operatorname= carrier.name_for_number(num,'en') 
countryname=geocoder.description_for_number(num,"en")
print(num)
print(operatorname)
print(countryname)