## Caught My Parents ##
label lbl_caught_my_parents:
    if winc == 0:
        jump lbl_caught_my_parents_winc0

    scene bg caughtmyparents_4
    with fade
    $ renpy.pause(0.8, hard=True)
    show bg caughtmyparents_5
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show bg caughtmyparents_6
    $ renpy.pause()
    show bg caughtmyparents_1
    $ renpy.pause(0.6, hard=True)
    show bg caughtmyparents_2
    $ renpy.pause(0.6, hard=True)
    show bg caughtmyparents_1
    $ renpy.pause(0.6, hard=True)
    show bg caughtmyparents_2
    $ renpy.pause(0.6, hard=True)
    show bg caughtmyparents_3
    with hpunch
    dad "Hey! We're busy here!"

    menu:
        "Mom! What are you doing?":
            pov "Mom! What the hell are you doing?!"
            dad "Hey! [povname]! What did I just say, get the fuck upstairs and leave us be."

            jump lbl_caught_my_parents_1
        "Why are you doing it out here?":
            pov "Why the fuck are you doing it out here?!"
            dad "My house, my rules. I can do what I want whenever and to whomever."

            jump lbl_caught_my_parents_1
        "Sorry..":
            pov "Oh my God.. sorry..."
            dad "Just get the fuck upstairs."

            jump lbl_caught_my_parents_1

label lbl_caught_my_parents_1:

    scene bg caughtmyparents_7
    $ renpy.pause(0.8, hard=True)

    scene bg caughtmyparents_8
    $ renpy.pause(0.2, hard=True)

    scene bg caughtmyparents_4
    $ renpy.pause()
    mum "[povname]!"
    mum "Ugh.. Honey, I'm sorry but I... we have to stop now."
    dad "Are you serious?"
    mum "Just.. just for a second. I have to make sure he's okay."
    dad "Fuck! Fine."
    dad "I'm gonna fuck your throat when you come back though."
    $ mum_path = 8

    jump lbl_mybedroom_night_setup

### NO WINC ###
label lbl_caught_my_parents_winc0:

    scene bg caughtmyparents_4
    with fade
    $ renpy.pause(0.8, hard=True)
    show bg caughtmyparents_5
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show bg caughtmyparents_6
    $ renpy.pause()
    show bg caughtmyparents_1
    $ renpy.pause(0.6, hard=True)
    show bg caughtmyparents_2
    $ renpy.pause(0.6, hard=True)
    show bg caughtmyparents_1
    $ renpy.pause(0.6, hard=True)
    show bg caughtmyparents_2
    $ renpy.pause(0.6, hard=True)
    show bg caughtmyparents_3
    with hpunch
    dad "Hey! We're busy here!"

    menu:
        "[missus]! What are you doing?":
            pov "[missus]! What the hell are you doing?!"
            dad "Hey! [povname]! What did I just say, get the fuck upstairs and leave us be."

            jump lbl_caught_my_parents_1_winc0
        "Why are you doing it out here?":
            pov "Why the fuck are you doing it out here?!"
            dad "My house, my rules. I can do what I want whenever and to whomever."

            jump lbl_caught_my_parents_1_winc0
        "Sorry..":
            pov "Oh my God.. sorry..."
            dad "Just get the fuck upstairs."

            jump lbl_caught_my_parents_1_winc0

label lbl_caught_my_parents_1_winc0:

    scene bg caughtmyparents_7
    $ renpy.pause(0.8, hard=True)

    scene bg caughtmyparents_8
    $ renpy.pause(0.2, hard=True)

    scene bg caughtmyparents_4
    $ renpy.pause()
    mum "[povname]!"
    mum "Ugh.. Honey, I'm sorry but I... we have to stop now."
    dad "Are you serious?"
    mum "Just.. just for a second. I have to make sure he's okay."
    dad "Fuck! Fine."
    dad "I'm gonna fuck your throat when you come back though."
    $ mum_path = 8

    jump lbl_mybedroom_night_setup
