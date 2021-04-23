# Extract text and triggers from a PVA zip file

Super quick and dirty python code to see text content in a PVA bot zip file. Uses some simple regex queries to find content.

- **getcontent.py** - get topic name and topic content 

- **gettriggers.py** - get topic name and topic triggers

💡 **Warning**: May or may not work ;)

## How to extract content from a Power Virtual Agent bot:

1. Get the PVA bot zip file. Go to https://powerva.microsoft.com/ and export it.
2. Download zip, extract zip, open the main folder
3. Download the python files in this folder, upload them in the main folder of the extracted zip file
4. Run the respective python file for triggers / content (requires python installed)
5. You'll find a new .txt file in the main folder
