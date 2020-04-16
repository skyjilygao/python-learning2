
def fs(n):
    if n==1 or n == 2:
        return 1
    return fs(n-1) + fs(n-2)

if __name__ == '__main__':
    num = 10
    # for i in range(1,num):
    #     print(fs(i),'', end='')
    preNum, sum=1,1
    print(preNum, '', end='')
    print(sum, '', end='')
    for i in range(1,num - 1):
        preNum,sum=sum,preNum+sum
        print(sum,'',end='')

    # print(preNum)
    print()
    print(sum)
    # 280571172992510140037611932413038677189525

    # print(fs(10))