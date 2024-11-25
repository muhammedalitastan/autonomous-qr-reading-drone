from MainPanel import MainPanel
from MapVisualizer import MapVisualizer
from QRReader import QRReader
from ExcelWriter import ExcelWriter
from DroneController import DroneController
import sys
from PyQt5.QtWidgets import QApplication
import threading


def main():
    app = QApplication(sys.argv)

    # Sınıfları oluştur
    map_visualizer = MapVisualizer()
    qr_reader = QRReader()  # DJI Tello ile QR Reader başlatıldı
    excel_writer = ExcelWriter()
    drone_controller = DroneController(map_visualizer, qr_reader, excel_writer)

    # Ana paneli başlat
    panel = MainPanel(drone_controller, map_visualizer, qr_reader, excel_writer)

    # QR kod tarama işlemi
    def start_qr_scan():
        while True:
            qr_reader.scan_qr_code(map_visualizer, drone_controller)

    # QR tarama için iş parçacığı oluştur
    qr_scan_thread = threading.Thread(target=start_qr_scan)
    qr_scan_thread.daemon = True
    qr_scan_thread.start()

    # Paneli göster
    panel.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
