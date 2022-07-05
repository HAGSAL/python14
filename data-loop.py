student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for i in student:
    if i["score"]>=80:
        for key,vale in i.items():
            print(key,vale)
            print("grade4")
    elif i["score"]>=70:
        for key,vale in i.items():
            print(key,vale)
            print("grade3")
    elif i["score"]>=60:
        for key,vale in i.items():
            print(key,vale)
            print("grade2")
    elif i["score"]>=50:
        for key,vale in i.items():
            print(key,vale)
            print("grade1")
    elif i["score"]<50:
        for key,vale in i.items():
            print(key,vale)
            print("grade0")
#ณัฐจักขณ์ สีเสนซุย ม.6/14 เลขที่25