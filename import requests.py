import requests

username = 'elifakyuz'  # Kendi kullanıcı adınızı girin
token = '0e64c8ac0ab97248c9660a49c63b33ad937c14b0'  # Kendi API tokenınızı girin

response = requests.get(
    f'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/',
    headers={'Authorization': f'Token {token}'}
)

if response.status_code == 200:
    print('API Token geçerli!')
    print('Yanıt:', response.json())  # Yanıtı JSON olarak yazdırabilirsiniz
else:
    print(f'Hata: API token geçersiz veya başka bir problem var. Durum kodu: {response.status_code}')
