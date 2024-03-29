
### About

MCEdit is an editor for The Legend of Zelda: The Minish Cap (US version only).  
It's currently a work in progress and has a number of bugs and half-finished features.  

Current features:
* Viewing rooms as well as the entities within them
* Editing the BG1 and BG2 layers of rooms
* Editing entities, with a UI that lists each entity's unique parameters
* Viewing the game's text
* Viewing entity sprites and animations
* Editing save files (partial support)
* Searching for specific entity types across all rooms in the game
* Testing rooms quickly by launching the game with you in the selected room

Planned features:
* Editing the game's text
* More convenient UI for editing entities
* Editing the BG3 layer of rooms
* Changing the size of rooms
* Adding and removing entities
* Implement editing more variables in save files
* Editing maps
* Editing image data

### Running from source

If you want to run the latest development version of MCEdit from source, follow the instructions below.

Download and install git from here: https://git-scm.com/downloads  
Then clone this repository with git by running this in a command prompt:  
`git clone --recursive https://github.com/LagoLunatic/MCEdit.git`  

Download and install Python 3.12 from here: https://www.python.org/downloads/release/python-3121/  
"Windows installer (64-bit)" is the one you want if you're on Windows.

Open the MCEdit folder in a command prompt and install dependencies by running:  
`py -m pip install -r requirements.txt`  

Then launch the editor with:  
`py mcedit.py`  
