#作者：qjm
#鸣谢：Kevil
import getopt
from string import ascii_lowercase as lowercase
import sys
import pyfiglet

def En(p, key):
    p = get_trim_text(p)
    ptLen = len(p)
    keyLen = len(key)

    quotient = ptLen // keyLen  # 商
    remainder = ptLen % keyLen  # 余

    out = ""
    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(p[i * keyLen + j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
            # global output
            out += chr(c)

    for i in range(0, remainder):
        c = int((ord(p[quotient * keyLen + i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
        # global output
        out += chr(c)

    return out

def De(output, key):
    ptLen = len(output)
    keyLen = len(key)

    quotient = ptLen // keyLen
    remainder = ptLen % keyLen

    inp = ""

    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(output[i * keyLen + j]) - ord('a') - (ord(key[j]) - ord('a'))) % 26 + ord('a'))
            # global input
            inp += chr(c)

    for i in range(0, remainder):
        c = int((ord(output[quotient * keyLen + i]) - ord('a') - (ord(key[i]) - ord('a'))) % 26 + ord('a'))
        # global input
        inp += chr(c)
        return inp
def helpyou ():
    print ("欢迎来到维吉尼亚\n-h --help 显示帮助\n-k --key 必要参数，秘钥\n-e --jiami输入加密信息\n-d --jiemi 输入要解密信息")

def get_trim_text(text):
    text = text.lower()
    trim_text = ''
    for l in text:
        if lowercase.find(l) >= 0:
            trim_text += l
    return trim_text 

if __name__ == '__main__':
    
    
    a = pyfiglet.Figlet (font='slant')
    print (a.renderText ('virginia'))
    print ("-h 显示帮助")
    try:

        longargs = ['help=','jiami=','jiemi=','key=']
        opts,args= getopt.getopt( sys.argv[1:], 'he:d:k:', longargs)

            
        for o, a in opts:
            if o in ("--key","-k"):
                ke = a
                
            if o in ("--help" ,"-h"):
                helpyou()
                sys.exit()
            if o in ("--jiami" ,"-e"):
                jiami = a
                print (En (jiami,ke))
            if o in ("--jiemi" ,"-d"):
                jiemi = a
                print (De (jiemi,ke))
        
            
    except getopt.GetoptError:
        helpyou()
