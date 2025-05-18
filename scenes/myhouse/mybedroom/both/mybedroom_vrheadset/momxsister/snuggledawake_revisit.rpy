## Snuggled Awake
label lbl_snuggled_awake_revisit:
    scene bg snuggledawake_1
    with fade

label lbl_snuggled_awake_revisit_hscene:
    show bg snuggledawake_1
    $ renpy.pause(0.3,hard=True)
    show bg snuggledawake_2
    $ renpy.pause(0.3,hard=True)
    show bg snuggledawake_3
    $ renpy.pause(0.3,hard=True)
    show bg snuggledawake_4
    $ renpy.pause(0.3,hard=True)
    show bg snuggledawake_2
    $ renpy.pause(0.3,hard=True)

    $ snuggledawake_counter += 1

    if snuggledawake_counter >= 10:
        show bg snuggledawake_5
        $ renpy.pause(0.2,hard=True)
        show bg snuggledawake_6
        $ renpy.pause(0.2,hard=True)
        show bg snuggledawake_5
        $ renpy.pause(0.2,hard=True)
        show bg snuggledawake_6
        $ renpy.pause(0.2,hard=True)
        show bg snuggledawake_5
        $ renpy.pause(0.5,hard=True)
        show bg snuggledawake_6
        $ renpy.pause(0.5,hard=True)
        show bg snuggledawake_5
        $ renpy.pause(1,hard=True)
        show bg snuggledawake_7
        $ renpy.pause(1,hard=True)
        show bg snuggledawake_8
        with hpunch

    else:
        jump lbl_snuggled_awake_revisit_hscene

    show bg snuggledawake_9
    mum "Morning, honey."
    show bg snuggledawake_10
    sis "Hope you didn’t mind, [povname]."
    show bg snuggledawake_11
    pov "..."
    show bg snuggledawake_12
    pov "What about me, do I get to finish?"
    show bg snuggledawake_13
    mum "Oh-"
    show bg snuggledawake_14
    sis "That’s a no from me, sir."
    show bg snuggledawake_15
    mum "Yeah, I’m with her. I’m exhausted."
    show bg snuggledawake_16
    pov "But it’s so hard… I really need to cum."
    show bg snuggledawake_17
    mum "Nawww…"
    show bg snuggledawake_14
    sis "Welp. Good luck with that."
    show bg snuggledawake_18
    mum "Hungry, baby?"
    show bg snuggledawake_14
    sis "Totally."
    show bg snuggledawake_18
    mum "I’ll make some French toast."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection
