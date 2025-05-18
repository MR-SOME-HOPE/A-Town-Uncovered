## Pet A Dog ##
label lbl_pet_a_dog:

    scene bg petadog_11
    if dog_points == 0:
        $ dog_points = 1
        pov "Hey, boy."
        show bg petadog_1
        pov "Whatcha' doing here?"
        pov "Where's your owner?"
        show bg petadog_11
        pov "I can't see a tag on you."
        pov "..."
        show bg petadog_1
        pov "You don't talk much, do you?"
        pov "..."
        show bg petadog_11
        pov "Ah well, I'll see you later then?"
        pov "Stay out of trouble, you fabulous son of a bitch."
    else:
        pov "Hey, boy."
        show bg petadog_1
        pov "Still no owner?"
        show bg petadog_11
        pov "I guess you just enjoy being a lone-wolf."
    show bg petadog_2
    $ renpy.pause(0.5,hard=True)
    show bg petadog_3
    $ renpy.pause(0.5,hard=True)
    show bg petadog_2
    $ renpy.pause(0.5,hard=True)
    show bg petadog_3
    $ renpy.pause(0.5,hard=True)
    if day == 0:
        show bg petadog_4
        $ renpy.pause()
    elif day == 1:
        show bg petadog_5
        $ renpy.pause()
    elif day == 2:
        show bg petadog_6
        $ renpy.pause()
    elif day == 3:
        show bg petadog_7
        $ renpy.pause()
    elif day == 4:
        show bg petadog_8
        $ renpy.pause()
    elif day == 5:
        show bg petadog_9
        $ renpy.pause()
    elif day == 6:
        show bg petadog_10
        $ renpy.pause()
    pov "Ooops.. sorry about that."
    show bg petadog_2
    $ renpy.pause(0.2,hard=True)
    show bg petadog_3
    $ renpy.pause(0.2,hard=True)
    show bg petadog_2
    $ renpy.pause(0.2,hard=True)
    show bg petadog_3
    $ renpy.pause(0.2,hard=True)
    show bg petadog_1
    $ renpy.pause()

    jump lbl_park_day_setup
