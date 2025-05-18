## In Trouble By Mom ##
label lbl_in_trouble_by_mom:
    if winc == 0:
        jump lbl_in_trouble_by_mom_winc0
    show pov embarrassed at left
    with dissolve
    show mum angry_talk at right
    with dissolve
    with hpunch
    mum "[povname]! Where were you?!"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "Hey, Mom. I'm so sorr-"
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Quit it, mister! Do you know how worried and panicky I became when I woke up this morning to find that my son isn't home?!"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "I'm really truly sor-"
    show pov embarrassed at left
    show mum angry_talk at right
    mum "I was so frikkin close to calling the police!"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "I know, Mom. I'm so-"
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Why didn't you call us? What's wrong with you? You have a phone and you can't even call us?"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "I didn't know the landline number and your phone was o-"
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Shut it. Just shut it. You're in huge trouble. We haven't even been here for a whole week yet!"
    show mum angry at right
    pov "..."
    hide mum angry
    show pov embarrassed at left
    show sis smirk_talk at Position(xpos=1300)
    show mum angry at right
    sis "Hey, look who decided to show up! How was that pussy last night?"
    show sis smirk at Position(xpos=1300)
    show mum angry_talk at right
    mum "[sister]! Watch your mouth."
    show sis smirk_talk at Position(xpos=1300)
    show mum angry at right
    sis "I'm just joking, [povname] couldn't get laid even if he tried."
    show pov bored_talk at left
    show sis smirk at Position(xpos=1300)
    show mum angry at right
    pov "Good to see you too, [sister]."
    show pov bored at left
    show sis bored at Position(xpos=1300)
    show mum angry_talk at right
    mum "[sister]! I'm not in the mood to handle the two of you. Get out of here and go eat your breakfast."
    show sis bored_talk at Position(xpos=1300)
    show mum angry at right
    if day == 0 or day == 3:#sis work morning
        sis "I'm not hungry. I'll just head to work now."
    else:
        sis "I'm not hungry. I'll be in my room."
    show sis bored at Position(xpos=1300)
    show mum angry_talk at right
    mum "Go on, get out of here before I pull all my hair out."
    show sis bored at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Love you, baby girl."
    show sis bored_talk at Position(xpos=1300)
    show mum neutral at right
    sis "Love you too, Mom."
    hide sis bored talk
    show pov sad at left
    show mum bored at right
    mum "..."
    pov "..."
    show pov sad_talk at left
    show mum angry at right
    pov "Mom, I'm sor-"
    show pov sad at left
    show mum bored_talk at right
    mum "I can't ground you. You're too old for that and you'll just be sleeping all day."
    mum "You're going to have to find yourself a part time job at the mall."
    show pov confused_talk at left
    show mum bored at right
    pov "What? Really? I'm not really in the need for a job."
    show pov sad at left
    show mum angry_talk at right
    mum "I don't care. Get a job. I want you to do something productive, instead of just wandering around, playing with your little wee wee in the corner."
    show pov bored_talk at left
    show mum bored at right
    pov "Mom, what the heck?"
    show pov sad at left
    show mum sad_talk at right
    mum "Sorry. Just- you really had me worried. I thought something bad happened to you."
    mum "Did something bad happen to you?"
    show pov embarrassed_talk at left
    show mum sad at right
    pov "No, Mom. I just stayed over at a new friend's house."
    show pov embarrassed at left
    show mum bored_talk at right
    mum "Oh? Is your new friend a girl?"

    menu:
        "Yes.":
            show pov embarrassed_talk at left
            show mum bored at right
            pov "Yes."
            show pov bored at left
            show mum angry_talk at right
            mum "Oh. You didn't..."
            mum "Did you?"

            menu:
                "Yes.":
                    if mum_points >= 1:
                        $ mum_points -= 1
                        $ renpy.notify("Your relationship with Mom has decreased")
                    else:
                        $ mum_points = 0
                    show pov embarrassed_talk at left
                    show mum sad at right
                    pov "Yeah, we had sex."
                    show pov embarrassed at left
                    show mum embarrassed_talk at right
                    mum "Oh, well. Um. I don't really know how to respond to that. I hope she's cute."
                    show pov neutral_talk at left
                    show mum embarrassed at right
                    pov "She is, don't worry."
                    show pov embarrassed at left
                    show mum embarrassed_talk at right
                    mum "Do I get to meet her sometime?"
                    show pov embarrassed_talk at left
                    show mum embarrassed at right
                    pov "Maybe, Mom."
                "No.":
                    if mum_points <= 9:
                        $ mum_points += 1
                        $ renpy.notify("Your relationship with Mom has increased")
                    else:
                        $ mum_points = 10
                    show pov bored_talk at left
                    show mum bored at right
                    pov "No, Mom. We didn't have sex if that's what you mean."
                    show pov bored at left
                    show mum neutral_talk at right
                    mum "Oh! Good. Good. Just friends right? Haha, no worries."
                    show pov embarrassed_talk at left
                    show mum neutral at right
                    pov "Yeah, don't worry about it."
        "No.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show pov bored_talk at left
            show mum bored at right
            pov "No."
            show pov bored at left
            show mum neutral_talk at right
            mum "Okay, cool. Well, it's really great to hear that you're making friends already!"
    show pov sad at left
    show mum bored_talk at right
    mum "Anyway, I'll be in the kitchen if you need me. I'm giving you a warning okay, [povname]? Don't you dare make your mother worry like that again, otherwise..."
    show mum angry_talk at right
    mum "Let's just see when the time comes. I'm sure that you won't do it again, right?"
    show pov sad_talk at left
    show mum bored at right
    pov "Understood, Mom. I'm sorry."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Now go get ready for university. I love you."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I love you too, Mom."
    $ main_story = 16
    $ renpy.notify("New Objective: Get a Job")

    jump lbl_mylivingroom_day_setup

