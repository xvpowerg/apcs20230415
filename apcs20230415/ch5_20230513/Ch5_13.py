song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
dict = {}                           # 空字典未來儲存單字計數結果
print("原始歌詞")
print(song)

# 將歌曲大寫字母改成小寫
songLower = song.lower()            # 歌曲改為小寫
print("小寫歌詞")
print(songLower)

# 去掉標點符號
for ch in songLower:                
    if ch in ".,?":                 # 將歌曲的標點符號用空字元取代
        songLower = songLower.replace(ch,'')
print("去掉標點符號")    
print(songLower)
