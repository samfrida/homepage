# Apply content to base html
def apply_template (content):
    text_base = open("templates/base.html").read()
    final_html = text_base.replace("{{content}}", content)
    return final_html

# Apply title to text
def apply_title (text, title):
    output = text.replace("{{title}}",title)
    return output


# Main Code
def main ():

    pages = [ {"filename":"content/index.html","output":"docs/index.html","title":"About Me","header":"Sam Frida"}]

    # Loop through pages list
    for page in pages:

        # Read in content html
        text_content = open( page['filename'] ).read()

        # Apply content to template
        text_untitled = apply_template( text_content )

        # Apply title to html
        text_final = apply_title(text_untitled, page['title'] )

        # Write text to html
        output_path = page['output']
        open(output_path,"w+").write(text_final)


if __name__=="__main__":
        main()


