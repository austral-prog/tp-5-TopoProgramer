# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    mes = int(month)

    if month == 1:
        mes = "enero"
    elif month == 2:
        mes = "febrero"
    elif month == 3:
        mes = "marzo"
    elif month == 4:
        mes = "abril"
    elif month == 5:
        mes = "mayo"
    elif month == 6:
        mes = "junio"
    elif month == 7:
        mes = "julio"
    elif month == 8:
        mes = "agosto"
    elif month == 9:
        mes = "septiembre"
    elif month == 10:
        mes = "octubre"
    elif month == 11:
        mes = "noviembre"
    elif month == 12:
        mes = "diciembre"
    else:
        mes = "error"
    return mes  # Remove this line and implement

number_to_month(1) # Retorna: "enero"
number_to_month(2) # Retorna: "diciembre"
number_to_month(99) # Retorna: "error"
