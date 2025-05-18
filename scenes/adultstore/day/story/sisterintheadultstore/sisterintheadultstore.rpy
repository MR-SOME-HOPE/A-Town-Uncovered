
label lbl_sister_in_the_adultstore:
    if winc == 0:
        jump lbl_sister_in_the_adultstore_winc0

    scene bg adultstore_day
    show btn adultstore_day_hazel_idle
    with fade
    show pov confused at left
    with dissolve
    pov "{i}Where the hell is she? I can't see her anywhere.{/i}"
    show pov confused_talk at left
    hide btn adultstore_day_hazel_idle
    show haz shocked at right
    with dissolve
    call lbl_adultstore_counter_check
    pov "Hey, Hazel. Have you seen a girl that sorta kinda but doesn't really look like me come in here?"
    show pov confused at left
    show haz confused_talk at right
    haz "Sorry, hot stuff, but I don't give out customer details unless you're an enforcer of the law. Company policy."
    show pov confused_talk at left
    show haz embarrassed at right
    pov "C'mon, it's me. Don't act like a stranger to me, Hazel."
    show pov embarrassed_talk at left
    pov "I'm not asking for details, I'm just asking if you know where the girl that just came in is?"
    show pov confused_talk at left
    show haz shocked at right
    pov "Do you know, [sister]?"
    show pov bored at left
    show haz embarrassed_talk at right
    haz "Again, it's part of company policy to not give out any form of information on our customers to the general public."
    show pov bored_talk at left
    show haz embarrassed at right
    pov "{i}*Sigh*{/i} Fine, thanks. Maybe I'm just imagining things, I definitely don't see her around."
    $ sister_path = 18

    jump lbl_adultstore_day_setup

