months_dict = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"June",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}

def mesDoAno(dia):
    return months_dict.get(dia)

print(mesDoAno(5))