### NO WINC ###
label lbl_in_trouble_by_mom_winc0:
    show pov embarrassed at left
    with dissolve
    show mum angry_talk at right
    with dissolve
    with hpunch
    mum "[povname]! Where were you?!"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "Hey, [missus]. I'm so sorr-"
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Quit it, mister! Do you know how worried and panicky I became when I woke up this morning to find that my [povmumrole] isn't home?!"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "I'm really truly sor-"
    show pov embarrassed at left
    show mum angry_talk at right
    mum "I was so frikkin close to calling the police!"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "I know, [missus]. I'm so-"
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Why didn't you call us? What's wrong with you? You have a phone and you can't even call us?"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "I didn't know the landline number and your phone was o-"
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Shut it. Just shut it. You're in huge trouble. We haven't even been here for a whole week yet!"
    show mum angry at right
    pov "..."
    hide mum angry
    show pov embarrassed at left
    show sis smirk_talk at Position(xpos=1300)
    show mum angry at right
    sis "Hey, look who decided to show up! How was that pussy last night?"
    show sis smirk at Position(xpos=1300)
    show mum angry_talk at right
    mum "[sister]! Watch your mouth."
    show sis smirk_talk at Position(xpos=1300)
    show mum angry at right
    sis "I'm just joking, [povname] couldn't get laid even if he tried."
    show pov bored_talk at left
    show sis smirk at Position(xpos=1300)
    show mum angry at right
    pov "Good to see you too, [sister]"
    show pov bored at left
    show sis bored at Position(xpos=1300)
    show mum angry_talk at right
    mum "[sister]! I'm not in the mood to handle the two of you. Get out of here and go eat your breakfast."
    show sis bored_talk at Position(xpos=1300)
    show mum angry at right
    sis "I'm not hungry, I'll just head to work now."
    show sis bored at Position(xpos=1300)
    show mum angry_talk at right
    mum "Go on, get out of here before I pull all my hair out."
    show sis bored at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Love you, baby girl."
    show sis bored_talk at Position(xpos=1300)
    show mum neutral at right
    sis "Love you too, [missus]."
    hide sis bored talk
    show pov sad at left
    show mum bored at right
    mum "..."
    pov "..."
    show pov sad_talk at left
    show mum angry at right
    pov "[missus], I'm sor-"
    show pov sad at left
    show mum bored_talk at right
    mum "I can't ground you. You're too old for that and you'll just be sleeping all day."
    mum "You're going to have to find yourself a part time job at the mall."
    show pov confused_talk at left
    show mum bored at right
    pov "What? Really? I'm not really in the need for a job."
    show pov sad at left
    show mum angry_talk at right
    mum "I don't care. Get a job. I want you to do something productive, instead of just wandering around, playing with your little wee wee in the corner."
    show pov bored_talk at left
    show mum bored at right
    pov "[missus], what the heck?"
    show pov sad at left
    show mum sad_talk at right
    mum "Sorry. Just- you really had me worried. I thought something bad happened to you."
    mum "Did something bad happen to you?"
    show pov embarrassed_talk at left
    show mum sad at right
    pov "No, [missus]. I just stayed over at a new friend's house."
    show pov embarrassed at left
    show mum bored_talk at right
    mum "Oh? Is your new friend a girl?"

    menu:
        "Yes.":
            show pov embarrassed_talk at left
            show mum bored at right
            pov "Yes."
            show pov bored at left
            show mum angry_talk at right
            mum "Oh. You didn't..."
            mum "Did you?"

            menu:
                "Yes.":
                    if mum_points >= 1:
                        $ mum_points -= 1
                        $ renpy.notify("Your relationship with [missus] has decreased")
                    else:
                        $ mum_points = 0
                    show pov embarrassed_talk at left
                    show mum sad at right
                    pov "Yeah, we had sex."
                    show pov embarrassed at left
                    show mum embarrassed_talk at right
                    mum "Oh, well. Um. I don't really know how to respond to that. I hope she's cute."
                    show pov neutral_talk at left
                    show mum embarrassed at right
                    pov "She is, don't worry."
                    show pov embarrassed at left
                    show mum embarrassed_talk at right
                    mum "Do I get to meet her sometime?"
                    show pov embarrassed_talk at left
                    show mum embarrassed at right
                    pov "Maybe, [missus]."
                "No.":
                    if mum_points <= 9:
                        $ mum_points += 1
                        $ renpy.notify("Your relationship with [missus] has increased")
                    else:
                        $ mum_points = 10
                    show pov bored_talk at left
                    show mum bored at right
                    pov "No, [missus]. We didn't have sex if that's what you mean."
                    show pov bored at left
                    show mum neutral_talk at right
                    mum "Oh! Good. Good. Just friends right? Haha, no worries."
                    show pov embarrassed_talk at left
                    show mum neutral at right
                    pov "Yeah, don't worry about it."
        "No.":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show pov bored_talk at left
            show mum bored at right
            pov "No."
            show pov bored at left
            show mum neutral_talk at right
            mum "Okay, cool. Well, that's really great to hear that you're making friends already!"
    show pov sad at left
    show mum bored_talk at right
    mum "Anyway, I'll be in the kitchen if you need me. I'm giving you a warning okay, [povname]? Don't you dare make your [mumrole] worry like that again, otherwise..."
    show mum angry_talk at right
    mum "Let's just see when the time comes. I'm sure that you won't do it again, right?"
    show pov sad_talk at left
    show mum bored at right
    pov "Understood, [missus]. I'm sorry."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Now go get ready for university. I love you."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I love you too, [missus]."
    $ main_story = 16
    $ renpy.notify("New Objective: Get a Job")

    jump lbl_mylivingroom_day_setup
