import pandas as p

rishta = {
    "name" : ["Ali","Ahmed","Sana","Rohan","Dua"],
    "gender" : ["Male","Male","Female","Male","Female"],
    "preferred_caste" : ["Syed","Qureshi","Syeda","Sheikh","Ansari"],
    "preferred_area" : ["Surjani","Orangi","Nazimabad","F.B Area","DHA"],
    "profession" : ["Software Engineer","Electrical Engineer","Teacher","Doctor","Nurse"],
    "no_of_sibling" : [2,3,4,5,1]
}

df_rishta = p.DataFrame(rishta)
df_rishta["age"] = [23,24,25,22,20]
df_rishta["marital_status"] = ["Single","Divorcee","Widow","Widower","Single"]
df_rishta["nationality"] = "Pakistani"
# print(df_rishta[df_rishta["preferred_caste"] == "Pathan"])
# print(df_rishta[df_rishta["no_of_sibling"] > 2])
# print(df_rishta[df_rishta["preferred_area"] == "DHA"])
# print(df_rishta[(df_rishta["preferred_area"] == "Nazimabad") & (df_rishta["gender"] == "Female")])
del df_rishta["profession"]
print(df_rishta)