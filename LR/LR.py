import pandas as p
import matplotlib.pyplot as map
from sklearn.linear_model import LinearRegression

# (pip install openpyxl)

# pip install numpy scipy pandas scikit-learn matplotlib
mydata = p.read_excel("ammar.xlsx")
x=mydata[["Hours Studied (X)"]]
y=mydata["Marks (Y)"]

# null hatane k liye
x=x.dropna()
y=y.loc[x.index]

model = LinearRegression()
model.fit(x,y)

# y= mx + b
print(f"m value = {model.coef_[0]:.2f}")
print(f"b value = {model.intercept_:.2f}")

user_value=float(input("Enter Value : "))
predict_value = model.predict([[user_value]])

print(f"On {user_value} this study hour\nScore will be: {predict_value[0]:.2f}")