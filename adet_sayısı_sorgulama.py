class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi, satici_calistigi_sehir,adet):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satici_calistigi_sehir = satici_calistigi_sehir
        self.__adet=adet

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

    def get_satici_calistigi_sehir(self):
        return self.__satici_calistigi_sehir

    def set_satici_calistigi_sehir(self, satici_calistigi_sehir):
        self.__satici_calistigi_sehir = satici_calistigi_sehir

    def get_adet(self):
        return self.__adet

    def set_adet(self,adet):
        self.__adet = adet

def main():
    magazalar_dict = {}
    while True:
        magaza_adi = input("Mağazanın adını girin: ")
        if not magaza_adi:
            break

        satici_adi = input("Satıcının adını girin: ")
        if not satici_adi:
            break

        satici_cinsi = input("Satış cinsi girin: ")
        if not satici_cinsi:
            break

        tutar = int(input("Satış tutarını girin: "))
        if not tutar:
            break

        satici_calistigi_sehir = input("Satıcının çalıştığı şehri girin: ")
        if not satici_calistigi_sehir:
            break
        adet = int(input("kaç adet aldığınızı girin: "))
        if not adet:
            break
        magaza_instance = Magaza(magaza_adi, satici_adi, satici_cinsi,satici_calistigi_sehir,adet)
        magazalar_dict[magaza_instance] = tutar

        def magaza_satis_tutar(magazalar_dict, magaza_adi):
            toplam_tutar = 0
            for magaza_instance, tutar in magazalar_dict.items():
                if magaza_instance.get_magaza_adi() == magaza_adi:
                    toplam_tutar +=adet* tutar
            return toplam_tutar

        for magaza_instance in magazalar_dict.keys():
            toplam_tutar = magaza_satis_tutar(magazalar_dict, magaza_instance.get_magaza_adi())
            print(
                f"{magaza_instance.get_satici_calistigi_sehir()} şehrinde ,{magaza_instance.get_magaza_adi()} mağazasında {magaza_instance.get_satici_adi()} adlı satıcıdan {toplam_tutar} TL değerinde ürün satıldı.")
main()
