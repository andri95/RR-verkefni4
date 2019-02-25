# Verkefni4 Andri Fannar

#Liður 2
def linear(listi, tala):
    for x in range(len(listi)):
        if listi[x] == tala:
            ny_tala = str(tala)
            index = str(x)
            return "Talan " + ny_tala +  " er í sæti " + index

        elif tala not in listi:
            return -1

#Liður 3
def binary(stak, listi, byrjun = 0, endir = False):
    if endir is False:
        endir = len(listi) - 1

    if byrjun > endir:
        return -1

    mid = (byrjun + endir) // 2
    if stak == listi[mid]:
        return mid

    if stak < listi[mid]:
        return binary(stak, listi, byrjun, mid - 1)

    return binary(stak, listi, mid + 1, endir)

#Liður 5
def setja_inn(listi, tala):
    if tala > len(listi) - 1:
        listi.append(tala)
        return listi
    for x in range (len(listi)):
        if listi[x] > tala:
            break
    nyr_listi = listi[:x] + [tala] + listi[x:]
    return nyr_listi

#Liður 6
class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self, d):
        if self.value == d:
            return False

        elif self.value > d:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True

        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True


class Tree:
    def __index__(self):
        self.root = None

    def insert(self, d):
        if self.root:
            return self.root.insert(d)

        else:
            self.root = Node(d)
            return True



val = ""
while val != "5":
    print("1 - Liður 2")
    print("2 - Liður 3")
    print("3 - Liður 5")
    print("4 - Liður 6")
    print("5 - Hætta")
    val = input("Veldu lið: ")

    if val == "1":

        tala = int(input("Hvaða tölu viltu finna? "))
        listi = [8, 5, 3, 7, 1, 9, 2, 6]
        utkoma = linear(listi, tala)
        if utkoma == -1:
            print("Talan ",tala," er ekki í listanum")
        else:
            print(linear(listi, tala))

    elif val == "2":

        listi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        stak = int(input("Hvaða stak viltu finna? "))

        utkoma = binary(stak, listi)
        if utkoma == -1:
            print("Talan ",stak," er ekki í listanum")
        else:
            print("Talan ",stak," er í sæti ",utkoma)

    elif val == "3":

        listi = [1, 5, 6, 10, 22, 27]
        tala = int(input("Hvaða tölu viltu setja inn? "))

        listi = setja_inn(listi, tala)
        print(listi)

    elif val == "4":

        t = Tree()
        print(t.insert(6))
        print(t.insert(2))
        print(t.insert(3))
        print(t.insert(7))
        print(t.insert(9))

    elif val == "5":
        print("Takk fyrir mig!")

    else:
        print("Rangur innsláttur, reyndu aftur!")