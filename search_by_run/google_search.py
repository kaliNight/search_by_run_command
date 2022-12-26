import webbrowser
import sys
sys.argv
if len(sys.argv)>1:
    search="+".join(sys.argv[1:])
    webbrowser.open(f"https://www.google.com/search?q={search}")