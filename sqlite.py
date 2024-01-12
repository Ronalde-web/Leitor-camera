import cv2
from pyzbar.pyzbar import decode
import sqlite3

# Função para criar a tabela no banco de dados
def create_table():
    conn = sqlite3.connect('barcode_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS barcodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir um código de barras no banco de dados
def insert_barcode(data):
    conn = sqlite3.connect('barcode_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO barcodes (data) VALUES (?)', (data,))
    conn.commit()
    conn.close()

def main():
    # Inicialize a câmera
    cap = cv2.VideoCapture(0)

    # Crie a tabela no banco de dados
    create_table()
    barcode_data = None
    app = True

    while True:
        # Capture um quadro da câmera
        ret, frame = cap.read()

        # Decodifique os códigos de barras no quadro
        decoded_objects = decode(frame)

        # Exiba os resultados
        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            print(f'Código de barras detectado: {barcode_data}')

            # Insira o código de barras no banco de dados
            insert_barcode(barcode_data)

            if barcode_data != None:
                app = False

          
        # Exiba o quadro
        cv2.imshow('Barcode Scanner', frame)

        # Verifique se a tecla 'q' foi pressionada para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libere os recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
