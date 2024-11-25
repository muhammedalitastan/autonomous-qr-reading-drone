class DroneController:
    def __init__(self, map_visualizer, qr_reader, excel_writer):
        self.x = 0  # Mevcut X pozisyonu
        self.y = 0  # Mevcut Y pozisyonu
        self.start_x = 0  # Başlangıç X pozisyonu
        self.start_y = 0  # Başlangıç Y pozisyonu
        self.map_visualizer = map_visualizer
        self.qr_reader = qr_reader
        self.excel_writer = excel_writer

    def reset_position(self):
        """Başlangıç pozisyonuna sıfırla."""
        self.x = 0
        self.y = 0

    def get_position(self):
        """Mevcut drone pozisyonunu döndür."""
        return self.x, self.y

    def return_to_start(self):
        """Drone'u başlangıç noktasına döndür."""
        print(f"Başlangıç noktasına dönülüyor: ({self.start_x}, {self.start_y})")
        self.x = self.start_x
        self.y = self.start_y
        self.map_visualizer.update_drone_position(self.x, self.y)
        print("Başlangıç noktasına dönüldü.")

    def move_with_qr_scan(self, direction, step_size):
        """
        Belirtilen yönde hareket eder ve QR kod tarar.
        :param direction: Hareket yönü ('up', 'down', 'left', 'right')
        :param step_size: Hareket mesafesi (cm)
        """
        if direction == "up":
            self.y += step_size
        elif direction == "down":
            self.y -= step_size
        elif direction == "left":
            self.x -= step_size
        elif direction == "right":
            self.x += step_size

        # Haritayı güncelle
        self.map_visualizer.update_drone_position(self.x, self.y)
        print(f"Drone pozisyonu güncellendi: ({self.x}, {self.y})")

        # QR kod tarama
        self.qr_reader.scan_qr_code(self.map_visualizer, self)
