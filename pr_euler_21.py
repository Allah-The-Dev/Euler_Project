for _ in range(int(input())):
    num = int(input())
    temp1,temp2,sum = 0,2,0
    while temp2 <= num:
        temp3 = temp1 #assigning temp1 value to temp1
        temp1 = temp2
        temp2 = temp2 * 4 + temp3
        sum += temp1
    print(sum)
