## Throwaway Dad Parents Bedroom Day Conversation

label lbl_parentsbedroom_day_dad:
## Add after caught parents
## Add when dad goes on his business trip in mom's story
    show btn parentsbedroom_day_dad_idle
    $ renpy.pause(0.001)
    jump lbl_parentsbedroom_day_dad_convo

label lbl_parentsbedroom_day_dad_convo:
## 1 - 5 is afternoon exclusive
## 6 - 10 is morning exclusive
## 11 - 15 is interchangable
    if date < 7:
        if day == 5:
            jump lbl_parentsbedroom_day_dad_1
        elif day == 6:
            jump lbl_myhouse_day_dad_11
    elif date < 14:
        if day == 5:
            jump lbl_parentsbedroom_day_dad_2
        elif day == 6:
            jump lbl_myhouse_day_dad_12
    elif date < 21:
        if day == 5:
            jump lbl_parentsbedroom_day_dad_3
        elif day == 6:
            jump lbl_myhouse_day_dad_13
    elif date < 27:
        if day == 5:
            jump lbl_parentsbedroom_day_dad_4
        elif day == 6:
            jump lbl_myhouse_day_dad_14
    elif date < 31:
        if day == 5:
            jump lbl_parentsbedroom_day_dad_5
        elif day == 6:
            jump lbl_myhouse_day_dad_15



## Morning Exclusive
label lbl_parentsbedroom_day_dad_1:
    show pov neutral at left
    with dissolve
    hide btn mylivingroom_day_dad_idle
    show dadc angry_talk at right
    with dissolve
    dad "What are you doing in my room?"
    show pov smirk_talk at left
    show dadc angry at right
    pov "I wanted to greet you 'good morning'."
    show pov smirk at left
    show dadc neutral_talk at right
    dad "Morning, now will you leave me in peace."
    show pov smirk_talk at left
    show dadc angry at right
    pov "What's the magic wooor-?"
    show pov smirk at left
    show dadc angry_talk at right
    dad "Get out, [povname], or I'll toss you out this window."

    jump lbl_parentsbedroom_day

label lbl_parentsbedroom_day_dad_2:
    show pov shocked at left
    with dissolve
    hide btn mylivingroom_day_dad_idle
    show dadc angry_talk at right
    with dissolve
    dad "Goddamn, what is it now?!"
    show pov confused_talk at left
    show dadc angry at right
    pov "...What? I didn't even say anything."
    show pov confused at left
    show dadc angry_talk at right
    dad "Why the hell are you in here?"
    show pov bored_talk at left
    show dadc angry at right
    pov "I just came in here to get something."
    show pov confused at left
    show dadc neutral_talk at right
    dad "Oh, please tell the whole world. What is it that you need."
    show pov embarrassed_talk at left
    show dadc angry at right
    pov "I... forgot."
    show pov embarrassed at left
    show dadc angry_talk at right
    dad "You-... {i}*grumble*{/i}"

    jump lbl_parentsbedroom_day

label lbl_parentsbedroom_day_dad_3:
    if winc == 1:
        show pov neutral at left
        with dissolve
        hide btn mylivingroom_day_dad_idle
        show dadc neutral_talk at right
        with dissolve
        dad "Hey- Oh... it's you."
        show pov smirk_talk at left
        show dadc neutral at right
        pov "Disappointed?"
        show pov confused at left
        show dadc neutral_talk at right
        dad "Greatly."
        show pov bored_talk at left
        show dadc neutral at right
        pov "Well, I'm disappointed too. I was looking for mother."
        show pov bored at left
        show dadc neutral_talk at right
        dad "She's not here, idiot."
        show pov bored_talk at left
        show dadc angry at right
        pov "I can see that, asshat."
    else:
        show pov neutral at left
        with dissolve
        hide btn mylivingroom_day_dad_idle
        show dadc neutral_talk at right
        with dissolve
        dad "Hey- Oh... it's you."
        show pov smirk_talk at left
        show dadc neutral at right
        pov "Disappointed?"
        show pov confused at left
        show dadc neutral_talk at right
        dad "Greatly."
        show pov bored_talk at left
        show dadc neutral at right
        pov "Well, I'm disappointed too. I was looking for [missus]."
        show pov bored at left
        show dadc neutral_talk at right
        dad "She's not here, idiot."
        show pov bored_talk at left
        show dadc angry at right
        pov "I can see that, asshat."

    jump lbl_parentsbedroom_day

