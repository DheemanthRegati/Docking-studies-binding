import math
import os
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
txtfile= open("totaldata.txt",'w+')
for c in range(9,13):
    print ("test =", c)
    txtfile.write(str(c))
    txtfile.write(' minimum residues having proximity')
    txtfile.write("\n")
    my_directory = os.getcwd()
    for folder, sub_folders, files in os.walk(my_directory):
        for special_file in files:
            if special_file.startswith('model_'):
                file_path = os.path.join(folder, special_file)
                pdb=open(file_path,'r')
                print file_path[-15:]
                #txtfile.write(file_path[-15:])
                #txtfile.write('\n')
                pepset = []
                seta = [' 346', ' 360', ' 289', ' 283', ' 105', ' 112',' 451',' 326','2560','2595','2622','1428']
                setb = ['1966', '1980', '1909', '1903', '1725', '1732','2071','1946',' 940',' 975','1002','3048']
                #seta, setb = [' 346', ' 360', ' 289', ' 283', ' 105', ' 112'], ['1966', '1980', '1909', '1903', '1725', '1732']#og set definition
                for l in pdb:
                    if l[12:16] == " CA " and l[21] == 'C':
                        pepset.append(l[7:11])#finding and storing atom numbers of CA in C chain(peptide)
                pdb.seek(0)
                counta, countb = 0, 0
                for a in seta:
                    for p in pepset:
                        pdb.seek(0)
                        if dist(a, p, pdb) <= 10:
                            pdb.seek(0)
                            counta= counta+1
                            break
                    if counta >=c:
                        break

                for b in setb:
                    for p in pepset:
                        pdb.seek(0)
                        if dist(b, p, pdb) <= 10:
                            pdb.seek(0)
                            countb= countb+1
                            break
                    if countb >=c:
                        break
                if counta>=c or countb>=c:
                    #print 'peptide is in binding site'
                    txtfile.write(file_path[-15:])
                    txtfile.write('\n')
                #else:
                #   print 'peptide is not in binding site'
txtfile.close()