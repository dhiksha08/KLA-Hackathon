import math

with open("/Users/dhikshitha./Desktop/KLA-Hackathon/Kla hackathon/Milestone2/Input/Testcase"+str(2)+".txt", "r") as file1:
        read_content = file1.readlines()
        print(read_content)
data={}
for line in read_content: 
    key, value = line.strip().split(':') 
    data[key] = value
    
print(data)
print(read_content,end='\n\n')
x=int(data['DieSize'].split('x')[0])
y=int(data['DieSize'].split('x')[1])
r=float(data['WaferDiameter'])*1.0/2

shift_x=x-float(data['DieShiftVector'].split(',')[0].split('(')[1])
shift_y=y-float(data['DieShiftVector'].split(',')[1].split(')')[0])

ref_die_x=float(data['ReferenceDie'].split(',')[0].split('(')[1])
ref_die_y=float(data['ReferenceDie'].split(',')[1].split(')')[0])

o_x,o_y=abs(int(math.trunc(ref_die_x/x))),abs(int(math.trunc(ref_die_y/y)))
print(o_x,o_y)
max_x=abs(math.ceil(r/x))
max_y=abs(math.ceil(r/y))

print(max_x,max_y)

res={}
for i in range(0,max_x+1):
    for j in range (0,max_y+1):
        #print(i,j,(math.dist((o_x*x,o_y*y),(i*x,j*y))))
        if ((math.dist((0,0),(i*x,j*y)))<=(r+x-1)):
            res[(i-o_x,j-o_y)]=(round(i*x*1.0,4)+shift_x,round(j*y*1.0,4)+shift_y)
            res[(-1*i-o_x,j-o_y)]=(round(i*x*1*-1.0,4)+shift_x,round(j*y*1.0,4)+shift_y)
            res[(i-o_x,-1*j-o_y)]=(round(i*x*1.0,4)+shift_x,round(j*y*-1*1.0,4)+shift_y)
            res[(-1*i-o_x,-1*j-o_y)]=(round(i*x*-1.0,4)+shift_x,round(j*y*-1.0,4)+shift_y)


print(res)
temp=""
for i in res:
    temp+=str(i)+":"+str(res[i])+"\n"
print(temp)
with open("/Users/dhikshitha./Desktop/KLA-Hackathon/KLA-Hackathon/Output24"+".txt", "w") as file1:
    file1.write(temp)