label lbl_parentsbedroom_day_dad_4:
    if winc == 1:
        show pov neutral_talk at left
        with dissolve
        hide btn mylivingroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "Breakfast is down."
        show pov smirk at left
        show dadc neutral_talk at right
        dad "Do you think I was born yesterday?"
        show pov smirk_talk at left
        show dadc neutral at right
        pov "No really, Mom made something this time."
        show pov neutral at left
        show dadc neutral_talk at right
        dad "Fool me once, shame on me."
        dad "Fool me twice, then fuck you."
        dad "Either way, fuck off."
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn mylivingroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "Breakfast is down."
        show pov smirk at left
        show dadc neutral_talk at right
        dad "Do you think I was born yesterday?"
        show pov smirk_talk at left
        show dadc neutral at right
        pov "No really, [missus] made something this time."
        show pov neutral at left
        show dadc neutral_talk at right
        dad "Fool me once, shame on me."
        dad "Fool me twice, then fuck you."
        dad "Either way, fuck off."

    jump lbl_parentsbedroom_day

label lbl_parentsbedroom_day_dad_5:
    if winc == 1:
        show pov confused_talk at left
        with dissolve
        hide btn mylivingroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "Hey, Dad. Can I ask you something?"
        show pov bored at left
        show dadc neutral_talk at right
        dad "Is it 'why is my son the most annoyingest shit in the world?'"
        show pov neutral_talk at left
        show dadc neutral at right
        pov "First off, 'annoyingest' is not a word."
        show dadc angry at right
        pov "And secondly, I do it to purposely piss you off."
        show pov smirk_talk at left
        pov "Get the hint yet?"
        show pov neutral at left
        show dadc angry_talk at right
        dad "Mother f-. Get the hell out and let me read."
    else:
        show pov confused_talk at left
        with dissolve
        hide btn mylivingroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "Hey, [dadname]. Can I ask you something?"
        show pov bored at left
        show dadc neutral_talk at right
        dad "Is it 'why is my [povdadrole] the most annoyingest shit in the world'?"
        show pov neutral_talk at left
        show dadc neutral at right
        pov "First off, 'annoyingest' is not a word."
        show dadc angry at right
        pov "And secondly, I do it to purposely piss you off."
        show pov smirk_talk at left
        pov "Get the hint yet?"
        show pov neutral at left
        show dadc angry_talk at right
        dad "Mother f-. Get the hell out and let me read."

    jump lbl_parentsbedroom_day

## Interchangable
label lbl_myhouse_day_dad_11:
    if winc == 1:
        show pov neutral_talk at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        hide btn mylivingroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "Hey, Dad."
        show pov neutral at left
        dad "..."
        show pov bored_talk at left
        pov "Hey... Dad."
        show pov bored at left
        dad "..."
        show pov confused_talk at left
        pov "Uh- daddy-o."
        show pov shocked at left
        show dadc angry_talk at right
        dad "Don't call me that. Ever. Again."
        show pov confused_talk at left
        show dadc neutral at right
        pov "Chill, just wanted to tell you that you have food in your mustache."
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        hide btn mylivingroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "Hey, [dadname]."
        show pov neutral at left
        dad "..."
        show pov bored_talk at left
        pov "Hey... [dadname]."
        show pov bored at left
        dad "..."
        show pov confused_talk at left
        pov "Uh- [dadname]-o."
        show pov shocked at left
        show dadc angry_talk at right
        dad "Don't call me that. Ever. Again."
        show pov confused_talk at left
        show dadc neutral at right
        pov "Chill, just wanted to tell you that you have food in your mustache."

    jump lbl_myhouse_day_dad_end

