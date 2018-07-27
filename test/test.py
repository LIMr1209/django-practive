import requests
from random import randint
def main():
    html = requests.get('http://127.0.0.1:8000').text
    print(html)

def get_random_code(code_length=8):
    code_sources = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        code += code_sources[randint(0,len(code_sources)-1)]
    return code
if __name__ == '__main__':
    # main()
    a=get_random_code(50)
    print(a)
