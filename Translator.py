import requests
import re
import googletrans

def pronounce(word : str) -> str:
    return re.findall('''<span class="phonetic" data-.+?>(.+?)</span>''', requests.get("https://youdao.com/result?word=" + word + "&lang=en").text)[0]

def translate(word : str) -> str:
    return googletrans.Translator().translate(word, dest = "zh-cn").text