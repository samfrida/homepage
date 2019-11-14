




def main ():

    pages = [ {"filename":"content/index.html","output":"docs/index.html","title":"About Me"},
              {"filename":"content/index.html","output":"docs/blah_blah.html","title":"About Me"} ]

    for page in pages:

        text_top = open("templates/top.html").read()
        text_bottom=open("templates/bottom.html").read()

        text_content=open( page['filename'] ).read()

        text_final = text_top + text_content + text_bottom

        output_path  = page['output']

        open(output_path,"w+").write(text_final)


if __name__=="__main__":
        main()


