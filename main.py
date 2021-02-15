from pymongo import MongoClient, collection
from datetime import datetime
# from termcolor import colored

# this is made by Rishav Kumar (lazy_codex)

try:
    conn = MongoClient()
    print("connected")
except:
    print("not connected")

db = conn.database
collection = db.messages

cluster = MongoClient("mongodb+srv://lazycodex:12345@messaging.te9v1.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["socialmessaging"]["messages"]
all = db.find({})
date = datetime.now().strftime("%x")

# for messages in all:
#     try:
#         if date != messages["date"]:
#             print(colored(f"Today - {messages['time']}", 'red'))
#         else:
#             print(colored(f"{messages['date']} - {messages['time']}", 'red'))
#         print(colored("From: ", 'green'), messages['id'])
#         print(colored("Message: ", 'green'), messages['message'])
#         print("--------------------------")
#     except:
#         pass

for messages in all:
    try:
        if date != messages["date"]:
            print(f"Today - {messages['time']}")
        else:
            print(f"{messages['date']} - {messages['time']}")
        print("From: ", messages['id'])
        print("Message: ", messages['message'])
        print("--------------------------")
    except:
        pass

person = input("Name: ")
message = input("Message: ")

time = datetime.now().strftime("%X")
msg = {"id": person, "message": message, "date": date, "time": time}

db.insert_one(msg)
