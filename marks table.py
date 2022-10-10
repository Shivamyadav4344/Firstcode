Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
P=input("Enter the marks:-")
Enter the marks:-43
C=input("Enter the marks:-")
Enter the marks:-22
M=input("Enter the marks:-")
Enter the marks:-92
agg= int(P) + int(C) + int(M)
print("Aggerate=",agg)
Aggerate= 157
per=(agg *100)/300
if per>=81:
    print("1")
elif per>=61:
    print("2")
elif per>=41:
    print("3")
else:
    print("FAIL")

    
3
