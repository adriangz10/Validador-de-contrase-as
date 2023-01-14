import re

def is_valid_password(password):
    pattern = re.compile(r'''
        ^                 # Inicio de la línea
        (?=.*[A-Z])        # Al menos dos mayúsculas
        (?=.*[0-9])        # Al menos un número
        (?=.*[$&+,:;=?@#|<>.^*()%!-]) # Al menos un carácter especial
        (?!.*\s)           # Sin espacios
        [A-Za-z0-9$&+,:;=?@#|<>.^*()%!-]{6,20} # Longitud entre 6 y 20 caracteres
        $                 # Fin de la línea
    ''', re.VERBOSE)
    return pattern.match(password) is not None

password = input("Introduzca una contraseña que cumpla las siguientes condiciones:\n- Longitud entre 6 y 20 caracteres\n- Al menos un numero\n- Al menos dos letras mayúsculas\n- Al menos un caracter especial\n- No spacios\n")

if is_valid_password(password):
    print("True")
else:
    print("Contraseña invalida")
