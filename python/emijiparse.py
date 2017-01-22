from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("http://www.unicode.org/emoji/charts/full-emoji-list.html")
soup = BeautifulSoup(html, "lxml")
towrite = ""
towrite+="[ \n"
print ("Start")
c = 0
path = "png64/"
readtr=soup.find_all("tr")
for trs in readtr:
    num=trs.find("td", "rchars")
    if (num!=None):
        #code
        #<td class="code"><a href="#1f600" name="1f600">U+1F600</a></td>
        num = num.string
        names = trs.find_all("td", "name")
        name = names[0].string
        code = trs.find("td", "code").string
        code = code.replace(" ", "_")
        echar = trs.find("td", "chars").string
        img = path + code.replace("_", "-") + "png"
        towrite= towrite + "{\n\"num\":" + num + ",\n\"name\":\"" + name + "\",\n\"code\":\"" + code + "\",\n\"echar\":\"" + echar + "\",\n\"img\":\"" + img + "\",\n\"keywords\":[\n"
        keywords = names[1].find_all("a")
        if (len(keywords) != 1):
            for i in range(len(keywords) - 2):
             keyword = keywords[i].string
             towrite= towrite + "\"" + keyword + "\",\n"
        towrite= towrite + "\"" + keywords[len(keywords)-1].string + "\"\n]\n}"
        if(c != len(readtr)-1):
            towrite +=",\n"
    c+=1
towrite += "]"
f=open("new.txt","wt", encoding="utf-16")
f.write(towrite)
f.close()
#no
#<td class="rchars">1</td>
#emoji
#<td class="chars">emoji</td>
#name
#<td class="name">grinning face</td>
#keywords
#<td class="name"><a href="emoji-annotations.html#face" target="annotate">face</a>
               #| <a href="emoji-annotations.html#grin" target="annotate">grin</a></td>
#num, name, ucode, tex, img, keywords
