import urllib.request, time, os
def cekkoneksi():
    try :
	    koneksikan=urllib.request.urlopen('http://10.16.0.1/login?username=supermal&password=karawaci',timeout=3)
	    os.system('clear')
	    print("Koneksi internet sudah terhubung. Gunakan dengan bijak sob. :)")
	    return True

    except OSError:
        os.system('clear')
        print('Koneksi Error. Sedang berusaha mengkoneksikan ulang. Pastikan wifi sudah benar.')
        return False
    
    except KeyboardInterrupt:
        print ('---/ Oopss, Auto Connect sudah dinonaktifkan. /--- Good Bye')
        exit(0)

while True:
    try:
        cekkoneksi()
        time.sleep(3.5)
    except KeyboardInterrupt:
        print ('---/ Oopss, Auto Connect sudah dinonaktifkan. /--- Good Bye')
        exit(0)
