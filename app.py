#import gradio as gr
from telethon.sync import TelegramClient, events
import datetime
import socks
import time
import os
import requests
import asyncio

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)





proxy_server = '142.93.68.63'
proxy_port = 2434
proxy_secret = 'ee32b920dffb51643028e2f6b878d4eac1666172616b61762e636f6d'
proxy_dc_id = 2  # This is usually 2 for MTProto proxies

proxy = (
    socks.SOCKS5,
    proxy_server,
    proxy_port,
    True,
    'vpn',
    'unlimited'
)

api_id=os.environ['apiID']
api_hash=os.environ['apiHash']
phone=os.environ['phone']
username=os.environ['username']

serssionFile=os.environ['sessionUrlFile']

download_file(serssionFile, 'anon.session')



# Dictionary to track the times when senders were last replied to
reply_times = {}

async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        @client.on(events.NewMessage())
        async def my_event_handler(event):
            sender = await event.get_sender()
            sender_id = sender.id
            sender_name = sender.first_name
            chat = await event.get_chat()
            chat_id = chat.id
            text = event.raw_text

            # Personal message
            if chat_id == sender_id and not sender.bot:
                # Check the last reply to this sender
                last_reply_time = reply_times.get(str(sender_id), None)
                if last_reply_time is None or time.time() - last_reply_time > 60*60*6:  # reply only if not replied in the last minute
                    response = f'Hello <a href="tg://user?id={sender_id}">{sender_name}</a>,\n I received your message and will reply as soon as possible. Thank you for your understanding.'
                    await client.send_message(chat_id, response, parse_mode='HTML')
                    reply_times[str(sender_id)] = time.time()  # update the last reply time

            # Group message
            elif username in text:
                last_reply_time = reply_times.get(str(str(chat_id)+str(sender_id)), None)
                if last_reply_time is None or time.time() - last_reply_time > 60*5:
                    response = f'Hello <a href="tg://user?id={sender_id}">{sender_name}</a> @ <a href="https://t.me/c/{chat_id}">{chat.title}</a>,\n I received your message and will reply as soon as possible. Thank you for your understanding.'
                    await client.send_message(chat_id, response, parse_mode='HTML')
                    reply_times[str(str(chat_id)+str(sender_id))] = time.time()

   
        await client.run_until_disconnected()


# Gradio Inteface
#inputs = []
#output = "text"
#gr.Interface(fn=main, inputs=inputs, outputs=output).launch()

    #    client.loop.run_until_complete(main())

if __name__ == '__main__':
    asyncio.run(main())