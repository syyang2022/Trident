import os

DIR_PATH = 'D:\\Download\\安监赛题\\安监赛题-电网典型作业现场防高坠类违章检测\\Dataset\\高空作业无人监护\\tg_gkzy_yrjh\\Annotation'
change = 'tg_gkzy_yrjh'

files = os.listdir(DIR_PATH)

for file in files:
    oldname = DIR_PATH + '\\' + file
    newname = DIR_PATH + '\\' + change + '_' + file
    os.rename(oldname, newname)
