
text_top = open("/Users/samanthafrida/Desktop/Kickstart Coding/Homework 2/homepage/templates/top.html").read()
text_bottom=open("/Users/samanthafrida/Desktop/Kickstart Coding/Homework 2/homepage/templates/bottom.html").read()
text_index=open("/Users/samanthafrida/Desktop/Kickstart Coding/Homework 2/homepage/content/index.html").read()

text_final = text_top + text_bottom + text_index

path  = "/Users/samanthafrida/Desktop/Kickstart Coding/Homework 2/homepage/docs/index.html"

open(path,"w+").write(text_final)

#"docs/index.html"