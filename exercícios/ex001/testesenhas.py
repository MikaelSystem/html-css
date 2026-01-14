import random
import string

geradorsenhas = string.ascii_letters + string.punctuation + string.digits

tamanhodeclarado = int(input("Qual é o tamanho da senha que você" \
"deseja?:  "))

for _ in range(tamanhodeclarado):
    
    random.choice(geradorsenhas)

senha = "".join([])