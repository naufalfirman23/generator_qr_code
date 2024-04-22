import cv2
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)

print("\nPress Button Q For Quit Apps!")
while True:
    _, frame = cap.read()
    # Mencari kode QR pada gambar
    barcodes = pyzbar.decode(frame)
    # Meloopi setiap kode QR pada gambar
    for barcode in barcodes:
        # Mencetak data dari kode QR
        print(barcode.data.decode('utf-8'))
    cv2.imshow('Barcode Scanner', frame)
    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
