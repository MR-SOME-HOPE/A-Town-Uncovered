## Mom at the Park ##
label lbl_mom_at_the_park:
    #default momattheparkbj_counter = 0
    default momhasdonebj = 0

    scene bg momatthepark_5
    with fade
    if winc == 0:
        pov "[missus]? What are you doing here?"
    else:
        pov "Mom? What are you doing here?"
    show bg momatthepark_6
    mum "Come sit with me, [povname]."
    show bg momatthepark_7
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg momatthepark_1
    with dissolve
    $ renpy.pause()
    mum "I knew you'd come find me here."
    show bg momatthepark_3
    pov "Of course I'd come find you, you weren't home and I got worried about you."
    mum "You really did keep your word."
    pov "About what?"
    mum "That you'd always be there for me."
    pov "..."

    menu:
        "I did say that I wouldn't leave you alone.":
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ renpy.notify("Your relationship with Mom has increased")
            pov "I did say that I wouldn't leave you alone."
            pov "Now you're stuck with me."
            mum "Hehehe, I honestly don't mind one single bit."
            show bg momatthepark_4
            mum "Not that I'm clingy or anything."
            show bg momatthepark_2
            pov "You are a little clingy."
            show bg momatthepark_1
            mum "Fine, I am clingy but only because I'm scared to watch my baby grow out of my arms."
            show bg momatthepark_3
            pov "I'll be your baby for as long as you call me that."
            mum "You can bet on that with everything you have."
        "I was just worried about you.":
            pov "I was just, y'know, worried about you."
            pov "You don't usually come out here by yourself. Maybe the mall, but definitely not the park at night."
            pov "Don't you think it's a little dangerous out here?"
            mum "It's fine, [povname]. You worry too much."
            mum "I just thought that..."
            mum "I don't know..."
            show bg momatthepark_1
            mum "I just had this intense urge to come out here tonight and enjoy the sparkle of the moonlight on the water."
            show bg momatthepark_3
            pov "When did you become such a poet?"
            show bg momatthepark_4
            mum "Oh, c'mon. You never had these random urges to just sit and think?"
            show bg momatthepark_3
            mum "You kids and your stupid phones."
            mum "Your generation is doomed when you're out somewhere and you can't use your phone."
            show bg momatthepark_1
            mum "You need to learn and appreciate the idea of just... doing absolutely nothing."
            mum "Your mind is so crammed full of, excuse my french, ‘dog poop' and meaningless online relationships."
            mum "You aren't living a human life if you can't sit and be bored, let your mind explore for itself."
            mum "Only eureka moments happen in a time when you aren't distracted by someone else's ideas."
            pov "..."
            if winc == 0:
                pov "Damn, [missus]."
            else:
                pov "Damn, Mom."
            pov "Where did that come from?"
            mum "As I said, once you just sit and do nothing, that's when the deepest and most meaningful realizations come to you."
            show bg momatthepark_3
            pov "I'll... I'll keep that in mind."
            show bg momatthepark_2
            mum "With that being said, I still find how jaw-dropping your ability to work technology is to me."
            show bg momatthepark_1
            mum "If only it came so easily to me."
            pov "We all have our strengths and weaknesses."
        "Are you just testing me?":
            pov "Are you testing me?"
            mum "What if I said I was? What would you do?"
            pov "..."
            mum "Is that another test question."
            mum "..."
            mum "What if I said I was? What would you do?"
            pov "..."
            show bg momatthepark_1
            pov "Please don't break me."
            show bg momatthepark_2
            mum "Hahaha, you're adorable, honey."
            mum "Or am I just saying that to test your response to affirmative treatment."
            show bg momatthepark_4
            if winc == 0:
                pov "I'm not your labrat, [missus]."
            else:
                pov "I'm not your labrat, Mom."
            if mum_points >= 8:
                show bg momatthepark_3
                mum "You'd totally wanna be my labrat and let me do all sorts of things to you."
                pov "..."
                show bg momatthepark_4
                mum "Cat got your tongue? Or should I say, pussy on your mind?"
                show bg momatthepark_2
                pov "Uh-"
                show bg momatthepark_1
                mum "I said it once, and I'll say it again; you're so adorable, honey."
            else:
                show bg momatthepark_3
                mum "Alright, alright. I'll stop with the teasing."
                show bg momatthepark_1
                pov "Thank you."
                mum "My other labrat would roll with the punches though. That's the type of labrat that would make it to the next round."
                show bg momatthepark_2
                if winc == 0:
                    pov "[missus]."
                else:
                    pov "Mom."
                show bg momatthepark_4
                mum "I'm joking! Jokes, just kidding. Don't talk to me in such an adorable tone."
    show bg momatthepark_3
    pov "Seriously though. Why are you here?"
    mum "..."
    if mum_points <= 7:
        show bg momatthepark_4
        mum "It... it doesn't matter."
        show bg momatthepark_3
        mum "I don't really know why I'm out here."
        show bg momatthepark_4
        mum "Thanks for coming out here to get me, let's go home."
        show bg momatthepark_3
        pov "You sure? We can just sit here and rela-"
        show bg momatthepark_4
        mum "No, I'm sure. It's pretty chilly and I might catch a cold if I stay out here any longer."
        show bg momatthepark_3
        if winc == 0:
            pov "Alright, [missus]. Let's get you home then."
        else:
            pov "Alright, Mom. Let's get you home then."
        $ mum_path = 22
        $ gtime = 3
        scene black
        with fade
        $ renpy.pause()
        scene bg myhousefront_night
        with fade

        jump lbl_myhousefront_night_setup
    else:
        pass
    mum "I..."
    mum "I wanted to be alone."
    pov "Alone?"
    show bg momatthepark_4
    mum "Heh.. yeah? Stupid, isn't it?"
    show bg momatthepark_3
    mum "After having complain and cause tension between us because of that."
    mum "For some reason, I just, wanted to be alone again."
    mum "After you took me out to the movies the other night. Something just... clicked."
    mum "I didn't feel alone anymore. And even if I was alone, I knew you'd come back to me."
    mum "You being here next to me, without me leaving a trace or a clue on where I am proves that to me."
    mum "I know I can only daydream that you'd stay home forever and be there with me as we grow older but you have your own life to live."
    if winc == 0:
        mum "I'm just your [mumrole]. My job is to raise you into a good man."
    else:
        mum "I'm just your mother. My job is to raise you into a good man."
    show bg momatthepark_4
    mum "I think I can safely say that I did my job well."
    if winc == 0:
        pov "You were, and still are, and amazing [mumrole]. The best one that [sister] and I could have ever asked for."
    else:
        pov "You were, and still are, and amazing mother. The best one that [sister] and I could have ever asked for."
    show bg momatthepark_3
    mum "{i}*Sniff*{/i}"
    pov "Are you..."
    mum "Hmm? No, I'm fine. It's just happy tears. Nothing but happiness in me."
    show bg momatthepark_3
    mum "I'm so proud of you, [povname]."
    mum "I know you'll be there for me when I need you, even at great distance."
    mum "Always remember that I'll be there for you, always. Period."
    mum "Nothing but a bad back or dementia will stop me from being there for you when you need me."
    show bg momatthepark_2
    if winc == 0:
        pov "Hehe, you're not at that age yet, Mom. Far from it."
    else:
        pov "Hehe, you're not at that age yet, [missus]. Far from it."
    show bg momatthepark_1
    mum "I know, I do hope so. Middle age really is a pain in all sorts of my body."
    show bg momatthepark_3
    if winc == 0:
        pov "But thanks, Mom. I can always count on you to keep me in line."
    else:
        pov "But thanks, [missus]. I can always count on you to keep me in line."
    show bg momatthepark_1
    pov "..."

    menu:
        "I'm going to miss you.":
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ renpy.notify("Your relationship with Mom has increased")
            show bg momatthepark_3
            pov "I really am going to miss you."
            mum "Oh, please, [povname]. Don't say that tonight. You're going to make me ball with tears."
            show bg momatthepark_1
            pov "Sorry."
            show bg momatthepark_2
            mum "And never. Ever apologise for showing your true feelings."
            show bg momatthepark_4
            mum "The world needs more men like you."
            show bg momatthepark_3
            mum "You may think it's weakness but women appreciates a man with a heart."
            show bg momatthepark_1
            pov "It's- it's still a little weird how you're referring to me as a ‘man' instead of a boy."
            show bg momatthepark_2
            if winc == 0:
                mum "You're responsible, you make your own money, hardworking, mature, big, protective of me and your [sisrole]."
            else:
                mum "You're responsible, you make your own money, hardworking, mature, big, protective of me and your sister."
            show bg momatthepark_4
            mum "I'd say that's a clear indication of a man in my books."
            show bg momatthepark_3
            if winc == 0:
                pov "Thanks, [missus]... but did you mean by ‘big'?"
            else:
                pov "Thanks, mom... but did you mean by ‘big'?"
            show bg momatthepark_4
            mum "Oh, you know exactly what I mean, honey."

            jump lbl_mom_at_the_park_bj
        "I'm afraid to leave you.":
            if skill_cha >= 8:
                if mum_points <= 8:
                    $ mum_points += 2
                else:
                    $ mum_points = 10
                $ skill_cha -= 4
                if winc == 0:
                    $ renpy.notify("You used 4 Charisma Points\nYour relationship with [missus] has increased by 2")
                else:
                    $ renpy.notify("You used 4 Charisma Points\nYour relationship with Mom has increased by 2")
            else:
                pass
            show bg momatthepark_3
            pov "After have grown much closer to you since we moved into this town. I'm so afraid to leave you when I graduate."
            mum "Don't."
            mum "Don't even think about the future now, honey."
            mum "Keep your mind on a leash tonight and just be in the present."
            mum "Enjoy what we have tonight."
            mum "Because once you know it, in a blink of an eye. You've moved onto a new chapter in your life."
            if winc == 0:
                mum "[dadrole]s don't lie when they say that their [povdadrole]s grow up so fast."
            else:
                mum "Parents don't lie when they say that their kids grow up so fast."
            mum "I still look in the mirror and wonder who that woman is looking back."
            mum "What I have engrained in my mind is the 20 year old me. 20 year old me doesn't recognise middle age me."
            show bg momatthepark_1
            pov "You know, a wise, lovely, amazingly beautiful, youthful, woman once told me to ‘be in the present'."
            mum "..."
            show bg momatthepark_2
            mum "Who is this woman, where can I find her and will you help me hide her body?"
            show bg momatthepark_3
            pov "Hahahaha!"
            show bg momatthepark_4
            mum "You can't just hit me with a doopsie doo like that, [povname]."
            show bg momatthepark_3
            mum "I'm teaching you about life."
            if winc == 0:
                pov "I'm listening, [missus]. I love hearing your voice."
            else:
                pov "I'm listening, Mom. I love hearing your voice."
            show bg momatthepark_4
            mum "You love my voice? I've always thought it sounded ‘out of body'. Like it doesn't fit with my appearance."
            pov "No, I can't imagine a more fitting person to embody that angelic voice of yours."
            mum "Well, aren't you a cheeseball son of a-"
            pov "Ah ah ahhh. Language."
            show bg momatthepark_4
            mum "I was 18 years old once, y'know. I know how to cuss like a real mother fucker."
            show bg momatthepark_3
            if winc == 0:
                pov "Jeez, [missus]! Dropping the ‘F' bomb all of a sudden?"
            else:
                pov "Jeez, Mom! Dropping the ‘F' bomb all of a sudden?"
            show bg momatthepark_1
            with hpunch
            mum "MOTHER FUCKER!!!!"
            show bg momatthepark_3
            if winc == 0:
                pov "Alright, [missus]. Not too loud..."
            else:
                pov "Alright, Mom. Not too loud..."
            show bg momatthepark_4
            mum "Yeah, that's right, mother fucker. You know how I know you're the real mother fucker?"
            pov "How's that?"
            mum "Exactly as described."

            jump lbl_mom_at_the_park_bj
        "We should get home and keep warm.":
            pov "It's definitely cold out tonight, we should get home before we get sick just sitting here."
            show bg momatthepark_2
            mum "You want to go already?"
            pov "Preferably."
            mum "Don't you wanna sit here with me for a little longer?"
            if mum_points >= 8:
                mum "I can make something else a little longer."

            menu:
                "Convince me.":
                    if skill_cha >= 15:
                        if mum_points <= 7:
                            $ mum_points += 3
                        else:
                            $ mum_points = 10
                        $ skill_cha -= 7
                        if winc == 0:
                            $ renpy.notify("You used 7 Charisma Points\nYour relationship with [missus] has increased by 3")
                        else:
                            $ renpy.notify("You used 7 Charisma Points\nYour relationship with Mom has increased by 3")
                    else:
                        if mum_points <= 9:
                            $ mum_points += 1
                        else:
                            $ mum_points = 10
                        if winc == 0:
                            $ renpy.notify("Your relationship with [missus] has increased")
                        else:
                            $ renpy.notify("Your relationship with Mom has increased")
                    show bg momatthepark_4
                    if winc == 0:
                        pov "Convince me how much you want me to stay,[missus]."
                    else:
                        pov "Convince me how much you want me to stay, Mom."
                    mum "Ooh, you're so naughty. So rebellious, and downright a pain-in-the-neck. I like it."
                    mum "I'll try my hardest then."

                    jump lbl_mom_at_the_park_bj
                "I insist that we should go.":
                    if mum_points >= 1:
                        $ mum_points -= 1
                    else:
                        $ mum_points = 0
                    if winc == 0:
                        $ renpy.notify("Your relationship with [missus] has decreased")
                    else:
                        $ renpy.notify("Your relationship with Mom has decreased")
                    show bg momatthepark_4
                    pov "I insist that we should go, I don't like being at the park at night."
                    if mum_points >= 8:
                        pov "Someone might see us."
                        mum "Wouldn't that make it so much hotter?"
                        if winc == 0:
                            pov "[missus]..."
                        else:
                            pov "Mom..."
                    show bg momatthepark_3
                    mum "{i}*Sigh*{/i} Alright, let's go, Mr Party-pooper."
                    $ mum_path = 22
                    $ gtime = 3
                    scene black
                    with fade
                    $ renpy.pause()
                    scene bg myhousefront_night
                    with fade

                    jump lbl_myhousefront_night_setup

