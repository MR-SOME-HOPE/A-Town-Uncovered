## Fort Destroyed ##
label lbl_fort_destroyed:
    default fortdestroyed_engage = 1

    scene bg fortdestroyed_1
    with hpunch

    menu:
        "Dad!" if winc == 1:
            show bg fortdestroyed_2
            pov "Dad, what are you doing?!"
        "What the fuck?!":
            show bg fortdestroyed_2
            pov "What the fuck is going on here?!"
        "You fucking asshole!":
            show bg fortdestroyed_2
            pov "You fucking asshole! What is wrong with you?!"
    show bg fortdestroyed_3
    if winc == 1:
        dad "You and your sister need to fucking grow up!"
    else:
        dad "You and your [sisrole] need to fucking grow up!"
    dad "Playing with castles and daydreaming your life away!"
    show bg fortdestroyed_2
    pov "You're a fucking piece of shit!"
    show bg fortdestroyed_3
    dad "Like I haven't heard that one before."

    menu:
        "Knock him out":
            show bg fortdestroyed_4
            $ renpy.pause(1,hard=True)
            show bg fortdestroyed_5
            $ renpy.pause(0.6,hard=True)
            if skill_str >= 14:
                $ skill_str -= 8
                $ renpy.notify("You used 8 Strength Points")
                show bg fortdestroyed_6
                with hpunch
                $ renpy.pause()
                show bg fortdestroyed_7
                $ renpy.pause(1,hard=True)
                show bg fortdestroyed_8
            else:
                if skill_str >= 6:
                    $ skill_str -= 6
                else:
                    $ skill_str = 0
                $ renpy.notify("You weren't strong enough and his counter cost you 6 Strength Points")
                show bg fortdestroyed_6
                with hpunch
                $ renpy.pause()
                show bg fortdestroyed_9
                $ renpy.pause()
                dad "You weak piece of-"
                show bg fortdestroyed_10
                with hpunch
                dad "I can't fucking believe that you fucking did th-"
                show bg fortdestroyed_10
                with hpunch
        "Dont engage":
            $ fortdestroyed_engage = 0
            show bg fortdestroyed_4
            pov "..."
            pov "...."
            pov "....."
            if winc == 1:
                dad "You and your sister are a goddamn waste of time."
            else:
                dad "You and your [sisrole] are a goddamn waste of time."
            show bg fortdestroyed_4
            with hpunch
    mum "What in holy fucking hell going on down here?!"

    scene bg mybasement_lightsonwreck
    with fade
    show pov angry at left
    with dissolve
    show mum angry_talk flip at Position(xpos=650)
    with dissolve
    show dad angry at right
    with dissolve
    mum "You all are waking up the entire neighbourhood!"
    mum "Why is [sister] crying her eyes out?!"
    mum "What a mess! What the hell are you two doing?!"
    show pov angry_talk at left
    show mum angry flip at Position(xpos=650)
    pov "This mother fucker is-"
    show pov angry at left
    show mum angry_talk flip at Position(xpos=650)
    mum "Hey! Watch your mouth!"
    show pov angry_talk at left
    show mum angry flip at Position(xpos=650)
    if winc == 1:
        pov "I don't fucking care, Mom! Dad ruined our fucking fort!"
    else:
        pov "I don't fucking care, [missus]! [dadname] ruined our fucking fort!"
    show pov angry at left
    show dad angry_talk at right
    if winc == 1:
        dad "Are you aware that our kids are using our basement for their childish bullshit?!"
    else:
        dad "Are you aware that our [povdadrole]s are using our basement for their childish bullshit?!"
    show mum angry_talk flip at Position(xpos=650)
    show dad angry at right
    mum "It's their fort!"
    show pov angry_talk at left
    show mum angry flip at Position(xpos=650)
    pov "It's our fucking fort!"
    show pov angry at left
    show dad angry_talk at right
    dad "Don't tell me you're siding with him!"
    show mum angry_talk flip at Position(xpos=650)
    show dad angry at right
    mum "You destroyed their fort! Didn't you?"
    show pov shocked at left
    show mum shocked flip at Position(xpos=650)
    show dad angry_talk at right
    dad "I'm doing them a favour."
    show pov angry_talk at left
    show mum angry flip at Position(xpos=650)
    show dad angry at right
    pov "You're ruining our lives, dickhead!"
    show pov angry_talk at left
    show mum shocked flip at Position(xpos=650)
    pov "Everything's better when you're not here!"
    show pov angry at left
    show mum angry flip at Position(xpos=650)
    show dad angry_talk at right
    dad "Things are better when I'm away from you disappointing piece of-"
    show mum angry_talk flip at Position(xpos=650)
    show dad angry at right
    mum "STOP! YELLING!"
    mum "You two are driving me insane and I'm pretty sure the fucking neighbours are calling the police right now!"
    show pov shocked at left
    mum "[povname], shut up for a second."
    show pov smirk at left
    show dad shocked at right
    mum "You, get the fuck out of my house."
    show pov angry at left
    mum "You act like a fucking drunk even when you're sober."
    mum "It's fucking disgraceful."
    show pov smirk at left
    show mum angry flip at Position(xpos=650)
    show dad angry_talk at right
    dad "You're kicking me out of MY house?!"
    show pov angry at left
    show mum angry_talk flip at Position(xpos=650)
    show dad angry at right
    mum "We're supposed to be a family, it's OUR house."
    show mum angry flip at Position(xpos=650)
    show dad shocked at right
    if winc == 1:
        mum "And because you're scaring me and the kids, I want you out."
    else:
        mum "And because you're scaring me and the [povdadrole]s, I want you out."
    show mum angry flip at Position(xpos=650)
    show dad shocked_talk at right
    dad "W-"
    show mum angry_talk flip at Position(xpos=650)
    show dad shocked at right
    mum "And not another fucking word, mister."
    show dad angry at right
    mum "You have been nothing but a jerk ever since we moved here."
    mum "I don't even know who you are anymore."
    show mum sad_talk flip at Position(xpos=650)
    mum "The old you that I know would never have done this."
    show mum sad flip at Position(xpos=650)
    dad "..."
    show pov shocked at left
    show mum sad_talk flip at Position(xpos=650)
    show dad shocked at right
    mum "Just get out already."
    show mum sad flip at Position(xpos=650)
    show dad angry at right
    dad "..."
    hide dad angry
    hide mum sad flip
    pov "..."
    show pov embarrassed_talk at left
    show mum sad at right
    with dissolve
    if winc == 1:
        pov "Thanks for having my back, Mom."
    else:
        pov "Thanks for having my back, [missus]."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "Don't even mention it, honey."
    show mum angry_talk at right
    mum "That man has gone too far..."
    show mum sad_talk at right
    mum "I better go talk to [sister]."

    menu:
        "I'll go talk to her.":
            show pov sad_talk at left
            show mum sad at right
            pov "I'll go talk-"
        "Alright, it's best if you do it.":
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Alright, it's bes-"
    show sis shocked flip at Position(xpos=650)
    with dissolve
    show pov shocked at left
    show mum shocked at right
    sis "..."
    show pov sad at left
    show sis shocked flip at Position(xpos=650)
    show mum sad_talk at right
    mum "Oh, hey, honey. Are you okay?"
    show mum sad at right
    sis "..."
    show mum sad_talk at right
    mum "I'm.. really sorry about what that asshole did to your box castle."

    menu:
        "It's a fort, Mom." if winc == 1:
            show pov sad_talk at left
            show sis sad flip at Position(xpos=650)
            show mum sad at right
            pov "It's a fort, Mom."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "Fort, sorry."
            show mum sad at right
            sis "..."
            if mum_points >= 1:
                $ mum_points -= 1
            else:
                $ mum_points = 0
            if sister_points <= 9:
                $ sister_points += 1
            else:
                $ sister_points = 10
            $ renpy.notify("Your relationship with [sister] has increased\nYour relationship with Mom has decreased")
        "It's a fort, [missus]." if winc == 0:
            show pov sad_talk at left
            show sis sad flip at Position(xpos=650)
            show mum sad at right
            pov "It's a fort, [missus]."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "Fort, sorry."
            show mum sad at right
            sis "..."
            if mum_points >= 1:
                $ mum_points -= 1
            else:
                $ mum_points = 0
            if sister_points <= 9:
                $ sister_points += 1
            else:
                $ sister_points = 10
            $ renpy.notify("Your relationship with [sister] has increased\nYour relationship with [missus] has decreased")
        "Stay silent":
            show sis sad flip at Position(xpos=650)
            show mum sad at right
            pov "..."
            sis "Mm..."

    scene bg fortdestroyed_sis_0
    with fade
    show bg fortdestroyed_sis_1
    $ renpy.pause(1,hard=True)
    show bg fortdestroyed_sis_2
    $ renpy.pause(0.7,hard=True)
    show bg fortdestroyed_sis_3
    $ renpy.pause(1,hard=True)
    show bg fortdestroyed_sis_4
    with vpunch
    $ renpy.pause(2,hard=True)
    show bg fortdestroyed_sis_5
    $ renpy.pause(2,hard=True)
    show bg fortdestroyed_sis_6
    $ renpy.pause(2,hard=True)
    show bg fortdestroyed_sis_7
    with fade
    $ renpy.pause(1,hard=True)

    menu:
        "Cuddle with her":
            show bg fortdestroyed_sis_8
            with fade
            $ renpy.pause()
            mum "I- I'll... be upstairs if you need to talk, honey. I love you."
        "Tell Mom to give you alone time" if winc == 1:
            pov "Mom, could you... give us some alone time?"
            pov "Maybe I can talk to [sister]."
            pov "We did build this fort together after all."
            mum "Are you sure? It seems like the mother should be there for her."
            pov "And you are, Mom."
            pov "We both know that."
            pov "It's just, this time. I think she needs me a bit more."
            mum "..."
            mum "Alright, sweetie."
            mum "[sister] baby, I'll be just upstairs if you need me, okay?"
            mum "I'll always be here for you."
            mum "I love you."
            show bg fortdestroyed_sis_8
            with fade
            $ renpy.pause()
            if siblingjailtime_hj == 1:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                pass
        "Tell [missus] to give you alone time" if winc == 0:
            pov "[missus], could you... give us some alone time?"
            pov "Maybe I can talk to [sister]."
            pov "We did build this fort together after all."
            mum "Are you sure? It seems like the [mumrole] should be there for her."
            pov "And you are, [missus]."
            pov "We both know that."
            pov "It's just, this time. I think she needs me a bit more."
            mum "..."
            mum "Alright, sweetie."
            mum "[sister] baby, I'll be just upstairs if you need me, okay?"
            mum "I'll always be here for you."
            mum "I love you."
            show bg fortdestroyed_sis_8
            with fade
            $ renpy.pause()
            if siblingjailtime_hj == 1:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                pass
    sis "{i}*Sniff*{/i}"
    sis "..."
    pov "..."

    menu:
        "Stay silent":
            pov "..."
        "Dad's an asshole." if winc == 1:
            pov "Dad's an asshole, isn't he?"
        "[dadname]'s an asshole." if winc == 0:
            pov "[dadname]'s an asshole, isn't he?"
        "I'm sorry.":
            pov "I'm sorry, [sister]."
        "We'll build a new one.":
            pov "Don't worry, we'll rebuild it again."
    sis "..."
    sis "...."
    sis "....."
    pov "[sister]?"
    show bg fortdestroyed_sis_9
    sis "I can't stay here, [povname]."
    pov "What do you mean?"
    sis "I can't stay here. I have to go."
    pov "..Now?"
    sis "..."
    if winc == 1:
        sis "It's best that I go as soon as I can, at least before Dad is allowed back."
        show bg fortdestroyed_sis_8
        pov "Doesn't seem like Dad will be allowed back anytime soon."
    else:
        sis "It's best that I go as soon as I can, at least before [dadname] is allowed back."
        show bg fortdestroyed_sis_8
        pov "Doesn't seem like [dadname] will be allowed back anytime soon."
    sis "He's going to be back by morning..."
    pov "Where are you going to stay?"
    sis "I don't know..."
    sis "But I'm leaving either way."
    show bg fortdestroyed_sis_9
    pov "So that's it?"
    pov "You're just going to go just like that?"
    sis "Do you expect me to stay?"
    pov "This is our home, it's your home."
    sis "My home was destroyed."
    pov "You're talking about the box fort? We can make a new one, a better on-"
    sis "No, [povname]. You don't get it do you?"
    sis "This boxfort was ours, it actually meant something to us."
    sis "Or at least to me it did."
    if winc == 1:
        sis "It's not Mom's, it's not Dad's, it's not anyone's but OUR'S!"
    else:
        sis "It's not [missus]'s, it's not [dadname]'s, it's not anyone's but OUR'S!"
    show bg fortdestroyed_sis_8
    sis "And here I lay, upon the rubble of what used to be what I would proudly proclaim as my home."
    sis "{i}*Sniff*{/i}"
    sis "I- It... makes me feel..."
    sis "When I'm in here..."
    sis "It makes me..."
    sis "I forget- about the whole world."
    sis "Nothing exists outside here but the darkness of reality."
    sis "I used to sneak in here at night and count the plastic stars, and create constellations with my mind."
    sis "Feeling like the luckiest girl in the world, even for just a second."
    sis "I miss being 6."
    sis "I miss being my unknowingly embarrassing self."
    sis "I miss the innocent mind of my younger self."
    sis "Everything was a hell lot more simpler for one hell of a simple mind."
    sis "But we didn't care, all we cared about was having fun."
    show bg fortdestroyed_sis_9
    sis "Don't you miss those days, [povname]?"
    sis "What I wouldn't give to get those days back."

    menu:
        "I didn't know you felt that way.":
            pov "I didn't know you felt that way."
            sis "It's not surprising. I really wanted to try and stay connected with you with this fort but I guess it didn't work as well as it did."
            if sister_points >= 8:
                pov "It did work, we got to know each other at such a deeper level every time we hung out together in here."
            else:
                pov "I'm tryin, [sister]. I really want us to be forever close, and to continually get closer."
        "I 100 percent understand.":
            pov "I 100 percent understand."
            sis "No, you think you do but you don't. How could you ever get me?"
            if sister_points >= 8:
                pov "We've become so much closer ever since we built this fort, haven't we?"
                pov "You can't deny that, if you do, you're lying."
            else:
                pov "You're right, I don't get you and it's wrong of me to even believe that I do."
                pov "But I'm trying, [sister]. Believe that at least."
        "I don't know what to say.":
            pov "I don't know what to say."
            sis "You don't need to say anything, [povname]. It's not like you can relate to me."
            if sister_points >= 8:
                pov "Don't say that I can't understand and relate to you after the times we shared in our Twin-Fortress."
                pov "I know you more than you think you know. I'm just... speechless."
            else:
                pov "You're right, maybe I can't relate to your youthful desires but..."
                pov "That doesn't mean I don't care, [sister]."
    sis "..."
    sis "Thanks, [povname]."
    sis "I'll miss you."
    pov "..."
    show bg fortdestroyed_sis_8
    pov "You won't be gone forever, will you?"
    sis "Just for a little while."
    pov "Can't you tell me where you'd go at least?"
    sis "As if I know, hahaha..."
    sis "I'll ask around."
    pov "I'm in no position to tell you what to do."
    pov "But be careful, wherever you are."
    sis "I will, [povname]."

    scene black
    with fade
    $ renpy.pause()
    "The next morning..."

    scene bg mybasement_lightsonwreck
    with fade
    show pov sad
    with dissolve
    pov "..."
    pov "{i}[sister]'s no where to be seen.{/i}"
    pov "{i}She probably already left...{/i}"
    $ sister_path = 27
    $ townmap_enabled = 1
    $ gtime = 0
    call lbl_next_date
    if day <= 5:
        $ day += 1
    else:
        $ day = 0

    jump lbl_mybasement_day_setup
