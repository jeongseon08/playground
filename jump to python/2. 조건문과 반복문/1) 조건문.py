money = 3000
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

b = "걸어가라" if money<2000 else "택시를 타고가라"
print(b)