label lbl_mom_at_the_park_bj:
    $ momhasdonebj = 1

    scene bg momattheparkbj_1
    with fade
    mum "You'll have to release it all in my mouth, we can't make a mess out here."
    mum "We also have to be quick in case someone {i}does{/i} come."
    show bg momattheparkbj_2
    pov "In case {i}I{/i} cum?"
    show bg momattheparkbj_3
    mum "Hush up."

label lbl_mom_at_the_park_bj_0:
    ##$ momattheparkbj_counter = 0
    #$ skill_sta = 8#TEMP TEST


label lbl_mom_at_the_park_bj_1:
    #$ momattheparkbj_counter += 1
    #show bg momattheparkbj_4
    #$ renpy.pause(0.3,hard=True)
    #show bg momattheparkbj_5
    #$ renpy.pause(0.1,hard=True)
    #show bg momattheparkbj_6
    #$ renpy.pause(0.1,hard=True)
    #show bg momattheparkbj_7
    #$ renpy.pause(0.2,hard=True)
    #show bg momattheparkbj_8
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and momattheparkbj_counter == 4:
    #    jump lbl_mom_at_the_park_bj_cum
    #elif skill_sta <= 14 and momattheparkbj_counter == 6:
    #    jump lbl_mom_at_the_park_bj_2
    #elif skill_sta <= 20 and momattheparkbj_counter == 8:
    #    jump lbl_mom_at_the_park_bj_2
    #else:
    #    jump lbl_mom_at_the_park_bj_1
    scene img_mom_at_the_park_bj_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_at_the_park_bj_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_at_the_park_bj_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_at_the_park_bj_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_at_the_park_bj_1

