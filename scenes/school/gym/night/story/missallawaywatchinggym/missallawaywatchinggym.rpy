## Miss Allaway Watching Gym ##
label lbl_miss_allaway_watching_gym:

    scene bg schoolgymdoor_night
    with hpunch
    pov "Miss Allaway?!"
    show pov confused at left
    with dissolve
    show mis embarrassed_talk at right
    with dissolve
    mis "Oh! H-hey... there..."
    mis "I was just uh... I wanted to see what was going on in there."
    show pov confused_talk at left
    show mis embarrassed at right
    pov "It's uh..."

    menu:
        "It's a fight club.":
            show pov embarrassed_talk at left
            show mis confused at right
            pov "It's a fight club"
        "It's a dance off.":
            show pov embarrassed_talk at left
            show mis confused at right
            pov "It's a dance off."
        "It's a heated debate on climate change.":
            show pov embarrassed_talk at left
            show mis confused at right
            pov "It's a heated debate on climate change."
    show pov embarrassed at left
    show mis confused_talk at right
    mis "Oh..? Is it now?"
    show pov embarrassed_talk at left
    show mis confused at right
    pov "Yeah, It's actually really intense."
    show pov neutral at left
    show mis confused_talk at right
    mis "I can see that, [povname]."
    show mis confused at right
    pov "..."
    show pov confused_talk at left
    show mis embarrassed at right
    pov "How long have you been standing here?"
    show pov confused at left
    show mis embarrassed_talk at right
    mis "What?! I just got here. It's not like I wasn't watching or anything."
    show pov confused at left
    show mis sad_talk at right
    mis "Which I wasn't."
    show pov confused_talk at left
    show mis embarrassed at right
    pov "Alright, if you say so."
    show pov confused at left
    show mis sad_talk at right
    mis "Don't think I was like, feeling hot from all the action or anything."
    show pov confused_talk at left
    show mis shocked at right
    pov "Huh?"
    show pov confused at left
    show mis shocked_talk at right
    mis "Because I wasn't!"
    show pov confused_talk at left
    show mis shocked at right
    pov "Miss..."
    show pov confused at left
    show mis embarrassed_talk at right
    mis "Huh!? What?"
    show mis angry_talk at right
    mis "C'mon, [povname]. Get out here and close the door."
    $ missallaway_path = 1
    $ townmap_enabled = 1

    jump lbl_why_am_i_in_trouble
