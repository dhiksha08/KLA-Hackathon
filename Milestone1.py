import math
import numpy as np
for i1 in range(1,5):
    
    with open("/Users/dhikshitha./Desktop/KLA-Hackathon/Kla hackathon/Milestone1/Input/Testcase"+str(i1)+".txt", "r") as file1:
        read_content = file1.readlines()
        print(read_content)
    data={}
    for line in read_content: 
        key, value = line.strip().split(':') 
        data[key] = int(value)

    print(data)
        
    radius = float(data['WaferDiameter'])/2
    angle  = float(data['Angle'])
    radians1= math.radians(angle)
    x1 = radius * math.cos(radians1)
    y1 = radius * math.sin(radians1)
    print(x1,y1)

    radians2=math.radians(angle+180)
    x2 = radius * math.cos(radians2)
    y2 = radius * math.sin(radians2)
    print(x2,y2,end="\n\n")
    x_=np.linspace(x1, x2, num=data['NumberOfPoints'])
    y_=np.linspace(y1, y2, num=data['NumberOfPoints'])
    final=""
    for i in range(data['NumberOfPoints']):
        x=str(round(x_[i],4))
        y=str(round(y_[i],4))
        coord='('+x+','+y+')'
        print(coord,end='\n')
        final+=coord+'\n'
    with open("/Users/dhikshitha./Desktop/KLA-Hackathon/KLA-Hackathon/Output"+str(i1)+".txt", "w") as file1:
        file1.write(final)