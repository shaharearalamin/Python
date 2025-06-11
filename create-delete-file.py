# **create single file 
with open ('create-single.py', 'w') as create:
    create.write()

# **create multiple file 
file_name= ['list1.pdf','list2.pdf','list3.pdf']
for create in file_name:
    with open(create,'w') as new_file:
        new_file.write("create multiple file")

# **Delete a single file
import os 
os.remove('create-single.py')

# **Delete multiple file
import os
del_file= ['list1.pdf', 'list2.pdf', 'list3.pdf']
for delete in del_file:
    os.remove(delete)

