## Tutoring Afterschool ##
label lbl_tutoring_afterschool:
    scene bg classroom_day
    show btn_classroom_day_missallaway_idle2
    show btn_classroom_day_luna_idle2
    $ renpy.pause(0.001)
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral at right
    with dissolve
    pov "Hey, Miss. I'm here for our one-on-one."
    if day <= 3:
        pass
    else:
        show pov confused at left
        show mis sad_talk at right
        mis "Oh- I'm sorry, [povname]. I actually have something important later."
        show pov smirk at left
        show mis bored_talk at right
        mis "A boring meeting but important none-the-less."
        show pov neutral_talk at left
        show mis embarrassed at right
        pov "Hakuna Matata, Miss Allaway. I guess we can do it next week."
        show pov neutral at left
        show mis neutral_talk at right
        mis "You bet cha'. I'll make sure to schedule you in sometime."

        jump lbl_classroom_day_setup
    show pov neutral at left
    show mis neutral_talk at right
    mis "Oh, fantastic. Give me second while I fix up my desk."

    scene bg tutoringafterschool_1
    with fade
    mis "So by using this quote, followed with an explanation such as this over here."
    mis "It creates a much more impactful effect on the reader. AKA, me."
    show bg tutoringafterschool_2
    pov "Oh, I understand now."
    show bg tutoringafterschool_1
    mis "Great, now let's move onto using more advanced vocabulary to replace the ones you're repeating over and over again."
    show bg tutoringafterschool_2
    pov "Weren't you the one that said it's better to keep things simple-stupid than to confuse the reader?"
    show bg tutoringafterschool_1
    mis "That goes for structuring sentences length."
    show bg tutoringafterschool_2
    pov "Oh, I understand now."
    show bg tutoringafterschool_1
    mis "Terrific!"
    $ skill_int += 1
    if skill_int > skill_intmax:
        $ skill_int = skill_intmax
    $ renpy.notify("You gained an Intelligence Point")

    scene black
    with fade
    "After a while..."

    scene bg classroom_dayempty
    with fade
    show pov neutral_talk at left
    with dissolve
    show mis neutral at right
    with dissolve
    pov "Thanks, Miss Allaway."
    show mis confused at right
    pov "I really did learn a lot more just then than all the classes I've had so far."
    show pov neutral at left
    mis "..."
    show pov embarrassed_talk at left
    show mis smirk at right
    pov "N-not saying that those classes were bad! I-I just mean that-"
    show pov neutral at left
    show mis smirk_talk at right
    mis "No, don't worry. I know what you mean. I'm just joking around."
    show mis neutral_talk at right
    mis "I'm glad you found this tutor session a big help."
    show mis smirk_talk at right
    mis "Compliments to the teacher! Hahaha."
    show mis neutral_talk at right
    mis "I'll walk you outside."

    jump lbl_locked_in_school
