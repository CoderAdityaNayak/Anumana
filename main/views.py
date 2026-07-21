import random
from django.shortcuts import render,redirect

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
    s = ""

    for i in range(len(arr)):
        if arr[i] == arr2[i]:
            c += 1
            s += str(arr[i])   
        else:
            s += "X"
    print(c)
    return c, s

def home(request):
    if "num" not in request.session:
        request.session["num"] = random.randint(1000, 9999)
        request.session["attempts"] = []

    num = request.session["num"]
    attempts = request.session["attempts"]

    tnum = "XXXX"
    result = ""
    if 'reset' in request.POST:
            request.session.flush()   
            return redirect('home')   
    if request.method == "POST":
        request.session["attempts"] = []
        gnum = request.POST.get("guessednum")

        if gnum and gnum.isdigit() and (0 < int(gnum) < 10000):
            gnum = int(gnum)

            attempts.append(gnum)
            request.session["attempts"] = attempts

            c,s = checker(num, gnum)

            if c == 4:
                result = "Perfect Guess 🎯"
                tnum = f"The number was {num} and you guessed it in {len(attempts)} attempts✅😃"

                del request.session["num"]
                del request.session["attempts"]
            else:
                result = f"{c} digits correct "
                tnum=s
        else:
            result = "Enter valid 4 digit number 😐"

    return render(request, 'main/index.html', {
        "tnum": tnum,
        "result": result,
        "attempts": attempts
    })