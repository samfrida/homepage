import glob
import os
from jinja2 import Template

# Takes a list of files and returns pages list of dictionaryes 
def create_pages (list_of_files):
    pages = []
    for content_html_file in all_content_html_files:
        file_name = os.path.basename (content_html_file)
        name_only, extension = os.path.splitext (file_name)
        if name_only == "index": # Change index.html title to About
            name_only = "about"
        pages.append({
            "filename": content_html_file,
            "title": name_only.capitalize(),
            "output": "docs/" + file_name,
            "output_filename": file_name,
        })
    return pages

def apply_template(base, content, page, pages):
        # Create a Jinja Template out of the base
        template = Template(base)
        
        # Render template
        output = template.render(
            title = page["title"],
            content = content,
            pages = pages
        )
        return output



# Main Code
def main ():

    # Create pages list of dictionaries
    all_content_html_files = glob.glob("content/*.html")
    pages = create_pages( all_content_html_files )

    # Read in template html
    base_html = open("templates/base.html").read()

    # Loop through pages list
    for page in pages:

        # Read in content html
        content_html = open( page['filename'] ).read()

        # Create template and apply
        text_final = apply_template(base_html,content_html, page, pages)

        # Write text to html
        output_path = page['output']
        open(output_path,"w+").write(text_final)


if __name__=="__main__":
        main()


