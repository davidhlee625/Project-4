import praw
import random
import time

#Extra Credit 1
#Make your bot create new submission posts instead of just new comments. You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative) and posting them to the class sub. I recommend creating a separate python file for creating submissions and creating comments.
#For full credit, you must have at least 200 submissions, some of which should be self posts and some link posts. Duplicate submissions (i.e. submissions with the same title/selftext/url) do not count.
#You must create a new file bot_submissions.py and place all of the code in this new file. You should not modify the bot.py file to create submissions.


self_count = 0 #self posts are text posts that don't link out of reddit
link_count = 0 #link posts are url posts
total_post = 0

reddit = praw.Reddit('bot', user_agent = 'cs40') #connect to reddit

link_subreddit = reddit.subreddit('finance')#link post
list_link = list(link_subreddit.top(limit=250))

self_subreddit = reddit.subreddit('WritingPrompts') #self posts
list_self = list(self_subreddit.top(limit=250))

og_subreddit = reddit.subreddit('cs40_2022fall')#cs 40 subreddit to compare against for duplicates
list_og = list((og_subreddit).new(limit=None))

total = True
while total:
    print()
    flip = random.choice(['head','tail']) #coinflip
    # print(flip)

    if flip == 'head': #if equal to head, then choose from the list of link url
        submission = random.choice(list_link)

        if submission in list_og:
            print('Duplicate')
            continue
        else:
            print('New link post')
            link_count+=1
            total_post+=1
            og_subreddit.submit(title=submission.title, url = submission.url)
            print('link post count=', link_count)
            if total_post == 200:
                total = False
            # print('submission title=', submission.title)
            time.sleep(10)

    else: #if not equal to head, then choose from the list of self urls
        submission = random.choice(list_self)

        if submission in list_og:
            print('Duplicate')
            continue
        else:
            print('New self post')
            self_count+=1
            total_post+=1
            og_subreddit.submit(title = submission.title, url = submission.url)
            print('self post count =', self_count)
            if total_post == 200:
                total = False
            # print('submission title = ', submission.title)
            time.sleep(10)

# print(total_post)
