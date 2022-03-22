def fibonacci_sequence(nPOS):
    first_Num = 0
    second_Num = 1
    seqList = [first_Num,second_Num]

    if nPOS-1 in seqList:
        return nPOS -1
    else:
        for i in range(nPOS - 2):
            seqList.append(seqList[i]+seqList[i+1])
        return seqList[-1]
def main():
    nPOS = input("Enter a valid n position")
    while(nPOS.lower() not in ['quit','exit','break']):
        try:
            print(fibonacci_sequence(int(nPOS)))
        except Exception:
            print("Something went wrong...")
        nPOS = input("Enter a valid n position")

if __name__ == '__main__':
    main()