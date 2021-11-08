import requests,logging

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)

username="akun16"
password="Akun16"
email="akun16@akun.com"

r = requests.get('http://127.0.0.1:8000/api/penjual/')
logging.info('test all product')
if r.status_code == 200:
    logging.info('test PASS, can see all product')
else:
    logging.error(r.status_code)

r = requests.post('http://127.0.0.1:8000/api/daftar/account/',data={'username':username,'password':password,'email':email})
if r.status_code == 201:
    logging.info('test PASS, can register account')
else:
    logging.error(r.status_code)
    logging.error(r.text)

r = requests.post('http://127.0.0.1:8000/api/login/',data={'username':username,'password':password})
logging.info('test login')
if r.status_code == 200:
    logging.info('test PASS')
else:
    logging.error(r.status_code)
    logging.error(r.text)
token=(r.json().get('access'))
if token:
    logging.info('Got a token')
else:
    logging.error('cant get a token')
    logging.error(r.text)


r = requests.post('http://127.0.0.1:8000/api/daftar/penjual/',headers={'Authorization':'Bearer '+token})
if r.status_code == 201:
    logging.info('test PASS, membuat akun seller')
else:
    logging.error(r.status_code)
    logging.error(r.text)


r = requests.post('http://127.0.0.1:8000/api/seller/',headers={'Authorization':'Bearer '+token})
if r.status_code == 200:
    logging.info('test PASS, access seller account')
    logging.info(r.text)
else:
    logging.error(r.status_code)
    logging.error(r.text)

files={'image':open('test.jpg','rb')}
r = requests.post('http://127.0.0.1:8000/api/daftar/product/',headers={'Authorization':'Bearer '+token},data={'name':'product2','price':'3000'},files=files)
if r.status_code == 200:
    logging.info('test PASS, Register Product')
    logging.info(r.text)
else:
    logging.error(r.status_code)
    logging.error(r.text)