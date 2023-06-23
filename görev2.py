import re

class Okunus:
    def __init__(self, dosya):
        self.dosya = dosya
        self.okunuslar = {
            'TRT': 'Türkiye Radyo Televizyon',
            'AİHM': 'Avrupa İnsan Hakları Mahkemesi',
            'TBMM': 'Türkiye Büyük Millet Meclisi',
            'AIDS': 'Akut Bağışıklık Yetmezlik Sendromu',
            'Dr.': 'Doktor',
            'Alb.': 'Albay'
        }

    def okunus_eslesme(self, match):
        if match.group().isdigit():
            return self.okunuslar.get(match.group(), match.group())
        else:
            return self.okunuslar.get(match.group().upper(), match.group())

    def texti_okunusları(self):
        with open(self.dosya, 'r', encoding='utf-8') as file:
            text = file.read()

        text_okunusu = re.sub(r'\b(?:\d+(?:\.\d+)*|\w+)\b', self.okunus_eslesme, text)
        return text_okunusu

# Sınıfı kullanarak örnek yapıyoruz
bulucu = Okunus('okunus.txt')

# Metindeki kısaltmaları Türkçe okunuşlarıyla değiştiriyoruz
text_okunusu = bulucu.texti_okunusları()

# Sonucu yazdırıyoruz
print(text_okunusu)
