import csv

for i in range(10):
    globals()['room{}'.format(i)] = []


room=list(globals().keys())


for k in room:
    if k[0:4] != 'room':
        room.remove(k)
room=room[5:]


with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    for row in data:
        for j in range(1,7):
            row[-j] = int(row[-j])
        for h in range(1,7):
            if row[1] == h:
                globals()[room[h]].append((row[0]))
      
         
fin = {}
for i in globals():
    if i in room:
        fin[i] = globals()[i]
del fin['room0']


with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    room_list = []
    for o in fin:
        if len(fin.get(o)) > 2:
                for row in data:
                    if row[0] in fin.get(o):
                        room_list.append(row)
                    
 
    favor = []

    for a in room_list:
        favor.append(a[2])


    favor.sort()
    max=int(favor[-1])
    select_list=[]
    remain=[]
    
    for a in room_list:
        if len(select_list) <= 2:
            if int(a[2]) == max:
                select_list.append(a[0])
            else:
                remain.append(a[0])
        else:
            max-=1
    if len(select_list+remain) != len(room_list):
        remain.append(a[0])


  
with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    for row in data:
        if row[0] in remain:
            globals()[room[int(row[3])]].append((row[0]))
            

for o in fin:
    if len(fin.get(o)) > 3:
        globals()[o]=select_list


for i in fin:
    fin[i] = globals()[i]



with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    room_list = []
    for o in fin:
        if len(fin.get(o)) > 2:
            for row in data:
                if row[0] in fin.get(o):
                    favor_list = []
                    favor_list.append(row[0])
                    favor_list.append(row[2])
                    favor_list.append(row[4])
                    favor_list.append(row[6])
                    room_list.append(favor_list)


sec_favor=[]
for j in room_list:    
    sec_favor.append(j[2])

sec_favor.sort()

max = int(sec_favor[-1])
select_list=[]
remain=[]

for i in room_list:
    if len(select_list) < 2:
        if int(i[2]) == max:
            select_list.append(i[0])

        else:
            remain.append(i[0])
    else:
        max-=1
if len(select_list+remain) != len(room_list):
    remain.append(i[0])

with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    for row in data:
        if row[0] in remain:
            globals()[room[int(row[3])]].append((row[0]))
        elif row[0] in select_list:
            globals()[room[int(row[1])]]=select_list
            

for i in fin:
    fin[i] = globals()[i]
 

    
    
with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    room_list = []
    for o in fin:
        if len(fin.get(o)) > 2:
            for row in data:
                if row[0] in fin.get(o):
                    favor_list = []
                    favor_list.append(row[0])
                    favor_list.append(row[2])
                    favor_list.append(row[4])
                    favor_list.append(row[6])
                    room_list.append(favor_list)
                    

sec_favor=[]
for j in room_list:    
    sec_favor.append(j[2])

sec_favor.sort()

max = int(sec_favor[-1])
select_list=[]
remain=[]

for i in room_list:
    if len(select_list) < 2:
        if int(i[2]) == max:
            select_list.append(i[0])
        else:
            remain.append(i[0])
    else:
        max-=1
if len(select_list+remain) != len(room_list):
    remain.append(i[0])

with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    for row in data:
        if row[0] in remain:
            globals()[room[int(row[3])]].append((row[0]))
        elif row[0] in select_list:
            globals()[room[int(row[1])]]=select_list
            

for i in fin:
    fin[i] = globals()[i]

    
                  

with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    room_list = []
    for o in fin:
        if len(fin.get(o)) > 2:
            for row in data:
                if row[0] in fin.get(o):
                    room_list.append(row)
           

             
for i in room_list:
    for j in range(len(remain)):
        if remain[j] in i:
            room_list.remove(i)
            with open('test_case.csv','r', encoding='utf-8') as f:
                data = csv.reader(f, delimiter=',')
                header = next(data)
                new_list=[]
                for row in data:
                    if row[0] in remain[j]:      
                        new_list.append(row)    
                        
room_list+=new_list                 

divi_list=[]
for o in fin:
    if len(fin.get(o)) > 2:
        for i in room_list:
            if i[1] == o[-1]:
                t_list=[]
                t_list.append(i[0])
                t_list.append(i[2])
                divi_list.append(t_list)
            else:
                t_list=[]
                t_list.append(i[0])
                t_list.append(i[4])
                divi_list.append(t_list)



sec_favor=[]
for j in divi_list:    
    sec_favor.append(j[1])

sec_favor.sort()

min = int(sec_favor[0])
select_list=[]
for i in divi_list:
    select_list.append(i[0])
remain=[]

while len(select_list) !=2:
    for i in divi_list:
        if int(i[1]) == min:
            select_list.remove(i[0])
            remain.append(i[0])
if len(select_list+remain) != len(divi_list):
    remain.append(i[0])

with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    for row in data:
        if row[0] in remain:
            globals()[room[int(row[5])]].append((row[0]))
        elif row[0] in select_list:
            globals()[room[int(row[1])]]=select_list
            
            

for i in fin:
    fin[i] = globals()[i]
    print(i, ':', globals()[i])