from utils import *
import sys

if __name__=="__main__":
        print("This is argv:", sys.argv)
        if len(sys.argv) > 1:
                command = sys.argv[1]
                if command == "build":
                        print("Build was specified")
                        main()
                elif command == "new":
                        print("New page was specified")
                        new_content()
        else:
                print("Usage:")
                print("     Please specify ’build’ or ’new’")
                print("     Rebuild site:    python manage.py build")
                print("     Create new page: python manage.py new")



         
         
