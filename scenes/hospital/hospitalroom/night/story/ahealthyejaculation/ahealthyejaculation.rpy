## A Healthy Ejaculation ##
label lbl_a_healthy_ejaculation:

    scene bg hospitalroom_night_lightson_closed
    with fade
    show povn embarrassed at left
    with dissolve
    show nursw bored_talk at right
    with dissolve
    nur "Well, I've marked down the results of your sperm sample."
    show povn confused_talk at left
    show nursw sad at right
    pov "And?"
    show povn sad at left
    show nursw sad_talk at right
    nur "You've got severe internal bleeding in your cranium."
    show povn sad_talk at left
    show nursw sad at right
    pov "What?! Really?"
    show povn bored at left
    show nursw neutral_talk at right
    nur "No, you idiot. It's a sperm sample. Just because I'm a nurse doesn't mean I can't make jokes."
    show povn bored at left
    show nursw smirk_talk at right
    nur "Hahahaha!"
    show povn bored at left
    show nursw neutral_talk at right
    nur "Anyways, you have nothing to worry about. Everything's fine. You may go home now."
    show povn bored_talk at left
    show nursw neutral at right
    pov "Really? That's it? You're not actually going to check my head for injuries?"
    show povn bored at left
    show nursw neutral_talk at right
    nur "Nope. As you said so yourself, you didn't hit your head on anything, you're fine."
    nur "The hospital has all the information we need."
    show povn confused_talk at left
    show nursw neutral at right
    pov "Well, alrighty then. Thanks for that, Nurse Hollick."
    $ renpy.notify("New Objective: Get back home")
    $ renpy.pause(3,hard=True)
    $ renpy.notify("New Contact: Nurse Hollick")
    $ renpy.pause(3,hard=True)
    $ main_story = 28
    $ gtime = 3

    jump lbl_townmap_setup
