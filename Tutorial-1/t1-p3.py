# Made by Ricky L.

t_clr = input("Colour of traffic light: ").lower()
dist = float(input("Distance to intersection: "))
spd = float(input("Current speed: "))

t = dist/spd

def p(status):
    print(f"\nGo" if status else f"\nStop")


if t_clr == "green":
    p(True)
elif t_clr == "yellow":
    if t<5:
        p(True)
    else:
        p(False)
elif t_clr == "red":
    if t<2:
        p(True)
    else:
        p(False)
else:
    p(False)
