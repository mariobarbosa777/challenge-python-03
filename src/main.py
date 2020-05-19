import re 


def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        codified_Message=f.read()
        Chars=(re.findall("[a-z]+", codified_Message))
        Message=''.join(Chars)
        
    print(Message)  
    # code


if __name__ == '__main__':
    run()
