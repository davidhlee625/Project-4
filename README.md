# Project-4

<h1>Reddit Bot</h1>

For this project, I made a Reddit Bot that would support Representative Katie Porter, utilizing the Praw API and Python. 


Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it. (Below each comment is a button labeled permalink that lets you link to a comment.)

1. 12 pts for completed bot.py file
2. 3 pts for this Github Repo
3. I reached 830 valid comments, so +6 points. So far 21 points without any additional credit.

```
davidlee@Lavids-MacBook-Pro CS 40 % /us/local/bin/python3 "/Users/davidlee/Desktop/Coursework F22/CS 40/project04 redditbot/bot_counter.py"
--username=augbot52
Version 7.6.0 of praw is outdated. Version 7.6.1 was released Friday November 11, 2022.
len(comments) = 1000
len(top_level_comments)= 131
len(replies)= 869
len(valid_top_level_comments)= 113
len(not_self_replies)=763
len(not_self_replies)= 717
========================================
valid_comments= 830
========================================
```

5. My `bot.submission.py` file made over 200 posts to the subreddit. For the self posts, I pulled from r/WritingPrompts and for the link posts, I pulled from r/Finance. Below is a tidbit of how many posts were made in the newest 1000 submissions that time, but there are definitely more than this number. +2


```
davidlee@Lavids-MacBook-Pro CS 40 % /us/local/bin/python3 "/Users/davidlee/Desktop/Coursework F22/CS 40/project04 redditbot/bot_submissions.py"
Version 7.6.0 of praw is outdated. Version 7.6.1 was released Friday November 11, 2022.
total post count: 233
```
6. I created an army of 5 bots for my project, including the original bot. All of these bots made at least 500 valid comments.
<ul>
  <li>augbot52</li>
  <li>augbot522</li>
  <li>augbot5</li>
  <li>augbot4</li>
  <li>augbot3</li>
</ul>

**bot2/augbot522**
```
davidlee@Lavids-MacBook-Pro CS 40 % /usr/local/bin/python3 "/Users/davidlee/Desktop/Coursework F22/CS 40/project_04/bot_counter.py" --username augbot522
Version 7.6.0 of praw is outdated. Version 7.6.1 was released Friday November 11, 2022.
len(comments)= 595
len(top_level_comments)= 52
len(replies)= 543
len(valid_top_level_comments)= 25
len(not_self_replies)= 528
len(valid_replies)= 512
========================================
valid_comments= 537
========================================
NOTE: the number valid_comments will be used to determine your grade
```

**bot3/augbot5**
```
davidlee@Lavids-MacBook-Pro CS 40 % /usr/local/bin/python3 "/Users/davidlee/Desktop/Coursework F22/CS 40/project_04/bot_counter.py" --username augbot5

Version 7.6.0 of praw is outdated. Version 7.6.1 was released Friday November 11, 2022.
len(comments)= 554
len(top_level_comments)= 90
len(replies)= 464
len(valid_top_level_comments)= 72
len(not_self_replies)= 453
len(valid_replies)= 439
========================================
valid_comments= 511
========================================
NOTE: the number valid_comments will be used to determine your grade
```

**bot4/augbot4**
```
davidlee@Lavids-MacBook-Pro CS 40 % /usr/local/bin/python3 "/Users/davidlee/Desktop/Coursework F22/CS 40/project_04/bot_counter.py" --username augbot4

Version 7.6.0 of praw is outdated. Version 7.6.1 was released Friday November 11, 2022.
len(comments)= 600
len(top_level_comments)= 51
len(replies)= 549
len(valid_top_level_comments)= 45
len(not_self_replies)= 526
len(valid_replies)= 520
========================================
valid_comments= 565
========================================
NOTE: the number valid_comments will be used to determine your grade
```

**bot5/augbot3**
```
davidlee@Lavids-MacBook-Pro CS 40 % /usr/local/bin/python3 "/Users/davidlee/Desktop/Coursework F22/CS 40/project_04/bot_counter.py" --username augbot3

Version 7.6.0 of praw is outdated. Version 7.6.1 was released Friday November 11, 2022.
len(comments)= 521
len(top_level_comments)= 187
len(replies)= 334
len(valid_top_level_comments)= 175
len(not_self_replies)= 331
len(valid_replies)= 325
========================================
valid_comments= 500
========================================
NOTE: the number valid_comments will be used to determine your grade
```

7. In my `bot.py` file, I define a command score to have my bot reply to the most upvoted comments. +2

Explains what you believe your score should be. Clearly state which tasks you complete/don't complete.
