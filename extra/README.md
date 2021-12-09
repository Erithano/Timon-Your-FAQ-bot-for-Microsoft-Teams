# Extract text and triggers from a PVA zip file (Experimental)

Super quick and dirty python code to see text content in a PVA bot zip file. Uses some simple regex queries to find content.

- **getcontent.py** - get topic name and topic content 

- **gettriggers.py** - get topic name and topic triggers

💡 **Warning**: This has not been tested in other environments - it may or may not work on your computer ;)

## How to extract content from a Power Virtual Agent bot:

1. Get the PVA bot zip file. If you're exporting a local bot: Go to the bot https://powerva.microsoft.com/ and export it (see Settings -> Export/import bot (preview)*).
2. Download zip, extract zip, open the main folder
3. Download the python files in this folder, upload them in the main folder of the extracted zip file
4. Run the respective python file for triggers / content (requires python installed)
5. You'll find a new .txt file in the main folder

*this should bring you to https://make.powerapps.com/ -> Solutions
