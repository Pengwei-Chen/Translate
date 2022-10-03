import re
import tqdm
from Translator import pronounce, translate

file = open("Word List.html", "r", encoding = "utf-8")
content = file.readlines()
file.close()

word_list = []
for line in range(len(content)):
    if content[line] == "<tr>\n" and re.match('<td><span style="font-weight: 400">.+?</span></td>', content[line + 1]):
        word_list.append(re.match('<td><span style="font-weight: 400">(.+?)</span></td>', content[line + 1]).group(1))

file = open("Word List.txt", "w", encoding = "utf-8")
# file.write("-" * 40 + "\n")
for word in tqdm.tqdm(word_list):
    file.write(f"{word} {translate(word)} {pronounce(word)}\n")
    # file.write("-" * 40 + "\n")
    file.flush()
file.close()
