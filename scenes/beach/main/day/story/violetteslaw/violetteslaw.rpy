## Violette's Law
label lbl_violettes_law:
    ## BG of the beach with crowd
    scene bg beachmain_day
    with fade

    show pov neutral at left
    show vio angry_talk  at right
    with dissolve
    vio "[povname]-"
    vio "Are you done?"
    show pov confused at left
    show vio angry_talk at right
    vio "Can I speak to you- later?"
    show pov confused_talk at left
    show vio bored at right
    pov "l-"
    show pov embarrassed_talk at left
    pov "Yeah, sure…"
    show pov embarrassed at left
    show vio bored_talk at right
    vio "Go and clean yourself off and help me get everyone to stop crowding."
    show pov smirk_talk at left
    show vio bored at right
    pov "Okay, yes, boss."
    show pov neutral at left
    show vio angry_talk at right
    vio "Hmmmph."

    ## Fade to black
    stop music fadeout 2.0
    play ambience 'audio/ambience/quietexteriornight_ambience.ogg' fadein 2.0
    
    scene black
    with fade
    $ renpy.pause()
    "Later when the sun has set…"

    $ gtime = 2

    scene bg beachmain_night

    show pov embarrassed at left
    show vio confused_talk at right
    with dissolve
    vio "…"
    show pov embarrassed_talk at left
    show vio confused at right
    pov "…"
    show pov confused_talk at left
    pov "You wanted to talk to me?"
    show pov bored at left
    show vio confused_talk at right
    vio "Mm…"
    show pov embarrassed_talk at left
    show vio smirk at right
    pov "…"
    show pov confused_talk at left
    pov "So…"
    show pov shocked at left
    show vio smirk_talk at right
    vio "You’re so stupid."
    show pov shocked_talk at left
    show vio bored at right
    pov "What?!"
    show pov confused at left
    show vio shocked_talk at right
    vio "You’re stupid and an asshole."
    show pov confused_talk at left
    show vio confused at right
    pov "What? Is it because-"
    show pov confused at left
    show vio angry_talk at right
    vio "YES!"
    show pov confused_talk at left
    show vio angry at right
    pov "Are you mad?"
    show pov confused at left
    show vio shocked_talk at right
    vio "You’re unbelievable."
    show pov shocked at left
    show vio smirk_talk at right
    vio "You really just do what you want, don’t you?"
    show pov smirk_talk at left
    show vio bored at right
    pov "I didn’t think you’d care since we’re not exclusive."
    show pov smirk at left
    show vio bored_talk at right
    vio "Yeah- we’re not…"
    show vio smirk_talk at right
    vio "So, I guess it’s my fault, I’m the asshole."
    show pov embarrassed at left
    show vio bored_talk at right
    vio "*Sigh*"
    vio "I know we’re not exclusive or even official for that matter."
    show pov shocked at left
    show vio confused_talk at right
    vio "But I still had some feelings and cared for you so yes."
    show pov smirk at left
    show vio bored_talk at right
    vio "I admit, it did hurt when you were gearing to fuck that bitch."
    show pov smirk_talk at left
    show vio bored at right
    pov "…"
    show pov embarrassed_talk at left
    pov "I dunno what you want me to say."
    show vio confused at right
    pov "I’m sorry if I hurt your feelings."
    show pov neutral_talk at left
    show vio smirk at right
    pov "It genuinely isn’t what I was intending to do."
    show pov neutral at left
    show vio smirk_talk at right
    vio "No, I’m sorry for even bringing this up."
    show pov confused at left
    show vio shocked_talk at right
    vio "Maybe my emotions got the best of me today."
    show vio neutral_talk at right
    vio "I shouldn’t be blaming you."
    show pov bored_talk at left
    show vio confused at right
    pov "I didn’t expect to see Ara Asika today."
    show pov confused at left
    show vio confused_talk at right
    vio "Haven’t even heard of her until today."
    show vio shocked_talk at right
    vio "It was…"
    show vio bored_talk at right
    vio "Quite the performance she gave the crowd."
    show pov embarrassed at left
    show vio smirk_talk at right
    vio "Felt like I was at a sporting stadium."
    show pov embarrassed_talk at left
    show vio smirk at right
    pov "Yeah, I had a bit of performance anxiety."
    show vio neutral_talk at right
    vio "I think you did well, my trainee."
    vio "Although, I do need to punish you for getting distracted from your training and duties."
    show pov smirk at left
    show vio bored_talk at right
    vio "I can’t let that go unpunished otherwise you’d be fooling around too often."
    show pov smirk_talk at left
    show vio bored at right
    pov "That’s- fine."
    show pov neutral_talk at left
    show vio smirk at right
    pov "I’ll take it, worth it."
    show pov neutral at left
    show vio smirk_talk at right
    vio "Oh, is it?"
    show pov confused at left
    vio "Come with me."

    scene black
    with fade
    $ renpy.pause()

    ## SCENE ENDS

    $ violette_path = 14

    jump lbl_violettes_punishment
