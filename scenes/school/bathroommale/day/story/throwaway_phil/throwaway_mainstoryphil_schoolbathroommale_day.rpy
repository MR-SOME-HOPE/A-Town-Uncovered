## Phil Main Story Throwaway Conversations School Bathroom Male ##
default sexaroundtownphil = 0

## Sex Around Town Phil
label lbl_schoolbathroommale_day_phil_sexworld:
    if sexaroundtownphil == 0:
        show pov confused_talk at left
        with dissolve
        show phi bored at right
        hide btn schoolbathroom_day_phil_idle
        with dissolve
        pov "He-"
        show pov confused at left
        show phi bored_talk at right
        phi "What do you want, punk?"
        show pov confused_talk at left
        show phi bored at right
        pov "Psh, why are you so mean?"
        show pov bored at left
        show phi bored_talk at right
        phi "Because I can beat the crap out of you, that's why."
        show pov sad_talk at left
        show phi bored at right
        pov "Look, dude. I'm just wondering what the fuck is going on around here."
        show pov bored at left
        show phi bored_talk at right
        phi "Why should I tell you, fuck-face? You gonna rat on me?"
        show pov confused_talk at left
        show phi bored at right
        pov "What's to rat about?"
        show pov confused at left
        show phi neutral_talk at right
        phi "Definitely not the four D's."
        phi "Drinks, drugs, and double D's."
        phi "Oh! Fuck yes! Mom's serving my favourite tonight!"
        show pov shocked at left
        phi "Check out the picture she just texted me."
        show pov embarrassed_talk at left
        show phi neutral at right
        pov "Those... are definitely... big boobs."
        show pov shocked at left
        show phi neutral_talk at right
        phi "Mmmm, she has the best, most delicious tits ever."
        phi "Dad's more into the dark meat, the thighs."
        show pov embarrassed at left
        show phi neutral at right
        pov "..."
        show pov bored at left
        show phi bored_talk at right
        phi "Alright, you can just about fuck off now."
        phi "Let me watch some porn in peace."

        $ sexaroundtownphil = 1

    else:
        show pov embarrassed at left
        with dissolve
        show phi bored_talk at right
        hide btn schoolbathroom_day_phil_idle
        with dissolve
        phi "I don't really like people watching over my shoulders."
        phi "You have a phone, watch your own shit and leave me alone."
        show phi neutral at right
        phi "..."
        show phi neutral_talk at right
        phi "Can't wait for dinner tonight."

    jump lbl_schoolbathroommale_day
