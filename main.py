S = "123456"
c = 0
p = S.find("12")

while p >= 0:
    c += 1
    p = S.find("12", p + 1)

print("S =", S)
print("Natija:", c, "ta '12' qatori mavjud.")
