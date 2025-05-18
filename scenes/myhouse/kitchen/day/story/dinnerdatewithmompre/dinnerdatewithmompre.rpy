## Dinner Date with Mom Pre ##
label lbl_dinner_date_with_mom_pre:
    if winc == 0:
        jump lbl_dinner_date_with_mom_pre_win0
    show pov shocked_talk at left
    with dissolve
    hide btn_mylivingroom_day_mother_idle2
    show mum shocked at right
    with dissolve
    pov "Mom!"
    show pov shocked at left
    show mum shocked_talk at right
    mum "What?!"
    show pov shocked_talk at left
    show mum shocked at right
    pov "You."
    show pov shocked at left
    show mum sad_talk at right
    mum "Me?"
    show pov shocked_talk at left
    show mum shocked at right
    pov "Me."
    show pov shocked at left
    show mum confused_talk at right
    mum "You?"
    show pov shocked_talk at left
    show mum shocked at right
    pov "Dinner."
    show pov shocked at left
    show mum shocked_talk at right
    mum "Dinner?!"
    show pov smirk_talk at left
    show mum shocked at right
    pov "Tonight."
    show pov smirk at left
    show mum shocked_talk at right
    mum "I- I'll go get ready!"
    show pov smirk_talk at left
    show mum angry at right
    pov "Haha, no rush, Mom. We still have plenty of time."
    show pov smirk at left
    show mum angry_talk at right
    mum "Speak for yourself."

    scene black
    with fade
    "Later that night..."

    jump lbl_dinner_date_with_mom_pre_night

### NO WINC ###
label lbl_dinner_date_with_mom_pre_win0:
    show pov shocked_talk at left
    with dissolve
    hide btn_mylivingroom_day_mother_idle2
    show mum shocked at right
    with dissolve
    pov "[missus]!"
    show pov shocked at left
    show mum shocked_talk at right
    mum "What?!"
    show pov shocked_talk at left
    show mum shocked at right
    pov "You."
    show pov shocked at left
    show mum sad_talk at right
    mum "Me?"
    show pov shocked_talk at left
    show mum shocked at right
    pov "Me."
    show pov shocked at left
    show mum confused_talk at right
    mum "You?"
    show pov shocked_talk at left
    show mum shocked at right
    pov "Dinner."
    show pov shocked at left
    show mum shocked_talk at right
    mum "Dinner?!"
    show pov smirk_talk at left
    show mum shocked at right
    pov "Tonight."
    show pov smirk at left
    show mum shocked_talk at right
    mum "I- I'll go get ready!"
    show pov smirk_talk at left
    show mum angry at right
    pov "Haha, no rush, [missus]. We still have plenty of time."
    show pov smirk at left
    show mum angry_talk at right
    mum "Speak for yourself."

    scene black
    with fade
    "Later that night..."

    jump lbl_dinner_date_with_mom_pre_night
