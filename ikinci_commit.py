class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi,tutar):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__tutar=tutar

    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    def get_tutar(self):
        return self.__tutar

    def set_tutar(self,tutar):
        self.__tutar


def main():
        magazalar_dict = {}
        while True:
            magaza_adi = input("Maðazanýn adýný girin: ")
            if not magaza_adi:
                break

            satici_adi = input("Satýcýnýn adýný girin: ")
            if not satici_adi:
                break

            satici_cinsi = input("Satýþ cinsi girin: ")
            if not satici_cinsi:
                break

            tutar = int(input("Satýþ tutarýný girin: "))
            if not tutar:
                break

            magaza_instance = Magaza(magaza_adi, satici_adi, satici_cinsi,tutar)
            magazalar_dict[magaza_instance] = tutar

            def magaza_satis_tutar(magazalar_dict, magaza_adi):
                toplam_tutar = 0
                for magaza_instance, tutar in magazalar_dict.items():
                    if magaza_instance.get_magaza_adi() == magaza_adi:
                        toplam_tutar += tutar
                return toplam_tutar

            for magaza_instance in magazalar_dict.keys():
                toplam_tutar = magaza_satis_tutar(magazalar_dict, magaza_instance.get_magaza_adi())
                print(f"{magaza_instance.get_magaza_adi()} maðazasýnda {magaza_instance.get_satici_adi()} adlý satýcýdan {toplam_tutar} TL deðerinde ürün satýldý.")

if __name__ == "__main__":
    main()

