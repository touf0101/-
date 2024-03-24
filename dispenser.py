import csv

for i in range(1,10):
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
        print(i,':',globals()[i])


with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    room_list = []
    for o in fin:
        if len(fin.get(o)) > 2:
            for row in data:
                if row[0] in fin.get(o):
                    value_list = []
                    value_list.append(row[0])
                    value_list.append(row[2])
                    room_list.append(value_list)

    value = []

    for a in room_list:
        value.append(a[1])
    value.sort()
    max=value[-1]
    max_list=[]
    remain=[]
    for a in room_list:
        if len(max_list) <= 2:
            if a[1] == max:
                max_list.append(a[0])
            else:
                remain.append(a[0])   
        else:
            break

    
with open('test_case.csv','r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)
    for row in data:
        if row[0] in remain:
            globals()[room[int(row[3])]].append((row[0]))
            

for o in fin:
        if len(fin.get(o)) > 3:
            globals()[o]=max_list


for i in globals():
    if i in room:
        fin[i] = globals()[i]
        print(i,':',globals()[i])
    

