## Lack of Water
label lbl_lack_of_water:
    ## CG of Violette in the hospital bed

    stop music fadeout 2.0
    play ambience 'audio/ambience/quietexteriorday_ambience.ogg' fadein 2.0

    scene bg hospitalroom_day
    with fade
    show pov embarrassed at left
    show vioc bored at right
    with dissolve
    vio "*Grumbles*"
    show vioc bored_talk
    vio "W-what happened?"

    show pov shocked_talk
    show vioc sad
    pov "Oh good- you’re okay."
    show pov sad_talk
    show vioc sad
    pov "You passed out, Vi."

    show pov embarrassed
    show vioc confused_talk
    vio "Did I?"
    show vioc sad_talk
    vio "Shit…"
    show vioc embarrassed_talk
    vio "That’s embarrassing…"

    show pov sad_talk
    show vioc embarrassed
    pov "Yeah, right in the middle of the beach, luckily some people were able to help and get you here."
    pov "We didn’t wanna risk anything in case it was something serious."

    show pov sad
    show vioc confused_talk
    vio "What was it? Heatstroke?"

    show pov sad_talk
    show vioc sad
    pov "Yup, that’s what the nurse said."
    show pov confused_talk
    pov "Didn’t you drink enough water?"

    show pov confused
    show vioc sad_talk
    vio "*Groan*"
    show vioc confused_talk
    vio "Ugh, I thought I did…"
    show vioc embarrassed_talk
    vio "I guess it wasn’t enough."
    vio "I underestimated how much the heat would affect me today."

    show pov confused_talk
    show vioc embarrassed
    pov "Which is unusual for you I would think."
    pov "Is there something else going on?"

    show pov confused
    show vioc sad_talk
    vio "*Sigh*"
    vio "I don’t know-"
    vio "I just, had a lot on my mind, I guess."
    vio "I forgot to take in enough liquids…"
    vio "Grrgh-"
    show pov embarrassed
    show vioc bored_talk
    vio "What’s with the sudden interrogation, I just woke up."

    show pov embarrassed_talk
    show vioc bored
    pov "You’re right, I apologize."
    pov "You should rest some more."
    pov "I’m glad you’re okay."

    show pov shocked
    show vioc bored_talk
    vio "We should get to work."

    show pov embarrassed
    show vioc confused
    nur "I would advise against that, miss."
    show nur neutral_talk
    nur "You really need to rest here overnight at least."

    show pov embarrassed
    show nur smirk
    show vioc confused_talk
    vio "Is that an order or a suggestion, Nurse."

    show pov sad_talk
    show nur smirk
    show vioc confused
    pov "C’mon, Violette."
    pov "You really scared me today."
    show nur neutral
    pov "It’s best to look after yourself for a change instead of others."
    pov "It’s what’s best."

    show pov shocked
    show nur neutral_talk
    show vioc bored
    nur "Listen to your boyfriend…"

    show pov embarrassed
    show nur neutral
    show vioc bored_talk
    vio "He’s-"
    vio "We’re not dating!"
    show vioc bored
    vio "..."
    show vioc bored_talk
    vio "But fine."
    vio "Just for tonight."
    vio "But going forward, I’m making sure this doesn’t happen again."
    show vioc sad_talk
    vio "I really can’t believe I fainted during my watch."
    vio "That’s so weak of me."

    show pov embarrassed
    show nur neutral_talk
    show vioc embarrassed
    nur "I wouldn’t have it any other way."
    nur "Especially on extra hot days, you must be extra wary of your body’s condition."

    show nur neutral
    show vioc bored_talk
    vio "*Sigh*"
    vio "Can’t believe I’m being lectured about this…"
    vio "I mean no disrespect to you, nurse."
    vio "But it really is embarrassing as the town’s lifeguard."
    vio "I really should’ve known better."
    vio "Thank you for taking care of me."

    show pov embarrassed
    show nur neutral_talk
    show vioc bored
    nur "I’ll leave you two to rest, just call me if you need anything."

    hide nur
    with dissolve
    show pov embarrassed
    show vioc bored_talk
    vio "Right."

    show pov neutral_talk
    show vioc embarrassed
    pov "I’ll look after the beach today, Violette."
    pov "If it helps keep your mind at ease."
    pov "I’ll make sure everyone abides by the rules and that people don’t get in situations that could lead to any risky rescues."

    show pov neutral
    show vioc embarrassed_talk
    vio "Are you sure?"
    vio "I mean- that would really help put my mind at ease."

    show pov neutral_talk
    show vioc embarrassed
    pov "You’ve trained me well so far, Vi."
    pov "I can manage a day."

    show pov neutral
    show vioc neutral
    vio "..."
    show pov embarrassed
    show vioc smirk_talk
    vio "I trust you, [povname]."
    vio "Don’t hesitate to be strict with anyone if it means keeping the beach safe and under control."

    show pov neutral_talk
    show vioc smirk
    pov "Understood."
    pov "I hope to see you tomorrow."

    show pov neutral
    show vioc neutral_talk
    vio "Sounds good."
    show vioc sad_talk
    vio "*Sigh*"
    show vioc embarrassed_talk
    vio "I can’t help but feel so pathetic right now."

    show pov embarrassed_talk
    show vioc embarrassed
    pov "You aren’t."
    pov "As you said, you just underestimated the heat today."
    pov "We’re all human, you must’ve also overexerted yourself."

    show pov embarrassed
    vio "Mmm..."

    show pov neutral_talk
    show vioc embarrassed
    pov "I’ll take my leave."
    pov "I’ll report in tomorrow."
    
    show pov neutral
    show vioc embarrassed_talk
    vio "Good luck."

    scene black
    with fade
    $ renpy.pause()
    "After returning to the beach and watching over it for the day..."

    $ violette_path = 7.9

    $ gtime = 3

    scene bg beachmain_night
    with fade
    jump lbl_beachmain_night_setup
