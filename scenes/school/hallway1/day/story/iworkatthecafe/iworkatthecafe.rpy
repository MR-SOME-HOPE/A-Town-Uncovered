## I Work at the Cafe ##
label lbl_i_work_at_the_cafe:
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    eff "Hey, [povname]! Where are you heading to now?"
    show pov neutral_talk at left
    show eff neutral at right
    pov "Oh hey, I'm not sure; around, I guess? Maybe explore a little bit more of the town."
    show pov neutral at left
    show eff neutral_talk at right
    eff "Oh, nice."
    show pov neutral_talk at left
    show eff neutral at right
    pov "What about you, Effie? You gonna head on home now?"
    show pov neutral at left
    show eff neutral_talk at right
    eff "I'm rarely home - I've got a part-time job at the local café. I'm pretty much there every afternoon."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Does it get busy at work?"
    show pov neutral at left
    show eff neutral_talk at right
    eff "Not all that busy, it's normally pretty chill."
    eff "Why don't you come down and order a little something sometime?"

    menu:
        "For sure.":
            if effie_points <= 9:
                $ effie_points += 1
            else:
                $ effie_points = 10
            $ renpy.notify("Your relationship with Effie has increased")
            show pov neutral_talk at left
            show eff neutral at right
            pov "For sure! If I'm free, I'll stop by today. Otherwise I'll come another time."
            pov "Do I get a friend discount?"
            show pov neutral at left
            show eff neutral_talk at right
            eff "I can't offer that but I'll do you better: You come down to see me and I'll hook you up with one free drink on me."
            show pov neutral_talk at left
            show eff neutral at right
            pov "I'll take it."
            show pov neutral at left
            show eff neutral_talk at right
            eff "Awesome! Well, I gotta run for my shift. See you, [povname]."
            hide eff neutral_talk
            show pov smirk at left
        "I'm kind of busy.":
            if effie_points >= 1:
                $ effie_points -= 1
            else:
                $ effie_points == 0
            $ renpy.notify("Your relationship with Effie has decreased")
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "I'm kind of busy. I don't really have time to drop by."
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "C'mon dude. Why do you have to reject me like that. Don't you like me?"
            show eff bored_talk at right
            eff "Don't answer that."
            show eff embarrassed_talk at right
            eff "You don't have to come today, but it'll be nice if you stopped by another day."
            show eff bored_talk at right
            eff "Why don't I throw in a free drink for you? Would that convince you to drop by? I'm trying to be nice here."
            show pov confused_talk at left
            show eff bored at right
            pov "Alright alright. I'll drop by when I can."
            show pov sad at left
            show eff bored_talk at right
            eff "Look, if you really don't want to, don't force yourself. But it'll really mean a lot to me if you did."
            eff "Anyway, I gotta run for my shift. See you, [povname]."
            hide eff bored_talk
            show pov embarrassed at left
    $ renpy.notify("New Objective: Meet Effie at the Cafe in the Afternoon")
    pov "{i}She seems pretty nice. I can't be picky with who I befriend on the first day, after all.{/i}"
    show pov confused at left
    idk "Go on! I fucking dare you!"
    idk "As if I give a shit about this school!"
    show pov shocked at left
    with hpunch
    "{i}*SLAM*{/i}"
    pov "..."
    pov "{i}What the hell was that? Sounded like it came from upstairs.{/i}"
    pov "{i}I hope a fight is about to start, that'll be a sight to see.{/i}"
    $ main_story = 9
    $ townmap_enabled = 0
    $ renpy.notify("New Objective: Explore the 2nd Floor")

    jump lbl_schoolhallway1_day_setup
