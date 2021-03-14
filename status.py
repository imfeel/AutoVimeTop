import requests, json, time, os
import webbrowser, getpass
os.system("title VimeTop AutoStatus by Yumix_")
token = 'YourApiDev'#/api dev
usernick = 'Yumix_'
statusword = 'Феноменально. @' 
statusstopped = 'Феноменально. '
userhash = 'userhashVT'
headers = {"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7","content-type": "application/x-www-form-urlencoded; charset=UTF-8", "x-requested-with": "XMLHttpRequest","cookie": "nickname=" + str(usernick) + "; auth_hash=" + str(userhash)}
class getnicknames(): 
    def main(): 
        print('Парсинг начал работать... \n\nЭто займет некоторое время')
        b = 1
        global nicknames
        nicknames = []
        while b < 100:
            matches = json.loads(requests.get('http://api.vimeworld.ru/match/latest?count=100&token=' + token).text)
            actualmatch = json.loads(requests.get('https://api.vimeworld.ru/match/' + matches[b]["id"] + '?token=' + token).text)
            try: 
                usernick = json.loads(requests.get('https://api.vimeworld.ru/user/' + str(actualmatch["players"][1]["id"]) + '?token=' + token).text)[0]["username"]
                nicknames.append(usernick)
                print(f'Парсинг: {b}/99 [Ник: {usernick}]')
                b+=1
            except KeyError: 
                print('Ошибка! Информация: ' + str(actualmatch) )
                b+=1
                break
class program(): 
    def start(): 
        getnicknames.main()
        d = 0
        while True: 
            while True: 
                if d == 98: 
                    print('Новый парсинг... \n Это займет какое-то время')
                    d = 0
                    getnicknames.main()
                #nicknameDATA = {"page": nicknames[d], "action": "like"}
                #headers = {"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7","content-type": "application/x-www-form-urlencoded; charset=UTF-8", "x-requested-with": "XMLHttpRequest","cookie": "nickname=" + str(usernick) + "; auth_hash=" + str(userhash)}
                try: 
                    data = {'text': str(statusword) + str(nicknames[d])}
                    requests.post('https://vimetop.ru/ajax/player/statusChange.php', headers=headers, data=data)
                    print(f'Статус: {str(statusword) + str(nicknames[d]) }')
                    d+=1
                except Exception as e: 
                    d+=1
                    print(f'Ошибка. Код: {e}')
    def hello(): 
        print("""
 __      _________                 _        _____ _        _             
 \ \    / |__   __|     /\        | |      / ____| |      | |            
  \ \  / /   | |       /  \  _   _| |_ ___| (___ | |_ __ _| |_ _   _ ___ 
   \ \/ /    | |      / /\ \| | | | __/ _ \\___ \| __/ _` | __| | | / __|
    \  /     | |     / ____ | |_| | || (_) ____) | || (_| | |_| |_| \__ \ 
     \/      |_|    /_/    \_\__,_|\__\___|_____/ \__\__,_|\__|\__,_|___/
                                [by Yumix_]
""");webbrowser.open('https://vimetop.ru/player/Yumix_')
        program.start()
if __name__ == '__main__': 
    try: 
        program.hello()
    except KeyboardInterrupt:
        print('Stopped') 
        data = {'text': str(statusstopped)}
        requests.post('https://vimetop.ru/ajax/player/statusChange.php', headers=headers, data=data)
        print(f'Статус: {str(statusstopped)}')
        os.system("pause");quit()
    except Exception as e: 
        if e == IndexError: 
            pass
        else: 
            print(f'Ошибка! Код ошибки: {e}') 
            data = {'text': str(statusstopped)}
            requests.post('https://vimetop.ru/ajax/player/statusChange.php', headers=headers, data=data)
            print(f'Статус: {str(statusstopped)}')
            os.system("pause");quit()