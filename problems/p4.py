def pal():
    result=[]
    for i in range(100,999):
        for j in range(100,999):
            m=j*i
            if str(m)==str(m)[::-1]:
                result.append(str(m))
                
    return (max(result)

print(pal())
