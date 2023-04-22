import os
str1 = 'This is May\'s car!'
print(str1)
 # 如果字串內容有單引號 那就雙引號包起來
str1 = "This is May's car!"
print(str1)
json1 = '{"name":"Ken","age":18 }'
print(json1)

html ='''<!DOCTYPE html>
<html lang="en" >
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>圖片管理系統</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>'''
print(html)

path = "C:\\python\\nscript"
path2 = r"C:\python\nscript"
print(path)
print(path2)
p = os.path.join("C:\\","cpp","DevCppPortable")
print(type(p))
print(p)

