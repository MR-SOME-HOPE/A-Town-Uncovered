## Camgurl Confrontation ##
label lbl_camgurl_confrontation:
    show btn_mylivingroom_day_mother_idle2
    show btn_mylivingroom_day_sister_idle2
    $ renpy.pause(0.01)

    default camgurlconfrontation_ask = 0
    if winc == 0:
        jump lbl_camgurl_confrontation_winc0
    if camgurlconfrontation_ask == 0:
        $ camgurlconfrontation_ask = 1
        show pov neutral_talk at left
        with dissolve
        hide btn_mylivingroom_day_sister_idle2
        show sis confused at right
        with dissolve
        pov "Oh, there you are!"
        show pov neutral at left
        show sis confused_talk at right
        sis "Hmm? What is it?"
        show pov confused_talk at left
        show sis confused at right
        pov "I need to talk to you about something."
        show pov embarrassed at left
        show sis confused_talk at right
        sis "Spit it out, then."
        show pov embarrassed_talk at left
        show sis confused at right
        pov "Well..."
        hide pov embarrassed_talk
        #hide sis confused
        show pov embarrassed at left
        #show sis confused at right
        $ renpy.pause(0.001)
        hide btn_mylivingroom_day_mother_idle2
        show mum bored_talk at Position(xpos=1300)
        with dissolve
        $ renpy.pause(1.0, hard=True)
        mum "Oh, don't mind me, I'm just here. Go ahead and talk over my show."
        show mum bored at Position(xpos=1300)
        pov "..."
        show pov embarrassed_talk at left
        show sis shocked at right
        pov "Please? It's about... your uh- streaming."
        show pov embarrassed at left
        show mum confused_talk at Position(xpos=1300)
        mum "What's that?"
        show pov shocked at left
        show mum shocked at Position(xpos=1300)
        show sis angry_talk at right
        sis "[povname]... shut your fucking mouth."
        show mum angry_talk at Position(xpos=1300)
        show sis angry at right
        mum "Hey! Language, and can you bring your conversation somewhere else?"
        if sister_points >= 8:
            show pov embarrassed at left
            show mum bored at Position(xpos=1300)
            show sis bored_talk at right
            sis "C'mon, let's go down to the fort."
            show pov embarrassed_talk at left
            show sis bored at right
            pov "Sounds good."
            show pov embarrassed at left
            show mum bored_talk at Position(xpos=1300)
            show sis bored at right
            mum "Sounds even better when I can't hear you two."
            show mum bored at Position(xpos=1300)
            show sis bored_talk at right
            sis "You have subtitles on, Mom. Just read them. Gosh."
            show pov embarrassed at left
            show sis bored at right
            pov "Let's go."
            $ sister_path = 25

            jump lbl_camgurl_confession
        else:
            show pov shocked at left
            show mum bored at Position(xpos=1300)
            show sis bored_talk at right
            sis "Sorry, Mom. Can you stop bothering us, [povname]?"
            sis "I don't feel like talking at the moment."
            sis "Come back and talk when you're not being annoying."
            show pov angry_talk at left
            show sis bored at right
            pov "How the hell? I'm not being annoying."
            show pov shocked at left
            show mum bored_talk at Position(xpos=1300)
            mum "Oooh, yes you are."
            show pov shocked_talk at left
            show mum bored at Position(xpos=1300)
            pov "Whose side are you on, Mom?"
            show pov bored at left
            show mum bored_talk at Position(xpos=1300)
            mum "The side of peace and quiet."
            show pov bored_talk at left
            show mum bored at Position(xpos=1300)
            pov "{i}*Sigh*{/i} Fine."

            jump lbl_mylivingroom_day_setup
    else:
        show pov embarrassed_talk at left
        with dissolve
        show sis confused at right
        with dissolve
        pov "Hey, can I talk to you about your uh- streaming habits."
        if sister_points >= 8:
            show pov neutral at left
            show sis bored_talk at right
            sis "{i}*Sigh*{/i} Let's get this over with."
            show pov embarrassed_talk at left
            show sis bored at right
            pov "Hey, no more secrets right?"
            hide pov embarrassed_talk
            hide sis bored
            show pov embarrassed at left
            show mum confused_talk at Position(xpos=1300)
            show sis embarrassed at right
            mum "Secrets? What secrets."
            show pov bored_talk at left
            show mum bored at Position(xpos=1300)
            pov "It's a secret, Mom."
            show pov embarrassed at left
            show mum angry_talk at Position(xpos=1300)
            mum "I'm your mother. There shouldn't be any secrets."
            show pov embarrassed_talk at left
            show mum shocked at Position(xpos=1300)
            pov "It's a teen thing. Kinda boring and complicated computer stuff."
            show pov embarrassed at left
            show mum embarrassed_talk at Position(xpos=1300)
            mum "Oh, well. Carry on."
            show pov neutral at left
            show mum embarrassed at Position(xpos=1300)
            show sis embarrassed_talk at right
            sis "Let's go to the fort, we'll have some privacy there."
            $ sister_path = 25

            jump lbl_camgurl_confession
        else:
            show pov embarrassed at left
            show sis angry_talk at right
            sis "I swear to God, why do you wanna talk about that?"
            sis "What does it matter to you?"
            sis "I don't wanna talk about it."
            show pov smirk_talk at left
            show sis shocked at right
            pov "Someone's moody."
            show pov embarrassed at left
            show sis angry_talk at right
            sis "And someone's a pain in the ass."

            jump lbl_mylivingroom_day_setup

