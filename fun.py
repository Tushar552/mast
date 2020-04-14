import gtts, os
from gtts import gTTS

print('8===> 8:>')
name = input('What is your name? = ')
print(' ')
tts = gTTS(f'welcome {name} to Thukkai chamta jacch kenddra', lang = 'en', slow = False)
tts.save('hell.mp3')
print('welcome', name, '!', 'Thukai chhamta janch kenddra me apka swagat hai')
print(' ')
print('........................................................................')
