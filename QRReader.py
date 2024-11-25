from pyzbar.pyzbar import decode
import cv2
from djitellopy import Tello


class QRReader:
    def __init__(self):
        self.qr_data = []
        self.tello = Tello()  # Tello drone nesnesi
        self.tello.connect()
        print(f"Tello Drone Bağlandı: Pil Seviyesi % {self.tello.get_battery()}")
        self.tello.streamon()  # Drone kamerasını aç

    def scan_qr_code(self, map_visualizer, drone_controller):
        """Drone kamerasından QR kodları algılar ve haritaya işaretler."""
        try:
            frame_read = self.tello.get_frame_read()
            frame = frame_read.frame
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            decoded_qrs = decode(gray_frame)

            for qr in decoded_qrs:
                qr_content = qr.data.decode('utf-8')  # QR kod içeriği
                if qr_content not in self.qr_data:
                    self.qr_data.append(qr_content)
                    x, y = drone_controller.get_position()
                    map_visualizer.mark_qr_code(x, y, qr_content)
                    print(f"QR Kod Algılandı: {qr_content} | Konum: ({x}, {y})")

            # Kamerayı görüntüleme (isteğe bağlı)
            cv2.imshow("Drone Kamerası", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' ile çıkış
                self.tello.streamoff()
                cv2.destroyAllWindows()
        except Exception as e:
            print(f"Kamera işleme hatası: {e}")
