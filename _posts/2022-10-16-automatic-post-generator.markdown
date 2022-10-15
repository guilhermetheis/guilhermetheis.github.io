---
title: Automatic Post Generator
date: 2022-10-16 00:33:13 +0200
categories: [Python, Automation]
tags: [python, automation, website]
author: Guilherme Theis
---

# Automatic Post Generator 

This post is about the creation of an automatic post generator (at the current date of 16/10/2022). The idea is to make possible, down the line, to automatically generate posts. Which will be meant to add things like sensor data and so on. The repository of this code can be found [here](https://github.com/guilhermetheis/automaticMDGen). 

## Base for the code

I've done a quick run down in google and found [Kris van der Mast](https://www.krisvandermast.com/post/2022/03/08/python-script-to-generate-a-new-jekyll-post-with-front-matter.html) post on something similar. I also thought that [mdutils](https://github.com/didix21/mdutils) would be an option, but it might be too strict to "normal" markdown usage, making the creation of the **Front Matter** hard. 

**Kris van der Mast** outputs the following Front Matter

```
---
layout: post
title: Python script to generate a new Jekyll post with front matter
date: 2022-07-29 07:59:46 +0200
comments: true
published: true
categories: ["post"]
tags: ["jekyll","python","front matter"]
author: Kris van der Mast
---
```

But it requires a big input to run such as the following

```
py .\createMarkdown.py 2022-07-29 “Python script to generate a new Jekyll post with front matter” “jekyll python front_matter”
```

We'd like to take the date automatically as we use the script and keep only the title. As we have the `layout: post` as a default we can also remove, as well for `published` and `comments`. The attributes `categories` and `tags` should be custom, so it should not be set within this, only created in order to allow us to modify it (i.e: `categories: [""]`.

## Create a simple Front Matter ready .md by simply requiring the Title

To first run this I simply took the code from **Kris van der Mast** and updated it to automatically get the current date and also accept `categories` as my website allows for multiple categories. I need to update the function `format_cat` to check if the first letter of each word is upper cased or not. The code is extremely similar from Kris, but the end goal should differ/improve upon it. 

This was firstly in the commit from [29/07/2022](https://github.com/guilhermetheis/automaticMDGen/commit/9d8ad6092ce6f4535210d019b49826cc99cf2ac7). It is already added to the github pages. 

For the improvement of upper-cased words for categories I've seen [this](https://thispointer.com/check-if-first-letter-of-string-is-uppercase-in-python/) post and used the portion of `regex` for ease in the usage. The `format_cat` became the following code

```python
def format_cat(cats):
    a = ''
    for s in cats.split():
        if re.search("^[A-Z]", s[0]) is not None:
            a += f'"{s.replace("_", " ")}",'
            #print("it is uppercase")
        else:
            print("The initials of the words need to be upper for the categories")
            break
    return a[:-1]
```

However, the `break` doesn't completely break the code, so running something like `py .\automaticMDGen.py "Automatic post test lower case" "python jekyll front_matter" "Python Automation small text and testing lower case"` generates the following .md

```
---
title: Automatic post test lower case
date: 2022-08-02 12:01:54 +0200
categories: [False]
tags: ["python","jekyll","front matter"]
author: Guilherme Theis
---
```

While we'd like to ideally break the code completely (not generate the .md I think).

I've then posted this question on [r/learnpython](https://www.reddit.com/r/learnpython/comments/we71px/trying_to_complete_break_my_program_and_even/) and got the correct understanding. I need to return none and then check whether it is truly none or not. So the overall view of the two necessary functions (`format_cat` and `writte_frontmatter`) need to be like the following

```python
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
        f = open(f"./_posts/{format_filename(date, args.title)}", "w")
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
```