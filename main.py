def gridOlustur(dx, lenght=1.0):
    adet = int(round(lenght/dx))
    xList = []
    for i in range(adet + 1):
        xList.append(i * dx)
    return xList

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
        print("x noktaları :", xList)
    else:
        x = float(locInput)
        print("TEK NOKTA")
        print("t :", t, "x :", x)

if __name__ == "__main__":
    main()