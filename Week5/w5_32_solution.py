import  csv

header = ['Sid','Sname','City','MONO']

file_record=[
    [1,'Nikhil','Songadh',1234567890],
    [2,'pritesh','Bardoli',1213141516],
    [3,'uday','Vyara',8989890000],
    [4,'jay','Songadh',1234500001],
    [5,'prince','Surat',7227848152]
    ]

main_list=[]
for i in range(5):
    sid=int(input("Enter Student Id :"))
    sname=input("Enter Student Name :")
    scity=input("Enter Student City :")
    scontact=int(input("Enter Student Contact :"))
    sub_lis=[sid,sname,scity,scontact]
    main_list.append(sub_lis)

file_record.extend(main_list)

with open('student.csv','w',newline="") as file_create:
    file_date = writer(file_create)
    file_date.writerow(header)
    file_date.writerows(file_record)

with open("student.csv",'r') as file_read:
    read_date = reader(file_read)
    for i in read_date:
        print(i)
