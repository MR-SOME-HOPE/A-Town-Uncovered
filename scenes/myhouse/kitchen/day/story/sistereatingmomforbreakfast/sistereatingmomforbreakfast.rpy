## Sister Eating Mom for Breakfast
default sistereatingmomforbreakfast_counter = 0

label lbl_sister_eating_mom_for_breakfast:
    scene bg sistereatingmomforbreakfast_1
    with fade
    $ renpy.pause()
    show bg sistereatingmomforbreakfast_2
    pov "Morning, [missus]."
    show bg sistereatingmomforbreakfast_3
    mum "Morning, sweetie."
    show bg sistereatingmomforbreakfast_4
    pov "[sister]’s out?"
    show bg sistereatingmomforbreakfast_5
    mum "Yup, she got up early today, she had a…"
    mum "She had a tough time sleeping last night."
    show bg sistereatingmomforbreakfast_6
    pov "Work’s really messing with her sleep schedule."
    pov "She should get some sleeping pills."
    show bg sistereatingmomforbreakfast_7
    mum "She’s too young for sleeping pills."
    show bg sistereatingmomforbreakfast_4
    pov "It’s just the over-the-counter stuff. Nothing strong, just something to help."
    show bg sistereatingmomforbreakfast_6
    mum "Mm.."
    show bg sistereatingmomforbreakfast_5
    mum "I’ll look into getting some for her."
    show bg sistereatingmomforbreakfast_6
    pov "Hm, alright."
    show bg sistereatingmomforbreakfast_7
    mum "Heading out now?"
    show bg sistereatingmomforbreakfast_8
    pov "Yeah, I’m late for school."
    show bg sistereatingmomforbreakfast_3
    mum "Well, make sure you eat something there, baby."
    show bg sistereatingmomforbreakfast_2
    pov "Will do, [missus]."
    show bg sistereatingmomforbreakfast_3
    mum "I love you, my little BB-gun."
    show bg sistereatingmomforbreakfast_9
    pov "Love you too, [missus]."
    show bg sistereatingmomforbreakfast_2
    mum "..."
    "{i}*Door Thuds*{/i}"
    show bg sistereatingmomforbreakfast_10
    mum "Okay, baby, he's gone."

    scene bg sistereatingmomforbreakfast_11
    with dissolve
    mum "Oh my god, that was close."
    sis "Mm- lucky he was rushing out the door, aye?"
    show bg sistereatingmomforbreakfast_15
    mum "Speaking of, shouldn’t you be heading out as well?"
    show bg sistereatingmomforbreakfast_16
    sis "Do you want me to stop?"
    show bg sistereatingmomforbreakfast_12
    mum "Finish your breakfast, honey."
    show bg sistereatingmomforbreakfast_13
    mum "I’m really close."
    show bg sistereatingmomforbreakfast_14
    sis "Mhmm…"
    show bg sistereatingmomforbreakfast_15
    mum "Ahh-"

label lbl_sister_eating_mom_for_breakfast_licking:
    show bg sistereatingmomforbreakfast_12
    $ renpy.pause(0.5,hard=True)
    show bg sistereatingmomforbreakfast_13
    $ renpy.pause(0.5,hard=True)
    show bg sistereatingmomforbreakfast_14
    $ renpy.pause(0.5,hard=True)
    show bg sistereatingmomforbreakfast_15
    $ renpy.pause(0.7,hard=True)
    $ sistereatingmomforbreakfast_counter +=1

    if sistereatingmomforbreakfast_counter >= 10:
        pass
    else:
        jump lbl_sister_eating_mom_for_breakfast_licking

    scene bg myhousefront_day
    with fade
    $ renpy.pause()

    $ mumsis_path = 9

    jump lbl_myhousefront_day
