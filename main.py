from pyrogram import Client

from time import sleep

from config import LIMIT, CHANELS, WORLDS_DATA, admin, API_ID, API_HASH


chanels = CHANELS.replace("https://t.me/", "@").replace("t.me/", "@").strip().split(" ")
worlds_data = [i.strip() for i in WORLDS_DATA.strip().split(";")]
ADMIN = admin.replace("https://t.me/", "@").replace("t.me/", "@")
print(f"[INFO] Входные данные (КАНАЛЫ): {chanels}")
print(f"[INFO] Входные данные (СЛОВА/ПРЕДЛОЖЕНИЯ/СЛОВОСОЧЕТАНИЯ): {worlds_data}")
print(f"[INFO] Админ: {ADMIN}")

#---------------------------------------------

api_id = API_ID

api_hash = API_HASH
app = Client("my_account", API_ID, API_HASH)

app.on_message()

def scan_text(worlds, text):
    for w1 in worlds:
        if w1 in text:
            
            return True 
        else: False



async def main():
    try:
        async with app:
            for chanel in chanels: 
                chat = await app.get_chat(chanel)
                chat_id = chat.id
                await app.join_chat(chat_id)

                async for message in app.get_chat_history(chat_id, limit=LIMIT):
                    sleep(0.5)
                    if message.caption != None:
                        if scan_text(worlds_data, message.caption):
                            await app.forward_messages(ADMIN, chat_id, message_ids=message.id)
                    elif message.text != None:
                        if scan_text(worlds_data, message.text):
                            await app.forward_messages(ADMIN, chat_id, message_ids=message.id)
            await app.send_message(ADMIN, )
    except Exception as er:
        print(er)
app.run(main())


