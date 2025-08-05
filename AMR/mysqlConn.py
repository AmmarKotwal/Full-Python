import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "studb"
)

db_info = con.cursor()

print("!------- Student's Data -------!")
name = input("Enter Your Name: ")
guardian_name = input("Enter Your Guardian's Name: ")
f_ph_no = input("Enter Your Father's Phone Number: ")
address = input("Enter Your Address: ")



query = "INSERT INTO `student`(`name`, `guardian_name`, `f_phoneNumber`, `address`) VALUES (%s,%s,%s,%s)"
value = (name,guardian_name,f_ph_no,address)

run = db_info.execute(query,value)
con.commit()

print(f"{name}  Data Has Been Saved Successfully")

con.close()