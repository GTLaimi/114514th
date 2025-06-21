def is_prime(num):
    """判断一个数是否为质数"""
    if num < 2 :
        return False
    for i in range(2,int(num**0.5 + 1)) :
        if num % i == 0 :
            return False
    return True

# 获取用户输入并验证
while True :
    try :
        n = int(input("请输入一个正偶数："))
        if n > 0 and n % 2 == 0 :
            break
        else :
            print("ERROR,TRY AGAIN!")
    except ValueError :
        print("ERROR,TRY AGAIN!")
result = []
for i in range(2,n//2+1) :
    if is_prime(i) and is_prime(n-i) :
        result.append((i,n-i))

#输出结果
if not result :
    print("can't help awa~")
else :
    print("The result is :")
    for pair in result :
        print(f"{pair[0]}+{pair[1]}")