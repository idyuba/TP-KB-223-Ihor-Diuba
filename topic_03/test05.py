while True:
    cnt = int(input("What's cnt? : "))
    if cnt <= 0:
        continue
    else:
        break

print("Cnt = ", cnt)

for _ in range(cnt):
    print("bark")