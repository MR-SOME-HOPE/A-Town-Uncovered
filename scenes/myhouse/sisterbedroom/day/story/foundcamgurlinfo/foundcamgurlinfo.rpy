## Found Camgurl Info ##
label lbl_found_camgurl_info:
    if sister_path == 4:
        scene bg foundcamgurlinfo_1
        with fade
        pov "What is this..?"
        pov "..."
        pov "LittleBowPeep?"
        pov "This must've been what she texted before..."
        pov "..."
        pov "I should leave it where I found it so she doesn't get suspicious."
        $ sister_path = 5
        $ renpy.notify("New Objective: Watch [sister]'s stream")
    else:
        scene bg foundcamgurlinfo_1
        with fade
        $ renpy.pause()

    jump lbl_sisterbedroom_day_setup
