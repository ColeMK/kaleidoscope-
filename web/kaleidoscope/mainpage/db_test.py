import pyrebase
from config import configUtils
configs = configUtils()
firebase = pyrebase.initialize_app(configs)
database = firebase.database()


# database.child("Downloads").set("Test_ID")
# database.child("Downloads").child("Test_ID").update({"Video_ID":"ID","Video_Status":"Queued"})

# database.child("Queued").set("Video_ID1")
# database.child("Queued").set("Video_ID2")

# database.child("Queued").child('Test_ID1').push("ML_Type")
database.child("Queued").push("Test9")
database.child("Queued").push("Test6")


# Pop Start
data = database.child("Queued").order_by_key().limit_to_first(1).get()

timestamp = data.each()[0].key()
ID = data.each()[0].val()

database.child("Queued").child(timestamp).remove()
# Pop End


# data = database.child("Queued").order_by_key().limit_to_first(1).get()
# timestamp = data.each()[0].key()
# ID = data.each()[0].val()
# print(timestamp)
# print(ID)

