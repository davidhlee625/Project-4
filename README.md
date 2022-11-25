# Project-4

**Reddit Bot**

For this project, I made a Reddit Bot that would support Representative Katie Porter, utilizing the Praw API and Python. 


Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it. (Below each comment is a button labeled permalink that lets you link to a comment.)

1. 12 pts for completed bot.py file
2. 3 pts for this Github Repo
3. I reached 830 valid comments, so +6 points

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

5. My bot.submission.py file made over 200 posts to the subreddit. For the self posts, I pulled from r/WritingPrompts and for the link posts, I pulled from r/Finance. Below is a tidbit of how many posts were made in the newest 1000 submissions that time, but there are definitely more than this number. +2


```
davidlee@Lavids-MacBook-Pro CS 40 % /us/local/bin/python3 "/Users/davidlee/Desktop/Coursework F22/CS 40/project04 redditbot/bot_submissions.py"
Version 7.6.0 of praw is outdated. Version 7.6.1 was released Friday November 11, 2022.
total post count: 233

```
6. In my bot.py file, I define a command score to have my bot reply to the most upvoted comments. +2
7. 
Includes the output of running the bot_counter.py file on your bot to count how many comments you've created. The output of this command must be inside of a markdown code block (i.e. use the triple backticks notation).
Explains what you believe your score should be. Clearly state which tasks you complete/don't complete.
