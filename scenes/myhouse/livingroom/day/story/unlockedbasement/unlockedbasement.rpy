## Unlocked Basement ##
label lbl_unlocked_basement:

    scene bg lockedbasement_14
    with fade
    $ renpy.pause(0.6,hard=True)
    show bg lockedbasement_15
    $ renpy.pause(0.6,hard=True)
    show bg lockedbasement_14
    $ renpy.pause(0.6,hard=True)
    show bg lockedbasement_15
    $ renpy.pause(0.6,hard=True)
    show bg lockedbasement_16
    pov "I got it!"
    show bg lockedbasement_17
    pov "Hey, [sister]! I got it opened!"
    show bg lockedbasement_18
    pov "Who's your daddy?"
    show bg lockedbasement_19
    sis "You got it?!"
    sis "Let me through! I get first dibs on whatever's inside."

    jump lbl_basement_plans