### NO WINC ###
label lbl_camgurl_confrontation_winc0:
    if camgurlconfrontation_ask == 0:
        $ camgurlconfrontation_ask = 1
        show pov neutral_talk at left
        with dissolve
        show btn_mylivingroom_day_sister_idle2
        show sis confused at right
        with dissolve
        pov "Oh, there you are!"
        show pov neutral at left
        show sis confused_talk at right
        sis "Hmm? What is it?"
        show pov confused_talk at left
        show sis confused at right
        pov "I need to talk to you about something."
        show pov embarrassed at left
        show sis confused_talk at right
        sis "Spit it out, then."
        show pov embarrassed_talk at left
        show sis confused at right
        pov "Well..."
        hide pov embarrassed_talk
        #hide sis confused
        show pov embarrassed at left
        #show sis confused at right
        $ renpy.pause(0.001)
        hide btn_mylivingroom_day_mother_idle2
        show mum bored_talk at Position(xpos=1300)
        with dissolve
        $ renpy.pause(1.0, hard=True)
        mum "Oh, don't mind me, I'm just here. Go ahead and talk over my show."
        show mum bored at Position(xpos=1300)
        pov "..."
        show pov embarrassed_talk at left
        show sis shocked at right
        pov "Please? It's about... your uh- streaming."
        show pov embarrassed at left
        show mum confused_talk at Position(xpos=1300)
        mum "What's that?"
        show pov shocked at left
        show mum shocked at Position(xpos=1300)
        show sis angry_talk at right
        sis "[povname]... shut your fucking mouth."
        show mum angry_talk at Position(xpos=1300)
        show sis angry at right
        mum "Hey! Language, and can you bring your conversation somewhere else?"
        if sister_points >= 8:
            show pov embarrassed at left
            show mum bored at Position(xpos=1300)
            show sis bored_talk at right
            sis "C'mon, let's go down to the fort."
            show pov embarrassed_talk at left
            show sis bored at right
            pov "Sounds good."
            show pov embarrassed at left
            show mum bored_talk at Position(xpos=1300)
            show sis bored at right
            mum "Sounds even better when I can't hear you two."
            show mum bored at Position(xpos=1300)
            show sis bored_talk at right
            sis "You have subtitles on, Mom. Just read them. Gosh."
            show pov embarrassed at left
            show sis bored at right
            pov "Let's go."
            $ sister_path = 25

            jump lbl_camgurl_confession
        else:
            show pov shocked at left
            show mum bored at Position(xpos=1300)
            show sis bored_talk at right
            sis "Sorry, [missus]. Can you stop bothering us, [povname]?"
            sis "I don't feel like talking at the moment."
            sis "Come back and talk when you're not being annoying."
            show pov angry_talk at left
            show sis bored at right
            pov "How the hell? I'm not being annoying."
            show pov shocked at left
            show mum bored_talk at Position(xpos=1300)
            mum "Oooh, yes you are."
            show pov shocked_talk at left
            show mum bored at Position(xpos=1300)
            pov "Whose side are you on, Mom?"
            show pov bored at left
            show mum bored_talk at Position(xpos=1300)
            mum "The side of peace and quiet."
            show pov bored_talk at left
            show mum bored at Position(xpos=1300)
            pov "{i}*Sigh*{/i} Fine."

            jump lbl_mylivingroom_day_setup
    else:
        show pov embarrassed_talk at left
        with dissolve
        show sis confused at right
        with dissolve
        pov "Hey, can I talk to you about your uh- streaming habits."
        if sister_points >= 8:
            show pov neutral at left
            show sis bored_talk at right
            sis "{i}*Sigh*{/i} Let's get this over with."
            show pov embarrassed_talk at left
            show sis bored at right
            pov "Hey, no more secrets right?"
            hide pov embarrassed_talk
            hide sis bored
            show pov embarrassed at left
            show mum confused_talk at Position(xpos=1300)
            show sis embarrassed at right
            mum "Secrets? What secrets."
            show pov bored_talk at left
            show mum bored at Position(xpos=1300)
            pov "It's a secret, [missus]."
            show pov embarrassed at left
            show mum angry_talk at Position(xpos=1300)
            mum "I'm your [mumrole]. There shouldn't be any secrets."
            show pov embarrassed_talk at left
            show mum shocked at Position(xpos=1300)
            pov "It's a teen thing. Kinda boring and complicated computer stuff."
            show pov embarrassed at left
            show mum embarrassed_talk at Position(xpos=1300)
            mum "Oh, well. Carry on."
            show pov neutral at left
            show mum embarrassed at Position(xpos=1300)
            show sis embarrassed_talk at right
            sis "Let's go to the fort, we'll have some privacy there."
            $ sister_path = 25

            jump lbl_camgurl_confession
        else:
            show pov embarrassed at left
            show sis angry_talk at right
            sis "I swear to God, why do you wanna talk about that?"
            sis "What does it matter to you?"
            sis "I don't wanna talk about it."
            show pov smirk_talk at left
            show sis shocked at right
            pov "Someone's moody."
            show pov embarrassed at left
            show sis angry_talk at right
            sis "And someone's a pain in the ass."

            jump lbl_mylivingroom_day_setup
