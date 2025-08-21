from datetime import datetime
def create_contact():
    first_name=""
    last_name=""
    phone=""
    while first_name != type(str) or first_name == "":
        first_name = input("Enter first name: ")
    while last_name != type(str) or last_name == "":
        last_name = input("Enter last name: ")
    while phone != type(str) or phone == "":
        phone = input("Enter phone number: ")
    email = input("Enter email: ")
    street = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")
    category = input("Category of contact: ")
    notes = input("Contact notes: ")
    return {'first_name':first_name,'last_name':last_name,'phone':phone,'email':email,'address':{'street':street,'city':city,'state':state,'zip_code':zip_code},'category':category,'notes':notes,'created_date':datetime.today().strftime('%Y-%m-%d'),'last_modified':datetime.today().strftime('%Y-%m-%d')}