image img_mom_at_the_park_bj_1:
    "bg momattheparkbj_4"
    pause 0.3
    "bg momattheparkbj_5"
    pause 0.1
    "bg momattheparkbj_6"
    pause 0.1
    "bg momattheparkbj_7"
    pause 0.2
    "bg momattheparkbj_8"
    pause 0.2
    repeat

label lbl_mom_at_the_park_bj_2:
    #$ momattheparkbj_counter += 1
    #show bg momattheparkbj_4
    #$ renpy.pause(0.3,hard=True)
    #show bg momattheparkbj_6
    #$ renpy.pause(0.1,hard=True)
    #show bg momattheparkbj_7
    #$ renpy.pause(0.2,hard=True)
    #show bg momattheparkbj_8
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and momattheparkbj_counter == 14:
    #    jump lbl_mom_at_the_park_bj_cum
    #elif skill_sta <= 20 and momattheparkbj_counter == 16:
    #    jump lbl_mom_at_the_park_bj_3
    #else:
    #    jump lbl_mom_at_the_park_bj_2
    scene img_mom_at_the_park_bj_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mom_at_the_park_bj_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_at_the_park_bj_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_at_the_park_bj_2
image img_mom_at_the_park_bj_2:
    "bg momattheparkbj_4"
    pause 0.3
    "bg momattheparkbj_6"
    pause 0.1
    "bg momattheparkbj_7"
    pause 0.2
    "bg momattheparkbj_8"
    pause 0.2
    repeat

