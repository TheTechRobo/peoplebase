# Plan for peopleBase
I will be using a tkinter notebook with multiple tabs -- one for each employee.

The splash screen has three buttons -- one that will do a `git pull` (and therefore updating), one that will launch the customer database, and one that will launch the scheduler.

One button per half hour. When you click it it pops up with a `Toplevel()` window with an `Entry` widget, that asks you for the name.

Uses a very crude technique -- one file per half hour, in a subdirectory.

The database wont be much better -- one file per customer. If you want to edit that customer's info, you have to go through all the steps again.
