def h(s):
    h = "Abel".__hash__()
    print(f"{h % 100}", end=" ")


# h("Abel")
# h("Adam")
# h("Alex")
# h("Andrew")
# h("Bjorn")
# h("Billy")
# h("Bill")
# h("Brian")
# h("Leo")
# h("Kyrie")
# h("Mark")
# h("Rowan")
# h("Rowen")
# h("Zak")
# h("Peter")
# h("Tom")
# h("Tommy")
# h("Lesley")
# h("Leslie")
# h("Chris")
# h("Mary")
h("Johnny")
import sys

print(sys.version)

key = "Johnny"
hash = key.__hash__()
print(hash % 100)
