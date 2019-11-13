import os

src = 'C:\\Users\\Administrator\\Downloads\\image'
lst_file = os.listdir(src)
new_file = open(os.path.join(src, "new_file.txt"), "a", encoding='utf-8')
for file_name in lst_file:
    if os.path.splitext(file_name)[1][1:] == "txt":
        full_file = os.path.join(src, file_name)
        with open(full_file) as file:
            new_file.write(file_name + "\n")
            new_file.write("-----------\n")
            new_file.write(file.read() + "\n")
            new_file.write("\n")

new_file.close()