label lbl_sister_in_the_adultstore_2:

    scene bg adultstore_day
    show btn adultstore_day_hazel_idle
    with hpunch
    $ renpy.pause()
    scene bg sisterintheadultstore_1
    with fade
    pov "[sister]!"
    show bg sisterintheadultstore_2
    haz "Oh my God! Are you okay, [sister]?"
    show bg sisterintheadultstore_1
    pov "What the hell are you doing back here?!"
    pov "Hazel, what is she doing he- do you guys know each other!?"
    show bg sisterintheadultstore_2
    haz "You see, the thing is-"
    show bg sisterintheadultstore_1
    pov "Why did you run inside when you saw me-?"
    pov "Do you work here?!"
    show bg sisterintheadultstore_3
    sis "What?! No... I-"
    sis "Yes! Fine, you caught me! You found my BIG secret!"
    sis "Go on, [povname]. Make fun of me, I deserve it don't I?"
    show bg sisterintheadultstore_4
    sis "Look at my fucking situation. I'm on the floor swimming in a hundred dicks."
    sis "Go on, just say what you wanna say."
    show bg sisterintheadultstore_5

    menu:
        "Stay silent":
            pov "..."
            show bg sisterintheadultstore_3
            sis "Nothing to say, [povname]? I bet that's not what's going on in that head of yours."
        "I'm not going to make fun of you.":
            pov "I'm not going to make fun of you."
            show bg sisterintheadultstore_3
            sis "Right, let's see how that goes when you get butthurt by me."
        "I've heard of a ball-pit...":
            pov "I've heard of a ball-pit, now I know where the dicks went."
            show bg sisterintheadultstore_3
            sis "Don't make me laugh, [povname]. I'm really embarrassed right fucking now."
        "If you told me that you're working here...":
            pov "If you told me that you're working here, I'd think you were out of your mind."
            show bg sisterintheadultstore_3
            sis "Yeah... thanks, [povname]. No matter what I do, I'm always the crazy, stupid one."
    show bg sisterintheadultstore_2
    haz "I'm gonna leave you two and go... clean over... uh- there."
    show bg sisterintheadultstore_5
    sis "..."
    show bg sisterintheadultstore_3
    sis "Get in here and close the door."

    scene bg sisterintheadultstore_0
    with fade
    show pov shocked at left
    with dissolve
    show sis sad_talk at right
    with dissolve
    sis "I'm sorry you had to see me like that..."
    show pov sad at left
    sis "You probably think I'm some sad life with no other options."

    menu:
        "Yeah, you are.":
            show pov confused_talk at left
            show sis sad at right
            pov "Yeah, you are. Out of all things, an adult store?"
            show pov sad_talk at left
            show sis angry at right
            pov "Aren't you ashamed?"
            show pov sad at left
            show sis angry_talk at right
            sis "You're actually asking if I'm ashamed of hiding this from you, or anyone for that matter?"
        "A little, but hey, that's life.":
            show pov embarrassed_talk at left
            show sis sad at right
            pov "A little, but hey, that's life. You do what you gotta do, a job's a job. A hustle is a hustle."
            show pov sad_talk at left
            pov "Weren't there any other options in the mall? I got a job at the mall."
            show pov sad at left
            show sis sad_talk at right
            sis "Again, you're the lucky one. There was no one hiring at the time of my search..."
            show sis sad_talk at right
            sis "...and you just came in and snatched yourself a job with a click of your fingers."
        "Not in the slightest bit at all.":
            show pov embarrassed_talk at left
            show sis embarrassed at right
            pov "Not in the slightest bit at all, [sister]. I see this as any other niche retail store."
            show pov confused_talk at left
            show sis sad at right
            pov "Why does it ever matter what the store sells, it's a job. Someone needs to do it."
            show pov embarrassed at left
            show sis sad_talk at right
            sis "I know that, but obviously that's not how everyone thinks. They always look at you on a surface level and judge you by what you do."
    show pov sad at left
    show sis sad at right
    pov "..."
    show pov embarrassed_talk at left
    show sis sad at right
    pov "Don't you want to look for a replacement job?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "I would... if this job wasn't paying way more than the jobs at the mall."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "How much are they paying you to sell sex toys?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Well, that's the thing that I should clarify to you..."
    show sis embarrassed at right
    pov "...?"
    sis "{i}*Inhale*{/i}"
    show sis embarrassed_talk at right
    sis "I don't exactly... {i}sell{/i} products."
    show sis sad_talk at right
    sis "I- uh..."
    sis "Erm..."
    show sis embarrassed_talk at right
    sis "Well, it's no point trying to keep hiding this from you. You already know where I work."
    sis "I'm uh... *mumbles* sxtytstr..."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "... What?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "I'm uh... *mumbles* sxtuy teztr..."
    show pov bored_talk at left
    show sis sad at right
    pov "Can you fucking spit it out."
    show pov shocked at left
    show sis sad_talk at right
    sis "I'm a sex toy tester!"
    show sis sad at right
    pov ".."
    pov "..."
    pov "...."
    show pov shocked_talk at left
    pov "I'm- I'm sorry, but you can't be serious."
    show pov embarrassed_talk at left
    pov "You're pulling my fuckin' leg, aren't you? This is one of your little prank-"
    show pov sad_talk at left
    pov "[sister], seriously?"
    show pov shocked at left
    show sis embarrassed_talk at right
    sis "It feels a lot better..."
    show sis embarrassed at right
    pov "..."
    show pov bored at left
    show sis embarrassed_talk at right
    sis "Getting it off my chest."
    show pov sad_talk at left
    show sis embarrassed at right
    pov "I- I'm speechless. My sister is a sex toy tester. I have no idea what to think."
    show pov embarrassed_talk at left
    pov "Good for you?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "I know it's not something that 99.9 percent of guys say but I'm fine, really."
    show pov embarrassed at left
    sis "I applied for this job, I knew what I'm getting myself into."
    sis "I'm not gonna lie, I like my job."
    show sis sad at right
    sis "I was just-"
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "Embarrassed?"
    show pov embarrassed at left
    show sis sad_talk at right
    sis "Yeah."
    sis "I was embarrassed with myself for liking a job that is deemed shameful to most people."
    sis "And it's definitely still embarrassing for me that you now know of it."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "Do Mom and Dad know about it?"
    show pov shocked at left
    show sis embarrassed_talk at right
    sis "Mom... knows of it."
    show pov shocked_talk at left
    show sis embarrassed at right
    pov "She does?!"
    show pov shocked at left
    show sis embarrassed_talk at right
    sis "Yeah, she was against it at first as MOST parents would be but y'know."
    sis "I've gotta start living my life as my own person and do what I need or want to do."
    show pov embarrassed at left
    sis "She told me that as long as I'm not flaunting my job title around like a medal or something, then she'll back me up."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "And what about Dad?"
    show pov confused at left
    show sis confused_talk at right
    sis "As long as I'm making money, that's all he cares about. But no, he doesn't know exactly what it is that I do. He still thinks I work in the mall."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "No wonder you were acting so weird when I tried to find out where in the mall you worked."
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Haha.. yeah."
    show sis sad_talk at right
    sis "I- I'm sure you have a lot going through your mind right now."
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "I sorta do but, I think what you told me just now is enough right now."
    pov "I should get out of your hair."
    show pov embarrassed at left
    sis "..."
    show pov embarrassed_talk at left
    show sis shocked at right
    pov "Oh, [sister]?"
    show pov embarrassed at left
    show sis sad at right
    sis "Mhmm?"
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "Don't worry about me, I won't tease you about this, or tell anyone about this."
    pov "You do you and do what makes you happy."

    menu:
        "I love you.":
            pov "I love you."
            show pov embarrassed at left
            show sis embarrassed_talk at right
            if sister_points >= 6:
                sis "I love you too, [povname]."
            else:
                sis "Thanks, [povname]."
        "See you around.":
            pov "See you around."
            show pov embarrassed_talk at left
            show sis embarrassed at right
            sis "See you a-square."
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Oh, actually-"
    show pov confused at left
    show sis embarrassed at right
    pov "Hmm?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Do you wanna head to the club next door and drink together?"
    show pov confused_talk at left
    show sis confused at right
    pov "Isn't that illegal?"
    show pov bored at left
    show sis smirk_talk at right
    sis "Because we're underaged? Tch, a-duh!"
    show pov bored_talk at left
    show sis bored at right
    pov "What if we get caught?"
    show pov shocked at left
    show sis bored_talk at right
    sis "Bitch, don't be a bitch, bitch. We won't get caught. I drink there all the time."
    show pov shocked_talk at left
    show sis neutral at right
    pov "You do?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "It's a convenient location for me to chill after work."
    show pov embarrassed at left
    sis "Plus, I may or may not have made a close friendship with the bartender there."
    show pov shocked_talk at left
    show sis smirk at right
    pov "You do? How?"
    show pov bored_talk at left
    pov "Everytime I try to ask him for a sneaky drink, he refuses me."
    show sis bored at right
    pov "That's sexist."
    show pov bored at left
    show sis bored_talk at right
    sis "It's not sexist, you just have a baby-face."
    show sis neutral_talk at right
    sis "He'll be totally cool with it."
    show pov confused at left
    show sis neutral at right
    pov "..."
    show pov embarrassed_talk at left
    show sis bored at right
    pov "{i}A close friendship{/i}?"
    show pov embarrassed at left
    show sis angry_talk at right
    sis "Don't say it like that, [povname]. I'm not a fucking slut, we're just legit close friends. No benefits."
    show pov embarrassed_talk at left
    show sis angry at right
    pov "I mean, not that it matters to me..."

    menu:
        "I accept.":
            show sis neutral at right
            pov "I accept your invitation."
            show pov embarrassed at left
            show sis embarrassed_talk at right
            sis "Great! Hehe, it'll really ease the uh- tension between us."
            show pov embarrassed at left
            show sis sad_talk at right
            sis "Or at least it'll help me get through the night and forget about my embarrassing accident here."
        "Raincheck?":
            show sis embarrassed at right
            pov "Raincheck on that, maybe another time?"
            show pov embarrassed at left
            show sis embarrassed_talk at right
            sis "Oh, sure. Yeah. We can go drinking another time."
            sis "I'll head on over there later either way... I still need to drown my embarrassment in liquor."
            sis "Stop by if you want."
    show sis embarrassed_talk
    sis "See you a-square, [povname]."

    scene black
    with fade

    scene bg adultstore_day
    with fade
    $ sister_path = 19
    $ townmap_enabled = 1

    jump lbl_adultstore_day_setup

