import glob
import re

for filepath in glob.iglob('**/*.json', recursive=True):
    print(filepath)

    reader=open(filepath,   encoding="utf8") 
    triggerlist = open("content.txt", "a", encoding="utf8")
   

    try:
        content  = reader.read()
       
        triggers = re.match("content.:*\s*:\s*.*", content)
        #if triggers:
            #triggers=triggers.group(0)
        #title = re.search("(?<=displayName.:)*\s*:\s*.*",content)
        title = re.search("displayName.:*\s*:\s*.*",content)

        if title:
            title=title.group(0)

        #print(title)
        #print(triggers)

        triggerlist.write("\n")
        triggerlist.write(str(title))
        triggerlist.write("\n")
        #for item in triggers:
        #    triggerlist.write(str(item))
        #    

        messages = re.findall("content.:*\s*:\s*.*", content)
        for item in messages:
            print(str(item))
            triggerlist.write(str(item))
            triggerlist.write("\n")

        triggerlist.write("\n")

    finally:
        reader.close()

triggerlist.close()