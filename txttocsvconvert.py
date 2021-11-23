#c = open('s')
import csv

f = open('energy.txt','r')
b = f.read()
f.close() 
c = []
d = "      "
i=0
while(i<6):
    c.append(d)
    d = d.replace(" ","",1)
    i=i+1
print (c)
for n in c:
    b= b.replace(n,",")
f = open('energy.txt','w')
f.write(b)
f.close()
with open('energy.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('energy.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow((' ','replica', 'frame','temparature','energy(receptor)','energy(ligand)','energy(interaction)','energy(total)'))
        writer.writerows(lines)