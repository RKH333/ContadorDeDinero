# Contador de Dinero de impresiones
# Roberto Chen

def contador():
    archivo = open("Desglose.txt", "w")
    archivo.write("Desglose de Monedas y Billetes\n")
    #Monedas
    print("-----Monedas-----")
    moneda500 = int(input("Monedas de 500: ") or 0)
    moneda100 = int(input("Monedas de 100: ")or 0)
    moneda50 = int(input("Monedas de 50: ") or 0)
    moneda25 = int(input("Monedas de 25: ") or 0)
    moneda10 = int(input("Monedas de 10: ") or 0)
    moneda5 = int(input("Monedas de 5: ") or 0)
    
    #Billetes4
    print("\n-----Billetes-----")
    billete5000 = int(input("Billetes de 5000: ") or 0)
    billete2000 = int(input("Billetes de 2000: ") or 0)
    billete1000 = int(input("Billetes de 1000: ") or 0)

    # Desglose de las monedas
    print("\n-----Desglose de Monedas y Billetes-----\n")
    print(str(moneda500) +  "x500: " + str(moneda500*500))
    print(str(moneda100) +  "x100: " + str(moneda100*100))
    print(str(moneda50) +  "x50: " + str(moneda50*50))
    print(str(moneda25) +  "x25: " + str(moneda25*25))
    print(str(moneda10) +  "x10: " + str(moneda10*10))
    print(str(moneda5) +  "x5: " + str(moneda5*5))
    print("")
    print(str(billete5000) + "x5000: " + str(billete5000*5000))
    print(str(billete2000) + "x2000: " + str(billete2000*2000))
    print(str(billete1000) + "x1000: " + str(billete1000*1000))

    archivo.write("500: " + str(moneda500) + "\n")
    archivo.write("100: " + str(moneda100) + "\n")
    archivo.write("50: "+ str(moneda50) + "\n")
    archivo.write("25: " + str(moneda25) + "\n")
    archivo.write("10: " + str(moneda10) + "\n")
    archivo.write("5: " + str(moneda5) + "\n")
    archivo.write("5000: " + str(billete5000) + "\n")
    archivo.write("2000: " + str(billete2000) + "\n")
    archivo.write("1000: " + str(billete1000) + "\n")
    

    total= moneda500*500+moneda100*100+moneda50*50+moneda25*25+moneda10*10+moneda5*5+billete5000*5000+billete2000*2000+billete1000*1000
    print("--------------------------------")
    print("\nTOTAL: " + str(total))
    archivo.write("TOTAL: " + str(total))
    
    print("\nGracias por usar el sistema contador de monedas")
    archivo.close()

contador()
input("\nPresione cualquier tecla para cerrar el programa...")
