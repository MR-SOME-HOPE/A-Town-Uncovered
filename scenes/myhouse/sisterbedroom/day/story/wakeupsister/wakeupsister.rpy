## Wake Up Sister ##
label lbl_wake_up_sister:

    scene bg wake_up_sister_1
    with fade
    pov "Hey, wake up..."
    show bg wake_up_sister_2
    sis "Mrmm..."
    show bg wake_up_sister_1
    pov "Time to wake up."
    show bg wake_up_sister_2
    sis "Mhmmm..."
    show bg wake_up_sister_1
    pov "Can you hear me or not? I said wake up!"
    show bg wake_up_sister_3
    sis "Jsst fyy mm minutes.."
    show bg wake_up_sister_1
    pov "Ugh... C'mon!"
    call screen scr_wake_up_sister_2

screen scr_wake_up_sister_2():
    add "bg wake_up_sister_1"
    imagebutton auto "btn wake_up_sister_sheet_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_wake_up_sister_1")

label lbl_wake_up_sister_1:
    show bg wake_up_sister_4
    $ renpy.pause (1,hard=True)
    show bg wake_up_sister_5
    $ renpy.pause (1,hard=True)
    show bg wake_up_sister_6
    with hpunch
    sis "GET OUTT!"
    pov "Ahh! Sorry!"

    scene bg myhallway_day
    with fade
    pov "{i}Uhm.. let's not go back in there for a while.{/i}"
    $ main_story = 4

    jump lbl_myhallway_day_setup
