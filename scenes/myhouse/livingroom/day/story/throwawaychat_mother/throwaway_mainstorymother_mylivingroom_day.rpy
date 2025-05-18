## Mother Main Story Throwaway Conversations Living Room ##
label lbl_mykitchen_day_mother_sexworld_1:
    if winc == 0:
        jump lbl_mykitchen_day_mother_sexworld_1_winc0
    show pov sad at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Hey, [povname]. How's your day so far."
    show pov sad_talk at left
    show mum confused at right
    pov "I-I am... at a fucking loss.. there's something strange going on.."
    show pov sad at left
    show mum confused_talk at right
    mum "Hmm? What is it?"
    show pov sad_talk at left
    show mum confused at right
    pov "I- I don't really get it.."
    pov "I'm going to find answers."
    show pov sad at left
    show mum embarrassed_talk at right
    mum "Uhh? Sure.. I'll be here if you need anything."
    show pov sad_talk at left
    show mum confused at right
    pov "Mom?"
    show pov sad_talk at left
    show mum confused at right
    pov "You're my real mother, right?"
    show pov sad at left
    show mum neutral_talk at right
    mum "Of course I am? I birthed you right out of my va-"
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "Okay okay. Just making sure.."

    jump lbl_mylivingroom_day

### NO WINC ###
label lbl_mykitchen_day_mother_sexworld_1_winc0:
    show pov sad at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Hey, [povname]. How's your day so far."
    show pov sad_talk at left
    show mum confused at right
    pov "I-I am... at a fucking loss.. there's something strange going on.."
    show pov sad at left
    show mum confused_talk at right
    mum "Hmm? What is it?"
    show pov sad_talk at left
    show mum confused at right
    pov "I- I don't really get it.."
    pov "I'm going to find answers."
    show pov sad at left
    show mum embarrassed_talk at right
    mum "Uhh? Sure.. I'll be here if you need anything."
    show pov sad_talk at left
    show mum confused at right
    pov "[missus]?"
    show pov sad_talk at left
    show mum confused at right
    pov "You're my real [mumrole], right?"
    show pov sad at left
    show mum neutral_talk at right
    mum "Of course I am?"
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "Okay okay. Just making sure.."

    jump lbl_mylivingroom_day
