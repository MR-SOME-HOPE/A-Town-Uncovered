## Mother Side Story Throwaway Conversations Living Room Day ##
label lbl_mykitchen_day_mother_fixedpc_1:
    show pov neutral at left
    with dissolve
    show mum embarrassed_talk at right
    with dissolve
    mum "Hey, [povname]. I did a rescan and uh.. it's all clean."
    show pov neutral_talk at left
    show mum neutral at right
    pov "That's good to hear, make sure you keep it like that."
    show pov neutral at left
    show mum neutral_talk at right
    mum "No doubt. Again, thanks for doing this for me."
    show pov smirk_talk at left
    show mum neutral at right
    if winc == 0:
        pov "It's aye okay, [missus]. Glad to be of service."
    else:
        pov "It's aye okay, Mom. Glad to be of service."

    jump lbl_mylivingroom_day

label lbl_mylivingroom_day_mother_mompastsunset_1_1:
    show pov neutral at left
    with dissolve
    show mum smirk_talk at right
    with dissolve
    if winc == 0:
        mum "Hey, sweetie. You ready for [mumrole]-[povmumrole] time?"
    else:
        mum "Hey, sweetie. You ready for mother-son time?"

    menu:
        "Yeah.":
            show pov neutral_talk at left
            show mum neutral at right
            pov "You know it."
            stop music fadeout 2.0
            if mompastsunset_attend == 0:
                jump lbl_mom_past_sunset
            elif mompastsunset_attend == 4:
                jump lbl_mom_past_sunset_again
        "Not yet.":
            show pov neutral_talk at left
            show mum neutral at right
            pov "Give me a second, I still need to do something."

            jump lbl_mylivingroom_day

label lbl_mylivingroom_day_mother_mompastsunset_2_1:
    show pov sad_talk at left
    with dissolve
    show mum bored at right
    with dissolve
    if winc == 0:
        pov "Can you please talk to me, [missus]?"
    else:
        pov "Can you please talk to me, Mom?"
    show pov sad at left
    show mum angry_talk at right
    mum "I'm still upset with you."
    show pov sad_talk at left
    show mum angry at right
    pov "I'm sorry I can't hang out with you tonight."
    show pov sad at left
    mum "..."

    jump lbl_mylivingroom_day
