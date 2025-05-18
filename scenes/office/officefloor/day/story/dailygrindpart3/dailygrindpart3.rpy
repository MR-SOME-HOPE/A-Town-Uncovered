label lbl_daily_grind_part3:
    $ officejobs_complete = 0
    $ officejobs_copymachine = 0
    $ officejobs_coffeerun = 0
    $ officejobs_emailproofread = 0
    default received_eloise_text_again = 0

    #[Office, afternoon - “Daily Grind Part 1”  - main_story =102]

    #-During the “Daily Grind” Scenes in the main story, the player and Mc will
    # have a short scene with some of the characters around the office before
    # playing the respective minigames of the day-

############################################################################################
    #-Mc enters the office only for his phone to vibrate indicating a text message.
    # Pulling up his phone, it shows it’s from Eloise-

    scene bg dailygrindpart3_1
    with fade
    $ renpy.pause()
    show bg dailygrindpart3_2
    $ renpy.pause()
    show bg dailygrindpart3_3
    $ renpy.pause()
    show bg dailygrindpart3_4
    $ renpy.pause()
    show bg dailygrindpart3_5
    $ renpy.pause()

    $ received_eloise_text_again = 1

    # elo "Hi, [povname]!"
    # elo "Looking good today!"
    # elo "I can see you via the cctv."
    # elo "I'm always watching"
    # elo "Remember that if you think about causing trouble~"
    # elo "Anyway, I got a lot on my agenda today"
    # elo "Busy busy"
    # elo "Next part of our tour will be on Thursday after work."
    # elo "See you then~"

    #-Mc puts his phone down-
############################################################################################

    scene bg officefloor_day
    with fade
    #[Office, afternoon - “Daily Grind Part 3”  - main_story =104]

    #-Mc enters the office only for his phone to vibrate indicating a text message. Pulling up his phone, it shows it’s from Eloise-
    #-Mc puts down his phone-

    show pov smirk_talk at left
    with dissolve
    pov "Huh, nice to see she remembered the tour promise."
    pov "Hopefully today’s work isn’t too hard-"

    #-Manager appears behind the mc before he can finish his sentence-

    show pov shocked at left
    show mrf bored_talk at right
    with dissolve
    mrf "Enough talking to yourself and get in gear, kid!"
    show pov embarrassed at left
    mrf "We have an overload of work today, and we need to get moving!"
    show pov neutral_talk at left
    show mrf confused at right
    pov "Oh, hey Sir, is everything okay?"
    show pov neutral at left
    show mrf bored_talk at right
    mrf "No it is not, kid."
    mrf "A manager friend of mine in yesterday's seminar told me he heard that some of the higher-ups are going to be sending their goons to make a surprise inspection to some of the underperforming departments on Monday morning."
    show pov embarrassed at left
    mrf "And considering how many of those fancy chair bastards see us as a catastrophe waiting to happen and would love to get rid of us, that means we are going to be the first on the list for their inspection."
    show mrf smirk_talk at right
    mrf "We haven’t finished setting everything up, so we are gonna have to add coal to the engine and double our efforts!"
    show pov confused_talk at left
    show mrf smirk at right
    pov "What’s the big deal?"
    pov "I thought that you said we would be finished with preparations by Friday anyway, so why panic now?"
    show pov confused at left
    show mrf bored_talk at right
    mrf "Because the preparations I had, were for us to start operations comfortably with the minimum standards."
    mrf "But those standards are definitely not gonna cut it for an inspection from the higher-ups."
    show mrf smirk_talk at right
    mrf "So instead of using two weeks to set up everything to company standards gradually, we are gonna have to push ourselves these next two days and the weekend to get everything done."
    show pov confused_talk at left
    show mrf smirk at right
    pov "You are going to need me to come over on the weekend too?"
    show pov embarrassed at left
    show mrf neutral_talk at right
    mrf "No, nothing like that."
    show pov confused at left
    show mrf smirk_talk at right
    mrf "Luckily for you, your internship doesn't allow you to cover extra hours on the weekends, so I’ll just need you to work extra hard today and tomorrow."
    show pov embarrassed at left
    show mrf neutral_talk at right
    mrf "That may mean that you are going to have to cut your mid-shift break a little but considering your schedule will open up significantly after friday, consider this your final initiation trial."
    show mrf confused_talk at right
    mrf "You don’t have an issue with that, do you?"
    show pov neutral_talk at left
    show mrf smirk_talk at right
    pov "Not at all, Sir."
    pov "Just let me know where I can help out if you need it."
    show pov neutral at left
    show mrf bored_talk at right
    mrf "Those are the words I wanted to hear!"
    show mrf confused_talk at right
    mrf "For now just focus on your usual tasks to keep the small stuff off our heads."
    show pov embarrassed at left
    show mrf bored_talk at right
    mrf "Alright kid, get to work while I keep trying to sort this whole mess out."
    show mrf angry_talk at right
    mrf "{i}*grumble*{/i} this really isn’t how I wanted to get back into work after one of the manager seminars…"
    show pov neutral at left
    show mrf bored_talk at right
    mrf "I was stressed all night because of it."
    show pov neutral_talk at left
    show mrf bored at right
    pov "Well, at least we know the inspection is coming in the first place and have time to prepare for it."
    pov "Just imagine how stressed you’d be had they just dropped in on us unannounced on Monday."
    show pov neutral at left
    show mrf bored_talk at right
    mrf "God, I don’t even want to picture it…"
    show pov embarrassed at left
    show mrf angry_talk at right
    mrf "{i}*Sigh*{/i} But you are right. Thanks, kid."
    show mrf smirk_talk at right
    mrf "We still have time to attack, and that’s what we should focus on right now."
    show pov neutral at left
    show mrf bored_talk at right
    mrf "Alright, enough chit-chat."
    mrf "Get to it!"
    show pov neutral at left
    show mrf bored at right
    pov "Yes, sir!"
    scene black with fade

