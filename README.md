Gphoto2Json
==============
will convert the output of the command 'gphoto2 --list-all-config'
to a json object.

Gphoto2Json.py
______________
the main class

main.py
______________
example of how to use the class.
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
/main/actions/viewfinder
Label: Nikon Viewfinder
Type: TOGGLE
Current: 0
/main/settings/meterofftime
Label: Meter Off Time
Type: RADIO
Current: 6 seconds
Choice: 0 4 seconds
Choice: 1 6 seconds
Choice: 2 8 seconds
Choice: 3 16 seconds
Choice: 4 30 seconds
Choice: 5 1 minute
Choice: 6 5 minutes
Choice: 7 10 minutes
Choice: 8 30 minutes

