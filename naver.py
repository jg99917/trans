import urllib.request
import json
import pytesseract as pyte

pyte.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

a = pyte.image_to_string('3.PNG', lang='jpn_vert', config='--psm 5 --oem 1')


client_id = "0xdYrf7TC9vSl235FR88" # 개발자센터에서 발급받은 Client ID 값
client_secret = "Vu083a8VAh" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote(a)
data = "source=ja&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read().decode('utf-8')
    result = json.loads(response_body)['message']['result']
    print(result['translatedText'])
else:
    print("Error Code:" + rescode)