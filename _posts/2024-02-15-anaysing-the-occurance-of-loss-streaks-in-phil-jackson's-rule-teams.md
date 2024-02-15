---
title: Analysis of the occurrence of loss-streaks in Phil Jackson's rule teams
date: 2024-02-15 18:30:08 +0200
categories: ["NBA","Celtics"]
tags: ["nba,","analysis,","basketball,","python"]
author: Guilherme Theis
---

I did a small [python script](https://pastebin.com/EDQ6z5g4) to retrieve this data. I'll probably do a better job and round up a better analysis later on when I can fully work on it. I'll probably do some sort of blog post about it so you can always check [my twitter](https://twitter.com/GuilhermeTheis) to see. I do warn you I mostly talk Celtics there.

> Disclaimer 1: while I am saying this is an analysis **Phil Jackson** positive teams I am actually checking the teams with a win percentage of 0.670 which corresponds to 55-win pace. I will work o checking two things later on which are the full Phil Jackson positive, meaning teams that got 40 wins in their first 59 games as well as checking for teams that might have had stretches of 40 wins in less than 59 games during the season.

> Disclaimer 2: I haven't fully proofed this so if there is some blatant error feel free to tell me so.

## Teams that won the championship

There are [207 teams](https://docs.google.com/spreadsheets/d/1qQpiz8v4_fRf9_ocdusg7sBAtdNH_NFbCBH-dFqbkOI/edit?usp=sharing) with a win percentage of 0.670 or better since the data is available excluding the current season (1970-71 to 2022-23). Out of these 52 seasons, 42 champions seem to have this win rate. As said in the Disclaimer 1, this not necessarily means the 10 teams missing teams aren't Phil Jackson positive, a great example is the [2021-22 Warriors](https://www.basketball-reference.com/teams/GSW/2022/gamelog/) who finished 2 wins below this 0.670 win rate but were Phil Jackson positive. 

![Winners Histogrram](/assets/images/winners.png)

Out of these 42 teams a pretty impressive 34 teams have registered 3 or more occurrences  of loss-streaks. I would highlight the most impressive one being the [1971-72 Lakers](https://www.basketball-reference.com/teams/LAL/1972.html) who had three occurrences  of loss-streaks (though only 2 games in a row at each time) while having a 69-13 record and the league best-ever winstreak at 33 games. Two other teams that can be highlighted in this range of 3 ocurrances are the 2019-20 Lakers, the 2011-12 Heat and the 1998-99 because of the length of their season. The Spurs managed to have three occurrences  in a total of 50 games (finished 37-13), one of which was a three game loss streak. The Heat managed to have **six** occurrences  in 20 losses and 66 total games, one of them being a three-game loss-streak.

Other teams that won that are highlighted worth: are the 1989-90 Pistons and 2017-18 Warriors, the only teams with lower than 60 wins to have less than four occurrences . Then there are two teams that won 60 or more games and have registered less than five occurrences ; the 1987-1988 Lakers are the only 60+ win team to register five or more occurrences .

I also checked the trends by year in a line plot, but for the champions it seems mostly that this doesn't matter much, looks a lot like noise

![Winners trend](/assets/images/championsTrends.png)

## Runner Ups

Out of the 207 teams, there are 30 runner-ups analyzed here. The two more impressive ones are the 2015-16 Warriors (73-9), the only team with no loss-streak in these 207 and the 1995-96 Supersonics that had only one loss-streak (like the team that beat them in the Bulls). It seems that a lot of runner ups register four occurrences  in a season so that might have some correlation but then again, very sample size. There isn't much to analyse  here. There isn't interesting cases here in terms of quantity, it would look like the trends show that runner-ups tend to register less occurrences  of loss-streaks more recently, but its mostly due to the lower amount of samples.

![runnerup](/assets/images/runnerUps.png)

![runnerrs trend](/assets/images/runnerUPTrends.png)

## Teams that didn't make to the finals

Here is more a way to see really good teams that didn't make the finals. The best record to do so is the 2006-07 Mavericks, then you have the 2008-09 Cavs, 2015-16 Spurs, 1972-73 Celtics, 2017-18 Rockets which are the teams with 65+ wins.

![nonFilan](/assets/images/nonFinalists.png)