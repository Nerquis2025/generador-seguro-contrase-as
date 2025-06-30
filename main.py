caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
clave = ""
i = 0
while i < 12:
    clave = clave + __builtins__.__import__("random").choice(caracteres)
    i = i + 1
print(clave)