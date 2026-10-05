from hashlib import sha256

senha = 'minha_senha'
cod = senha.encode('utf-8')

hash = sha256(cod).hexdigest()
print(hash)