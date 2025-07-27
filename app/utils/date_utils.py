def zodiac_sign(date):
    day, month = date.day, date.month
    signos = [
        (120, "Capricornio"), (218, "Acuario"), (320, "Piscis"),
        (420, "Aries"), (521, "Tauro"), (621, "Géminis"),
        (722, "Cáncer"), (823, "Leo"), (923, "Virgo"),
        (1023, "Libra"), (1122, "Escorpio"), (1221, "Sagitario"),
        (1231, "Capricornio")
    ]
    value = month * 100 + day
    for cutoff, sign in signos:
        if value <= cutoff:
            return sign
