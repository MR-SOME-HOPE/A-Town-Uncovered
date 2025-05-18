## Ask Mom to Cinema ##
label lbl_ask_mom_to_cinema:
    if winc == 0:
        jump lbl_ask_mom_to_cinema_winc0
    if mum_path == 18:
        show pov neutral_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum confused at right
        with dissolve
        pov "Hey, Mom. I've got an idea."
        show pov neutral at left
        mum "Mhmm?"
        show pov smirk_talk at left
        show mum neutral at right
        pov "Let's go watch a movie."
        show pov neutral at left
        show mum neutral_talk at right
        mum "In the living room?"
        show pov neutral_talk at left
        show mum shocked at right
        pov "No, Mom. Out of the house, at the local cinema."
        show pov neutral at left
        show mum shocked_talk at right
        mum "Ooh?! Movies old-school style?"
        show pov smirk_talk at left
        show mum neutral at right
        pov "Ah yup!"
        show pov smirk at left
        show mum neutral_talk at right
        mum "That sounds like a fantastic idea!"
        show pov neutral at left
        show mum smirk_talk at right
        mum "I'll have to go get ready. How about we leave in the evening?"
        show pov neutral_talk at left
        show mum smirk at right
        pov "Sure thing."
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral at right
        with dissolve
        pov "Hey, Mom. Wanna go watch another movie?"
        show pov neutral at left
        show mum neutral_talk at right
        mum "At the cinema?"
        show pov smirk_talk at left
        show mum neutral at right
        pov "The one and only place."
        show pov smirk at left
        show mum neutral_talk at right
        mum "I'm free. Give me a while and we'll head out."

    scene black
    with fade
    $ renpy.pause()
    "At the cinema..."
    stop music fadeout 2.0
    $ moviedate = 1
    $ gtime = 2

    jump lbl_cinema_night_setup

### NO WINC ###
label lbl_ask_mom_to_cinema_winc0:
    if mum_path == 18:
        show pov neutral_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum confused at right
        with dissolve
        pov "Hey, [missus]. I've got an idea."
        show pov neutral at left
        mum "Mhmm?"
        show pov smirk_talk at left
        show mum neutral at right
        pov "Let's go watch a movie."
        show pov neutral at left
        show mum neutral_talk at right
        mum "In the living room?"
        show pov neutral_talk at left
        show mum shocked at right
        pov "No, [missus]. Out of the house, at the local cinema."
        show pov neutral at left
        show mum shocked_talk at right
        mum "Ooh?! Movies old-school style?"
        show pov smirk_talk at left
        show mum neutral at right
        pov "Ah yup!"
        show pov smirk at left
        show mum neutral_talk at right
        mum "That sounds like a fantastic idea!"
        show pov neutral at left
        show mum smirk_talk at right
        mum "I'll have to go get ready. How about we leave in the evening?"
        show pov neutral_talk at left
        show mum smirk at right
        pov "Sure thing."
    else:
        show pov neutral_talk at left
        with dissolve
        hide btn_mylivingroom_day_mother_idle2
        show mum neutral at right
        with dissolve
        pov "Hey, [missus]. Wanna go watch another movie?"
        show pov neutral at left
        show mum neutral_talk at right
        mum "At the cinema?"
        show pov smirk_talk at left
        show mum neutral at right
        pov "The one and only place."
        show pov smirk at left
        show mum neutral_talk at right
        mum "I'm free. Give me a while and we'll head out."

    scene black
    with fade
    $ renpy.pause()
    "At the cinema..."
    stop music fadeout 2.0
    $ moviedate = 1
    $ gtime = 2

    jump lbl_cinema_night_setup