label lbl_sister_in_the_adultstore_winc0:

    scene bg adultstore_day
    show btn adultstore_day_hazel_idle
    with fade
    show pov confused at left
    with dissolve
    pov "{i}Where the hell is she? I can't see her anywhere.{/i}"
    show pov confused_talk at left
    hide btn adultstore_day_hazel_idle
    show haz shocked at right
    with dissolve
    call lbl_adultstore_counter_check
    pov "Hey, Hazel. Have you seen a girl that sorta kinda but doesn't really look like me come in here?"
    show pov confused at left
    show haz confused_talk at right
    haz "Sorry, hot stuff, but I don't give out customer details unless you're an enforcer of the law. Company policy."
    show pov confused_talk at left
    show haz embarrassed at right
    pov "C'mon, it's me. Don't act like a stranger to me, Hazel."
    show pov embarrassed_talk at left
    pov "I'm not asking for details, I'm just asking if you know where the girl that just came in is?"
    show pov confused_talk at left
    show haz shocked at right
    pov "Do you know, [sister]?"
    show pov bored at left
    show haz embarrassed_talk at right
    haz "Again, it's part of company policy to not give out any form of information on our customers to the general public."
    show pov bored_talk at left
    show haz embarrassed at right
    pov "{i}*Sigh*{/i} Fine, thanks. Maybe I'm just imagining things, I definitely don't see her around."
    $ sister_path = 18

    jump lbl_adultstore_day_setup

