import os, sys

# Specify directory
# In your case, you may want something like the following
my_directory = os.getcwd()

#print("hello")
# Start the loop
for folder, sub_folders, files in os.walk(my_directory):
  for special_file in files:
    if special_file.startswith('ener'):
      #print 'testing'
      file_path = os.path.join(folder, special_file)
     # with open(file_path, 'r+') as read_file:
      #print('Reading math txt file ' )

        # Print the file
       # for line in read_file:
      #     print(line)


      # Open and read
      k = open(file_path, 'r')
      a=k.read()
      k.close()
  
        # Print the file
      a = a.replace(",","  ")
      f = open(file_path,'w')
      f.write(a)
      f.close()
        # Increment the counter
        
        