class Memur:
    def __init__(self, Ad, Soyad, Maas):
        self.Ad = Ad
        self.Soyad = Soyad
        self.__Maas = Maas
        self.__Zam = 0.2

    def zamOranı(self):
        self.__Maas = self.__Maas + self.__Maas * self.__Zam

    def getMaas(self):
        return self.__Maas

    def getZam(self):
        return self.__Zam

    def setZam(self, yeniOran):
        self.__Zam = yeniOran


memur1 = Memur("Fati", "Yıldırım", 30000)

memur1.setZam(0.17)
memur1.zamOranı()
print(memur1.getMaas())
