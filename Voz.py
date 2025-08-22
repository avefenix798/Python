import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = '''San Miguel Arcángel,

defiéndenos en la batalla.

Sé nuestro amparo

contra las perversidad y asechanzas

del demonio.

Reprímale Dios, pedimos suplicantes,

y tu príncipe de la milicia celestial

arroja al infierno con el divino poder

a Satanás y a los otros espíritus malignos

que andan dispersos por el mundo

para la perdición de las almas.

Amén.'''
speak.Speak(text)


