
The examples below assume the following directory structure in the root directory `/webapp`

    -+ templates
     |
     +-+ signup
     | |
     | + new.html
     | |
     | ` confirm.html
     |
     +-+ example
     | |
     | + index.html
     | |
     | ` index.js
     |
     `- base.html

listdir
=======

    listdir("/webapp/templates")

will return ["signup","example","base.html"], and so will the following:

    listdir("templates",base="/webapp")

When you need the full path the following

    listdir("/webapp/templates",full_path=True)

will return ["/webapp/templates/signup","/webapp/templates/example","/webapp/templates/base.html"]
If you only want part of the path prepended do something like,

    listdir("templates",base="/webapp",full_path=True)

you get a more simple ["templates/signup","templates/example","templates/base.html"]
