## The Mother Obstacle
label lbl_the_mother_obstacle:
    default themotherobstacle_complain = 0

    scene bg myhallway_day
    with dissolve
    ## Sprite Start
    show pov confused at left
    with dissolve
    show mumt sad_talk at right
    with dissolve

    #"you head up the stairs trying your best to run to your room only to meet Mum on the way coming out of the bathroom with a towel around her"

    mum "Honey? Are you alright?"
    show pov confused at left
    show mumt confused_talk at right
    mum "I heard some of the ruckus as you were coming up the stairs, are you constipated again?"
    show pov sad at left
    show mumt embarrassed_talk at right
    mum "I can get you the medicine if you want, I just finished my shower."

    menu:
        "I am not constipated!":
            show pov angry_talk at left
            show mumt shocked at right
            pov "F-For the last time, I am not constipated!"
            pov "I just had a very long day and need to rest for a bit. Is that so much to ask nowadays, or what?!"
        "Yes!":
            show pov sad_talk at left
            show mumt sad at right
            pov "Yes! Please!"
            show pov embarrassed at left
            show mumt embarrassed_talk at right
            mum "Alright, hang on a secon-"
            show pov embarrassed_talk at left
            show mumt confused_talk at right
            pov "I’m joking! I’m not constipated. Why doesn’t anyone get my joke?"
            pov "Ahahahaha!"
    show pov sad at left
    show mumt shocked_talk at right
    mum "Oh my God, honey, you are shaking!"
    mum "It looks as if you’ve seen a ghost or something!"
    show pov embarrassed_talk at left
    show mumt shocked at right
    pov "I-I’m fine!"
    show pov neutral_talk at left
    show mumt sad at right
    pov "Just took the long way home and decided to run harder than normal so I am a little winded."
    show pov embarrassed_talk at left
    show mumt sad at right
    pov "Nothing weird going on."
    show pov embarrassed at left
    show mumt sad_talk at right
    mum "Come on, [povname], you know you can tell me anything."
    show pov shocked at left
    show mumt sad_talk at right
    mum "Was someone mean and teased you about the whole… “Public Nudity” thing?"
    show pov embarrassed at left
    show mumt embarrassed_talk at right
    mum "Oh no-"
    mum "Did they laugh at your pictures..?"
    show pov shocked_talk at left
    show mumt confused at right
    pov "You know about the pictures?!"
    show pov shocked at left
    show mumt confused_talk at right
    mum "Well, of course."
    show pov embarrassed at left
    show mumt embarrassed_talk at right
    mum "Director Lashley and [sister] informed me of their existence."
    mum "It’s one of the main reasons that I’ve been all over you lately."
    show pov sad at left
    show mumt sad_talk at right
    mum "You must be so stressed about that!"
    show pov embarrassed_talk at left
    show mumt embarrassed at right
    pov "Don’t tell me you have seen them too!"
    show pov embarrassed at left
    show mumt embarrassed_talk at right
    if winc == 0:
        mum "W-Well, I’m your [mumrole], after all. I need to see the severity of what’s being thrown on the interwebs."
    else:
        mum "W-Well, I’m your mother, after all. I need to see the severity of what’s being thrown on the interwebs."
    mum "I needed to assess the damage so I could take proper action with your administration and everything"
    if mum_path >= 29 and mum_points >= 8:

        mum "Totally don’t have them saved in my phone, or anything like that."
        show pov embarrassed at left
        show mumt smirk_talk at right
        mum "It’s not like I use them for those nights we are too busy to have some fun, or anything."
        mum "Hehe… He."
        show pov embarrassed_talk at left
        show mumt smirk at right
        pov "Um."
        show pov embarrassed at left
        show mumt smirk_talk at right
        mum "Besides, why care for pictures when I have the actual trophy under the same roof, right?"

        ## CG Scene Start

        scene bg themotherobstacle_1
        with fade

        #"Mum goes ahead and cups a feel of your groin-"

        if winc == 0:
            pov "N-Nice to see you too, [missus]."
        else:
            pov "N-Nice to see you too, mom."
        mum "Hmm?"
        mum "Oh! S-Sorry [povname]!"

        #"she snaps out of her daze and removes her hand from your groin"
        show bg themotherobstacle_2
        mum "I-I’ve just been feeling, a little bit in the mood for you lately."
        mum "Think we can schedule something for this week?"

        #"your natural urges overcoming your increasing fear, you soon find yourself in a bit of a daze as well"
        show bg themotherobstacle_3
        pov "I-I am sure we can schedule something out."
        show bg themotherobstacle_4
        mum "That sounds great! Thank you, dear~"
        show bg themotherobstacle_5
        mum "Anyway, back on topic!"
        scene bg myhallway_day
        with dissolve

    ## Dissolve back to background
    ## Sprite start same as above
    show pov embarrassed at left
    show mumt sad_talk at right
    mum "[povname], if someone is giving you a hard time or anything, I am sure we can help you solve it."
    show pov embarrassed_talk at left
    show mumt sad at right
    if winc == 0:
        pov "No one is bothering me, [missus]."
    else:
        pov "No one is bothering me, [missus]."
    show pov sad_talk at left
    show mumt sad at right
    pov "I-I’ve just had a very long day and I am in the mood to relax on my own for a bit."
    show pov sad at left
    show mumt shocked_talk at right
    mum "You say that, but you’re actually scaring me, [povname]."
    show pov sad at left
    show mumt sad_talk at right
    mum "Is there anything going on that you are not telling me?"
    show pov embarrassed_talk at left
    show mumt sad at right
    pov "N-Nothing! It’s just-"

    if skill_int >= 12:
        $ themotherobstacle_complain = 1

        pov "I’ve just had a long day; with everyone laughing behind my back. And then being outed to the administrator’s office in front of the whole class."
        show pov angry_talk at left
        show mumt shocked at right
        pov "And for what? For her to tell me that they want to monitor me 24-7."
        show pov bored_talk at left
        show mumt sad at right
        pov "I really just want to sleep all the bad vibes off and maybe forget thing whole thing ever happened, is that weird of me to ask?!"
        show pov bored at left
        show mumt shocked_talk at right
        mum "So you WERE being harassed about this…"
        show pov angry_talk at left
        show mumt shocked at right
        if winc == 1:
            pov "Moooom!"
        else:
            pov "[missus]!"
        show pov embarrassed at left
        show mumt angry_talk at right
        mum "I can speak to the administration tomorrow; have them all stop-"
        show pov embarrassed_talk at left
        show mumt shocked at right
        pov "D-Don’t!"
        show pov embarrassed at left
        show mumt angry_talk at right
        mum "Why not?"
        mum "I don’t want this to start affecting your mental health, [povname]..."
        show pov sad_talk at left
        show mumt sad at right
        pov "I-It won’t, if I don’t pay attention to it they will eventually stop, right?"
        pov "They’ll get bored and eventually move on to something else."
        show pov bored_talk at left
        show mumt shocked at right
        pov "If you go in and show them that all of this is affecting me and bringing a reaction out of me, then it will only get harder to deal with."
        show pov bored at left
        show mumt shocked_talk at right
        mum "I-I guess I can see the logic in that."
        show pov embarrassed_talk at left
        show mumt embarrassed at right
        if winc == 0:
            pov "Plus, I’ll be known as the boy who went home and cried for his [mumrole]."
        else:
            pov "Plus, I’ll be known as the boy who went home and cried for his mommy."
        pov "Doing that at my age is social suicide and it will lead to way worse bullying."
        show pov neutral at left
        show mumt sad_talk at right
        mum "A-Alright…"
        show pov embarrassed at left
        show mumt angry_talk at right
        mum "But I still don’t like it!"
        show pov neutral_talk at left
        show mumt sad at right
        if winc == 0:
            pov "I-It’s alright, [missus]!"
        else:
            pov "I-It’s alright, [missus]!"
        show pov sad_talk at left
        show mumt sad at right
        pov "You didn’t raise me to let words get under my skin, just like that, anyhow."
        show pov neutral_talk at left
        show mumt sad at right
        pov "Sticks and stones and all that jazz, right?"
        show pov neutral at left
        show mumt sad_talk at right
        mum "I-I guess I did, but-"
        show pov embarrassed_talk at left
        show mumt sad at right
        pov "I am perfectly fine, really!"
        pov "I’ll be back in shape in no time, honest!"
        show pov neutral_talk at left
        show mumt sad at right
        pov "Nothing a night of sleep can’t fix."
        show pov embarrassed at left
        show mumt sad_talk at right
        mum "Okay, but I’ll totally understand if you need a few days off school, I-I can let your administration know and-"
        show pov embarrassed_talk at left
        show mumt sad at right
        pov "L-Let’s see how I feel after a nap, alright?"
        pov "I really need to rest my head, right about now."
        pov "I feel fine, I promise!"
        show pov neutral at left
        show mumt sad_talk at right
        mum "O-Okay, I’ll trust you…"
        show pov neutral_talk at left
        show mumt neutral at right
        if winc == 0:
            pov "Thanks, [missus], I appreciate it."
        else:
            pov "Thanks, [missus], I appreciate it."
        pov "See you in a bit!"
        show pov shocked at left
        show mumt shocked_talk at right
        mum "Ah, [povname] wait!"
        show pov neutral_talk at left
        show mumt embarrassed at right
        pov "Yeah?"

    else:
        show pov bored_talk at left
        show mumt sad at right
        pov "I-I just have been through a lot lately."
        pov "I need some time alone and to organize some thoughts in my head and all…"
        show pov angry_talk at left
        show mumt angry at right
        pov "I am really not in the mood to have people digging on my back asking questions."
        show pov embarrassed at left
        show mumt shocked_talk at right
        mum "I can’t help but to ask them, [povname]!"
        mum "You came home, white as a corpse, sweating like you just ran a marathon, and with your legs shaking as if they were made of jello!"
        show pov neutral at left
        show mumt angry_talk at right
        if winc == 0:
            mum "What [mumrole] in their right mind wouldn’t be concerned if they saw their [povmumrole] like that?!"
        else:
            mum "What mother in their right mind wouldn’t be concerned if they saw their son like that?!"
        mum "Hell, what would you be doing if I was the one in your shoes?"
        show pov embarrassed_talk at left
        show mumt sad at right
        pov "I-"
        show pov embarrassed at left
        show mumt sad_talk at right
        mum "Look, I know you are really stressed and on the defensive right now, so I’ll likely won’t get anything out of you."
        mum "But I want you to know that as soon as you feel rested enough, you are going to come straight to me and give me an honest answer as to what is going on."
        show pov embarrassed at left
        show mumt angry_talk at right
        mum "I think I’ve done more than enough for you through the years, to at the very least be in my right, to ask such a thing from you."
        show pov embarrassed_talk at left
        show mumt angry at right
        pov "But I-"
        show pov embarrassed at left
        show mumt angry_talk at right
        mum "No buts, mister!"
        mum "It’s the least you can do for me since I let you stay under my roof and eat my food."
        show pov neutral at left
        show mumt neutral_talk at right
        mum "So when you are ready, we are going to sit down on the living room with a giant tub of ice cream on each other’s laps and we are going to talk about this like adults."
        show pov smirk_talk at left
        show mumt bored at right
        pov "Heheh- Adults talk about their problems with ice cream on their lap?"
        show pov neutral at left
        show mumt bored_talk at right
        mum "Not the point I want you to take from this, [povname]."
        mum "Now, did I made myself clear?"
        show pov neutral_talk at left
        show mumt bored at right
        pov "Y-"
        show pov shocked at left
        show mumt angry_talk at right
        mum "Did I make myself clear?"
        show pov embarrassed at left
        show mumt angry at right
        pov "…"
        show pov embarrassed_talk at left
        show mumt neutral at right
        pov "Yeah, you did."
        show pov neutral at left
        show mumt neutral_talk at right
        mum "Good!"
        show pov neutral at left
        show mumt sad_talk at right
        mum "Now head to bed and have some rest, okay?"
        mum "I’ll make sure you aren’t bothered until it’s time to eat."
        show pov neutral_talk at left
        show mumt neutral at right
        if winc == 0:
            pov "Thanks, [missus]."
        else:
            pov "Thanks, mom."
        show pov neutral at left
        show mumt sad_talk at right
        mum "Never a problem, sweetie."
        show pov neutral at left
        show mumt sad at right
        mum "Oh, and [povname]?"
        show pov neutral_talk at left
        show mumt embarrassed at right
        pov "Yeah?"
    show pov embarrassed at left
    show mumt neutral_talk at right
    mum "I just wanted to remind you that I love you."
    show pov sad at left
    show mumt sad_talk at right
    mum "And whatever it is you are going through, I am sure we can find a solution together."
    show pov neutral at left
    show mumt neutral_talk at right
    mum "So just keep your head up for me, okay?"
    mum "You’ll find the answer."
    show pov neutral at left
    show mumt smirk_talk at right
    mum "You are [povname], after all."
    mum "You’ve climbed higher obstacles than this."
    show pov embarrassed at left
    show mumt embarrassed at right
    pov "…"
    show pov embarrassed_talk at left
    show mumt neutral at right
    pov "Y-Yeah."
    show pov neutral_talk at left
    show mumt neutral at right
    if winc == 0:
        pov "Thanks, [missus], I needed to hear that."
    else:
        pov "Thanks, [missus], I needed to hear that."
    show pov neutral at left
    show mumt neutral_talk at right
    mum "Always a pleasure to lift your spirits, honey!"

    if mum_path >= 29 and mum_points >= 7:
        show pov embarrassed at left
        show mumt embarrassed_talk at right
        mum "Besides, you got a… ‘mature’... lady like me to feel both; sexy for her age, and like a teenager all over again."
        show pov smirk at left
        show mumt smirk_talk at right
        mum "If you can do that, then what’s the limit of what you can do?"
        show pov neutral at left
        show mumt neutral_talk at right
        mum "You are a terrific person who can achieve anything he sets his mind to."
        mum "Nothing is impossible for you, so please believe in yourself the same way I believe in you, alright?"
        show pov neutral at left
        show mumt embarrassed_talk at right
        mum "I love you with everything I have and I am sure you can beat whatever is eating you up."
        show pov embarrassed_talk at left
        show mumt sad at right
        if winc == 0:
            pov "I don’t deserve your love. You are just too much, [missus]."
        else:
            pov "I don’t deserve your love. You are just too much, [missus]."
        show pov neutral at left
        show mumt neutral_talk at right
        mum "You deserve all the happiness as the next person, [povname]."
        show pov neutral at left
        show mumt smirk at right
        mum "Oh, and before you go-"

        ## CG Scene Start

        #"Mum looks around to make sure no one else is looking before opening up her towel to let you look at her wet and naked body-"
        scene bg themotherobstacle_7
        with fade
        $ hardpause(1.5)
        show bg themotherobstacle_6
        $ hardpause(0.5)
        show bg themotherobstacle_7
        $ hardpause(0.5)
        show bg themotherobstacle_8
        $ hardpause(0.5)
        show bg themotherobstacle_9
        $ hardpause(0.5)
        mum "I am always here to help you out if you need to de-stress~"
        show bg themotherobstacle_8
        pov "I, um, uh-"

        #"you are clearly in a daze over the sudden hot naked lady in front of you-"
        show bg themotherobstacle_9
        mum "Hehehe, good to know I can still take your breath away, just like that~"
        show bg themotherobstacle_10
        pov "Y-You have quite the talent to do it."
        show bg themotherobstacle_11
        mum "Seeing as how high you are pitching a tent over there, I can clearly see that I do~"
        show bg themotherobstacle_12
        mum "And I mean what I said: anytime you want or are feeling way too stressed, just call me over, and I’ll be sure to show you how to get rid of that pent up stress in a proper, healthy way."

        if mum_points >= 9:
            show bg themotherobstacle_13
            mum "And just because it’s you, I’ll let you go as rough as you want~"
        show bg themotherobstacle_11
        pov "I- Uhm-"
        show bg themotherobstacle_15
        if winc == 0:
            pov "T-thanks for the reminder, [missus], I’ll keep it in mind."
        else:
            pov "T-thanks for the reminder, [missus], I’ll keep it in mind."

        #"Mom leans in to kiss you for a bit, letting you relax and lean into it before breaking away"
        show bg themotherobstacle_16
        mum "Hopefully this will give you more pleasant dreams~"
        scene bg myhallway_day
        with dissolve

    show pov neutral at left
    show mumt embarrassed_talk at right
    mum "I love you, [povname]. Always remember that."
    show pov embarrassed at left
    show mumt embarrassed at right
    pov "…"
    show pov embarrassed_talk at left
    show mumt neutral at right
    if winc == 0:
        pov "I could never forget, [missus]."
    else:
        pov "I could never forget, [missus]."
    show pov neutral_talk at left
    show mumt neutral at right
    pov "I love you too."

    $ main_story = 48

    jump lbl_you_can_freak_out_now
