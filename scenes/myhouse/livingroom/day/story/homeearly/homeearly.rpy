## Home Early
default homeearly_63c_watchedtv = 0
default homeearly_63c_talked = 0
default homeearly_63c_fooledaround = 0

label lbl_home_early:
    scene bg mylivingroom_day
    with fade
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right
    with dissolve
    pov "I- am- home~!"
    show pov neutral
    show mum confused_talk
    mum "Sweetie?"
    show mum shocked_talk
    mum "Wow, you are home way earlier than I expected you to be."
    show pov neutral_talk
    pov "Well, I didn’t want to worry you guys, so I hurried home."
    #+2 Mom rp.
    show pov neutral
    show mum embarrassed
    $ add_points("mum_points",2)
    show mum embarrassed_talk
    mum "Awww, well."
    mum "Thank you, sweetie. That means the world to me!"
    show mum embarrassed
    show pov neutral_talk
    pov "Anything to keep you happy."
    show pov neutral
    show mum embarrassed_talk
    mum "Why, aren’t you a charmer?"

    if mum_path <= 30:
        mum "Your future wife is going to be a very lucky woman if you are as considerate with her as you are with me."
        show mum embarrassed
        show pov neutral_talk
        pov "I just don’t want to give you any reason not to trust me or worry unnecessarily."
        show pov neutral
        show mum neutral_talk
        mum "You haven’t given me any reason thus far, and made me happy in the process."
        mum "What more I could ask?"
        show mum neutral

    else:
        show mum smirk_talk
        mum "Had you not stolen it already, you would have stolen my heart right there."
        show mum smirk
        show pov smirk_talk
        pov "I work hard to keep my number one girl happy."
        show pov smirk
        show mum smirk_talk
        mum "And you do such a good job on it."
        mum "Now come on, my lips have been missing you."
        show mum smirk

        ##"you move in to give her a passionate kiss, breaking it off after some tongue action or groping."

    #=RESULT END#=
    show pov neutral_talk
    if winc == 1:
        pov "So, is sister home yet?"
    else:
        pov "So, is [sister] home yet?"
    show pov neutral
    show mum neutral_talk
    mum "No, she's not back yet."
    mum "Actually, it’s a good thing you are here early, since I wanted to talk to both of you about something important."
    show mum neutral
    show pov confused_talk
    pov "Is it about what’s happening in town?"
    show pov confused
    show mum neutral_talk
    mum "Among other things, yes."
    show pov neutral_talk
    pov "Wouldn’t miss it for the world."
    show pov neutral
    show mum neutral_talk
    mum "Thank you, honey."
    if winc == 1:
        mum "Well, since your Sister is not home and your father is staying late at work today."
    else:
        mum "Well, since your [povsisrole] is not home and your [dadrole] is staying late at work today."
    mum "How about we spend some time together?"
    show mum neutral
    show pov neutral_talk
    pov "Sounds great! What should we do?"
    show pov neutral
    show mum neutral_talk
    mum "I am up for anything. Any ideas?"
    show mum neutral
    show pov confused_talk
    pov "Well…"

    menu:
        "We could watch some tv.":
            show pov neutral_talk
            pov "We could watch some tv."
            show pov confused_talk
            pov "Weren’t they premiering that one drama about the brothel working girl turning into a pimp today?"
            show pov neutral
            #+1 Mom rp.
            $ add_points("mum_points",1)
            show mum shocked_talk
            mum "That was today?!"
            mum "Oh, it has some of my favorite drama actors working on it too!"
            show mum shocked
            show pov neutral_talk
            pov "I’ll make some popcorn."
            show pov neutral
            show mum neutral_talk
            mum "Thank you darling!"

            $ homeearly_63c_watchedtv = 1

        "We haven’t talked in a long while.":
            show pov bored_talk
            pov "We haven’t talked in a long while."
            pov "I was actually hoping we could talk for a while."
            pov "It’s been a long time since we just sat down and had a moment for ourselves, you know?"
            show pov bored
            show mum embarrassed
            #+2 Mom rp.
            $ add_points("mum_points",2)
            show mum embarrassed_talk
            mum "Oh, darling that’s such a wonderful idea!"
            mum "It warms my heart so much to know you want to spend time and open up to me."
            mum "We used to be so close back in the day and I was starting to think we were really growing apart."
            show mum embarrassed
            show pov confused_talk
            pov "Don’t be silly."
            pov "Even if I moved to the other side of the world, I would still do my best to stay in contact with you."
            pov "You are never going to lose me."
            show pov confused
            show mum bored_talk
            mum "And I am so happy you feel that way, sweetie."
            mum "But I know one day some girl or job is going to take you away from me and have you start your own life."
            mum "I know I’ll need to eventually let you go and stay behind as you spread your wings."
            show mum bored
            show pov bored_talk
            pov "A bird doesn’t fly far from his nest."
            pov "but let’s not worry about that or the future for now."
            show pov neutral_talk
            pov "How about you make some tea and I’ll bring in the blankets and we can cuddle on the sofa while we talk?"
            show pov neutral
            show mum neutral_talk
            mum "You are just a good idea machine today!"
            mum "Nothing would make me happier, I’ll get started on it!"
            show mum neutral

            $ homeearly_63c_talked = 1

        "We could fool around while we wait." if mum_path >= 31:
            show pov smirk_talk
            pov "We could fool around while we wait."
            show mum smirk
            pov "Well, my bed is feeling rather empty right now and you are looking mighty fine today."
            show pov smirk
            #+3 Mom rp.
            $ add_points("mum_points",3)
            show mum smirk_talk
            mum "Oh, you read my mind here, you stud."
            mum "Mmmm, we could also try doing it on the tub or shower."
            mum "I read somewhere online that you can get really creative with where you place some of those dissolving bath salts."
            show mum smirk
            show pov confused_talk
            pov "We have some of those?"
            show mum neutral_talk
            mum "I ordered 3 boxes online the moment I finished reading that article."
            show mum neutral
            show pov smirk
            pov "God, I love you."
            show pov smirk
            show mum smirk_talk
            mum "I know, now fuck me until I can’t feel my legs and ass anymore or the neighbors complain about the noise."
            show mum smirk
            show pov smirk_talk
            pov "Yes Ma’am!"

            $ homeearly_63c_fooledaround = 1

    $ main_story = 64.2
    $ mainstory_62_crossroads_home = 1
    scene black with fade
    jump lbl_sister_comes_home
