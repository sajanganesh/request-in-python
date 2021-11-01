import requests
import json
import os.path
# using os.path.isfile for check data inside the data.json file
exists = os.path.exists("/home/sajan/PYTHON/request.py/data.json")
print(exists)
if exists:
    with open("/home/sajan/PYTHON/request.py/data.json","r") as data:
        Data=json.load(data)
else:
    x = requests.get("http://saral.navgurukul.org/api/courses")
    Data = x.json()
    with open("/home/sajan/PYTHON/request.py/data.json","w") as f:
        json.dump(Data,f,indent=4)

name_list=[]
serial_number=1
for index in Data["availableCourses"]:
    print(serial_number,"-",index["name"],index["id"])
    name_list.append(index["name"])
    serial_number+=1
topic=int(input("Enter the topic number:"))
# calling parents Api:
exists = os.path.exists("/home/sajan/PYTHON/request.py/parent.json")
print(exists)
if exists:
    with open("/home/sajan/PYTHON/request.py/parent.json","r") as data:
        data=json.load(data)
else:
    x = requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercises")
    data = x.json()
    with open("/home/sajan/PYTHON/request.py/parent.json","w") as f:
        json.dump(data,f,indent=4)
# pushing data into json file:

topic_list=[]
serial_no=1
serial_no1=1
    #for printing the details of the specific courses:

for index1 in data["data"]:
    if len(index1["childExercises"])==0:
        print("   ",serial_no,".",index1["name"])
        topic_list.append(index1["name"])
        print("           ",serial_no1,".",index1["slug"])
        serial_no+=1
    else:
        serial_no2=1
        print("   ",serial_no,".",index1["name"])
        topic_list.append(index1["name"])
        for questions in index1["childExercises"]:
            print("         ",serial_no2,".",questions["name"])
            serial_no2+=1
        serial_no+=1

# taking user input asking for specific parent course:

slug=int(input("Enter the topic number:"))
question_list=[]
slug_list=[]
print("     ",slug,".",topic_list[slug-1])

#code for slug having childExercise(More than one question):

for index1 in data["data"][slug-1]["childExercises"]:
    s_num=1
    for index1 in data["data"][slug-1]["childExercises"]:
        print("           ",s_num,".",index1["name"])
        question_list.append(index1["name"])
        s_num+=1

    que=int(input("Enter question number:")) 
    w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-1]["slug"]))
    DATA=w.json()
    with open("question.json","w") as f:
        json.dump(DATA,f,indent=4)
        print(DATA["content"])
        break

for i in range(len(question_list)):
    a=input("Enter whether you want to go next or previous(n/p):")
    if a=="n":
        if que==len(question_list): 
            print("Next page.")
            break
        else:
            w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que]["slug"]))
            DATA=w.json()
            with open("question.json","w") as f:
                json.dump(DATA,f,indent=4)
                print(DATA["content"])
                que=que+1
    if a=="p":
        if que==len(question_list):
            print("No more questions")
            break
        else:
            w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-2]["slug"]))
            DATA=w.json()
            with open("question.json","w") as f:
                json.dump(DATA,f,indent=4)
                print(DATA["content"])
                que=que-1      

que=int(input("Enter question number:"))
exists = os.path.exists("/home/sajan/PYTHON/request.py/question.json")
print(exists)
if exists:
    with open("/home/sajan/PYTHON/request.py/question.json","r") as data:
        data=json.load(data)
else:
    v=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["slug"]))
    data=v.json()
    with open("/home/sajan/PYTHON/request.py/question.json","w") as f:
        a=json.dump(data,f,indent=4)
        print(a)
        for i in range(len(slug_list)):
            a=input("Enter whether you want to go next or previous:(n/p)")
            if a=="n":
                print("programm finish")
                break
            if a=="p":
                print("No more questions.")
                break



            