## Effie Couch on Phone Pre
label lbl_effie_couch_on_phone_pre:
    show pov neutral_talk at left
    show eff neutral at right
    with dissolve
    pov "Hey, Effie."
    eff "[povname]? What are you doing here on a Saturday morning?"
    pov "Wanted to see you."
    eff "Don't you have a bed to sleep in on?"
    pov "I like making use of daylight."
    eff "I see."
    eff "Well, I'm just chilling on the couch watching some Webflix if you wanna hang out."
    eff "My dad's out running some errands."
    menu:
        "I'm down.":
            pov "I'm down, if you don't mind me intruding."
            eff "Oh, no way, dude."
            eff "Could use some company."
            eff "But for real, I do wanna pay attention to the show."
            pov "Yeah- no, of course."
            pov "I'll be like a silent fly on the wall."
            eff "Alright, come in."

            jump lbl_effie_couch_on_phone

        "No, thanks.":
            pov "Sounds fun, but no, thanks."
            pov "Been staying indoors too much recently so I really should be out and about."
            eff "Whatever you say, dude."
            eff "Peace."

    jump lbl_effiehouseoutside_day_setup
