## Morning Mom ##
label lbl_morning_mom:
    if winc == 0:
        jump lbl_morning_mom_winc0
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right
    with dissolve
    pov "Morning, Mom."
    show mum neutral_talk at right
    show pov neutral at left
    mum "Morning, honey. How was your sleep?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was alright."
    show mum neutral_talk at right
    show pov neutral at left
    mum "That's good. Excited about university?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "I guess so. What's for breakfast?"
    show mum neutral_talk at right
    show pov neutral at left
    mum "Help yourself to anything. We've got cereal, toast, you can make yourself an omelette."
    show pov bored_talk at left
    show mum neutral at right
    pov "Eh.. I'll pass. I'm not really hungry."
    show mum neutral_talk at right
    show pov bored at left
    mum "Well, could you at least call [sister] down to eat? I don't know when her shifts starts and I don't want her to miss it."
    show pov bored_talk at left
    show mum neutral at right
    pov "Will do."
    show pov bored at left
    show mum neutral_talk at right
    mum "Thanks, honey."
    $ main_story = 3
    $ renpy.notify("New Objective: Wake up [sister]")

    jump lbl_mykitchen_day

### NO WINC ###
label lbl_morning_mom_winc0:
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right
    with dissolve
    pov "Morning, [missus]."
    show mum neutral_talk at right
    show pov neutral at left
    mum "Morning, honey. How was your sleep?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was alright."
    show mum neutral_talk at right
    show pov neutral at left
    mum "That's good. Excited about university?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "I guess so. What's for breakfast?"
    show mum neutral_talk at right
    show pov neutral at left
    mum "Help yourself to anything. We've got cereal, toast, you can make yourself an omelette."
    show pov bored_talk at left
    show mum neutral at right
    pov "Eh.. I'll pass. I'm not really hungry."
    show mum neutral_talk at right
    show pov bored at left
    mum "Well, could you at least call your [sisrole] down to eat? I don't know when her shifts starts and I don't want her to miss it."
    show pov bored_talk at left
    show mum neutral at right
    pov "Will do."
    show mum neutral_talk at right
    show pov bored at left
    mum "Thanks, honey."
    $ main_story = 3
    $ renpy.notify("New Objective: Wake up [sister]")

    jump lbl_mykitchen_day
