# Made by Ricky L.

g1 = float(input("Enter the first midterm grade: "))
g2 = float(input("Enter the second midterm grade: "))
g3 = float(input("Enter the third midterm grade: "))
g4 = float(input("Enter the final exam mark: "))


g1w,g2w,g3w,g4w = 0.2,0.2,0.2,0.4


if g4 > g1:
    g1w -= 0.1
    g4w += 0.1

if g4 > g2:
    g2w -= 0.1
    g4w += 0.1

if g4 > g3:
    g3w -= 0.1
    g4w += 0.1

res = (g1 * g1w) + (g2 * g2w) + (g3 * g3w) + (g4 * g4w)

print(f"\n{res}")
