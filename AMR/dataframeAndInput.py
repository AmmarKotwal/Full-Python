import pandas as pd
import lxml

# Step 1: Create the list of 6 dishes
dishes = {
"FoodName": ["Chicken Biryani", "Beef Burger", "Veg Sandwich", "Mutton Karahi", "Zinger Burger", "Paneer Biryani"],
"Price":[1200,550,300, 1800, 600, 950],
"Category": ["Main Course", "Fast Food", "Fast Food", "Main Course", "Fast Food", "Main Course"],
"Main Ingredient": ["Chicken", "Beef", "Vegetables", "Mutton", "Chicken", "Paneer"],
"Quantity":["1 Plate","1 Piece","1 Piece", "1 Dish","1 Piece","1 Plate"],
"Status":["Available", "Available", "Unavailable", "Available", "Available", "Unavailable"]
}

# Step 3: Convert dictionary to DataFrame
df = pd.DataFrame(dishes)
#Step 4: Print DataFrame
print(df)
# Step 5: Add new column *Country*
df["Country"] = "Pakistan"
# Step 6: Add new column "Sale Price" (e.g., 10% discount)
df["Sale Price"]=df["Price"] * 0.9
#Step 7: Print all food item prices greater than 500
print("\nFood items with price greater than 500:")
print(df [df["Price"] > 500])
# Step 8: Print all available food items
print("\nAvailable food items: ")
print(df [df["Status"] == "Available"])
# Step 9: Print all available fast food items
print("\nAvailable fast food items: ")
print(df[(df["Status"] == "Available") & (df["Category"] == "Fast Food")])
# Step 10: Print Biryani items
print(df [df["FoodName"]=="Biryani"])
# Step 11: Print available food items with price greater than 1500
print("\nAvailable food items with price greater than 1500:")
print(df[(df["Status"] == "Available") & (df["Price"] > 1500)])
# Step 12: Ask user for desired format
format_choice = input("\nIn which format do you want to convert data? (csv/json/excel/xml): ").strip().lower()
if format_choice == "csv":
    df.to_csv("dishes.csv", index=False)
    print("Data saved to dishes.csv")
elif format_choice == "json":
    df.to_json("dishes.json")
    print("Data saved to dishes.json")
elif format_choice == "excel":
    df.to_excel("dishes.xlsx", index=False)
    print("Data saved to dishes.xlsx")
elif format_choice == "xml":
    df.to_xml("dishes.xml")
    print("Data saved to dishes.xlsx")
else:
    print("Invalid format selected.")







