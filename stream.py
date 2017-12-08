import requests
import urllib

import settings


BOTURL = f"https://api.telegram.org/bot{settings.tg_bot_token}"


def get(url):
    return requests.get(url).content.decode('utf8')


def tg_send(text, chat_id=None, markup=None):
    text = f"text={urllib.parse.quote_plus(text)}"
    chat_id = f"&chat_id={chat_id}" if chat_id else ""
    parse_mode = f"&parse_mode=Markdown"
    markup = f"&reply_markup={markup}" if markup else ""
    get(f"{BOTURL}/sendMessage?{text}{chat_id}{parse_mode}{markup}")

mapping = {
    'stdout': print,
    'telegram': tg_send
}
