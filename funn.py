import gtts, os
from gtts import gTTS
print('........................................................................')
lund_size = int(input('Apke lund ka size kitna hai (in inches) = '))
loura_w = int(input('Apka auzar kitna mota hai (in inches) = '))
lond_c = input('Apke loure ka colour kya hai = ')
dick_mut = int(input('App ke lourry ko jagne me kitna time lagta hai (in minutes) = '))
if lund_size >= 5 and loura_w >= 3 and dick_mut <= 10:
    print('    ')
    print('---------------------------------------------------------------------')
    print('  ')
    print('Tohar auzaar ba dharedhaar   ;) ')
    print('App chodne ke liye ready ho 8====> .... ')
    print('jo apse chudwaye , pani bhi na maang paye  : () ')
    tts = gTTS("Tohar auzaar ba dharedhaar, App sex ke liye ready ho, jo apse thukway , pani bhi na maangg paye, ", lang='en', slow=False)
    tts.save('hello.mp3')
    os.system('hello.mp3')
else:
    print('**********************************************************************')
    print('  ')
    print('Auzaar na layak khodne ko , miya chale chodne ko')
    print('chhoriyo ki jawani ki tu nahi bujha payega pyass , Bada kar loure ko pike endura mass')

    tts = gTTS("Auzaar na layak khodne ko , miya chale chodne ko,chhoriyo ki jawani ki tu nahi bujha payega pyass , Bada kar loure ko pike endura mass  ",lang='en', slow=False)
    tts.save('hella.mp3')
