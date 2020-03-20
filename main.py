import argparse

parser = argparse.ArgumentParser(description="""\
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
""", formatter_class=argparse.RawTextHelpFormatter)
parser.parse_args()

import pathlib

def read_all_contents():
    paths = pathlib.Path('content').glob("*.txt")
    contents = []
    for path in paths:
        with open(path,"r") as f:
            contents += read_content_file(f.read())
    return contents

def read_content_file(file_text):
    contents = []
    splits = file_text.split("\n\n\n")
    for split in splits:
        split = split.replace("\n\n","<br>")
        lines = split.split("\n")
        key = lines[0]
        content = " ".join(lines[1:])
        contents.append((key,content))
    return contents

import shutil
from os import path

def duplicate_template_dir():
    src = "template/"
    dest = "target/"
    if path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(src,dest)

def fill_file_with_content(path,contents):
    with open(path,"r") as f:
        text = f.read()
    
    for content in contents:
        key = content[0]
        body = content[1]
        to_replace = "{{"+key+"}}"
        text = text.replace(to_replace,body)
    
    with open(path,"w") as f:
        f.write(text)

def fill_all_files(dir,contents):
    paths = pathlib.Path(dir).glob("*.html")
    for path in paths:
        fill_file_with_content(path,contents)

def run():
    contents = read_all_contents()
    print(contents)
    duplicate_template_dir()
    fill_all_files("target",contents)
    print("Finished!")

run()
    