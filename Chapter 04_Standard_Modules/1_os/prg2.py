import os

BASE_DIR = r'C:\Users\loki\PycharmProjects\Learning_Python\Chapter 04_Standard_Modules'

print(os.walk(BASE_DIR))
# for root, _dir, _file in os.walk(BASE_DIR):
#     print("Root: ", root)
#     print("Dir: ", _dir)
#     print("File: ", _file)

new_path = os.path.join(BASE_DIR, 'loki', 'test')
print(new_path)
print(os.path.split(BASE_DIR))
_file = r'C:\Users\loki\PycharmProjects\Learning_Python\Chapter 04_Standard_Modules\1_os\prg1.py'
print(os.path.dirname(_file))
print(os.path.basename(_file))
print(os.path.abspath(_file))


