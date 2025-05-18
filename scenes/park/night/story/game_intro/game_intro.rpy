## Game Intro Cutscene ##
label intro_cutscene:

    scene bg intro_cutscene_1
    with fade
    $ renpy.pause ()

    scene bg intro_cutscene_2
    with fade
    $ renpy.pause ()

    scene bg intro_cutscene_3
    with fade
    pov "One mile... done."

    scene bg intro_cutscene_4
    pov "{i}How long did I take? Oh, wow! New record?{/i}"

    scene bg intro_cutscene_5
    $ renpy.pause (1,hard=True)

    scene bg intro_cutscene_6
    $ renpy.pause (1,hard=True)

    scene bg intro_cutscene_7
    $ renpy.pause (0.5,hard=True)

    scene bg intro_cutscene_8
    $ renpy.pause (1,hard=True)

    scene bg intro_cutscene_9
    $ renpy.pause (1,hard=True)

    scene bg intro_cutscene_10
    $ renpy.pause (3,hard=True)

    scene bg intro_cutscene_11
    pov "{i}What the hell was that?{/i}"

    scene bg intro_cutscene_10
    pov "{i}Maybe I was just seeing things. I do feel a little lightheaded from my run after all.{/i}"
    pov "{i}Maybe I should get back home before I get shanked or something.{/i}"

    scene black
    with fade

    scene bg park_night
    with fade
    $ main_story = 1
    $ renpy.notify("Sunday Night")
    $ renpy.pause(3,hard=True)
    $ renpy.notify("New Objective: Head home")
    $ renpy.pause(3,hard=True)

    jump lbl_park_night_setup
