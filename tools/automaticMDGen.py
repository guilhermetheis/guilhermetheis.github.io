
"""
This code is meant to create markdown files for future automation of github pages specifically

Author: Guilherme Theis
"""

import os    # standard library
import sys
import argparse
from datetime import datetime #to get name of the file based on YYYY-MM-DD
import re

def format_tags(tags):
    a = ''
    for s in tags.split():
        a += f'"{s.replace("_", " ")}",'
        
    return a[:-1]

def format_cat(cats):
    a = ''
    for s in cats.split():
        if re.search("^[A-Z]", s[0]) is not None:
            a += f'"{s.replace("_", " ")}",'
            #print("it is uppercase")
        else:
            return None
    return a[:-1]

def format_filename(date, title):
    return f'{date}-{title.replace(" ", "-").lower()}.markdown'

def write_frontmatter(args, date, current_time):
    if format_cat(args.cats) is not None:
        f = open(f"../_posts/{format_filename(date, args.title)}", "w")
        f.write("---\n")
        f.write(f"title: {args.title}\n")
        f.write(f"date: {date} {current_time} +0200\n")
        f.write(f"categories: [{format_cat(args.cats)}]\n")
        f.write(f"tags: [{format_tags(args.tags)}]\n")
        f.write(f"author: {args.author}\n")
        f.write("---\n")
        f.close()
    else:
        print('Categories need to start in upper case, re-run the code with the correct input')
        
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new post')
    parser.add_argument("title", type=str, help="Provide a title")
    parser.add_argument("tags", type=str, help="Provide a comma separated list of tags")
    parser.add_argument("cats", type=str, help="Provide a comma separated list of categories (upper case initial)")
    parser.add_argument("--author", type=str, help="Provide a name for the author of the post", default="Guilherme Theis")
    args = parser.parse_args()
    date = datetime.today().strftime('%Y-%m-%d')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    write_frontmatter(args, date, current_time)
