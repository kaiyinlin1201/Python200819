import os.path


if os.path.isfile('g.txt'):
    print('存在') 
    file=open('g.txt','a')
    file.write('檔案94存在')
    file.close()
else:
    print('不存在')
    file=open('g.txt','w')
    file.write('這是新的檔案')
    file.close()
    

    