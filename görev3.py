class TextiDuzenleyici:
    def __init__(self, text):
        self.metin = text

    def duzenle(self):
        text = self.metin.strip()
        text = text.replace("Afyonkarahisarda", "Afyonkarahisar'da")
        text = text.replace("biz dur dedik", "biz dur dedik.")
        text = text.replace("5 ten", "5'ten")
        text = text.replace("itiraz ettik dedi", "itiraz ettik,")

        cumleler = text.split("\n")
        cumleler = [cumle.strip() for cumle in cumleler if cumle.strip()]

        duzenlenmis_texti = ". ".join(cumleler)
        return duzenlenmis_texti


text = """Cumhurbaşkanı Recep Tayyip Erdoğan Afyonkarahisarda düzenlenen mitingde açıklamalarda bulundu 
Cumhurbaşkanı Erdoğan Tüm mazlum ve mağdurların elinden tutarak emperyalist sömürge düzenine biz dur dedik 
Birleşmiş Milletler kürsüsünden bu kardeşiniz dünya 5 ten büyüktür diye haykırarak emperyalistlerin kurduğu 
küresel sisteme biz itiraz ettik dedi Erdoğan TCG Anadolu İstanbul Sirkeci de halkın ziyaretine açıldı 
Ama bu CHP lobisi masanın etrafındaki 7 liler TCG Anadolu yu gördükçe kuduruyorlar 
Biz yaptık Çünkü onlar yapamazdı İHA mız SİHA mız Kızılelma mız var 
Hepsi de şu anda TCG Anadolu nun güvertesinde  Biz yaparız Yaparsa Cumhur İttifakı yapar ifadelerini kullandı"""

duzenleyici = TextiDuzenleyici(text)
duzenlenmis_texti = duzenleyici.duzenle()
print(duzenlenmis_texti)
