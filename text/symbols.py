'''
Defines the set of symbols used in text input to the model.
'''

text_cleaners = 'zh_ja_mixture_cleaners'


if text_cleaners == 'sora_cleaners':
    text_cleaners = 'zh_ja_mixture_cleaners'

# japanese_cleaners
if text_cleaners == "japanese_cleaners":
    _pad        = '_'
    _punctuation = ',.!?-'
    _letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧ↓↑ '


# japanese_cleaners2
elif text_cleaners == "japanese_cleaners2":
    _pad        = '_'
    _punctuation = ',.!?-~…'
    _letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧʦ↓↑ '


# korean_cleaners
elif text_cleaners == "korean_cleaners":
    _pad        = '_'
    _punctuation = ',.!?…~'
    _letters = 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅓㅗㅜㅡㅣㅐㅔ '


# chinese_cleaners
elif text_cleaners == "chinese_cleaners":
    _pad        = '_'
    _punctuation = '，。！？—…'
    _letters = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩˉˊˇˋ˙ '


# zh_ja_mixture_cleaners
elif text_cleaners == "zh_ja_mixture_cleaners":
    _pad        = '_'
    _punctuation = ',.!?-~…'
    _letters = 'AEINOQUabdefghijklmnoprstuvwyzʃʧʦɯɹəɥ⁼ʰ`→↓↑ '


# sanskrit_cleaners
elif text_cleaners == "sanskrit_cleaners":
    _pad        = '_'
    _punctuation = '।'
    _letters = 'ँंःअआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहऽािीुूृॄेैोौ्ॠॢ '


# cjks_cleaners
elif text_cleaners == "cjks_cleaners":
    _pad        = '_'
    _punctuation = ',.!?-~…'
    _letters = 'NQabdefghijklmnopstuvwxyzʃʧʥʦɯɹəɥçɸɾβŋɦː⁼ʰ`^#*=→↓↑ '


# thai_cleaners
elif text_cleaners == "thai_cleaners":
    _pad        = '_'
    _punctuation = '.!? '
    _letters = 'กขฃคฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลวศษสหฬอฮฯะัาำิีึืุูเแโใไๅๆ็่้๊๋์'


# cjke_cleaners2
elif text_cleaners == "cjke_cleaners2":
    _pad        = '_'
    _punctuation = ',.!?-~…'
    _letters = 'NQabdefghijklmnopstuvwxyzɑæʃʑçɯɪɔɛɹðəɫɥɸʊɾʒθβŋɦ⁼ʰ`^#*=ˈˌ→↓↑ '


# shanghainese_cleaners
elif text_cleaners == "cjke_cleaners2":
    _pad        = '_'
    _punctuation = ',.!?…'
    _letters = 'abdfghiklmnopstuvyzøŋȵɑɔɕəɤɦɪɿʑʔʰ̩̃ᴀᴇ15678 '


# chinese_dialect_cleaners
elif text_cleaners == "cjke_cleaners2":
    _pad        = '_'
    _punctuation = ',.!?~…─'
    _letters = '#Nabdefghijklmnoprstuvwxyzæçøŋœȵɐɑɒɓɔɕɗɘəɚɛɜɣɤɦɪɭɯɵɷɸɻɾɿʂʅʊʋʌʏʑʔʦʮʰʷˀː˥˦˧˨˩̥̩̃̚ᴀᴇ↑↓∅ⱼ '


else:
    raise TypeError("The cleaners in config is wrong!")

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters)

# Special symbol ids
SPACE_ID = symbols.index(" ")
