import pandas as pd 
name=["Amit", "Sumit","Kapil"]
print(name)
print("--------------------------------------------------")
data=pd.Series(name)
print(data)
print("________________________________--------------------")

roll=[101,102,103,104,105]
name=["Amit","Sumit","Kapil","Rohan","Sumit"]
s_class=[11,12,11,11,12]
section=["A","A","A","B","B"]
eng=[23,23,45,56,78]
sci=[89,56,89,23,56]
com=[78,76,90,56,88]
math=[66,89,90,56,89]

total= list(map(lambda a,b,c,d:a+b+c+d,eng,sci,com,math))
print(total)

data=pd.DataFrame(
    {
        "NAME":name,
        "CLASS":s_class,
        "SECTION":section,
        "ENGLISH":eng,
        "SCIENCE":sci,
        "COMPUTER":com,
        "MATH":math,
        "TOTAL":total
    }
    ,index=roll
)

print(data)
print("-----------------------------------------------------------------")
print(data.describe)
print("-----------------------------------------------------------")
print(data.info())
print("----------------------------------------------------------")

# data=pd.DataFrame(
#     [
#         roll,
#         name,
#         s_class,
#         section
#     ]
# )
# print(data)
print("----------- name--------------")
print(data["NAME"])
print("------------NAME---TOTAL---------------")
print(data[["NAME","TOTAL"]])
print("------------LOC-----------")
print(data.loc[101])
print("----------LOC")
print(data.loc[[101,103]])
print("-----------ILOC---------")
print(data.iloc[[2,3]])
print("-----------")
print(data.iloc[0,6])
print("-----------")
print(data.at[101,"MATH"])
print("-----------")
print(data.iat[0,6])
print("-----------")
print(data.loc[101,"SECTION"])
print("--------------------------")
print(data[data["SCIENCE"]>70])