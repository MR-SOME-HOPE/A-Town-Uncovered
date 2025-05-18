## Places Everyone
label lbl_places_everyone:
    ## Everyone is getting seated.

    ## Effie and Edward sit together at the back of the rows of pews in the
    # church-like hall.
    scene bg placeseveryone_1
    with fade

    eff "Ed, let's just sit here in the back near the door."
    eff "It's the best for escaping."

    edw "Good call."

    pov "Boys, I need you to come with me, we gotta sneak off on the side and close to the stage."
    pov "When I give the signal, we attack him from behind and hold him down."
    pov "He may be strong but there’s three of us."

    jac "Got it."

    col "Go go go."
    col "Get behind the curtains before anyone notices."

    ## The 3 guys head over to the side of the hall and hide behind the decorative
    # curtains, using it to make their way up the room towards the stage.
    show bg placeseveryone_2_1
    $ renpy.pause(1,hard=True)
    show bg placeseveryone_2_2
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg placeseveryone_2_3
    with dissolve
    $ renpy.pause(1,hard=True)
    show bg placeseveryone_2_4
    with dissolve
    $ renpy.pause(1,hard=True)

    ## SCENE ENDS

    $ main_story = 175

    jump lbl_a_hypnotic_trance
