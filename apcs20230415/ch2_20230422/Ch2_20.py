places = {'A':'臺北市', 'B':'臺中市', 'C':'基隆市', 'D':'臺南市', 'E':'高雄市', 'F':'新北市',
          'G':'宜蘭縣', 'H':'桃園市', 'I':'嘉義市', 'J':'新竹縣', 'K':'苗栗縣',
          'M':'南投縣', 'N':'彰化縣', 'O':'新竹市', 'P':'雲林縣', 'Q':'嘉義縣', 'T':'屏東縣',
          'U':'花蓮縣', 'V':'臺東縣', 'W':'金門縣', 'X':'澎湖縣', 'Z':'連江縣',
          'L':'臺中縣', 'R':'臺南縣', 'S':'高雄縣', 'Y':'陽明山'}
pid = input("請輸入身分證")
birth = pid[0]
print("出生地:",places[birth])
