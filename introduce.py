import os



def banner():
    banner = """
    ================================================
        DE TAI NGHIEN CUU KHOA HOC - TOP 5 OWASP
        
        TOMATO TEAM
            LE VAN CHON
            VO XUAN KHANG
            LY THAI QUYNH
        
        2017
    ================================================
    """
    print banner

def init():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
