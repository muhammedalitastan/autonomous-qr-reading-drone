import pandas as pd
from datetime import datetime
import os


class ExcelWriter:
    def __init__(self):
        self.data = []

    def add_data(self, qr_code, x, y):
        """QR kodunu, konum bilgilerini ve zaman bilgisini sakla."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data.append({"QR Code": qr_code, "X": x, "Y": y, "Timestamp": timestamp})

    def save_to_excel(self):
        """QR kodlarını bir Excel dosyasına kaydet."""
        if not self.data:
            print("Kaydedilecek veri yok.")
            return

        # Verileri bir DataFrame'e çevir ve Excel'e kaydet
        df = pd.DataFrame(self.data)

        # Belirtilen dizin ve dosya adı
        save_directory = r"C:\Users\monster\Desktop\Code\python\save"
        os.makedirs(save_directory, exist_ok=True)  # Dizin yoksa oluştur
        file_name = os.path.join(save_directory, f"qr_codes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")

        df.to_excel(file_name, index=False)
        print(f"QR kodlar Excel dosyasına kaydedildi: {file_name}")
