import os

dirname = "C:\\Program Files\\VideoLAN\\VLC"

# os.chdir(dirname)
# cmd = "vlc.exe"
# os.system(cmd)
current_dir = os.path.dirname(__file__)
new_file_path = os.path.join(current_dir,'loki.txt')
# print(new_file_path)

file_list = os.listdir(current_dir)

for _file in file_list:
    print(os.path.join(current_dir,_file))
