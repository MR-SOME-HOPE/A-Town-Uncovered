## Found a Job ##
label lbl_found_a_job:
    if winc == 0:
        jump lbl_found_a_job_winc0
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right
    with dissolve
    pov "Hey, Mom. I'm home."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Hey, sweetie. How was university?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was good."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Did you go down to the mall to find a job like I told you?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "As a matter of fact, I did get a job."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Oh? What is it?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It's at this place called Ice Cream'py."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Ohh, the ice cream store."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Yeah, I start tomorrow!"
    show pov neutral at left
    show mum bored_talk at right
    mum "Already?! No interview?"
    show pov neutral_talk at left
    show mum bored at right
    pov "None at all. I was hired by one of the other employees and I was the lucky one to snatch the job before anyone else."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Well, I'm really proud of you, honey! This calls for a celebration!"
    mum "[povname]'s first job!"
    hide mum neutral talk
    show sis bored at Position(xpos=1300)
    show mum neutral_talk at right
    mum "[sister], guess what? Your brother just got his first job!"
    show sis neutral_talk at Position(xpos=1300)
    show mum neutral at right
    sis "Finally, it's about time you make your own mullah instead of constantly bugging me for handouts."
    show pov neutral_talk at left
    show sis bored at Position(xpos=1300)
    show mum neutral at right
    pov "Whatever, [sister]. You're the older sibling, you should be taking care of your little brother."
    show pov neutral at left
    show sis angry_talk at Position(xpos=1300)
    show mum bored at right
    sis "Bitch, you're only younger by 13 minutes."
    show sis angry at Position(xpos=1300)
    show mum angry_talk at right
    mum "I just love hearing you two fight. Always fighting. Always getting on each other's nerve. It's music to my ears. I love it."
    show pov bored at left
    show sis smirk_talk at Position(xpos=1300)
    show mum angry at right
    sis "Pussy."

    menu:
        "Dickhead.":
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Your relationship with [sister] has increased")
            else:
                $ sister_points = 10
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
            $ renpy.pause (3,hard=False)
            show pov smirk_talk at left
            show sis smirk at Position(xpos=1300)
            show mum angry at right
            pov "Dickhead."
            show pov bored at left
            show sis bored at Position(xpos=1300)
            show mum angry_talk at right
            mum "[sister], [povname], shut up before I give you both a spanking on the behind."
            show sis bored_talk at Position(xpos=1300)
            show mum angry at right
            sis "Sorry."
            show pov bored_talk at left
            show sis bored at Position(xpos=1300)
            show mum angry at right
            pov "Sorry."
        "Just grow up.":
            show pov angry_talk at left
            show sis bored at Position(xpos=1300)
            show mum angry at right
            pov "Oh, just grow up, [sister]."
            show pov angry at left
            show sis bored at Position(xpos=1300)
            show mum angry_talk at right
            mum "[sister], [povname], shut up before I give you both a spanking on the behind."
            show pov bored at left
            show sis bored_talk at Position(xpos=1300)
            show mum angry at right
            sis "Sorry."
            show pov bored_talk at left
            show sis bored at Position(xpos=1300)
            show mum angry at right
            pov "Sorry."
        "Stay Quiet":
            if sister_points >= 1:
                $ sister_points -= 1
            else:
                $ sister_points = 0
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            $ renpy.pause (3,hard=False)
            $ renpy.notify("Your relationship with [sister] has decreased")
            show pov angry at left
            show sis smirk at Position(xpos=1300)
            show mum angry at right
            pov "..."
            show pov bored at left
            show sis smirk at Position(xpos=1300)
            show mum bored_talk at right
            mum "Mhmm. Just as I thought."
    show pov neutral_talk at left
    show sis bored at Position(xpos=1300)
    show mum bored at right
    pov "Um, hey, [sister]. You work in the mall too right?"
    show pov neutral at left
    show sis embarrassed_talk at Position(xpos=1300)
    show mum bored at right
    sis "Um, yeah. Yeah I do. Though I think I work on the other side of the mall from Ice Cream'py."
    show pov neutral_talk at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored at right
    pov "What's the store called? I might know where that is."
    show pov neutral at left
    show sis embarrassed_talk at Position(xpos=1300)
    show mum bored at right
    sis "I don't think you know it, it's just some clothing store."
    show pov neutral_talk at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored at right
    pov "Oh, M&H?"
    show pov confused at left
    show sis embarrassed_talk at Position(xpos=1300)
    show mum bored at right
    sis "No."
    show pov confused_talk at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored at right
    pov "JaySee Penny?"
    show pov confused at left
    show sis embarrassed_talk at Position(xpos=1300)
    show mum bored at right
    sis "Not that either."
    show pov confused_talk at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored at right
    pov "The Cap?"
    show pov bored at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored_talk at right
    mum "If she wants to keep it to herself, she'll do that. I don't think you'd even want to be seen at the mall together."
    show pov bored at left
    show sis neutral_talk at Position(xpos=1300)
    show mum neutral at right
    sis "Well said, Mom. You know us so well."
    show sis neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Now, c'mon. Dinner's almost done. Go set the table."
    scene bg familydinner_28 with fade
    $ renpy.pause(2.0)

    scene black
    with fade
    "Later that night..."

    scene bg mybedroom_night
    with fade
    $ main_story = 22
    $ townmap_enabled = 1
    $ gtime = 2
    $ thetext_reject = 0

    jump lbl_mybedroom_night_setup

