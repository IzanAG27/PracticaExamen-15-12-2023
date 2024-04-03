def segons_a_hms(segons):
    hores = segons // 3600
    segons %= 3600
    minuts = segons // 60
    segons %= 60
    return hores, minuts, segons

def hms_a_segons(hores, minuts, segons):
    return hores * 3600 + minuts * 60 + segons