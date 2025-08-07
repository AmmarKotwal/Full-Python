import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("C:\\Users\\asp\\Desktop\\Full-Python\\AMR\\amr.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

print("Connection With Firebase - Firestore")


name = input("Enter Name: ")
f_name = input("Enter Father's Name: ")
ph_no = input("Enter Phone Number: ")
address = input("Enter Address: ")
eng = float(input("Enter English's Marks: "))
math = float(input("Enter Math's Marks: "))
urdu = float(input("Enter Urdu's Marks: "))
total = eng + math + urdu
print(f"\n{name}'s Total Marks From 300 Is: {total}")
per = (total/300)*100
print(f"{name}'s Percentage Is: {per}%")



fetch_std = db.collection("student").document()
fetch_std.set({
    "name" : name,
    "F_Name": f_name,
    "Phone": ph_no,
    "address": address,
    "Eng_Marks": eng,
    "Math_Marks": math,
    "Urdu_Marks": urdu,
    "total": total,
    "percentage": per
})

print("\nStd's Data Has Been Added Successfully!")