label lbl_myhouse_day_dad_12:
    if winc == 1:
        show pov bored_talk at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        hide btn mylivingroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "I need help with my coursework."
        show pov bored at left
        show dadc neutral_talk at right
        dad "You don't pay me to tutor you."
        show pov confused_talk at left
        show dadc neutral at right
        pov "I don't pay you for anything, you're my dad."
        pov "You should help me when I need it."
        show pov angry at left
        show dadc neutral_talk at right
        dad "Sorry, stopped caring after you said 'I don't pay you for anything'."
    else:
        show pov bored_talk at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        hide btn mylivingroom_day_dad_idle
        show dadc neutral at right
        with dissolve
        pov "I need help with my coursework."
        show pov bored at left
        show dadc neutral_talk at right
        dad "You don't pay me to tutor you."
        show pov confused_talk at left
        show dadc neutral at right
        pov "I don't pay you for anything, you're my [dadrole]."
        pov "You should help me when I need it."
        show pov angry at left
        show dadc neutral_talk at right
        dad "Sorry, stopped caring after you said 'I don't pay you for anything'."

    jump lbl_myhouse_day_dad_end

label lbl_myhouse_day_dad_13:
    if winc == 1:
        show pov bored at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        hide btn mylivingroom_day_dad_idle
        show dadc neutral_talk at right
        with dissolve
        dad "Son, you stink."
        show pov angry_talk at left
        show dadc neutral at right
        pov "No, I don't. That stench must be you."
        show pov shocked at left
        show dadc neutral_talk at right
        dad "I have a musky smell, you smell like balls."
        show pov smirk_talk at left
        show dadc angry at right
        pov "That's because I have them."
        show pov embarrassed at left
        show dadc angry_talk at right
        dad "You really wanna piss me off?"
    else:
        show pov bored at left
        with dissolve
        hide btn mylivingroom_day_dad_idle
        show dadc neutral_talk at right
        with dissolve
        dad "[povname], you stink."
        show pov angry_talk at left
        show dadc neutral at right
        pov "No, I don't. That stench must be you."
        show pov shocked at left
        show dadc neutral_talk at right
        dad "I have a musky smell, you smell like balls."
        show pov smirk_talk at left
        show dadc angry at right
        pov "That's because I have them."
        show pov embarrassed at left
        show dadc angry_talk at right
        dad "You really wanna piss me off?"

    jump lbl_myhouse_day_dad_end

label lbl_myhouse_day_dad_14:
    if winc == 1:
        show pov bored at left
        with dissolve
        hide btn parentsbedroom_day_dad_idle
        hide btn mylivingroom_day_dad_idle
        show dadc neutral_talk at right
        with dissolve
        dad "Did you get a job yet?"
        show pov bored_talk at left
        show dadc neutral at right
        pov "I told you a million times, I have one at the mall."
        show pov angry at left
        show dadc angry_talk at right
        dad "Then where's the board money?"
        show pov angry_talk at left
        show dadc angry at right
        pov "I'm still studying, douche."
        show pov angry at left
        show dadc angry_talk at right
        dad "Whiny, little boy, demands to be treated like an adult."
    else:
        show pov bored at left
        with dissolve
        hide btn mylivingroom_day_dad_idle
        hide btn parentsbedroom_day_dad_idle
        show dadc neutral_talk at right
        with dissolve
        dad "Did you get a job yet?"
        show pov bored_talk at left
        show dadc neutral at right
        pov "I told you a million times, I have one at the mall."
        show pov angry at left
        show dadc angry_talk at right
        dad "Then where's the rent money?"
        show pov angry_talk at left
        show dadc angry at right
        pov "I'm still studying, douche."
        show pov angry at left
        show dadc angry_talk at right
        dad "Whiny, little boy, demands to be treated like an adult."

    jump lbl_myhouse_day_dad_end

label lbl_myhouse_day_dad_15:
    show pov bored at left
    with dissolve
    hide btn parentsbedroom_day_dad_idle
    hide btn mylivingroom_day_dad_idle
    show dadc neutral at right
    with dissolve
    dad "..."
    show pov confused_talk at left
    show dadc neutral at right
    pov "What? Is there something on my forehead."
    show pov bored at left
    show dadc neutral_talk at right
    dad "A big 'L'."
    show pov bored_talk at left
    show dadc neutral at right
    pov "I can't see why you're not the life of a party."
    pov "Pulling out the big guns and shooting fun in all directions."

    jump lbl_myhouse_day_dad_end

label lbl_myhouse_day_dad_end:
    if gtime == 1:
        jump lbl_parentsbedroom_day
    else:
        jump lbl_mylivingroom_day
