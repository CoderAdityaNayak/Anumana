gnum=2; arr=[]; arr2=[]; c=0;
ognum=100;
def checker(ognum,gnum):
    arr=[];
    arr2=[];
    c=0; #number of correct digits
    while(ognum>0):
        arr2.append(ognum%10)
        ognum=ognum//10;
    while(gnum>0):
        arr.append(gnum%10)
        gnum=gnum//10;
    if len(arr)==2:
        arr.append(0)
    if len(arr)==1:
        arr.append(0)
        arr.append(0)
    arr=arr[::-1];arr2=arr2[::-1]
    print(arr,arr2)
    for i in range(len(arr)):
        if arr[i]==arr2[i]:
            c+=1;
    print(c)
    return c