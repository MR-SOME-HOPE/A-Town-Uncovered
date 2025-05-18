## Throwaway Cole School Cafeteria Day Conversation ##
label lbl_schoolcafeteria_day_cole:
    ## Background
    if insexworld == 0:
        scene bg schoolcafeteria_day
    elif insexworld == 1:
        scene bg schoolcafeteria_daysexworld
    show btn_schoolcafeteria_day_cole_idle2
    $ renpy.pause(0.001)

    ## Main Story
    ## Sex World
    if insexworld == 1 and main_story <= 35:
        jump lbl_schoolcafeteria_day_cole_sexworld
    ## Investigations Cole
    elif main_story == 84:
        jump lbl_investigations_cole
    ## NO EVENT
    else:
        jump lbl_schoolcafeteria_day_cole_convo

label lbl_schoolcafeteria_day_cole_convo:
## 1 - 5 is morning exclusive (School Cafeteria)
## 6 - 10 is night exclusive (Street Night)
## 11 - 15 is interchangeable
    if date == 10 or date == 14 or date == 22:
        jump lbl_schoolcafeteria_day_cole_1
    elif date == 9 or date == 13 or date == 21:
        jump lbl_schoolcafeteria_day_cole_2
    elif date == 8 or date == 12 or date == 24:
        jump lbl_schoolcafeteria_day_cole_3
    elif date == 5 or date == 11 or date == 23:
        jump lbl_schoolcafeteria_day_cole_4
    elif date == 4 or date == 20 or date == 26:
        jump lbl_schoolcafeteria_day_cole_5
    elif date == 3 or date == 17 or date == 25:
        jump lbl_town_day_cole_11
    elif date == 2 or date == 16 or date == 28:
        jump lbl_town_day_cole_12
    elif date == 1 or date == 19 or date == 27:
        jump lbl_town_day_cole_13
    elif date == 7 or date == 18 or date == 30:
        jump lbl_town_day_cole_14
    elif date == 6 or date == 15 or date == 29 or date == 0:
        jump lbl_town_day_cole_15

## Morning Exclusive
label lbl_schoolcafeteria_day_cole_1: ##
    show pov neutral_talk at left
    with dissolve
    hide btn_schoolcafeteria_day_cole_idle2
    show col neutral at right
    with dissolve
    pov "Morning, Cole."
    show pov neutral at left
    show col neutral_talk at right
    col "Good morning, [povname]."
    show pov smirk_talk at left
    show col neutral at right
    pov "Any new get-rich-quick scheme you cooked up over the weekend?"
    show pov smirk at left
    show col smirk_talk at right
    col "Oh-hoho~! Funny you ask, I have plenty in the works."
    show pov neutral_talk at left
    show col shocked at right
    pov "Care to share?"
    show pov confused at left
    show col embarrassed_talk at right
    col "Oh- not yet my friend, it's not ready yet."
    col "You gotta wait for it to rise and go golden brown."
    show pov smirk_talk at left
    show col confused at right
    pov "Is it bread?"
    show pov smirk at left
    show col confused_talk at right
    col "..."
    show pov embarrassed at left
    show col bored_talk at right
    col "No..."

    jump lbl_schoolcafeteria_day

label lbl_schoolcafeteria_day_cole_2: ##
    show pov neutral at left
    with dissolve
    hide btn_schoolcafeteria_day_cole_idle2
    show col neutral_talk at right
    with dissolve
    col "Morning, [povname]."
    show pov angry_talk at left
    show col shocked at right
    pov "Fuck mornings."
    show pov bored at left
    show col shocked_talk at right
    col "Damn, what did mornings ever do to you?"
    show pov bored_talk at left
    show col embarrassed at right
    pov "It woke me up."
    show pov bored at left
    show col smirk_talk at right
    col "It didn't want you to be late for school."
    show pov bored_talk at left
    show col smirk at right
    pov "School exists because mornings exists."
    pov "The day system is a social construct."

    jump lbl_schoolcafeteria_day

