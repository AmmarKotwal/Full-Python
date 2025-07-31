import os.path
import pandas
from pydriller import Repository

url = input("Please Enter Github's Repository Links: ")

comName,comEmail,date,projectName,comMsg = [],[],[],[],[]
print(f"Fetching URL {url}")
for a in Repository(url).traverse_commits():
    comName.append(a.author.name)
    comEmail.append(a.author.email)
    date.append(a.committer_date)
    projectName.append(a.project_name)
    comMsg.append(a.msg)

print("Fetching Completed")
github_dict = {
    "Project Name" : projectName,
    "Author Name" : comName,
    "Author Email" : comEmail,
    "Msg" : comMsg,
    "Date" : date
}

github_df = pandas.DataFrame(github_dict)

FileName = input("Enter FilleName: ")
if os.path.exists(f"{FileName}.csv"):
    print(f"{FileName} already exist!, Please Choose Different Name: ")
else:
    github_df.to_csv(f"{FileName}.csv",index = False)
    print("File Created Successfully!")