label lbl_mom_at_the_park_bj_3:
    #$ momattheparkbj_counter += 1
    #show bg momattheparkbj_4
    #$ renpy.pause(0.2,hard=True)
    #show bg momattheparkbj_6
    #$ renpy.pause(0.1,hard=True)
    #show bg momattheparkbj_8
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and momattheparkbj_counter == 24:
    #    jump lbl_mom_at_the_park_bj_cum
    #else:
    #    jump lbl_mom_at_the_park_bj_3
    scene img_mom_at_the_park_bj_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mom_at_the_park_bj_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mom_at_the_park_bj_3
image img_mom_at_the_park_bj_3:
    "bg momattheparkbj_4"
    pause 0.2
    "bg momattheparkbj_6"
    pause 0.1
    "bg momattheparkbj_8"
    pause 0.2
    repeat

label lbl_mom_at_the_park_bj_cum:
    call screen scr_mom_at_the_park_bj_cum

screen scr_mom_at_the_park_bj_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_at_the_park_bj_0")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mom_at_the_park_bj_cumming")
    else:
        pass

label lbl_mom_at_the_park_bj_cumming:
    scene bg momattheparkbj_4
    $ renpy.pause(0.3,hard=True)
    show bg momattheparkbj_6
    $ renpy.pause(0.1,hard=True)
    show bg momattheparkbj_7
    $ renpy.pause(2,hard=True)
    show bg momattheparkbj_9
    $ renpy.pause(1,hard=True)
    show bg momattheparkbj_10
    $ renpy.pause(1,hard=True)
    show bg momattheparkbj_11
    $ renpy.pause(1,hard=True)
    show bg momattheparkbj_12
    $ renpy.pause(1.5,hard=True)
    show bg momattheparkbj_13
    $ renpy.pause(1,hard=True)
    show bg momattheparkbj_14
    mum "You big baby. You nearly drowned me."
    if winc == 0:
        pov "Sorry, [missus]. Your mouth was asking for it."
    else:
        pov "Sorry, Mom. Your mouth was asking for it."
    show bg momattheparkbj_15
    mum "I know, I did this to myself..."
    $ mum_path = 22
    $ gtime = 3

    scene black
    with fade
    $ renpy.pause()

    scene bg mybedroom_night
    with fade

    jump lbl_mybedroom_night_setup
