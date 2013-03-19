Gphoto2Json
================================
*will convert the output of the command 'gphoto2 --list-all-config'
to a json object.*

Gphoto2Json.py
-------------------------
the main class 

main.py
-------------------------
example of how to use the class

	gphotoConfigVar = open('gphoto2-config-input.log', 'r').read()

	c=gPhoto2setting(gphotoConfigVar)
	print json.dumps(c.formObject,separators=(',',':'),indent=4,sort_keys=True)


It read the "gphoto2-config-input.log" witch is a example output of the command:

/main/actions/autofocusdrive
Label: Drive Nikon DSLR Autofocus
Type: TOGGLE
Current: 0
/main/actions/manualfocusdrive
Label: Drive Nikon DSLR Manual focus
Type: RANGE
Current: 0
Bottom: -32767
Top: 32767
Step: 1

json-output.data
-------------------------
example of the output in JSON

	{
        "current":"0",
        "currentindex":null,
        "group":"actions",
        "label":"Drive Nikon DSLR Autofocus",
        "name":"autofocusdrive",
        "options":false,
        "path":"/main/actions/autofocusdrive",
        "type":"TOGGLE"
    },