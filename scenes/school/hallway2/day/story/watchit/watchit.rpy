## Watch It ##
label lbl_watch_it:

    scene bg jackbump_1
    with fade
    $ renpy.pause()
    show bg jackbump_2
    with hpunch
    $ renpy.pause()

    menu:
        "Watch it!":
            scene bg schoolhallway2_day
            with fade
            show pov angry_talk at left
            with dissolve
            show jack angry at Position(xpos=1300)
            with dissolve
            pov "Hey! Watch it!"
            show pov angry at left
            show jack angry_talk at Position(xpos=1300)
            idk "How about not standing in my way, bitch."

            jump lbl_watch_it_2
        "Stay silent":
            scene bg schoolhallway2_day
            with fade
            show pov angry at left
            with dissolve
            show jack bored at Position(xpos=1300)
            with dissolve
            pov "..."
            show jack bored_talk at Position(xpos=1300)
            idk "What the hell? Are you going to apologize, bitch?"

            jump lbl_watch_it_2

label lbl_watch_it_2:
    show pov angry_talk at left
    show jack bored at Position(xpos=1300)
    pov "What's your problem, man? I'm just trying to get through."
    show pov angry at left
    show jack bored_talk at Position(xpos=1300)
    idk "Oh, yeah? Why don't you come a little closer, and we'll see who's going to make it through."
    hide jack bored_talk
    show pov bored at left
    show jack bored at Position(xpos=1300)
    show pri bored_talk at right
    idk "Now, Jack: Didn't we just talk about starting fights on the university grounds?"
    show pov smirk at left
    show jack angry at Position(xpos=1300)
    show pri bored at right
    jack "..."
    show pov embarrassed at left
    show jack angry_talk at Position(xpos=1300)
    show pri bored at right
    jack "Gym. Tonight. We'll settle this then."
    hide jack angry_talk
    hide pri bored
    show pov sad at left
    show pri neutral_talk at right
    ## 19 Years Old
    idk "Don't pay any attention to him. He just has a short temper, and he's 18 years old. I believe you're new here right?"
    show pov neutral_talk at left
    show pri neutral at right
    pov "Yes, I am. I'm [povname]."
    show pov neutral at left
    show pri neutral_talk at right
    pri "I'm Director Lashley. I haven't formally introduced myself to you yet. I'm dreadfully sorry for that; I was out counselling a Christian church camp, for the break."
    show pov neutral_talk at left
    show pri neutral at right
    pov "Oh, it's okay. It's very nice to meet you."
    show pov neutral at left
    show pri neutral_talk at right
    pri "As with you."
    pri "Well, it's lunch time. I better go eat - I'm fairly busy busy busy today. Hehe."
    show pov neutral_talk at left
    show pri neutral at right
    pov "Sure thing, Director Lashley. Enjoy your lunch."
    show pov neutral at left
    show pri neutral_talk at right
    pri "Thank you. God bless, [povname]."
    show pov confused at left
    hide pri neutral talk
    pov "{i}What did that Jack guy say about the gym? Meet him there tonight?{/i}"
    show pov sad at left
    pov "{i}I don't think I actually want to...{/i}"
    show pov angry at left
    pov "{i}But, why am I cursed to be so curious?{/i}"
    show pov smirk at left
    pov "{i}Also, that admin...{/i}"
    pov "{i}I guess God was pretty generous when choosing her assets. Goddamn!{/i}"
    $ jack_path = 1
    $ principallashley_path = 1
    $ townmap_enabled = 1
    $ renpy.notify("New Objective: Meet Jack at the Gym at Night")
    $ renpy.pause(1,hard=False)
    $ renpy.notify("New Contacts: Jack, Director Lashley")
    $ renpy.pause(1,hard=False)

    jump lbl_schoolhallway2_day_setup
