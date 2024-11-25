from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QGridLayout, QListWidget, QLineEdit
from PyQt5.QtCore import Qt


class MainPanel(QMainWindow):
    def __init__(self, drone_controller, map_visualizer, qr_reader, excel_writer):
        super().__init__()
        self.setWindowTitle("Drone Control Panel")
        self.setGeometry(100, 100, 1200, 600)

        self.drone_controller = drone_controller
        self.map_visualizer = map_visualizer
        self.qr_reader = qr_reader
        self.excel_writer = excel_writer

        # Ana widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Sol üst: Harita
        left_layout.addWidget(self.map_visualizer.canvas)

        # Sol alt: Kontroller ve QR kod listesi
        controls_layout = QGridLayout()

        # Manuel kontrol düğmeleri
        self.up_button = QPushButton("Yukarı")
        self.down_button = QPushButton("Aşağı")
        self.left_button = QPushButton("Sola")
        self.right_button = QPushButton("Sağa")
        self.return_to_start_button = QPushButton("Başlangıç Noktasına Dön")  # Yeni buton
        self.save_button = QPushButton("Kaydet")
        self.update_map_button = QPushButton("Haritayı Güncelle")
        self.qr_list = QListWidget()

        controls_layout.addWidget(self.up_button, 0, 1)
        controls_layout.addWidget(self.left_button, 1, 0)
        controls_layout.addWidget(self.right_button, 1, 2)
        controls_layout.addWidget(self.down_button, 2, 1)
        controls_layout.addWidget(self.return_to_start_button, 3, 1)  # Yeni butonun eklenmesi
        controls_layout.addWidget(QLabel("QR Kodlar"), 4, 0, 1, 3, alignment=Qt.AlignCenter)
        controls_layout.addWidget(self.qr_list, 5, 0, 1, 3)
        controls_layout.addWidget(self.save_button, 6, 0, 1, 3)
        controls_layout.addWidget(self.update_map_button, 7, 0, 1, 3)

        # Depo Boyutları ve Hareket Parametreleri
        self.width_input = QLineEdit("Depo Genişliği (cm)")
        self.height_input = QLineEdit("Depo Uzunluğu (cm)")
        self.step_size_input = QLineEdit("Hareket Adımı (cm)")
        self.altitude_input = QLineEdit("Yükseklik Adımı (cm)")
        controls_layout.addWidget(self.width_input, 8, 0, 1, 3)
        controls_layout.addWidget(self.height_input, 9, 0, 1, 3)
        controls_layout.addWidget(self.step_size_input, 10, 0, 1, 3)
        controls_layout.addWidget(self.altitude_input, 11, 0, 1, 3)

        left_layout.addLayout(controls_layout)

        # Sağ: Kamera Görüntüsü
        self.camera_label = QLabel("Kamera Görüntüsü")
        self.camera_label.setFixedSize(640, 480)
        self.camera_label.setStyleSheet("border: 1px solid black;")
        right_layout.addWidget(self.camera_label, alignment=Qt.AlignCenter)

        # Layoutları birleştirme
        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 3)
        self.central_widget.setLayout(main_layout)

        # Olay bağlantıları
        self.up_button.clicked.connect(lambda: self.move_drone("up"))
        self.down_button.clicked.connect(lambda: self.move_drone("down"))
        self.left_button.clicked.connect(lambda: self.move_drone("left"))
        self.right_button.clicked.connect(lambda: self.move_drone("right"))
        self.return_to_start_button.clicked.connect(self.return_to_start)  # Yeni butonun bağlantısı
        self.save_button.clicked.connect(self.save_data)
        self.update_map_button.clicked.connect(self.update_map_dimensions)

    def move_drone(self, direction):
        """Drone'u belirtilen yöne hareket ettir."""
        step_size = int(self.step_size_input.text()) if self.step_size_input.text().isdigit() else 50
        self.drone_controller.move_with_qr_scan(direction, step_size)

    def return_to_start(self):
        """Drone'u başlangıç noktasına döndür."""
        self.drone_controller.return_to_start()
        print("Drone başlangıç noktasına döndü.")

    def save_data(self):
        """QR kodları ve haritayı kaydet."""
        self.excel_writer.save_to_excel()
        self.map_visualizer.save_map()
        print("QR kodlar ve harita kaydedildi.")

    def update_map_dimensions(self):
        """Kullanıcıdan alınan santimetre cinsindeki boyutlarla haritayı güncelle."""
        try:
            width = int(self.width_input.text())  # Santimetre cinsinden genişlik
            height = int(self.height_input.text())  # Santimetre cinsinden uzunluk
            self.map_visualizer.update_dimensions(width, height)
            print(f"Harita boyutları güncellendi: {width}cm x {height}cm")
        except ValueError:
            print("Lütfen geçerli bir genişlik ve uzunluk değeri girin.")
