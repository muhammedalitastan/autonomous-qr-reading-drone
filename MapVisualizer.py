from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MapVisualizer:
    def __init__(self):
        self.canvas = FigureCanvas(Figure(figsize=(5, 10)))
        self.ax = self.canvas.figure.add_subplot(111)
        self.width = 100  # Varsayılan genişlik (cm)
        self.height = 1000  # Varsayılan uzunluk (cm)
        self.drone_position = None  # Drone'un son pozisyonu
        self.qr_positions = []  # QR kodlarının pozisyonlarını sakla
        self.reset_map()

    def reset_map(self):
        """Haritayı sıfırla ve mevcut genişlik ve yüksekliğe göre ayarla."""
        self.ax.clear()
        self.ax.set_xlim(-self.width // 2, self.width // 2)  # Genişlik
        self.ax.set_ylim(0, self.height)  # Uzunluk
        self.ax.set_title("Drone Haritası")

        # QR kodlarını sembollerle tekrar çizin
        for (x, y, label) in self.qr_positions:
            self.ax.scatter(x, y, color="red", marker="x", label=f"QR: {label}")

        # Drone'un pozisyonunu tekrar çizin
        if self.drone_position:
            self.ax.scatter(
                self.drone_position[0],
                self.drone_position[1],
                color="blue",
                marker="o",
                label="Drone",
            )

        self.canvas.draw()

    def update_dimensions(self, width, height):
        """Depo genişliği ve uzunluğu için yeni harita sınırlarını ayarla."""
        self.width = width  # Santimetre cinsinden alınır
        self.height = height  # Santimetre cinsinden alınır
        print(f"Harita Güncelleniyor: Genişlik={self.width}cm, Uzunluk={self.height}cm")
        self.reset_map()

    def update_drone_position(self, x, y):
        """Drone'un pozisyonunu güncelle."""
        self.drone_position = (x, y)  # Drone'un son pozisyonunu sakla
        self.reset_map()  # Haritayı yenile

    def mark_qr_code(self, x, y, label):
        """QR kod algılandığında işaretle."""
        self.qr_positions.append((x, y, label))  # QR kod pozisyonu ve etiketi sakla
        self.reset_map()  # Haritayı yenile

    def save_map(self):
        """Haritayı dosyaya kaydet."""
        self.canvas.figure.savefig("map_output.png")
        print("Harita kaydedildi.")
