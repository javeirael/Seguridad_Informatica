def obtener_signo_zodiacal(dia_nacimiento, mes_nacimiento, año_nacimiento):
    signos_zodiacales_occidentales = {
        (3, 21): "Aries",
        (4, 20): "Tauro",
        (5, 21): "Géminis",
        (6, 21): "Cáncer",
        (7, 23): "Leo",
        (8, 23): "Virgo",
        (9, 23): "Libra",
        (10, 23): "Escorpio",
        (11, 22): "Sagitario",
        (12, 22): "Capricornio",
        (1, 20): "Acuario",
        (2, 19): "Piscis",
    }
    
    signos_zodiacales_chinos = {
        0: "Mono",
        1: "Gallo",
        2: "Perro",
        3: "Cerdo",
        4: "Rata",
        5: "Buey",
        6: "Tigre",
        7: "Conejo",
        8: "Dragón",
        9: "Serpiente",
        10: "Caballo",
        11: "Cabra",
    }
    
    mes_nacimiento = mes_nacimiento.lower()
    
    for (dia_inicio, mes), signo in signos_zodiacales_occidentales.items():
        if (mes_nacimiento == mes and dia_nacimiento >= dia_inicio) or (mes_nacimiento == mes + 1 and dia_nacimiento < dia_inicio):
            signo_occidental = signo
            break
    else:
        signo_occidental = "Mes no válido."
    
    año_nacimiento = int(año_nacimiento)
    signo_chino = signos_zodiacales_chinos[(año_nacimiento - 1924) % 12]
    
    return signo_occidental, signo_chino
