## Meet Janae ##
label lbl_meet_janae:
    show pov neutral_talk at left
    with dissolve
    show jan neutral at right
    call lbl_retailstore_counter_check
    with dissolve
    pov "Hi."
    show pov neutral at left
    show jan neutral_talk at right
    jan "Hi, my name's Janae. I haven't seen you around before."
    jan "How can I help you today?"
    show pov neutral_talk at left
    show jan neutral at right
    pov "Yeah, I just moved in not too long ago."
    show pov neutral at left
    show jan neutral_talk at right
    jan "Oh, welcome to our town. I hope you like it here."
    show pov neutral_talk at left
    show jan neutral at right
    pov "Thanks."
    $ janae_path = 1
    $ add_contact("Janae")
    jump lbl_how_can_i_help_you_1
