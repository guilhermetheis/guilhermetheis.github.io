---
title: How I setup this website
date: 2022-07-28 22:50:00 +0200
categories: [Website, Github]
tags: [github, github pages, website]
---

# How I set up this website

Firstly I've found [Techno Tim's video](https://www.youtube.com/watch?v=F8iOU1ci19Q) about Jekyll, which uses the [Chirpy's Theme](https://github.com/cotes2020/jekyll-theme-chirpy). From there was just a matter of following the different tutorials available. However, I had a problem where, when trying to save the `gh-pages` as my source branch for deployment, the save button would be greyed out. This was asked in [stackoverflow](https://stackoverflow.com/questions/72739053/github-pages-cant-save). While there is no reasoning and real fix, there is the walk around of inspecting the button and removing the `disabled` attribute.