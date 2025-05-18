label lbl_bathroom_stakeout_2:
    ## IF principallashley_path == 8 ##
    ##-Scene takes place a week or so after the last, once again the player stumbles upon Lashley when approaching the bathrooms, she is looking shifty and out of place just standing next to the door to the girl's restroom-
    scene bg bathroomstakeout_1
    with fade
    show pov confused_talk at left
    with dissolve
    show pri confused at right
    with dissolve
    pov "On patrol again, Director Lashley?"
    show pov confused at left
    show pri neutral_talk at right
    pri "Ah, [povname]. I was hoping you would show up."
    show pov confused_talk at left
    show pri smirk at right
    pov "You were? Why?"
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "Well, you have proven to be a bit of a good luck charm when it comes to my stake outs."
    pri "I have routinely placed myself under surveillance of the restrooms for a few days and there is no sign of our mystery gal."
    show pov embarrassed_talk at left
    show pri confused at right
    pov "Maybe she is sick?"
    show pov neutral_talk at left
    pov "You could start from there and see who's been missing."
    show pov shocked at left
    show pri confused_talk at right
    pri "I tried that. There are six students who have been reported sick this week, all of them have rock solid alibis of having food poisoning from the university cafeteria."
    show pri bored_talk at right
    pri "I inspected the cafeteria and the caterers shall be punished accordingly."
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Well, remind me not to eat there for a while…"
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Anyway, perhaps with you around my luck is any different this time."
    show pov embarrassed_talk at left
    show pri confused at right
    pov "I really don't think I'll be much help to-"
    show pov shocked at left
    show pri shocked_talk at right
    pri "Coast is clear! Come on, hurry!"
    show pov shocked_talk at left
    show pri shocked at right
    pov "I'm coming again?!"

    jump lbl_secrets_between_stalls
