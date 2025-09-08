from datetime import datetime
def create_contact():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    street = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")
    category = input("Category of contact: ")
    notes = input("Contact notes: ")
    return {'first_name':first_name,'last_name':last_name,'phone':phone,'email':email,'address':{'street':street,'city':city,'state':state,'zip_code':zip_code},'category':category,'notes':notes,'created_date':datetime.today().strftime('%Y-%m-%d'),'last_modified':datetime.today().strftime('%Y-%m-%d')}
#contact=create_contact()
sam={'first_name':'Samuel','last_name':'Rookstool','phone':'9943042358','email':'srrookstool01@indianatech.net','address':{'street':'1653 Abby Dr','city':'Fort Wayne','state':'IN','zip_code':'46803'},'category':'work','notes':'This is not real information','created_date':'2025-08-25','last_modified':'2025-08-25'}

contacts_db = {}
def add_contact(contacts_db,contact_data):
    id = len(contacts_db)+1
    contacts_db[id] = contact_data
    return id
add_contact(contacts_db,sam)
print(contacts_db)
def display_contact(contacts_db, contact_id):
    try: contact = contacts_db[contact_id]
    except: return False
    else:
        print('Name: ', contact['first_name'],contact['last_name'])
        print('Phone: ', contact['phone'])
        print('Email: ', contact['email'])
        print('Address: ', contact['address']['street']+",",contact['address']['city']+",",contact['address']['state']+",",contact['address']['zip_code'])
        print('Category: ',contact['category'])
        print('Additional notes: ',contact['notes'])
        print('Date created: ',contact['created_date']," Date modified: ",contact['last_modified'])
        return True
display_contact(contacts_db,1)
    
def list_all_contacts(contacts_db):
    for x,y in contacts_db.items():
        print("ID = ",x)
        print("Name = ",y['first_name'],y['last_name'])
        print("Phone = ",y['phone'])
        print()
list_all_contacts(contacts_db)

def search_contacts_by_name(contacts_db, search_term):
    group=dict()
    for x,y in contacts_db.items():
        if y['first_name'] or y['last_name'] == search_term:
            group[x] = y
    return group

print(search_contacts_by_name(contacts_db,"Samuel"))

def search_contacts_by_category(contacts_db,category):
    group=dict()
    for x,y in contacts_db.items():
        if y['category']== category:
            group[x] = y
    return group

def find_contact_by_phone(contacts_db, phone_number):
    group=dict()
    for x,y in contacts_db.items():
        if y['phone'] == phone_number:
            return x,y
    return (None,None)

def update_contact(contacts_db,contact_id,field_updates):
    contacts_db[contact_id].update(field_updates)
    contacts_db[contact_id].update({'last_modified': datetime.today().strftime('%Y-%m-%d')})

def delete_contact(contacts_db, contact_id):
    try: contacts_db.pop(contact_id)
    except: return False
    else: return True

def merge_contacts(contacts_db, contact_id1, contact_id2):
    newid=len(contacts_db)+1
    conflict=0
    mergecontact={newid:dict()}
    for x,y in contacts_db[contact_id1],contacts_db[contact_id2]:
        for a,b,c,d in x.items() and y.items():
            if b == d:
                mergecontact[newid].update({a,b})
            else:
                while conflict != "1" or conflict != "2":
                    conflict=input("Conflict in field: ",a,"/n Value 1: ",b,"/n Value 2: ",d,"/n Enter a number: ")
                if conflict == "1":
                    mergecontact[newid].update({a,b})
                elif conflict == "2":
                    mergecontact[newid].update({c,d})
    return mergecontact
        
def run_contact_manager():
    pass
if __name__ == "__main__":
    run_contact_manager()