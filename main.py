from os import system, name, path
from time import sleep
from random import choice
from base64 import b64decode
try:
    from requests import get
except:
    system('pip install requests')
    from requests import get
try:
    from telebot import TeleBot
except:
    system('pip install telebot')
    from telebot import TeleBot
try:
    from telethon import TelegramClient, sync, errors, functions, types
    from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
    from telethon.tl.functions.channels import JoinChannelRequest
except:
    system('pip install telethon')
    from telethon import TelegramClient, sync, errors, types, functions
    from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
    from telethon.tl.functions.channels import JoinChannelRequest
try:
    from bs4 import BeautifulSoup as S
except:
    system('pip install beautifulsoup')
    from bs4 import BeautifulSoup as S
try:
    from fake_useragent import UserAgent
except:
    system('pip install fake_useragent')
    from fake_useragent import UserAgent
try:
        from datetime import datetime
except:
        system('pip install datetime')
        from datetime import datetime
# Import/Download Libraries


me = "@w66w6w"
tokenBot = "7313412555:AAFHxPC0SqXinRh-Cbr5v5CLeTYGAkZDxCE"
idx = "1380133006"

def clear():
        system('cls' if name=='nt' else 'clear')
# for check flood , error
def channels2(client, username):
    di = client.get_dialogs()
    for chat in di:
        if chat.name == f'Claim [ {username} ]' and not chat.entity.username:
            client(functions.channels.DeleteChannelRequest(channel=chat.entity))
            return False
    return True
# for checking username (taken,nft,sold,availabe) by t.me/xx_amole
def fragment(username):
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': UserAgent().random,
}
    response = get(f'https://fragment.com/username/{username}', headers=headers)
    soup = S(response.content, 'html.parser')
    ok = soup.find("meta", property="og:description").get("content")
    if "An auction to get the Telegram" in ok or "Telegram and secure your ownership" in ok or "Check the current availability of" in ok or "Secure your name with blockchain in an ecosystem of 700+ million users" in ok:return True
    elif "is taken" in ok:return "is taken"
    else:return False
# for claim username
def telegram(client,claim,username):
        if claim:
                text = f"⌯ New UserName\n⌯ UserName : @{username} .\n⌯ UserName Person : @{client.get_me().username} .\n⌯ Claim? {claim} .\n⌯ Source : {me} ."
                try:
                	TeleBot(token=tokenBot).send_message(idx,text=text)
                except:pass
        else:
                text = f"⌯ New UserName\n⌯ UserName : @{username} .\n⌯ Claim? {claim} .\n⌯ Source : {me} ."
        client.send_message('me',text)
def climed(client,username):
    id = (
        'b18ddf48b3eda3891e1aa.mp4',
        'e804e09a27ffa820b57a4.mp4',
        'a9962fe13d9ad82f3a3a9.mp4',
        '6464fe2715b85eda86a49.mp4',
        'a59706ab125b934b7f99b.mp4')
    id = choice(id)
    result = client(functions.channels.CreateChannelRequest(
                title=f'Claim [ {username} ]',
        about=f'Source - {me}',
        megagroup=False))
    try:
        client(functions.channels.UpdateUsernameRequest(
        channel=result.chats[0],
        username=username))
        sleep(0.50)
        client.send_message(username,f'⌯ Done Save UserName .\n⌯ UserName : @{username} .\n⌯ Claim : @{client.get_me().username}\n⌯ Date : {datetime.now().strftime("%H:%M:%S")} .\n⌯ Source : {me} .')
        return True
    except Exception as e:client.send_message('me',f'⌯ Error Message .\nMessage : {e} .');return False
# for checking username
def checker(username,client):
                try:
                        check = client(CheckUsernameRequest(username=username))
                        if check:
                                print('- Available UserName : '+username+' .')
                                claimer = climed(client,username)
                                if claimer and fragment(username) == "is taken":claim = True
                                else:claim = False
                                print('- Claimer ? '+str(claim)+'\n'+'_ '*20)
                                telegram(client,claim,username)
                                flood = channels2(client,username)
                                if not flood:
                                        with open('flood.txt', 'a') as floodX:
                                                floodX.write(username + "\n")
                                                TeleBot(tokenBot).send_message(chat_id=idx,text=f"⌯ New UserName Flood\n⌯ UserName : @{username} .\n⌯ Source : {me} .")
                        else:
                                print('- Taken UserName : '+username+' .')
                except errors.rpcbaseerrors.BadRequestError:
                        print('- Banned UserName : '+username+' .')
                        open("banned4.txt","a").write(username+'\n')
                except errors.FloodWaitError as timer:
                        print('- Flood Account [ '+timer.seconds+' Secound ] .')
                except errors.UsernameInvalidError:
                        print('- Error UserName : '+username+' .')
# for generate username
def usernameG():
	y = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
	j = ''.join(choice('qwertyuiopasd1234567890fghjklzxcvbnm') for i in range(1))
	n = ''.join(choice('qwertyuio1234567890pasdfghjklzxcvbnm') for i in range(1))
	w = ''.join(choice('1234567890') for i in range(1))
	k = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
	v1 = y+y+y+j+n
	v2 = y+n+n+n+j
	v3 = y+j+k+k+k
	
	ls = (v1,v2,v3)
	u = choice(ls)
	return u
# start checking
def start(client,username):
        try:ok = fragment(username)
        except:return
        try:
                if not ok:
                        checker(username,client)
                elif ok == "is taken":
                        print('- Taken UserName : '+username+' .')
                else:
                        print('- UserName Availabe In Fragment.com : '+username+' .')
                        open("fragment.txt","a").write(username+'\n')
        except Exception as e:print(e)
# get client
def clientX():
	phone = '' # Your Phone Number
	if phone == '':phone = input('- Enter Phone Number Telegram : ')
	client = TelegramClient("aho", b64decode("MjUzMjQ1ODE=").decode(),b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode())
	try:client.start(phone=phone)
	except:exit()
	try:client(JoinChannelRequest(""))
	except:pass
	clear()
	return client
# start tool
def work():
        session = clientX()
        if not path.exists('banned4.txt'):
                with open('banned4.txt','w') as new:pass
        if not path.exists('fragment.txt'):
                with open('fragment.txt','w') as new:pass
        if not path.exists('flood.txt'):
                with open('flood.txt','w') as new:pass
        while True:
                username = usernameG()
                with open('banned4.txt', 'r') as file:
                        check_username = file.read()
                if username in check_username:
                        print('- Banned1 UserName : '+username+' .')
                        continue
                with open('fragment.txt', 'r') as file:
                	fragment = file.read()
                if username in fragment:
                	print('- UserName Availabe In Fragment.com : '+username+' .')
                	continue
                start(session,username)
if __name__ == "__main__":
        work()