label lbl_daily_grind_part3_jobs_menu:
    scene bg officefloor_day with fade
    menu:
        "Copy Machine" if not officejobs_copymachine:
            jump lbl_officejobs_copymachine

        "Coffee Run" if not officejobs_coffeerun:
            jump lbl_officejobs_coffeerun

        #"Email Proofreading" if not officejobs_emailproofread:
        #    jump lbl_officejobs_emailproofread

        #-Screen fades to black and minigame selection comes up-

    #-This time there is no mid minigame scene as the MC is too busy and doesn’t have the time in between his shift to do it so once one minigame ends, players can decide which one they take next right away-

        #-After both minigames are over, the Mc’s shift ends and scene continues-

label lbl_daily_grind_part3_jobs_end:
    scene bg officefloor_day
    show pov neutral at left
    show mrf smirk_talk at Position(xpos=1000)
    show cor neutral at Position(xpos=1300)
    show glo confused at Position(xpos=1600)
    show kan embarrassed at Position(xpos=1800)
    with dissolve
    mrf "Alright everybody, that’s enough for today."
    mrf "Those of you willing and capable to stay a bit extra to help ease up the workload for tomorrow, are more than welcome to do so."
    mrf "I will make sure to compensate for any extra hours in your next paycheck."
    show mrf smirk at Position(xpos=1000)
    show cor confused_talk at Position(xpos=1300)
    cor "Come on, Schnookums, you know I only feel comfortable leaving when I know you are also out of the office."
    show pov confused at left
    show cor confused at Position(xpos=1300)
    show glo neutral at Position(xpos=1600)
    show kan neutral_talk at Position(xpos=1800)
    kan "I’ll have to call home to let them know I'll be late tonight, but I totally can."
    show pov neutral at left
    show mrf confused at Position(xpos=1000)
    show glo neutral_talk at Position(xpos=1600)
    show kan neutral at Position(xpos=1800)
    glo "Oh, it’s gonna be a girls night tonight, then!"
    show pov embarrassed at left
    show mrf bored at Position(xpos=1000)
    show cor smirk at Position(xpos=1300)
    show glo smirk_talk at Position(xpos=1600)
    show kan smirk at Position(xpos=1800)
    glo "With the exception of the manager, of course."
    show pov embarrassed_talk at left
    show mrf confused at Position(xpos=1000)
    show glo smirk at Position(xpos=1600)
    pov "Need me to stay and help out, Sir?"
    show pov embarrassed at left
    show mrf bored_talk at Position(xpos=1000)
    mrf "No need, kid. Your internship contract doesn’t allow extra hours, remember?"
    show pov embarrassed_talk at left
    show mrf confused at Position(xpos=1000)
    show cor embarrassed at Position(xpos=1300)
    pov "Well yeah, but it’s unpaid anyway, so why care to keep track of them?"
    show pov embarrassed at left
    show mrf bored_talk at Position(xpos=1000)
    show cor shocked at Position(xpos=1300)
    show glo confused at Position(xpos=1600)
    show kan embarrassed at Position(xpos=1800)
    mrf "Heh, keep that attitude and you are definitely going places. Just be careful not to get taken advantage of because of that."
    mrf "Still, the ladies and I have it under control for now."
    show pov confused_talk at left
    show mrf smirk at Position(xpos=1000)
    show cor neutral at Position(xpos=1300)
    pov "What about the guys?"
    show pov confused at left
    show glo embarrassed at Position(xpos=1600)
    show kan embarrassed_talk at Position(xpos=1800)
    kan "We decided that the guys would take over the extra hours on the weekend and we ladies will take the ones today and on friday."
    show pov shocked at left
    show cor embarrassed at Position(xpos=1300)
    show kan confused_talk at Position(xpos=1800)
    kan "It’s a bit of a short notice thing so they at least were kind enough to give us the weekend."
    show pov bored at left
    show mrf neutral at Position(xpos=1000)
    show cor neutral at Position(xpos=1300)
    show kan neutral_talk at Position(xpos=1800)
    kan "Still though, it's sweet of you to want to help out, but you’ve done more than enough for today."
    show glo neutral_talk at Position(xpos=1600)
    show kan neutral at Position(xpos=1800)
    glo "Yeah, we used to have to do all the stuff you do ourselves. And since you are here, that’s taken a lot of weight off our shoulders. So just focus on keeping that up."
    show pov embarrassed_talk at left
    show glo neutral at Position(xpos=1600)
    pov "Alright, if all of you are sure."
    show pov embarrassed at left
    show mrf neutral_talk at Position(xpos=1000)
    mrf "We are, kid."
    show pov shocked at left
    show mrf smirk_talk at Position(xpos=1000)
    show cor confused at Position(xpos=1300)
    show glo shocked at Position(xpos=1600)
    show kan confused at Position(xpos=1800)
    mrf "Now get out of here, and don’t keep that girl waiting for you, downstairs in the lobby."
    show mrf smirk at Position(xpos=1000)
    show kan confused_talk at Position(xpos=1800)
    kan "What?"
    show pov confused at left
    show cor shocked_talk at Position(xpos=1300)
    show kan confused at Position(xpos=1800)
    cor "What?!"
    show cor shocked at Position(xpos=1300)
    show glo shocked_talk at Position(xpos=1600)
    show kan shocked at Position(xpos=1800)
    glo "WHAT?!"
    show pov embarrassed_talk at left
    show glo confused at Position(xpos=1600)
    show kan confused at Position(xpos=1800)
    pov "U-Uh…"
    show pov confused_talk at left
    pov "I-I don’t know what you are talking about. What lady?"
    show pov confused at left
    show mrf smirk_talk at Position(xpos=1000)
    mrf "Hehehe, don’t think you can fool this old man, kid."
    mrf "I definitely saw you texting a chick when you came in for work."
    show mrf neutral_talk at Position(xpos=1000)
    mrf "And if she is willing to wait for you until you finish your shift, you shouldn’t keep her waiting."
    show mrf neutral at Position(xpos=1000)
    show cor smirk_talk at Position(xpos=1300)
    show kan shocked at Position(xpos=1800)
    cor "My my! Who knew our little intern was this smooth~"
    show cor shocked at Position(xpos=1300)
    show glo shocked_talk at Position(xpos=1600)
    show kan confused at Position(xpos=1800)
    glo "No way! How could I let such a tasteful piece of gossip slip by me!"
    show glo smirk_talk at Position(xpos=1600)
    glo "I’m the best when it comes to detecting romances among coworkers, why wasn’t I informed of this?!"
    show pov confused at left
    show glo embarrassed at Position(xpos=1600)
    show kan shocked_talk at Position(xpos=1800)
    kan "My word, what am I gonna tell Luna?"
    show pov embarrassed_talk at left
    show mrf smirk at Position(xpos=1000)
    show cor smirk at Position(xpos=1300)
    show kan shocked at Position(xpos=1800)
    pov "Y-You got the wrong idea, it’s nothing like that!"
    pov "I uh… J-Just planned to meet up with a friend after work!"
    show pov embarrassed at left
    show mrf smirk_talk at Position(xpos=1000)
    mrf "Sure you did, kiddo. In the middle of the night and they agree to wait out in the lobby?"
    mrf "I completely understand."
    show mrf neutral_talk at Position(xpos=1000)
    show cor neutral at Position(xpos=1300)
    show glo smirk at Position(xpos=1600)
    mrf "Heh, I agreed to meet with quite a lot of “friends” like that in my youth, you know?"
    show mrf smirk at Position(xpos=1000)
    show cor smirk_talk at Position(xpos=1300)
    cor "Oh, you don’t say, Honey Buns?"
    show cor bored_talk at Position(xpos=1300)
    show glo embarrassed at Position(xpos=1600)
    show kan bored at Position(xpos=1800)
    cor "How about you tell me all about that while we head to your office… ALONE…"
    show mrf embarrassed_talk at Position(xpos=1000)
    show cor bored at Position(xpos=1300)
    mrf "U-Uh, yeah! You know, it was just the guys who wanted to do an extra hour of practice or needed to do other masculine and totally not sexual stuff, Nothing like that!"
    show mrf embarrassed at Position(xpos=1000)
    show cor bored_talk at Position(xpos=1300)
    cor "As if I’ll believe such a thing!"
    show mrf neutral at Position(xpos=1000)
    show cor confused at Position(xpos=1300)
    show glo smirk_talk at Position(xpos=1600)
    glo "Say boss, I just remembered I forgot something in the lobby last time I went down, so is it okay if I go fetch it real quick?~"
    show pov confused at left
    show glo neutral at Position(xpos=1600)
    show kan bored_talk at Position(xpos=1800)
    kan "I just want to see this girl who apparently caught the boys interest. No one’s better than my Luna!"
    show pov embarrassed at left
    show cor bored_talk at Position(xpos=1300)
    show kan bored at Position(xpos=1800)
    cor "Alright, alright. Settle down, you two."
    cor "If the kiddo is saying things aren’t like that, we shouldn’t gossip, and take their word for it."
    show pov confused at left
    show cor confused at Position(xpos=1300)
    show glo confused at Position(xpos=1600)
    show kan bored_talk at Position(xpos=1800)
    kan "Are you just saying that so we drop the subject, and you can drag the manager into the office and force him to keep telling you what he was talking about just now?"
    show pov bored at left
    show mrf smirk at Position(xpos=1000)
    show cor smirk_talk at Position(xpos=1300)
    show kan bored at Position(xpos=1800)
    cor "Don’t be silly, we have far too much work for that."
    show mrf smirk_talk at Position(xpos=1000)
    show cor smirk at Position(xpos=1300)
    mrf "Right, let's not get ahead of ourselv-"
    show mrf shocked at Position(xpos=1000)
    show cor bored_talk at Position(xpos=1300)
    show glo embarrassed at Position(xpos=1600)
    cor "Plus, I don’t have the paddle on hand at the moment, so his questioning will resume on Monday once we have more time on our hands."
    show pov confused at left
    show mrf bored_talk at Position(xpos=1000)
    show cor bored at Position(xpos=1300)
    mrf "Ah shit…"
    show pov embarrassed_talk at left
    show mrf confused at Position(xpos=1000)
    pov "Well, you guys definitely look busy, so…"
    show pov embarrassed at left
    show cor neutral_talk at Position(xpos=1300)
    show glo neutral at Position(xpos=1600)
    cor "Have a safe trip home. And tell your friend to come say hi next time, I’m sure Kanako and Gloria would Love to talk to them~"
    show cor embarrassed at Position(xpos=1300)
    show glo smirk_talk at Position(xpos=1600)
    glo "I still can’t believe this gossip just slipped past me like that!"
    show mrf confused at Position(xpos=1000)
    show cor bored at Position(xpos=1300)
    show glo embarrassed at Position(xpos=1600)
    show kan bored_talk at Position(xpos=1800)
    kan "Luna is still prettier…"
    show pov neutral_talk at left
    show cor neutral at Position(xpos=1300)
    show glo neutral at Position(xpos=1600)
    show kan bored at Position(xpos=1800)
    pov "Alright, OK. See you tomorrow!"

    #-Scene fades to black to indicate scene transition-

    #=SCENE END=

    $ officejobs_complete = 0
    $ officejobs_copymachine = 0
    $ officejobs_coffeerun = 0
    $ officejobs_emailproofread = 0

    $ gtime = 2
    $ main_story = 104

    scene black with fade
    jump lbl_meeting_with_eloise

    #=SCENE ENDS=
