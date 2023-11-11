ingreso_mensual = 10000
gasto_mensual = 6999

#If anidados y elif

if ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual >3000:
        print("Estas bien")
    else:
        print('Tus gastos son muy elevados')

elif ingreso_mensual > 10000:
    print("Estas bien en cualquier parte del mundo")

else:
    print("Sos pobre")