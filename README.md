# Minesweeper

Small application with Tkinter in Python for playing minesweeper.

## Presentation of the application

This code creates a Tkinter application with a home page, a game page, a statistics page and a parameter page.

### Home page

The home page must allow the user to choose the level of difficulty and launch the game. Of course, it must also allow access to the other pages.  
The choices made on this page are saved, so that the last choice of difficulties will be remembered the next time the application is opened.  
<img src="/test_img/home.png" style="width:400px" />

### Game page

The game page displays the minesweeper with the options you chose earlier.  
A timer starts when the game starts and stops only if the game is over (won or lost). Statistics are renewed at each end of the game.  
The game rules and procedures follow the general rules of Minesweeper.  
<img src="/test_img/game.png" style="width:400px" />

### Statistics page

The statistics page simply displays the game statistics. The statistics are not saved and accumulate even when the application is closed.  
<img src="/test_img/statistic.png" style="width:400px" />

### Parameter page

The settings page must allow the user to change language.  
The application is renewed with the chosen language. The language value is also saved for the next time the application is opened. The default language is set to English.  
<img src="/test_img/setting.png" style="width:400px" />

### Video demonstrating the application

https://github.com/ZEmilie/Minesweeper/assets/95745011/23547844-be15-4e5b-a93c-5e04d0bbb445

## File description

Here is the list of folders required to run the application:
<a id="file-required"></a>
```
/Minesweeper
    /img                    # image set
    /language               # set of {language}.json for each language
    /module
        application.py      # create the main window
        calculate.py        # functions for creating a matrix for the game board
        game.py             # create and manage the game page
        home.py             # create and manage the home page
        management.py       # manage all variables common in the application
                            # eg. colors, image, data, ...
        setting.py          # create and manage the setting page
        statistic.py        # create and manage the statistic page
        text.py             # manage all labels in the application
    main.py
```

When the application is launched, the following folders are created (or can be created):
```
/Minesweeper
    /data
        difficult.json      # save the level selected
        {level}.json        # save the statistics for {level}
                            # {level} = easy/medium/hard
                            # no statistics for custom settings
        language.json       # save the language selected
        wlm.json            # save custom settings
```

There are other files in this git (they are optional for the installation):
```
/Minesweeper
    /test_img               # all screenshots visible in the readme
    .gitignore
    README.md
```

## Installation and launch

PS: The entire application is in Python, so you need to install Python to launch the application.  
Download all the [files needed to run the application](#file-required) then launch the command `python main.py`.

## Reference

The images have been downloaded from https://icones8.fr/icons
