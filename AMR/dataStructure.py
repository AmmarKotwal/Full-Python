# list,Dictionary

courses = ["ms-office","DMW","PHP","Laravel","SSMS","Dart","Flutter","MERN","R","Python"]

print(courses)
print(courses[6])
print(courses[-3])
print(courses[-1])
print(courses[2:6])

print(f"Total Elements In This List: {len(courses)}")


courses.append("Python")
courses.append("Hadoop")
courses.insert(6,"PWD")
courses.insert(9,"Data Analytics")
print(f"Now Length Of List Is: {len(courses)}")

more_courses = ["mongodb","flutter","NodeJs","Vuejs"]
courses.extend(more_courses)
print(f"Now Length Of List Is: {len(courses)}")

courses.remove("DMW")
courses.pop()
print(f"Now Length Of List Is: {len(courses)}")

courses.sort()
courses.sort(reverse=True)

more_courses_add = ["Urdu","IOT","Networking"]
courses.extend(more_courses_add)
print(f"Now Length Of List Is: {len(courses)}")

courses.clear()
print(f"Now Length Of List Is: {len(courses)}")


