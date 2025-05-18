## Finally a Customer ##
label lbl_stuffstore_day_grundlesam_0:
    show pov embarrassed at left
    with dissolve
    show sam neutral_talk at right
    with dissolve
    call lbl_stuffstore_counter_check
    sam "Oooh! Finally a customer! Hehehe~"
    show pov embarrassed_talk at left
    show sam neutral at right
    pov "Yeah, hi."
    show pov embarrassed at left
    show sam neutral_talk at right
    sam "I'm Grundle Sam and welcome to Grundle Sam's uh- {i}*snort*{/i} things and stuff?"
    show sam confused_talk at right
    sam "Hehehe~ I think that's what I named it..."
    show sam smirk_talk at right
    sam "How can I help you, ma good sir? Hehehe~"
    show sam neutral_talk at right
    sam "Can I interest you in some... {i}*snort*{/i}"
    show pov confused at left
    sam "Totems Idols? Hehehe~"
    show pov bored_talk at left
    show sam neutral at right
    pov "Interest me."
    show pov bored at left
    show sam smirk_talk at right
    sam "Well! Ma good sir. {i}*snort*{/i}"

    scene bg stuffstore_totemcloseup
    with dissolve
    sam "These specially made Totems give off a pretty {i}*snort*{/i} wicked aura that has many health benefits."

    menu:
        "They look like toys.":
            scene bg stuffstore_day
            show pov bored_talk at left
            show sam neutral at right
            pov "They look like promotional movie toys that you get from cereal boxes."
            show pov smirk_talk at left
            pov "What kind of health benefits do they have? Will they make me last longer in bed?"
        "I guess that's interesting.":
            scene bg stuffstore_day
            show pov confused_talk at left
            show sam neutral at right
            pov "I guess that's some pretty interesting hippie-dippie-mumbo-jumbo."
            scene bg stuffstore_day
            show pov smirk_talk at left
            show sam neutral at right
            pov "What kind of health benefits do they have? Will they make me last longer in bed?"
        "You have my attention.":
            scene bg stuffstore_day
            show pov smirk_talk at left
            show sam neutral at right
            pov "Benefits you say? I'm interested. Will they make me last longer in bed?"
    show pov shocked at left
    show sam smirk_talk at right
    sam "{i}*snort*{/i} Funny enough, it actually does!"
    show pov embarrassed_talk at left
    show sam neutral at right
    pov "I was jokin-"

    scene bg stuffstore_totemcloseup
    with dissolve
    sam "See here, this Elk totem. Hehehe~ It's known as the stamina spirit animal!"
    sam "An- an- andd! You see how they have add-ons?"
    sam "The sweat drop in particular {i}*snort*{/i} gives you higher stamina. Hehehe~"
    pov "They don't look like they're meant to belong on there."
    sam "Oh, pish-posh. Of course they are! I made them myself! Hehehe~ {i}*snort*{/i}"
    sam "Using various materials such as wood, bronze, silver, gold, and meteor rock. Hehehe~"
    show bg stuffstore_day
    show pov shocked_talk at left
    show sam smirk at right
    if store_counter == 1:
        show counter stuffstore at right
    else:
        pass
    pov "Meteor rock? That sounds expensive."
    show pov bored at left
    show sam neutral_talk at right
    sam "Hehehe~ Yes, yes it is, ma good sir."
    show sam smirk_talk at right
    sam "But the benefits are phenomenal! Hehehe~"
    show pov confused at left
    show sam confused_talk at right
    sam "Oh, I may I add. That it's bad ju-ju to have more than one totem in your possession at a time."
    show pov bored_talk at left
    show sam bored at right
    pov "Doesn't their 'aura' stack?"
    show pov bored at left
    show sam confused_talk at right
    sam "Hehehe~ You'd think so.. but no. These little spirit animals are territorial and {i}*snort*{/i} protective of their owner."
    show pov bored_talk at left
    show sam neutral at right
    pov "Alright, I'll buy that excuse."
    show pov confused at left
    show sam neutral_talk at right
    sam "You'll need to trade them in with me. Hehehe~"
    show pov confused_talk at left
    show sam shocked at right
    pov "Will I get a refund if I return one for another?"
    show pov bored at left
    show sam smirk_talk at right
    sam "Hehehe~ Are you kidding me, ma good sir?"
    show pov angry at left
    sam "I need this place running, not out of business. {i}*snort*{/i}"
    show pov angry_talk at left
    show sam shocked at right
    pov "You're a scam."
    show pov angry at left
    show sam bored_talk at right
    sam "{i}*snort*{/i} Why does every keep saying that to me?"
    show pov confused at left
    show sam embarrassed_talk at right
    sam "Here, I tell you what. Because you actually gave me a chance. {i}*snort*{/i} I'll let you have this beginner Elk Totem for free. Hehehe~"
    show pov smirk_talk at left
    show sam neutral at right
    pov "Can't say no to free stuff."

    $ inventory.money += 10
    $ inventory.buy(Items.skillitem1)
    $ renpy.notify("New Item Obtained: Totem #1")

    show pov confused at left
    show sam smirk_talk at right
    sam "Hehehe~ Give it a name, ma good sir."
    show pov bored_talk at left
    show sam smirk at right
    pov "I'd rather not."
    show pov bored at left
    show sam smirk_talk at right
    sam "Do it, you'll bond a lot closer. Hehehe~ {i}*snort*{/i}"
    show pov embarrassed_talk at left
    show sam smirk at right
    pov "Alright, I'll keep that in mind."
    show pov embarrassed at left
    show sam neutral_talk at right
    sam "If you're ever confused about all this, feel free to ask, ma good sir!"
    show pov embarrassed_talk at left
    show sam neutral at right
    pov "Thanks, Sam."
    $ grundlesam_path = 1
    $ add_contact("Grundle Sam")
    jump lbl_stuffstore_day
