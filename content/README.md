# Instructions to Use Content:
This is copy pasted from main.py file.
This program writes information from the content/ directory
    to the current directory using the template provided in the
    template/ directory.

    Instructions for the content directory:
    The information must be provided in a key/value format.
    First, type the key, such as a title, and then insert a new
    line(enter/return). All of these keys must be UNIQUE. Then 
    type the content. There can be new lines in this content
    (or even two in a row), but there cannot be three new lines 
    in this block. After you finish this key/value pair, move
    onto the next key/value pair by inserting THREE new 
    lines(pressing return 3 times) and then typing your
    next key.
    The files with these key/value pairs may be in ANY configuration
    of .txt FILES but there must NOT BE ANY FOLDERS or nexting of
    files!

    NOTE: If you want custom HTML formatting for content inside
    a block of content, use standard HTML tags.

    Here is an example content file:
    greeting <-- this is a key
    Welcome to this amazing website! <-- this is content


    body <-- this is the next key, notice two empty lines(means 3 new lines)
    This is such a <i>cool</i> place, why don't you do some cool
    stuff here.

    This is another paragraph <-- this and previous paragraph are content
    ^^^^^ notice there is one empty line(this means there were 2 new lines
    which is valid)
    ^^^^^ the word cool in the first paragraph under body will be italicized.

    Instructions for template directory:
    The HTML files should simply be correctly formatted HTML files.
    In order to choose where content must be inserted use use two open
    curly braces and two closed curly braces. Here is an example HTML snippet:
    <h1>{{greeting}}</h1>
    <p>
        {{body}}
    </p>