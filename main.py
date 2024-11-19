from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup


def get_summary(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    req = Request(url=url, headers=header)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    description = ''
    second_sentence = ''
    add = False
    one_more = False

    for word in text:
        if word == '—':
            add = True
            continue
        if word == '\r\n':
            continue
        if add and word == '.':
            second_sentence += word
        if second_sentence == '..':
            add = False
        if add:
            description += word
    description += '.'

    print(description)
    return description

while __name__ == '__main__':

    file = open('summary-service.txt', mode='r+')
    test_1 = file.read(4)
    if test_1 == 'http':
        summary = get_summary(test_1 + file.read())

        open('summary-service.txt', 'w').close()

        file.write(summary)



