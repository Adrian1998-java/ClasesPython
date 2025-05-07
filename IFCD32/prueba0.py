monto_bruto = 200
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes

print( "El monto bruto es de", monto_bruto )
print( "El monto neto es de", monto_neto )