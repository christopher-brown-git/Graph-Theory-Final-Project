# graphTheoryProject
**Set-up:**

I installed Python3 and Tkinter using this website, which uses homebrew: https://www.pythonguis.com/installation/install-tkinter-mac/ 
homebrew is a package management system that makes installing python3 and Tkinter very easy (just one line commands)

Here is a link the explains how to install homebrew: https://brew.sh/ 

Installing Tkinter took about 5 minutes

Here are the 3 steps required to install the packages needed to run my executable, as explain on the two websites linked above: 

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 
brew install python3
brew install tkinter

When everything is installed, download the executable and place it in a directory. 
Open up a new terminal window and navigate to that directory. If you downloaded the executable in a folder called “graphTheoryProject” that is on your desktop, you can navigate to “graphTheoryProject” using the following command: 

cd ~/Desktop/graphTheoryProject

To run the executable, type “python3 organized_mini.py”

My executable allows the user to do the following:

* Place vertices of a given color on the screen. The possible colors are pink, purple, black, yellow, green, blue, and red
* Change the color of vertices on the screen
* Create edges between vertices 
* Prevent the creation of edges between vertices of the same color. 
* Check if the coloring of the graph is valid (no two adjacent vertices have the same color)
* Determine with 1-click if the graph drawn is bipartite 
* If the graph is bipartite, draw a 2-coloring with 1 click
* Get the number of vertices of each color that are on the screen at a given moment
* Delete a vertex and all edges incident to it

