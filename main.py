import re
import time
##### we dont handel hours

path = input(".ass file path example (c:subtitle.ass) :")
file_text=""
with open(path, "r",encoding="UTF-8") as f:
    file_text = f.read()
shift = int(input("time shift in seconds (examples : +1 ,-2 ,+7 ,...) :"))
res = re.findall(r'Dialogue: (\d+),0:(\d{2}):(\d{2}).(\d{2}),0:(\d{2}):(\d{2}).(\d{2})', file_text)


for ___,m1, sp11, _, m2, sp12, __ in res:
    sp11 = int(sp11)
    m1 = int(m1)
    sp11+=shift
    if sp11 >= 60:
        m1+=sp11//60
        sp11-=60
    elif sp11 < 0:
        m1-=1
        sp11=60+sp11

    sp12 = int(sp12)
    m2 = int(m2)
    sp12+=shift
    if sp12 >= 60:
        m2+=sp12//60
        sp12-=60
    elif sp12<0:
        m2-=1
        sp12 += 60
    file_text = re.subn(r'Dialogue: (\d+),0:(\d{2}):(\d{2}).(\d{2}),0:(\d{2}):(\d{2}).(\d{2})', f"Dialogue:  {___},0:{m1}:{sp11}.{_},0:{m2}:{sp12}.{__}", file_text, count=1)[0]
    print(file_text)
with open(path, "w" ,encoding="UTF-8") as f:
    f.write(file_text)
print("done!!")