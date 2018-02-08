I've documented the code, make sure to read the comments too.

In **gen_data.py**:
There are few parameters to set in the **main** function before you run. The number of frames you want in each sequence and how many sequences you want to generate.

Also, **make sure** to create a folder named "**data**", so that all sequences get dumped into that folder, else change the path to **data directory** in the code.

Make sure to install *matplotlib* and *numpy* using pip or conda to get the code running. I've used **python 2.7**. If you are using **python 3.6**, just change the print statements, if any. It should work.

In **visualize_seq.py** make sure to set the **path to the sequence** you want to see. Every time a frame is shown, *close the window* to see the *next frame*.

Make sure to run *gen_data.py* before you try *visualize_seq.py*

PS: A lot of places I have used list comprehensions to keep the code compact. Here's a reference: https://www.python-course.eu/list_comprehension.php

All the best.

PFA