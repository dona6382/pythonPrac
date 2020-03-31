#Lotto.py
import random
numberArr = list(range(1, 46))
i = input("게임 수 : ")

for j in range(0, int(i)):
    lottoArr = []
    while len(lottoArr) < 6:
        num = random.choice(numberArr)
        if not num in lottoArr:
            lottoArr.append(num)
    lottoArr.sort()
    
    #lottoArr.sort(reverse=True) 내림차순 정렬
    print(lottoArr) 
