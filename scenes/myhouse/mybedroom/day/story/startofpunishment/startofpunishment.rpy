## Start of Punishment

label lbl_start_of_punishment:
    scene black
    with fade
    $ renpy.pause()
    scene bg startofpunishment_1
    with dissolve
    scene black
    with fade
    $ renpy.pause()
    scene bg startofpunishment_1
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg startofpunishment_2
    sis "Heeey!"
    show bg startofpunishment_3
    pov "[sister]!"
    pov "Ah- get off me, it’s hard to breathe."
    show bg startofpunishment_4
    sis "Really? You were breathing fine when you were sleeping."
    show bg startofpunishment_3
    pov "Ugh- what are you doing here."
    show bg startofpunishment_5
    sis "I’m your wakeup call. I’m here to make sure you keep your pants off."
    show bg startofpunishment_3
    pov "You’re so fuckin’ weird."
    show bg startofpunishment_4
    sis "Am I?"
    sis "We’ll see about that later."
    show bg startofpunishment_6
    pov "Where’s [missus]?"
    show bg startofpunishment_7
    sis "She’s still asleep."
    show bg startofpunishment_4
    sis "But we came up with a to-do list for you today. Wanted to give it to you personally."
    show bg startofpunishment_3
    pov "How thoughtful…"
    show bg startofpunishment_8
    pov "..."
    pov "{i}*Sigh*{/i}"
    pov "Fine, let’s get this over with."
    sis "Wait, I need to check to make sure [missus]’s awake."
    sis "She’ll wanna… evaluate your progress."

    scene black
    with fade
    #"Developer Note: The some art assets for these scenes are yet to be completed."

    ## Dishes
    scene bg startofpunishment_dishes
    with fade
    $ renpy.pause()

    ## Vaccuum
    scene bg startofpunishment_vaccuum
    with fade
    $ renpy.pause()

    ## Dusting
    scene bg startofpunishment_dusting
    with fade
    $ renpy.pause()

    ## Mowing
    scene bg startofpunishment_chores_4
    with fade
    $ renpy.pause(1,hard=True)
    scene bg startofpunishment_chores_4_2
    with dissolve
    $ renpy.pause(1,hard=True)
    scene bg startofpunishment_chores_4_3
    with dissolve
    $ renpy.pause(1,hard=True)
    scene bg startofpunishment_chores_4_4
    with dissolve
    $ renpy.pause(1,hard=True)
    scene bg startofpunishment_chores_4_5
    with dissolve
    $ renpy.pause()

    ## Cooking
    scene bg startofpunishment_chores_5
    with fade
    $ renpy.pause()
    scene bg startofpunishment_chores_5_2
    with hpunch
    $ renpy.pause()

    # "-Fade to washing dishes task, mom and sister are eating breakfast while you’re washing dishes in front of them, he has a hard on and they make fun of him-"
    #
    # "-Then in the living room for vacuuming, sister is on her phone with legs over mom and mom on reading a magazine as they take glances at the MC, they’re eyes are swaying with his cock as he moves back and forth-"
    #
    # "-Then they’re cuddled up on the couch as MC dusts the TV, Mom’s in the background touching sister while the MC isn’t looking-"
    #
    # "-Then they’re sitting outside with drinks mowing watching the MC mow the lawn. Finally the lawn is mowed-"
    #
    # "-Then they’re in the kitchen, mom squeezes your butt as you stir the stew while wearing a pink apron. Sister watches from the bench-"

    scene black
    with fade
    $ renpy.pause()
    "Later that night..."

    $ gtime = 2
    $ mowed_lawn = 1

    jump lbl_end_of_punishment

image bg startofpunishment_dishes:
    "/scenes/myhouse/mybedroom/day/story/startofpunishment/assets/bg_startofpunishment_chores_1.jpg"
    pause 0.3
    "/scenes/myhouse/mybedroom/day/story/startofpunishment/assets/bg_startofpunishment_chores_1_2.jpg"
    pause 0.3
    repeat

image bg startofpunishment_vaccuum:
    "/scenes/myhouse/mybedroom/day/story/startofpunishment/assets/bg_startofpunishment_chores_2.jpg"
    pause 0.3
    "/scenes/myhouse/mybedroom/day/story/startofpunishment/assets/bg_startofpunishment_chores_2_2.jpg"
    pause 0.3
    repeat

image bg startofpunishment_dusting:
    "/scenes/myhouse/mybedroom/day/story/startofpunishment/assets/bg_startofpunishment_chores_3.jpg"
    pause 0.3
    "/scenes/myhouse/mybedroom/day/story/startofpunishment/assets/bg_startofpunishment_chores_3_2.jpg"
    pause 0.3
    repeat
