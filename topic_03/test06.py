
def getCnt():
    while True:
        cnt = int(input("What's cnt? : "))
        if cnt <= 0:
            print("ERROR: Cnt mast be grater then 0")
            continue
        else:
            break
    return cnt

def dogSay(n):
    for _ in range(n):
        print("bark")

def main():
    cnt = getCnt()
    dogSay(cnt)


main()