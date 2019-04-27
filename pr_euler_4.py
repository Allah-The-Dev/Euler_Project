mul_no = set()
for i in range(100,1000):
    for j in  range(i,1000):
        temp = str(i*j)
        if temp == temp[::-1]:
            mul_no.add(int(temp))

list_mul_no = list(mul_no)
list_mul_no.sort()
print(len(list_mul_no))
no_of_input = int(input())
for _ in range(no_of_input):
    input_no = int(input())
    for i in list_mul_no[::-1]:
        if i > input_no:
            continue
        else:
            print(i)
            break