label lbl_schoolcafeteria_day_cole_3: ##
    show pov neutral_talk at left
    with dissolve
    hide btn_schoolcafeteria_day_cole_idle2
    show col shocked at right
    with dissolve
    pov "Good- {i}*yawn*{/i} morning."
    show pov shocked at left
    show col shocked_talk at right
    col "Oof- I can smell that from over here."
    show pov confused_talk at left
    show col embarrassed at right
    pov "That bad? Got a mint, buddy-ol-pal?"
    show pov confused at left
    show col smirk_talk at right
    col "Yeah, you don't gotta ask me twice, bro."
    show col confused_talk at right
    col "Where did I put it-"
    show pov shocked at left
    col "Is this it? No- that's where I keep the {i}other{/i} stuff."
    show pov confused_talk at left
    show col smirk at right
    pov "Other stu-?"
    show pov shocked at left
    show col embarrassed_talk at right
    col "I don't have any, sorry. Gotta run!"

    jump lbl_schoolcafeteria_day

label lbl_schoolcafeteria_day_cole_4: ##
    show pov neutral at left
    with dissolve
    hide btn_schoolcafeteria_day_cole_idle2
    show col shocked_talk at right
    with dissolve
    col "God- can you believe the cafeteria is out of bagels?"
    show pov embarrassed_talk at left
    show col shocked at right
    pov "Damn, that sucks."
    show pov smirk at left
    show col smirk_talk at right
    col "I rely on my morning bagels!"
    col "Who's dick do I have to suck to get a simple frikkin- bagel!"
    show pov shocked_talk at left
    show col smirk at right
    pov "Whoa, man. I'm sure there's other stuff to eat."
    show pov confused at left
    show col bored_talk at right
    col "It's not the same, man..."
    col "This will definitely throw me off my groove for today."

    jump lbl_schoolcafeteria_day

label lbl_schoolcafeteria_day_cole_5: ##
    show pov neutral at left
    with dissolve
    hide btn_schoolcafeteria_day_cole_idle2
    show col bored_talk at right
    with dissolve
    col "Dude, don't order today's lunch."
    show pov confused_talk at left
    show col bored at right
    pov "Why?"
    show pov confused at left
    show col shocked_talk at right
    col "I overheard the lunch ladies saying stuff about mold."
    show pov shocked_talk at left
    show col smirk at right
    pov "Mold?"
    show pov confused at left
    show col bored_talk at right
    col "Yeah, cupcake molds. Disgusting."
    show pov smirk_talk at left
    show col bored at right
    pov "You sure they don't mean like the mould you put cupcakes into?"
    show pov smirk at left
    show col smirk_talk at right
    col "You wanna take that risk, my man?"

    jump lbl_schoolcafeteria_day

## Interchangeable
label lbl_town_day_cole_11:
    show pov confused at left
    with dissolve
    if gtime == 0:
        hide btn_schoolcafeteria_day_cole_idle2
    elif gtime >= 2:
        hide btn_street_night_cole_idle2

    show col embarrassed_talk at right
    with dissolve
    col "Partner! Did I sell you some face cream recently?!"
    show pov smirk_talk at left
    show col embarrassed at right
    pov "No? Look at me, my skin is already flawless."
    show pov smirk at left
    show col embarrassed_talk at right
    col "I'm not commenting on that."
    show pov confused at left
    show col confused_talk at right
    col "Dude, I need to find out who I sold that face cream to!"
    show col embarrassed_talk at right
    col "I may have accidentally mixed up the bottles."
    show pov confused_talk at left
    show col embarrassed at right
    pov "With what, may I ask?"
    show pov shocked at left
    show col embarrassed_talk at right
    col "Well, actually-"
    show pov bored_talk at left
    show col embarrassed at right
    pov "Y'know what, I change my mind. I already have nasty shit entering my brain-magination."

    jump lbl_town_day_cole_end

