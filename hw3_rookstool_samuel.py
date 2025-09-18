import re
def format_receipt(items, prices, quantities):
    print("=" * 40)
    print(f"{"Item":<20} {"Qty":^5} {"Price":>8}")
    print("="*40)
    for item,price,quantity in zip(items, prices, quantities):
        print(f"{item:<20} {quantity:^5} {"$":>4} {price:>4.2f}")
    print("=" * 40)
    print(f"{"TOTAL":<20} {"$":>10} {sum(prices):>4.2f}")
    print("=" * 40)
items = ["Coffee", "Sandwich", "Cookie"]
prices = [3.50, 8.99, 2.00]
quantities = [2, 1, 3]
print(format_receipt(items, prices, quantities))
def process_user_data(raw_data):
    cleaned_name = raw_data['name'].strip().title()
    cleaned_email= raw_data['email'].lower().replace(" ","")
    cleaned_phone= ""
    for x in raw_data['phone']:
        if x.isnumeric():
            cleaned_phone += x
    cleaned_address="".join(raw_data['address'].split()).title()
    namelist = cleaned_name.lower().split()
    username= namelist[0] + "_" + namelist[1]
    return {'name':cleaned_name,'email':cleaned_email,'phone':cleaned_phone,'address':cleaned_address,'username':username}

data = {
    'name': ' john DOE ',
    'email': ' JOHN.DOE @EXAMPLE.COM ',
    'phone': '(555) 123-4567',
    'address': '123 main street, apt 5'
    }
result = process_user_data(data)
print(result['name'],result['email'],result['phone'],result['username'])