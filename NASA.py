volumen_reservorio = 4.445e8
lluvia = 5e6
print(f"El volumen inicial es {volumen_reservorio}m3")
volumen_reservorio = volumen_reservorio - (10*volumen_reservorio/100)
print(f"El volumen del reservorio sin el 10% es {volumen_reservorio}m3")
volumen_reservorio = volumen_reservorio + lluvia
print(f"Si se le agrega la lluvia seria {volumen_reservorio}m3")
volumen_reservorio = volumen_reservorio + (5*volumen_reservorio/100)
print(f"El volumen del reservorio con las aguas pluviales es {volumen_reservorio}m3")
volumen_reservorio = volumen_reservorio - (2*volumen_reservorio/100)
print(f"El volumen del reservorio descontando la evaporacion {volumen_reservorio}m3")
volumen_reservorio = volumen_reservorio - 2.5e5
print(f"El volumen del reservorio descontando el agua en regiones áridas {volumen_reservorio}m3")
print(f"El volumen del reservorio es {volumen_reservorio}m3, en notación cietífica {volumen_reservorio:.1E}")