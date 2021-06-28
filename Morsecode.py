"""This program convert text to morse code/morse code to text and accorindg to user choice it will display converted input."""

def main():
    
    MORSE_CODE_DICT = { ' ':'/','A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
                        'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
                        'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--',
                        'X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-',
                        '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',',':'--..--',
                        '.':'.-.-.-','?':'..--..','/':'-..-.','-':'-....-','(':'-.--.',')':'-.--.-','!':'-.-.--',
                        '"':'.-..-.','&':'.-...',':':'---...',';':'-.-.-.','_':'..--.-','=':'-...-','+':'.-.-.',
                        '$':'...-..-','@':'.--.-.'}

    print('''\n1 - Convert Text to Morse \n2 - Convert Morse to Text\n3 - Quit\n ''')
    selection = int(input('Select Your Choice: '))

    def Txt_to_Morse():
        txt = input('Enter Text to Convert to Morse: ')
        code = [MORSE_CODE_DICT[i.upper()] + ' ' for i in txt if i.upper() in MORSE_CODE_DICT.keys()]
        morse=''.join(code)
        print(morse)
    

    def Morse_to_Txt():
        txt = input('Enter Morse to Convert to Text: ')
        code = [k for i in txt.split() for k,v in MORSE_CODE_DICT.items() if i==v]
        newtxt = ''.join(code)
        print(newtxt)
    
    while selection != 3:
        if selection == 1:
            Txt_to_Morse()
        elif selection == 2:
            Morse_to_Txt()
        else:
            print('Wrong Selection, enter again')

        print('''\n1 - Convert Text to Morse \n2 - Convert Morse to Text\n3 - Quit\n ''')
        selection = int(input('Select Your Choice: '))
    print('Exiting')
    return selection

if __name__ == '__main__':
    main()
