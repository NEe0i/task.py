a = int(input("Введите число: "))
aa = a
ab = a
av = a
ag = a
ad = a
ae = a

aa2 = a * a
aa3 = a * aa2
aa5 = aa2 * aa3
aa10 = aa5 * aa5

print("a)", aa3, aa10)

ab2 = a * a
ab4 = ab2 * ab2
ab5 = ab4 * a
ab10 = ab5 * ab5
ab20 = ab10 * ab10

print("б)", ab4, ab20)

av2 = a * a
av3 = av2 * a
av4 = av2 * av2
av5 = av4 * a
av10 = av5 * av5
av13 = av10 * av3

print("в)", av5, av13)

ag2 = a * a
ag4 = ag2 * ag2
ag5 = ag4 * a
ag9 = ag4 * ag5
ag10 = ag9 * a
ag19 = ag10 * ag9

print("г)", ag5, ag19)
