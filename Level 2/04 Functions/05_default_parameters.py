############################################################
#
#    default parameters
#
############################################################


def Display(a, b=10, c=100):
    print(f"a = {a:6.2f}, b = {b:6.2f}, c = {c:6.2f}")


Display(a=19, b=-6.2, c=4.8)
Display(b=-6.2, c=4.8, a=19)
Display(17)
Display(17, 21)
Display(17, c=0)
