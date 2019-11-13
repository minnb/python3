import os
import shutil

src = 'C:\\Users\\Administrator\\Downloads\\image'
des = 'C:\\Users\\Administrator\\Downloads\\image\\new\\'

#BAI 1
names = os.listdir(src)
for name in names:
    file_src = os.path.join(src, name)
    if os.path.isfile(file_src):
        new_des = des + os.path.splitext(name)[1][1:]
        if not os.path.isdir(new_des):
            os.mkdir(new_des)
        file_des = os.path.join(new_des, name)
        shutil.copyfile(file_src, file_des)

#BAI 2
lst_file = os.listdir(src)
join_file = os.path.join(src, "new_file.txt")
if os.path.exists(join_file):
    os.remove(join_file)

new_file = open(join_file, "a", encoding='utf-8')

for file_name in lst_file:
    full_file = os.path.join(src, file_name)
    if os.path.isfile(full_file) and full_file != join_file and os.path.splitext(file_name)[1][1:] == "txt":
        with open(full_file) as file:
            new_file.write(file_name + "\n")
            new_file.write("-----------\n")
            new_file.write(file.read() + "\n")
            new_file.write("\n")

new_file.close()