### NO WINC ###
label lbl_found_a_job_winc0:
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right
    with dissolve
    pov "Hey, [missus]. I'm home."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Hey, sweetie. How was university?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was good."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Did you go down to the mall to find a job like I told you?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "As a matter of fact, I did get a job."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Oh? What is it?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It's at this place called Ice Cream'py."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Ohh, the ice cream store."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Yeah, I start tomorrow!"
    show pov neutral at left
    show mum bored_talk at right
    mum "Already?! No interview?"
    show pov neutral_talk at left
    show mum bored at right
    pov "None at all. I was hired by one of the other employees and I was the lucky one to snatch the job before anyone else."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Well, I'm really proud of you, honey! This calls for a celebration!"
    mum "[povname]'s first job!"
    hide mum neutral talk
    show sis bored at Position(xpos=1300)
    show mum neutral_talk at right
    mum "[sister], guess what? Your [povsisrole] just got his first job!"
    show sis neutral_talk at Position(xpos=1300)
    show mum neutral at right
    sis "Finally, it's about time you make your own mullah instead of constantly bugging me for handouts."
    show pov neutral_talk at left
    show sis bored at Position(xpos=1300)
    show mum neutral at right
    pov "Whatever, [sister]. You're the older [povsisrole], you should be taking care of your little [povsisrole]."
    show pov neutral at left
    show sis angry_talk at Position(xpos=1300)
    show mum bored at right
    sis "Bitch, you're only younger by 13 minutes."
    show sis angry at Position(xpos=1300)
    show mum angry_talk at right
    mum "I just love hearing you two fight. Always fighting. Always getting on each other's nerve. It's music to my ears. I love it."
    show pov bored at left
    show sis smirk_talk at Position(xpos=1300)
    show mum angry at right
    sis "Pussy."

    menu:
        "Dickhead.":
            if sister_points <= 9:
                $ sister_points += 1
                $ renpy.notify("Your relationship with [sister] has increased")
            else:
                $ sister_points = 10
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
            $ renpy.pause (3,hard=False)
            show pov smirk_talk at left
            show sis smirk at Position(xpos=1300)
            show mum angry at right
            pov "Dickhead."
            show pov bored at left
            show sis bored at Position(xpos=1300)
            show mum angry_talk at right
            mum "[sister], [povname], shut up before I give you both a spanking on the behind."
            show sis bored_talk at Position(xpos=1300)
            show mum angry at right
            sis "Sorry."
            show pov bored_talk at left
            show sis bored at Position(xpos=1300)
            show mum angry at right
            pov "Sorry."
        "Just grow up.":
            show pov angry_talk at left
            show sis bored at Position(xpos=1300)
            show mum angry at right
            pov "Oh, just grow up, [sister]."
            show pov angry at left
            show sis bored at Position(xpos=1300)
            show mum angry_talk at right
            mum "[sister], [povname], shut up before I give you both a spanking on the behind."
            show pov bored at left
            show sis bored_talk at Position(xpos=1300)
            show mum angry at right
            sis "Sorry."
            show pov bored_talk at left
            show sis bored at Position(xpos=1300)
            show mum angry at right
            pov "Sorry."
        "Stay Quiet":
            if sister_points >= 1:
                $ sister_points -= 1
            else:
                $ sister_points = 0
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            $ renpy.pause (3,hard=False)
            $ renpy.notify("Your relationship with [sister] has decreased")
            show pov angry at left
            show sis smirk at Position(xpos=1300)
            show mum angry at right
            pov "..."
            show pov bored at left
            show sis smirk at Position(xpos=1300)
            show mum bored_talk at right
            mum "Mhmm. Just as I thought."
    show pov neutral_talk at left
    show sis bored at Position(xpos=1300)
    show mum bored at right
    pov "Um, hey, [sister]. You work in the mall too right?"
    show pov neutral at left
    show sis embarrassed_talk at Position(xpos=1300)
    show mum bored at right
    sis "Um, yeah. Yeah I do. Though I think I work on the other side of the mall from Ice Cream'py."
    show pov neutral_talk at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored at right
    pov "What's the store called? I might know where that is."
    show pov neutral at left
    show sis embarrassed_talk at Position(xpos=1300)
    show mum bored at right
    sis "I don't think you know it, it's just some clothing store."
    show pov neutral_talk at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored at right
    pov "Oh, M&H?"
    show pov confused at left
    show sis embarrassed_talk at Position(xpos=1300)
    show mum bored at right
    sis "No."
    show pov confused_talk at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored at right
    pov "JaySee Penny?"
    show pov confused at left
    show sis embarrassed_talk at Position(xpos=1300)
    show mum bored at right
    sis "Not that either."
    show pov confused_talk at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored at right
    pov "The Cap?"
    show pov bored at left
    show sis embarrassed at Position(xpos=1300)
    show mum bored_talk at right
    mum "If she wants to keep it to herself, she'll do that. I don't think you'd even want to be seen at the mall together."
    show pov bored at left
    show sis neutral_talk at Position(xpos=1300)
    show mum neutral at right
    sis "Well said, [missus]. You know us so well."
    show sis neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Now, c'mon. Dinner's almost done. Go set the table."
    scene bg safetyandhomelife_temp1 with fade
    $ renpy.pause(2.0)
    scene black
    with fade
    "Later that night..."

    scene bg mybedroom_night
    with fade
    $ main_story = 22
    $ townmap_enabled = 1
    $ gtime = 2
    $ thetext_reject = 0

    jump lbl_mybedroom_night_setup
