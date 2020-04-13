# Plan for peopleBase
I will be using a tkinter notebook with multiple tabs -- one for each employee.

The splash screen has three buttons -- one that will do a `git pull` (and therefore updating), one that will launch the customer database, and one that will launch the scheduler.

One button per half hour. When you click it it pops up with a `Toplevel()` window with an `Entry` widget, that asks you for the name.

Will have a save file that contains a list: one entry of list per half-hour, and one file per employee.

The database will be terrible -- one file per customer (with a list).
