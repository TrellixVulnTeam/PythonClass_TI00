# format() : python3 지원
#            대체될 부분에 {} 표시
print("{} and {}".format("You", "me"))
print("{1} and {0}".format("You", "me"))
print("{1} and {0} and {1}".format("You", "me"))
print("I eat {0} apples".format(3))
print()
print(
    "{var1} and {var2}".format(
        var1="You", var2="me"
    )
)
print(
    "I ate {number} apples. so I was sick for {day} days".format(
        number=10, day=3
    )
)

print(
    "I ate {} apples. so I was sick for {day} days".format(
        10, day=3
    )
)

print(
    "Test1 : {0: 5d}, Price:{1: 4.2f}".format(
        776, 6534.123
    )
)

