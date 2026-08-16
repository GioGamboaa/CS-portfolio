import sys
zodiacs = [ "Rat (鼠 / Shǔ)","Ox (牛 / Niú)","Tiger (虎 / Hǔ)","Rabbit (兔 / Tù)","Dragon (龙 / Lóng)","Snake (蛇 / Shé)","Horse (马 / Mǎ)","Goat (羊 / Yáng)","Monkey (猴 / Hóu)","Rooster (鸡 / Jī)","Dog (狗 / Gǒu)","Pig (猪 / Zhū)",]

year = int(input(" what is your birthyear? "))

year -= 1900

if year <1:
    print("Invalid year, it should be earlier than 1900")

    sys.exit()

year = year//12


zodiac = zodiacs[year]

print(f" Your Chinese Zodiac sign is :{zodiac}")
