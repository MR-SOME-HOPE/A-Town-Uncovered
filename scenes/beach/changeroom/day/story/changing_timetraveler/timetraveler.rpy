label lbl_beachchangeroom_timetraveller:
    show changeroom timetraveller_1
    $ renpy.pause ()
    hide changeroom timetraveller_1
    show changeroom timetraveller_2
    $ renpy.pause ()
    show changeroom timetraveller_3
    pov "Uhm..."
    show changeroom timetraveller_2
    pov "Sorry...?"
    show changeroom timetraveller_4
    $ renpy.pause (0.1,hard=True)
    hide changeroom timetraveller_2
    hide changeroom timetraveller_3
    hide changeroom timetraveller_4
    $ renpy.pause (0.5,hard=True)
    pov "Whoa!! What the actual fuck just happened?"
    pov "Where did she go?"
    pov "..."
    pov "{i}I'll- just be on my merry way.{/i}"

    jump lbl_beachmain_day_setup
