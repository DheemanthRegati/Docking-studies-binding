import math
def dist(a1, a2, file): # function to give distance given 2 co-ordinates
    xyz1, xyz2 = [], []
    if a1 == a2:
        #print 'same atom'#trivial condition
        return 0
    for row in file:
        if row[7:11] == a1 and (row[:4] == 'ATOM' or row[:4] == 'HETA'):
            xyz1 = getcoor(row) #getting co-ordinates of atom1
        elif row[7:11] == a2 and (row[:4] == 'HETA' or row[:4] == 'ATOM'):
            xyz2 = getcoor(row)#getting co-ordinates of atom2
    ans = math.sqrt(((xyz1[0]-xyz2[0])**2)+((xyz1[1]-xyz2[1])**2)+((xyz1[2]-xyz2[2])**2))#formula of distance
    return ans

def getcoor(line):#function to give co-ordinates given atom no.
    var1 = line[31:54]
    var1 = var1.split()
    for count in range(len(var1)):
        var1[count] = float(var1[count])
    return var1

pdb = open("model_2.pdb", "r")
pepset = []
seta = [' 346', ' 360', ' 289', ' 283', ' 105', ' 112',' 451',' 326','2560','2595','2622','1428']
setb = ['1966', '1980', '1909', '1903', '1725', '1732','2071','1946',' 940',' 975','1002','3048']
#seta, setb = [' 451',' 326','2560','2595','2622','3048'], ['2071','1946',' 940',' 975','1002','1428']#only white parts
#seta, setb = [' 346', ' 360', ' 289', ' 283', ' 105', ' 112'], ['1966', '1980', '1909', '1903', '1725', '1732']#og binding site
for l in pdb:
    if l[12:16] == " CA " and l[21] == 'C':
        pepset.append(l[7:11])#finding and storing atom numbers of CA in C chain(peptide)
pdb.seek(0)
v1, v2 = False, False
for a in seta:
    k = False
    for p in pepset:
        pdb.seek(0)
        if dist(a, p, pdb) <= 8:
            pdb.seek(0)
            v1 = True
            k = True
            break
    if k == False:
        v1 = False
        break

for b in setb:
    k = False
    for p in pepset:
        pdb.seek(0)
        if dist(b, p, pdb) <= 8:
            pdb.seek(0)
            v2 = True
            k = True
            break
    if k == False:
        v2 = False
        break
if v1 == True or v2 == True:
    print('peptide is in binding site')
else:
    print('peptide is not in binding site')
