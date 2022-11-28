import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "Katie Porter [WON] her [HOUSE] seat in California earlier this week. Porter [REPRESENTS] the Orange County district. Regardless, the [REPUBLICANS] will [CONTROL] the [HOUSE]. ", 
    "Porter's educational background is [INCREDIBLE]. She [ATTENDED] Phillips Academy, then Yale, and then Harvard Law School. Porter then [WORKED] as a [LAWYER] and a law professor before her election to the [HOUSE].",
    "In 2018, Porter ran [AGAINST] twice incumbent and Republican Mimi Walters. It was a [TOUGH] race and quite a [CHALLENGE]. However, at the end, Porter was the [WINNER]. Porter was the first Democrat to represent the 45th district since its [INCEPTION] in 1953.",
    "Porter quickly [ROSE] to [FAME], becoming an [ADMIRABLE] figure in the Democratic party. Her [POINTED] questioning at the Congressional hearings [ATTRACTED] a lot of [VIEWERSHIP]. Simultaneously, she became a [THORN] in Republicans' sides.",
    "One of her most [INCREDIBLE] [FEATS] came during these hearings. In March of 2020, the pandemic was [SPREADING] rapidly. At the [ONSET] of the pandemic, she made the CDC chief agree to use his [AUTHORITY] to [PROMISE] COVID testing, [FREE] for all Americans. Simply [INCREDIBLE]!",
    "With this [FEAT], Porter [WON] her third term in Congress. Her national fame helped her build a [SUBSTANTIAL] cash chest. With her already [INCREDIBLE] track record, Porter will continue onto [GREATER] success."
    ]

replacements = {
    'WON' : ['won', 'secured', 'regained'],
    'REPRESENTS' : ['represents', 'speaks for', ],
    'HOUSE' : ['House', 'House of Representatives'],
    'REPUBLICANS' : ['Republicans', 'Conservatives'],
    'CONTROL' : ['control', 'hold', 'govern', 'manage', 'run'],
    'INCREDIBLE' : ['incredible', 'amazing', 'impressive'],
    'ATTENDED' : ['attended', 'was a student at', 'was educated at', 'learned at'],
    'WORKED' : ['worked', 'labored', 'toiled'],
    'LAWYER' : ['lawyer', 'attorney', 'legal practitioner'],
    'AGAINST' : ['against', 'opposed to', 'in opposition to'],
    'TOUGH' : ['tough', 'challenging', 'hard', 'competitive', 'hard-fought'],
    'CHALLENGE' : ['challenge', 'struggle', 'trial', 'difficult time'],
    'WINNER' : ['winner', 'victor', 'champion'],
    'INCEPTION' : ['inception', 'establishment', 'creation', 'origination', 'initiation'],
    'ROSE' : ['rose', 'ascended', 'skyrocketed', 'grew'],
    'FAME' : ['fame', 'renown', 'popularity', 'stardom'],
    'ADMIRABLE' : ['admirable', 'praiseworthy', 'esteemable', 'respectable'],
    'POINTED' : ['pointed', 'sharp', 'cutting', 'scathing'],
    'ATTRACTED' : ['attracted', 'drew', 'enticed'],
    'VIEWERSHIP' : ['viewership', 'fanbase', 'audience', 'following'],
    'THORN' : ['thorn', 'pain', 'nuisance', 'annoyance'],
    'ONSET' : ['onset', 'beginning', 'arrival', 'outbreak'],
    'FEATS' : ['feats', 'achievements', 'accomplishments', 'triumphs'],
    'AUTHORITY' : ['authority', 'promise', 'legal control', 'authorization'],
    'PROMISE' : ['promise', 'guarantee', 'pledge', 'swear'],
    'FREE' : ['free', 'complimentary', 'gratis', 'without charge', 'free of charge'],
    'SPREADING' : ['spreading', 'proliferating', 'expanding', 'growing', 'increasing'],
    'FEAT' : ['feat', 'achievement', 'accomplishment', 'triumph'],
    'GREATER' : ['greater', 'even more' , 'more', 'larger'],
    'SUBSTANTIAL' : ['substantial', 'considerable', 'huge', 'prodigious', 'vast']
    }

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys(): #replacement is keys of dictionary
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib


def score(comment): #gives upvote score for comment, extra credit 3
    comment = random.choice(comments_without_replies) #comments_without_replies should be excluding comments authored by myself
    score = comment.score
    return score

# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40') #connecting to reddit

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/z2zt7t/sometimes_i_see_things_and_im_just_so_proud/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True:
# posted = True
# if posted:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    submission.comments.replace_more(limit = None)
    for comment in submission.comments.list():
        all_comments.append(comment)

    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not

    
    not_my_comments = []
    for comment in all_comments:
        # print('type comment author', type(comment.author))
        if str(comment.author) != 'augbot52':
            not_my_comments.append(comment)

    print('not my comments', not_my_comments)
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))



    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('hasnotcommented status=', has_not_commented)

    # posted = False #troubleshooting without while == True

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        submission.reply(generate_comment())
        time.sleep(5)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            reply_indicator = True
            for reply in comment.replies:
                if str(reply.author) == 'augbot52':
                    reply_indicator = False
            if reply_indicator:
                comments_without_replies.append(comment)


        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        try:
            # comment = random.choice(comments_without_replies)
            comment = sorted(comments_without_replies, key = score, reverse = True)[0] #key takes function score as parameter
            print(comment)
            comment.reply(generate_comment())
        except praw.exceptions.RedditAPIException:
            print('already replied to this comment')
        except IndexError:
            pass
        time.sleep(5)


    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    subreddit = reddit.subreddit("cs40_2022fall")
    hot_submissions = list(subreddit.hot(limit = 5))
    submission = random.choice(hot_submissions)
    print('submission =', submission)

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)

