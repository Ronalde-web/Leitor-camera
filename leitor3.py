import keyboard
import time

def main():
    # Simula a leitura de código de barras a laser
    simulated_barcodes = ["123456789", "987654321", "555555555"]

    # Crie a tabela no banco de dados
    create_table()

    for barcode_data in simulated_barcodes:
        print(f'Código de barras detectado: {barcode_data}')

        # Insira o código de barras no banco de dados
        insert_barcode(barcode_data)

        # Espere por um curto período para simular o intervalo entre leituras
        time.sleep(1)

if __name__ == "__main__":
    main()
