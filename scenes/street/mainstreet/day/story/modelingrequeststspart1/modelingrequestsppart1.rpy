## MODELLING REQUESTS
default modeling_requests_asked_effie = 0
default modeling_request_people_asked_count = 0

label lbl_modelling_requests_part1:


    $ map_enabled = 1
    #default modeling_requests_asked_girl1 = 0
    #default modeling_requests_asked_girl2 = 0
    #default modeling_requests_asked_girl3 = 0

    #[Street in front of comic book shop, Afternoon - “Modeling requests part 1”
    # - hitomi_path = 16]#13.5
    #-Scene takes place as soon as getting back on the street with the Mc talking
    # to himself-

    scene bg street_day with fade

            ## SPRITEWORK ##

    show pov shocked_talk at left
    with dissolve
    pov "Alright, gotta be quick about this, so don’t really have time to plan this out too much."
    show pov smirk_talk at left
    pov "Knowing this town, there is bound to be someone I can rely on that wouldn’t find it too weird having to model for Hitomi…"
    show pov embarrassed_talk at left
    pov "Though I should have better luck trying to approach people I already have a positive relationship with."
    show pov smirk_talk at left
    pov "Or people who are willing to do a solid for Hitomi and like her enough for it."
    show pov embarrassed_talk at left
    pov "Alright, let's stop talking to myself in the middle of the street and get to it, then!"

    $ hitomi_path = 14

    jump lbl_street_day
