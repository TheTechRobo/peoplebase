# THE SCHEDULER

#command-line program (gui later?) that enables you to create timesheets

class Plan:
    Plan = '''
PLAN: Type command (e.g. del 1) each appointment has an id 
When adding, it asks time and turns the colon into a Period
then its a float
THEN it will ask you what NAME is it
and what id
and will sort the floats (optional: when you type "sync")
then will add the text (<TIME> <name>) to a list
`list` command shows time id and name
`output` (or render?) iterates over the list and will display a tkinter Listbox that has that text
`save <FILENAME>` will save it as filename
to process commands with arguments e.g. `save <FILENAME>` it will run command.split("save ", "") and that would be the filename
AND THATS IT
MAYBE IN FUTURE THIS COULD BE GUI, IT DOESNT SOUND TOO HARD???
like the `list` command could show in a Toplevel and it will only render whenever you click `Render' or `output'
    '''

print(Plan.Plan)
