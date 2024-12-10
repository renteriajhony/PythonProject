# a = True
# b = True
#
# print(a and b)
# print(not (a and b))

# Desceunto VIP

# print('*** Descuento VIP ***')
#
# NO_PRODUCT_DES = 10
# DES_VALUE = 10
# productsNumber: int = int(input('Cuantos productos compraste hoy: '))
# clientVIP = input('Eres cliente VIP (SI/NO): ').lower().strip()
# purchaseValue: float = float(input('Ingresa el valor de la compra: '))
# isVIP = (True if clientVIP == 'si' else False)
#
# isApplyDesc = (productsNumber >= NO_PRODUCT_DES) and isVIP
# purchaseValueDesc =(purchaseValue-((purchaseValue * DES_VALUE)/100) if isApplyDesc == True else purchaseValue)
#
# print(f'''\n Resltado de venta
# \t Numero de productos: {productsNumber}
# \t Valor de la compra: {purchaseValue}
# \t CLiente VIP: {clientVIP.upper()}
# \t Valor de la compra Con descuento : {purchaseValueDesc}
# ''')

precio_leche = float(input('Ingrese precio de leche: '))
precio_pan = float(input('Ingrese precio de pan: '))
precio_lechuga = float(input('Ingrese precio de lechuga: '))
precio_platanos = float(input('Ingrese precio de platanos: '))
porcentaje_desc= float(input('Ingrese descuento (%): '))

subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos
descuento = subtotal * (porcentaje_desc/100)
subtotal_con_desc = subtotal -descuento
# Calculo de impuesto 16%
impuesto = subtotal_con_desc * 0.16
total = subtotal_con_desc + impuesto

print(f'''\n*** Tickect de venta ***\n
$Subtotal: {subtotal:.2f}
$Descuento: {descuento:.2f} ({porcentaje_desc}%)
$Subtotal con descuento: {subtotal_con_desc:.2f}
$Impuesto (16%): {impuesto:.2f}
$Total: {total:.2f}
''')