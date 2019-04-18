def fib_num(max = 4 * 10 ** 16):
    a,b = 0,1
    while a <= max:
        yield a
        a,b = b,a+b

even_fib_num=[]
for num in fib_num():
    if num%2 == 0:
        even_fib_num.append(num)

print(even_fib_num)

for _ in range(int(input())):
    num = int(input())
    filtered_nums = filter(lambda x:x <= num, even_fib_num)
    print(sum(filtered_nums))
