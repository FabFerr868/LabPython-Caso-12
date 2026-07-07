with open("CajaSuper/lista_productos.txt", "w") as archivo:
    archivo.write("1001;Leche Entera 1L;2500;10\n")
    archivo.write("1002;Pan Lactal;3200;5\n")
    archivo.write("1003;Arroz 1Kg;1800;0\n")
    archivo.write("1004;Azúcar 1Kg;1700;15\n")
    archivo.write("1005;Aceite Girasol 900ml;4200;20\n")
    archivo.write("1006;Fideos Tallarín;1500;10\n")
    archivo.write("1007;Gaseosa Cola 2.25L;3800;25\n")

with open("CajaSuper/lista_descuentos.txt", "w") as archivo:
    archivo.write("0;Sin descuento\n")
    archivo.write("5;Promoción semanal\n")
    archivo.write("40;Black Friday\n")
    archivo.write("50;2x1\n")

