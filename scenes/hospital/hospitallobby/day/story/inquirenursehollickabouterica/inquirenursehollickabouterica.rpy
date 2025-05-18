## Inquire Nurse Hollick About Erica
label lbl_inquire_nurse_hollick_about_erica:
    scene black
    with fade
    $ renpy.pause()
    "After texting and waiting for the two..."

    scene bg hospitallobby_daynight
    with fade
    ## SPRITES
    ## Use nurr (for Nurse Hollick Regular sprite)
    ## When you text Effie and Cole to visit you outside the hospital, you all go into the lobby together.

    show pov embarrassed_talk
    with dissolve
    pov "I guess we’ll talk to the receptioni-"
    show pov confused_talk
    pov "Oh?"
    show pov embarrassed_talk
    pov "Nurse Hollick?"
    show pov neutral_talk at left
    show nur neutral at right
    with dissolve
    pov "Do you remember me?"
    show pov neutral at left
    show nur confused_talk at right
    nur "Mmmm- you’re gonna have to jog my memory. I see a lot of people every day."
    show pov smirk_talk at left
    show nur confused at right
    pov "It’s [povname]. The guy who… drowned at the park."
    show pov embarrassed at left
    show nur shocked_talk at right
    nur "Oh! Right. I remember now."
    show pov neutral at left
    show nur confused_talk at right
    nur "How’s your head injury?"
    show nur smirk_talk at right
    nur "Or should I say, lack thereof."
    nur "I’m glad you’re okay that night and did the right thing by getting checked up just in case."
    show pov smirk_talk at left
    show nur smirk at right
    pov "Yeah- it really was an… intense night."
    show pov neutral_talk at left
    show nur neutral at right
    pov "That’s for sure."
    show pov neutral at left
    show nur confused_talk at Position(xpos=1400)
    show col smirk at Position(xpos=1600)
    with dissolve
    col "Why are you talking like that?"
    show pov confused at left
    show col neutral at Position(xpos=1600)
    pov "Say, do you know of a patient named Erica? We wanna pay her a visit."
    show pov neutral at left
    show nur shocked_talk at Position(xpos=1400)
    show col smirk at Position(xpos=1600)
    nur "Ah yes, Erica."
    show pov confused at left
    show nur embarrassed_talk at Position(xpos=1400)
    nur "She’s had a lot of visitors and dare I say admirers."
    nur "A lot of boys have been dropping off gifts and flowers and those chocolates that are supposed to heighten your sex drive."
    show nur smirk_talk at Position(xpos=1400)
    show col confused at Position(xpos=1600)
    nur "Just FYI, a scam."
    nur "Chocolate is already a natural aphrodisiac."
    show nur confused at Position(xpos=1400)
    show eff neutral_talk at Position(xpos=1800)
    with dissolve
    eff "Can we go see her by any chance?"
    show nur confused_talk at Position(xpos=1400)
    show eff neutral at Position(xpos=1800)
    nur "Mmmm.. visiting hours are…"
    show pov neutral at left
    show nur embarrassed_talk at Position(xpos=1400)
    nur "Yeah, you still have time."
    show nur neutral_talk at Position(xpos=1400)
    nur "Go to room 369 and you’ll find her there."
    nur "You have about 2 hours."
    show nur neutral at Position(xpos=1400)
    show col neutral_talk at Position(xpos=1600)
    col "Oh don’t worry, we won’t be staying for that long."
    show pov embarrassed at left
    show nur embarrassed_talk at Position(xpos=1400)
    show col smirk at Position(xpos=1600)
    show eff confused at Position(xpos=1800)
    nur "I must warn you though, she’s been running around the floor begging people to have sex with her."
    nur "We had no other option but to give her a calming sedative to keep that libido under control."
    show nur smirk_talk at Position(xpos=1400)
    nur "Can’t have her disturbing other patients, especially ones who are seriously ill and in no position to give her what she wants, even if they wanted to."
    show nur embarrassed at Position(xpos=1400)
    show col smirk_talk at Position(xpos=1600)
    col "I hear you. Thanks for letting us know."
    show col confused_talk at Position(xpos=1600)
    col "We just wanted to drop off-"
    show nur neutral_talk at Position(xpos=1400)
    col "Chocolates."
    col "…"
    show nur neutral at Position(xpos=1400)
    show col neutral_talk at Position(xpos=1600)
    col "I swear, they’re not the scammy ones, just some good quality gift chocolates."
    show nur neutral_talk at Position(xpos=1400)
    show col neutral at Position(xpos=1600)
    nur "I’m sure she’ll appreciate it."
    show pov neutral at left
    show nur embarrassed_talk at Position(xpos=1400)
    nur "I gotta go, I have stuff to tend to."
    nur "Tell her Nurse Hollick is always watching, hehehe~"
    show nur neutral at Position(xpos=1400)
    show col smirk at Position(xpos=1600)
    show eff neutral_talk at Position(xpos=1800)
    eff "Bye, thank you."
    show eff bored_talk at Position(xpos=1800)
    eff "Alright, room 334."
    show pov smirk at left
    hide nur
    show col smirk_talk at Position(xpos=1600)
    show eff bored at Position(xpos=1800)
    with dissolve
    col "You sure it’s not room 344?"
    show pov  at left
    show col smirk at Position(xpos=1600)
    show eff shocked_talk at Position(xpos=1800)
    eff "Fuck-"
    show pov embarrassed at left
    show col smirk_talk at Position(xpos=1600)
    show eff bored at Position(xpos=1800)
    col "I’m joking, it’s 334."
    show pov embarrassed_talk at left
    show col smirk at Position(xpos=1600)
    pov "Are you sure?"
    show pov embarrassed at left
    show col embarrassed_talk at Position(xpos=1600)
    show eff  at Position(xpos=1800)
    col "…"
    show pov smirk at left
    show col bored_talk at Position(xpos=1600)
    col "Fuck."

    ## SCENE END

    $ main_story = 168

    jump lbl_questioning_erica
