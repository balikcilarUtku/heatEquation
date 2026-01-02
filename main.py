import math
import numpy as np



#gridOlustur fonksiyonu ile x listemizi oluşturuyoruz. Uzaklık 0.1 olacak.
def gridOlustur(dx, length=1.0):
    adet = int(round(length/dx))
    xList = []
    for i in range(adet + 1):
        xList.append(i * dx)
    return xList
#icNokta fonksiyonu sayesinde ilk ve son noktaları çıkarıyoruz.
def icNokta(xList):
    return xList[1:-1]
#baslangicVektoru ile x noktalarının t = 0 anındaki sıcaklıklarını buluyoruz.
def baslangicVektoru(xInner):
    u0 = []
    for x in xInner:
        u0.append(math.sin(math.pi * x))
    return u0
#Alpha*dt/alpha*dx^2 = r formülünü kullanarak r yi hesapladık
def rHesapla(alpha, dt, dx):
    return alpha * dt / (dx * dx)

# a matrisini oluşturduk
def aMatrisiOlustur(n,r):
    A = np.zeros((n,n),dtype = float)
    for i in range(n):
        A[i,i] = 1 + 2 * r
        if i - 1 >= 0:
            A[i,i-1] = -r
        if i + 1 < n:
            A[i,i+1] = -r
    return A

def implicit(A, uOnceki):
    uOncekiVec = np.array(uOnceki, dtype = float)
    uYeni = np.linalg.solve(A, uOncekiVec)
    return uYeni

def zamanaIlerle(A, u0, dt, t):
    adimSayisi = int(round(t/dt))
    u = np.array(u0, dtype = float)

    for _ in range(adimSayisi):
        u = implicit(A, u)
    return u

#Ana fonksiyonumuz
def main():
    dx = 0.1
    timeInput = input("Zaman değerini giriniz* : ").strip()
    if timeInput == "":
        print("Zaman değeri boş olamaz.")
        return
    t = float(timeInput)

    locInput = input("Konum değerini giriniz : ").strip()

    if locInput == "":
        print("TABLO")
        print("t :", t)
        xList = gridOlustur(dx, 1.0)
        xInner = icNokta(xList)
        u0 = baslangicVektoru(xInner)
        alpha = 1.0
        dt = 0.01
        r = rHesapla(alpha, dt, dx)
        a = aMatrisiOlustur(len(xInner),r)
        u1 = implicit(a, u0)
        print("u1 =",u1.tolist())
        print("x'in tüm noktaları :", xList)
        print("x'in iç noktaları :", xInner)
        print("u0 =", u0)
        print("r =", r)
        print("A Boyutu :", a.shape)
        print("A ilk satır :",a[0])
    else:
        x = float(locInput)
        print("TEK NOKTA")
        print("t :", t, "x :", x)

if __name__ == "__main__":
    main()