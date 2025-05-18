## She's At My House Part 1 ##
label lbl_shes_at_my_house_pt1:
    mum "[povname]!"
    pov "Huh?!"
    pov "..."
    pov "Yeaaah?!"
    pov "..."
    mum "[povname]! I'm calling y-"
    if winc == 1:
        pov "What, Mom?!"
    else:
        pov "What, [missus]?!"
    mum "Get down here! There's someone at the door for you!"
    pov "W-what?"
    pov "Who's that?"
    pov "..."
    $ sister_path = 27.5
    $ townmap_enabled = 0

    jump lbl_mybedroom_day_setup
