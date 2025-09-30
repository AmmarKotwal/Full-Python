import pandas as p
import matplotlib.pyplot as map
from sklearn.linear_model import LinearRegression

my_data = p.read_excel("std.xlsx")
X = my_data[["studyHours"]]
Y = my_data["Marks"]

