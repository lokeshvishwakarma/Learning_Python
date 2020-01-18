import os

print(os.getenv('PATH'))
env_variables = os.environ

os.environ['LOKI'] = "TEST VALUE"
print(os.getenv('LOKI'))
# for key in env_variables:
#     print(key)

# print(os.name)
# print(os.getcwd())
# print(os.getlogin())
# # print(os.chmod())
# print(os.chdir(r'C:\Users\loki\PycharmProjects\Learning_Python\Chapter 04_Standard_Modules\2_sys'))
# print(os.getcwd())

BASE_DIR = r'C:\Users\loki\PycharmProjects\Learning_Python'
print(os.listdir(BASE_DIR))
directories = os.listdir(BASE_DIR)
new_dir = BASE_DIR + '\\' + directories[-3] + '\\loki'

if os.path.exists(new_dir):
    os.chdir(new_dir)
else:
    print("Path doesn't exist")
    os.makedirs(new_dir)
print(os.getcwd())
