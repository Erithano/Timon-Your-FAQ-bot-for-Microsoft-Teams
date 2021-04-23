import glob
import re

for filepath in glob.iglob('**/*.json', recursive=True):
    print(filepath)

    reader=open(filepath,   encoding="utf8") 
    triggerlist = open("triggers.txt", "a")
   

    try:
        content  = reader.read()
       
        triggers = re.search("(?<=triggerQueries(?:.):..)[^]]*", content)
        if triggers:
            triggers=triggers.group(0)
        #title = re.search("(?<=displayName.:)*\s*:\s*.*",content)
        title = re.search("displayName.:*\s*:\s*.*",content)

        if title:
            title=title.group(0)

        print(title)
        print(triggers)

        triggerlist.write("\n")
        triggerlist.write(str(title))
        triggerlist.write("\n")
        triggerlist.write(str(triggers))
        triggerlist.write("\n")

    finally:
        reader.close()

triggerlist.close()