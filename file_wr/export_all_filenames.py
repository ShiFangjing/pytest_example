import os

allpath = []
allname = []


def getallfile(dir):
    """"递归输出所有文件名称（绝对路径）"""
    allfilelist = os.listdir(dir)
    # 遍历该文件夹下的所有目录或者文件
    for file in allfilelist:
        filepath = os.path.join(dir, file)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            allpath.append(filepath)
            allname.append(file)
    return allpath, allname


a, b = getallfile('E:\\2_PythonProject\\pytest_api_autotest')
print([item for item in allpath])
print('\n'.join(item for item in allpath))