label lbl_sister_in_the_adultstore_2_winc0:

    scene bg adultstore_day
    with hpunch
    $ renpy.pause()
    show bg sisterintheadultstore_1
    with fade
    pov "[sister]!"
    show bg sisterintheadultstore_2
    haz "Oh my God! Are you okay, [sister]?"
    show bg sisterintheadultstore_1
    pov "What the hell are you doing back here?!"
    pov "Hazel, what is she doing he- do you guys know each other!?"
    show bg sisterintheadultstore_2
    haz "You see, the thing is-"
    show bg sisterintheadultstore_1
    pov "Why did you run inside when you saw me-?"
    pov "Do you work here?!"
    show bg sisterintheadultstore_3
    sis "What?! No... I-"
    sis "Yes! Fine, you caught me! You found my BIG secret!"
    sis "Go on, [povname]. Make fun of me, I deserve it don't I?"
    show bg sisterintheadultstore_4
    sis "Look at my fucking situation. I'm on the floor swimming in a hundred dicks."
    sis "Go on, just say what you wanna say."
    show bg sisterintheadultstore_5

    menu:
        "Stay silent":
            pov "..."
            show bg sisterintheadultstore_3
            sis "Nothing to say, [povname]? I bet that's not what's going on in that head of yours."
        "I'm not going to make fun of you.":
            pov "I'm not going to make fun of you."
            show bg sisterintheadultstore_3
            sis "Right, let's see how that goes when you get butthurt by me."
        "I've heard of a ball-pit...":
            pov "I've heard of a ball-pit, now I know where the dicks went."
            show bg sisterintheadultstore_3
            sis "Don't make me laugh, [povname]. I'm really embarrassed right fucking now."
        "If you told me that you're working here...":
            pov "If you told me that you're working here, I'd think you were out of your mind."
            show bg sisterintheadultstore_3
            sis "Yeah... thanks, [povname]. No matter what I do, I'm always the crazy, stupid one."
    show bg sisterintheadultstore_2
    haz "I'm gonna leave you two and go... clean over... uh- there."
    show bg sisterintheadultstore_5
    sis "..."
    show bg sisterintheadultstore_3
    sis "Get in here and close the door."

    scene bg sisterintheadultstore_0
    with fade
    show pov shocked at left
    with dissolve
    show sis sad_talk at right
    with dissolve
    sis "I'm sorry you had to see me like that..."
    show pov sad at left
    sis "You probably think I'm some sad life with no other options."

    menu:
        "Yeah, you are.":
            show pov confused_talk at left
            show sis sad at right
            pov "Yeah, you are. Out of all things, an adult store?"
            show pov sad_talk at left
            show sis angry at right
            pov "Aren't you ashamed?"
            show pov sad at left
            show sis angry_talk at right
            sis "You're actually asking if I'm ashamed of hiding this from you, or anyone for that matter?"
        "A little, but hey, that's life.":
            show pov embarrassed_talk at left
            show sis sad at right
            pov "A little, but hey, that's life. You do what you gotta do, a job's a job. A hustle is a hustle."
            show pov sad_talk at left
            pov "Weren't there any other options in the mall? I got a job at the mall."
            show pov sad at left
            show sis sad_talk at right
            sis "Again, you're the lucky one. There was no one hiring at the time of my search..."
            show sis sad_talk at right
            sis "...and you just came in and snatched yourself a job with a click of your fingers."
        "Not in the slightest bit at all.":
            show pov embarrassed_talk at left
            show sis embarrassed at right
            pov "Not in the slightest bit at all, [sister]. I see this as any other niche retail store."
            show pov confused_talk at left
            show sis sad at right
            pov "Why does it ever matter what the store sells, it's a job. Someone needs to do it."
            show pov embarrassed at left
            show sis sad_talk at right
            sis "I know that, but obviously that's not how everyone thinks. They always look at you on a surface level and judge you by what you do."
    show pov sad at left
    show sis sad at right
    pov "..."
    show pov embarrassed_talk at left
    show sis sad at right
    pov "Don't you want to look for a replacement job?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "I would... if this job wasn't paying way more than the jobs at the mall."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "How much are they paying you to sell sex toys?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Well, that's the thing that I should clarify to you..."
    show sis embarrassed at right
    pov "...?"
    sis "{i}*Inhale*{/i}"
    show sis embarrassed_talk at right
    sis "I don't exactly... {i}sell{/i} products."
    show sis sad_talk at right
    sis "I- uh..."
    sis "Erm..."
    show sis embarrassed_talk at right
    sis "Well, it's no point trying to keep hiding this from you. You already know where I work."
    sis "I'm uh... *mumbles* sxtytstr..."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "... What?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "I'm uh... *mumbles* sxtuy teztr..."
    show pov bored_talk at left
    show sis sad at right
    pov "Can you fucking spit it out."
    show pov shocked at left
    show sis sad_talk at right
    sis "I'm a sex toy tester!"
    show sis sad at right
    pov ".."
    pov "..."
    pov "...."
    show pov shocked_talk at left
    pov "I'm- I'm sorry, but you can't be serious."
    show pov embarrassed_talk at left
    pov "You're pulling my fuckin' leg, aren't you? This is one of your little prank-"
    show pov sad_talk at left
    pov "[sister], seriously?"
    show pov shocked at left
    show sis embarrassed_talk at right
    sis "It feels a lot better..."
    show sis embarrassed at right
    pov "..."
    show pov bored at left
    show sis embarrassed_talk at right
    sis "Getting it off my chest."
    show pov sad_talk at left
    show sis embarrassed at right
    pov "I- I'm speechless. My [sisrole] is a sex toy tester. I have no idea what to think."
    show pov embarrassed_talk at left
    pov "Good for you?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "I know it's not something that 99.9 percent of guys say but I'm fine, really."
    show pov embarrassed at left
    sis "I applied for this job, I knew what I'm getting myself into."
    sis "I'm not gonna lie, I like my job."
    show sis sad at right
    sis "I was just-"
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "Embarrassed?"
    show pov embarrassed at left
    show sis sad_talk at right
    sis "Yeah."
    sis "I was embarrassed with myself for liking a job that is deemed shameful to most people."
    sis "And it's definitely still embarrassing for me that you now know of it."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "Does [missus] and [dadname] know of it?"
    show pov shocked at left
    show sis embarrassed_talk at right
    sis "[missus]... knows of it."
    show pov shocked_talk at left
    show sis embarrassed at right
    pov "She does?!"
    show pov shocked at left
    show sis embarrassed_talk at right
    sis "Yeah, she was against it at first as MOST parents would be but y'know."
    sis "I've gotta start living my life as my own person and do what I need or want to do."
    show pov embarrassed at left
    sis "She told me that as long as I'm not flaunting my job title around like a medal or something, then she'll back me up."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "And what about [dadname]?"
    show pov confused at left
    show sis confused_talk at right
    sis "As long as I'm making money, that's all he cares about. But no, he doesn't know exactly what it is that I do. He still thinks I work in the mall."
    show pov confused_talk at left
    show sis embarrassed at right
    pov "No wonder you were acting so weird when I tried to find out where in the mall you worked."
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Haha.. yeah."
    show sis sad_talk at right
    sis "I- I'm sure you have a lot going through your mind right now."
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "I sorta do but, I think what you told me just now is enough right now."
    pov "I should get out of your hair."
    show pov embarrassed at left
    sis "..."
    show pov embarrassed_talk at left
    show sis shocked at right
    pov "Oh, [sister]?"
    show pov embarrassed at left
    show sis sad at right
    sis "Mhmm?"
    show pov embarrassed_talk at left
    show sis embarrassed at right
    pov "Don't worry about me, I won't tease you about this, or tell anyone about this."
    pov "You do you and do what makes you happy."

    menu:
        "I love you.":
            pov "I love you."
            show pov embarrassed at left
            show sis embarrassed_talk at right
            if sister_points >= 6:
                sis "I love you too, [povname]."
            else:
                sis "Thanks, [povname]."
        "See you around.":
            pov "See you around."
            show pov embarrassed_talk at left
            show sis embarrassed at right
            sis "See you a-square."
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Oh, actually-"
    show pov confused at left
    show sis embarrassed at right
    pov "Hmm?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Do you wanna head to the club next door and drink together?"
    show pov confused_talk at left
    show sis confused at right
    pov "Isn't that illegal?"
    show pov bored at left
    show sis smirk_talk at right
    sis "Because we're underaged? Tch, a-duh!"
    show pov bored_talk at left
    show sis bored at right
    pov "What if we get caught?"
    show pov shocked at left
    show sis bored_talk at right
    sis "Bitch, don't be a bitch, bitch. We won't get caught. I drink there all the time."
    show pov shocked_talk at left
    show sis neutral at right
    pov "You do?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "It's a convenient location for me to chill after work."
    show pov embarrassed at left
    sis "Plus, I may or may not have made a close friendship with the bartender there."
    show pov shocked_talk at left
    show sis smirk at right
    pov "You do? How?"
    show pov bored_talk at left
    pov "Everytime I try to ask him for a sneaky drink, he refuses me."
    show sis bored at right
    pov "That's sexist."
    show pov bored at left
    show sis bored_talk at right
    sis "It's not sexist, you just have a baby-face."
    show sis neutral_talk at right
    sis "He'll be totally cool with it."
    show pov confused at left
    show sis neutral at right
    pov "..."
    show pov embarrassed_talk at left
    show sis bored at right
    pov "{i}A close friendship{/i}?"
    show pov embarrassed at left
    show sis angry_talk at right
    sis "Don't say it like that, [povname]. I'm not a fucking slut, we're just legit close friends. No benefits."
    show pov embarrassed_talk at left
    show sis angry at right
    pov "I mean, not that it matters to me..."

    menu:
        "I accept.":
            show sis neutral at right
            pov "I accept your invitation."
            show pov embarrassed at left
            show sis embarrassed_talk at right
            sis "Great! Hehe, it'll really ease the uh- tension between us."
            show pov embarrassed at left
            show sis sad_talk at right
            sis "Or at least it'll help me get through the night and forget about my embarrassing accident here."
        "Raincheck?":
            show sis embarrassed at right
            pov "Raincheck on that, maybe another time?"
            show pov embarrassed at left
            show sis embarrassed_talk at right
            sis "Oh, sure. Yeah. We can go drinking another time."
            sis "I'll head on over there later either way... I still need to drown my embarrassment in liquor."
            sis "Stop by if you want."
    show sis embarrassed_talk
    sis "See you a-square, [povname]."

    scene black
    with fade

    scene bg adultstore_day
    with fade
    $ sister_path = 19
    $ townmap_enabled = 1

    jump lbl_adultstore_day_setup
