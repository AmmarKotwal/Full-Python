import pandas as p
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = p.read_csv("diabetes2.csv")
data = data.replace({"Yes":1,"No":0,"yes":1,"no":0})

x = data[["Glucose","BloodPressure","Insulin","BMI","DiabetesPedigreeFunction"]]
y = data["Outcome"]
data = data.dropna()

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3,random_state=50)

model = LogisticRegression(max_iter=1000)
model.fit(xtrain,ytrain)

Glucose = float(input("Enter Your Glucose Level: "))
BloodPressure = float(input("Enter Your Blood Pressure: "))
Insulin = float(input("Enter Your Insulin Count: "))
BMI = float(input("Enter Your BMI Count: "))
DiabetesPedigreeFunction = float(input("Enter Your DiabetesPedigreeFunction Level: "))

user_input = [[Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction]]
prediction = model.predict_proba(user_input)
predict = prediction[0][0]
pridiction_Percentage = prediction[0][0] * 100

if(pridiction_Percentage >= 50):
    print(f"You Can Have Sugar, Chances has {pridiction_Percentage:.2f}%")
else:
    print(f"You Are Atleast Save From Sugar Now!")

