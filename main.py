import requests, json, time, os
import webbrowser, getpass
#import modules.getnicknames as getnicks
os.system("title VimeTop AutoLiker by g7tufix")
token = 'YourApiDev'#/api dev
usernick = 'g7tufix'
userhash = 'userhashVT'
class getnicknames(): 
    def main(): 
        print('Парсинг начал работать... \n\nЭто займет некоторое время')
        b = 1
        global nicknames
        nicknames = []
        while b < 100:
            matches = json.loads(requests.get('http://api.vimeworld.ru/match/latest?count=100' + token).text)
            actualmatch = json.loads(requests.get('https://api.vimeworld.ru/match/' + matches[b]["id"] + '?token='+ token).text)
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
                nicknameDATA = {"page": nicknames[d], "action": "like"}
                headers = {"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7","content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-requested-with": "XMLHttpRequest","cookie": "nickname=" + usernick + "; auth_hash=" + userhash}
                requests.post('https://vimetop.ru/ajax/player/likeProfile.php', headers=headers, data=nicknameDATA)
                print(f'Использованно: {d}/99 [Лайкнул {nicknames[d]}]')
                d+=1
    def hello(): 
        print("""
 __      _________                 _        _      _ _             
 \ \    / |__   __|     /\        | |      | |    (_| |            
  \ \  / /   | |       /  \  _   _| |_ ___ | |     _| | _____ _ __ 
   \ \/ /    | |      / /\ \| | | | __/ _ \| |    | | |/ / _ | '__|
    \  /     | |     / ____ | |_| | || (_) | |____| |   |  __| |   
     \/      |_|    /_/    \_\__,_|\__\___/|______|_|_|\_\___|_|   
                                [by g7tufix]
""")#;webbrowser.open('https://vimetop.ru/player/g7tufix')
        program.start()
if __name__ == '__main__': 
    try: 
        program.hello()
    except KeyboardInterrupt:
        print('Stopped') 
        os.system("pause");quit()
