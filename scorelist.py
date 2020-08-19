score=[]
maxscore=0
minscore=100
total=0

l=[]


for i in range(5):
    n=int(input("成績:"))
    score.append(n)
    a=input("請輸入名字:")
    l.append(a)

    if n>maxscore:
        maxscore=n
        maxname=a
    if n<minscore:
        minscore=n
        miname=a
    total=total+n
    
s=total/len(score)
print('總分:',total)
print('平均:',s)
print('最高分:',maxscore)
print('最低分:',minscore)
print('最高分姓名:',maxname)
print('最低分姓名:',miname)