label lbl_town_day_cole_12:
    show pov neutral at left
    with dissolve
    if gtime == 0:
        hide btn_schoolcafeteria_day_cole_idle2
    elif gtime >= 2:
        hide btn_street_night_cole_idle2

    show col smirk_talk at right
    with dissolve
    col "[povname]! Just the dude I wanted to see!"
    show pov bored at left
    col "My man, do I have a question for you - and you alone!"
    show pov bored_talk at left
    show col smirk at right
    pov "Oh boy, here we go..."
    show pov bored at left
    show col smirk_talk at right
    col "My man, what would you say to the opportunity in joining me in my latest business venture?"
    show pov bored_talk at left
    show col smirk at right
    pov "What are you selling now?"
    show pov confused at left
    show col smirk_talk at right
    col "Just what you have been looking for your entire life!"
    show pov confused_talk at left
    show col shocked at right
    pov "You pitched me in the exact same way last time, Cole. Do you have all these scripted out?"
    show pov bored at left
    show col confused_talk at right
    col "Did I? I think I just went through my whole contact list. This is why I need an assistant to keep track of things!"

    jump lbl_town_day_cole_end

label lbl_town_day_cole_13:
    show pov confused at left
    with dissolve
    if gtime == 0:
        hide btn_schoolcafeteria_day_cole_idle2
    elif gtime >= 2:
        hide btn_street_night_cole_idle2

    show col smirk_talk at right
    with dissolve
    col "Partner! You want to earn some quick cash?"
    show pov bored_talk at left
    show col smirk at right
    pov "I told you before, I'm not joining any pyramid."
    show pov bored at left
    show col smirk_talk at right
    col "N-n-n-n-n-noo, nothing of that sort this time."
    show pov confused at left
    show col neutral_talk at right
    col "I just need some help moving some boxes from my storage."
    show pov neutral_talk at left
    show col smirk at right
    pov "Sure man, I can help you out with that."
    show pov bored at left
    show col smirk_talk at right
    col "While we move stuff though, I do want to tell you of a business opportunity I don't want you to miss!"
    show pov bored_talk at left
    show col smirk at right
    pov "I just remembered, I have my own boxes that need.. moving..."

    jump lbl_town_day_cole_end

label lbl_town_day_cole_14: ##
    show pov confused_talk at left
    with dissolve
    hide btn_schoolcafeteria_day_cole_idle2
    show col confused at right
    with dissolve
    pov "What's happening, Cole?"
    show pov confused at left
    show col confused_talk at right
    col "Uh- nothing- nothing at all!"
    col "Why, what did you hear?"
    show pov embarrassed_talk at left
    show col confused at right
    pov "Uhm... nothing? Why? Is there something I shouldn't have heard?"
    show pov embarrassed at left
    show col smirk_talk at right
    col "Depends on what you heard, playa'."
    show pov smirk_talk at left
    show col smirk at right
    pov "I'm sure there's nothing you should worry about."
    show pov confused at left
    show col shocked_talk at right
    col "Haha! I ain't worried, who said I was worried-"

    jump lbl_town_day_cole_end

label lbl_town_day_cole_15: ##
    show pov neutral at left
    with dissolve
    hide btn_schoolcafeteria_day_cole_idle2
    show col smirk_talk at right
    with dissolve
    col "[povname]! Just the person I wanted to see."
    show pov neutral_talk at left
    show col smirk at right
    pov "Yo, what's up."
    show pov confused at left
    show col smirk_talk at right
    col "You hear about that new street treat?"
    show pov confused_talk at left
    show col smirk at right
    pov "Depends, what kind of high does it give you?"
    show pov smirk at left
    show col neutral_talk at right
    col "The good kind."
    show pov neutral_talk at left
    show col shocked at right
    pov "What's it called?"
    show pov neutral at left
    show col smirk_talk at right
    col "Plenty of water, enough sleep, and a healthy diet."

    jump lbl_town_day_cole_end

label lbl_town_day_cole_end:
    if gtime == 0:
        jump lbl_schoolcafeteria_day
    else:
        jump lbl_street_night
