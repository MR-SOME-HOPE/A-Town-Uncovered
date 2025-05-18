## Sister Passed Out

label lbl_sister_passed_out:
    scene bg passedoutsister_1
    with fade
    $ renpy.pause(0.8,hard=True)
    show bg passedoutsister_2
    $ renpy.pause(0.8,hard=True)
    show bg passedoutsister_1
    $ renpy.pause(0.8,hard=True)
    show bg passedoutsister_2
    $ renpy.pause(0.8,hard=True)
    show bg passedoutsister_1
    $ renpy.pause(0.8,hard=True)
    show bg passedoutsister_2
    $ renpy.pause(0.8,hard=True)
    show bg passedoutsister_3
    with dissolve
    pov "{i}*Whisper*{/i} Hey."
    show bg passedoutsister_4
    mum "{i}*Whisper*{/i} Shhh, [sister]’s sleeping."
    show bg passedoutsister_3
    pov "I can see that."
    show bg passedoutsister_4
    mum "What do you want?"
    show bg passedoutsister_3
    pov "Oh nothing, just wanted to see if she’s alright, I’ve never seen her sleep on your lap before."
    show bg passedoutsister_5
    mum "She was just stressed with work and passed out while we were watching."
    show bg passedoutsister_6
    mum "It’s cute, isn’t it?"
    show bg passedoutsister_7
    pov "I guess."
    show bg passedoutsister_4
    mum "Best just leave us be before she wakes up from our voices."
    show bg passedoutsister_8
    sis "{i}*Mumble*{/i} Mmuuh- uhhh..."
    show bg passedoutsister_9
    sis "{i}*Mumble*{/i} Eeepnn…"
    show bg passedoutsister_3
    pov "Oop- alright, g’night, [missus]."
    show bg passedoutsister_10
    mum "Good night, sweetie. I love you."
    show bg passedoutsister_11
    pov "I love you too."

    $ mumsis_path = 2

    jump lbl_mykitchen_night
