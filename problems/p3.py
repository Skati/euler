def prime(number):
    lst=[]
    i=2
    while number>=i:
        if number%i==0:
             number/=i
             lst.append(i)
        else: i+=1
    return lst

print(prime(4444))
