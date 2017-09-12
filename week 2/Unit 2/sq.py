x = int(input("Enter an integer: "))
ans = 0
while ans ** 2 <= x:
    if ans **2 != x:
        print(ans, "is not the square root of" ,x)
        ans = ans + 1
    else:
        print("the square root is ", ans)
        break
if ans **2 == x:
    print("we found the answer")
else:
    print("no answer discovered")
