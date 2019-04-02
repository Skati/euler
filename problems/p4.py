def pal(num=3):
    result=[]
    largest=0
    for i in range(10**(num-1),10**num):
        for j in range(i,10**num):
            m=j*i
            if str(m)==str(m)[::-1] and m>largest:
                largest=i*j
                i_=i
                j_=j
                result.append(m)
    return largest,i_,j_

print(pal())
