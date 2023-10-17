a='ksfgiewlivj gkiwlv ewkqh vK, EEKHVIWYH K HN\VJWGQKI JNAMV EK,DIJN,  MNBZSJDHFMS FCNNFCBNVKNHFKTFH'
from collections import Counter
def top3(a):
    counter_top3 = Counter(a.replace(' ', '')).most_common(3)
    print(counter_top3)
top3(a)
    