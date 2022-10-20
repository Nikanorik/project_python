def main():
    amount_main = precipitation()
    precipitation_mid(amount_main)
    precipitation_max_min(amount_main)
def precipitation():
    precip=[]
    for i in range(12):
        amount_precip = float(input(f'Enter amount precipitation from {i+1} month: '))
        precip.append(amount_precip)
    return precip
def precipitation_mid(num):
    sum=0
    for i in num:
        sum+=i
    mid=sum/12
    print(f'Middle amount precipitation = {mid}')
    return mid
def precipitation_max_min(minmax):
    maximum = max(minmax)
    minimum = min(minmax)
    print(f'Amount precipitation maximum= {maximum} and minimum = {minimum}')
if __name__=='__main__':
    main()

