import numpy as np
import librosa
import soundfile as sf

# Ses dosyasını yükle
ses_dosyasi, ornek_hizi = librosa.load("ses_dosyasi.wav", sr=None)

# Sesin zaman-frekans temsili
spektrogram = np.abs(librosa.stft(ses_dosyasi))

# Spektrogramdaki gürültüyü azaltmak için bir gürültü eşiği belirleyin
gurultu_esigi = np.median(spektrogram) * 1.5

# Spektrogramda gürültüyü azaltma
temizlenmis_spektrogram = np.where(spektrogram < gurultu_esigi, 0.0, spektrogram)

# Temizlenmiş spektrogramdan sesi yeniden oluşturun
temizlenmis_ses = librosa.istft(temizlenmis_spektrogram)

# Yeni ses dosyasını kaydedin
sf.write("temizlenmis_ses.wav", temizlenmis_ses, ornek_hizi)
