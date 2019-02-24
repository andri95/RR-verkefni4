# RR-verkefni4 Andri Fannar  
**Keyranlegur kóði fylgir hér að ofan**  

**1. Skoðaðu myndina vel og svaraðu spurningum:**  
**a) Hvað gerir forritið hér fyrir neðan?**  
Það skilar listanum L í stærðarröð, lægsta tala fyrst.  
**b) Hvað er reikniritið kallað?**  
Counting sort  
**c) Hvert er flækjustig reikniritsins?**  
O(n + k)  

**2.**  
```python
def linear(listi, tala):
    for x in range(len(listi)):
        if listi[x] == tala:
            ny_tala = str(tala)
            index = str(x)
            return "Talan " + ny_tala +  " er í sæti " + index

        elif tala not in listi:
            return -1

tala = int(input("Hvaða tölu viltu finna? "))
listi = [8, 5, 3, 7, 1, 9, 2, 6]
utkoma = linear(listi, tala)
if utkoma == -1:
    print("Talan ",tala," er ekki í listanum")
else:
    print(linear(listi, tala))
```  
**3.**  
```python
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


listi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
stak = int(input("Hvaða stak viltu finna? "))

utkoma = binary(stak, listi)
if utkoma == -1:
    print("Talan ",stak," er ekki í listanum")
else:
    print("Talan ",stak," er í sæti ",utkoma)
```  
**4. Flækjustig:**  
**a) Hvert er flækjustig forritsins í lið 2?**  
O(n) held ég þar sem flækjustigið er bara ein for lykkja.  
**b) Hvert er flækjustig forritsins í lið 3?**  
O(log(n)) er almennt flækjustigið fyrir binary leit.  
**5.**  
```python
def setja_inn(listi, tala):
    if tala > len(listi) - 1:
        listi.append(tala)
        return listi
    for x in range (len(listi)):
        if listi[x] > tala:
            break
    nyr_listi = listi[:x] + [tala] + listi[x:]
    return nyr_listi


listi = [1, 5, 6, 10, 22, 27]
tala = int(input("Hvaða tölu viltu setja inn? "))

listi = setja_inn(listi, tala)
print(listi)
```  
**6.**  
Ég klóraði mér mikið í hausnum yfir þessu, er búinn að vera veikur alla vikuna og var erlendis í síðustu viku þannig ég missti alveg af yfirferðinni í tíma fyrir þetta verkefni. Ég skil þetta ekki alveg nógu vel, fékk upp eh errora þegar ég skrifaði Node og Tree clasana inn í pycharm..

