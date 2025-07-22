import  random as rd

city_list = ["Karachi", "Lahore", "Islamabad", "Rawalpindi","Faisalabad", "Multan", "Peshawar", "Quetta","Sialkot","Gujranwala"
]
print(rd.sample(city_list,3))
rd.shuffle(city_list)
print(city_list)
print(rd.choice(city_list))