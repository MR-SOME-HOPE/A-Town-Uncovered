## Scolding ##
label lbl_miss_allaway_scolding:
    default missallawayscolding_newcar = 0
    show pov neutral at left
    with dissolve
    show mis neutral_talk at right
    with dissolve
    mis "Hey, [povname]."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Hey, Miss Allaway."
    show pov neutral at left
    show mis embarrassed_talk at right
    mis "Did you get home safe?"
    show pov neutral_talk at left
    show mis embarrassed at right
    pov "Yeah, I did. And yourself?"
    show pov shocked at left
    show mis embarrassed_talk at right
    mis "Barely made it home, nearly broke down in the middle of the road."
    show pov confused_talk at left
    show mis embarrassed at right
    pov "Oh, really? Did you forget to fill up?"
    show pov confused at left
    show mis embarrassed_talk at right
    mis "No, it's not that. It's just a hunk of junk car that I've had for 15 years."
    show pov neutral at left
    show mis embarrassed_talk at right
    mis "It was my dad's truck and I never really had a reason or desire to get a new one."

    menu:
        "I think it's about time you do.":
            show pov smirk_talk at left
            show mis sad at right
            pov "I think it's about time you get a new car, Miss."
            show pov embarrassed_talk at left
            show mis bored at right
            pov "It's definitely not safe to be driving that old piece of crap around."
            $ missallawayscolding_newcar = 1
            if missallaway_points >= 1:
                $ missallaway_points -= 1
            else:
                $ missallaway_points = 0
            $ renpy.notify("Your relationship with Miss Allaway has decreased")
            show pov embarrassed at left
            show mis sad_talk at right
            mis "Hey! It's not a piece of crap, it's my baby."
            show pov sad at left
            mis "It may run a little on the rougher side but it means a lot to me."
            show pov embarrassed_talk at left
            show mis angry at right
            pov "I'm just saying, Miss. It's just a car."
            show pov embarrassed at left
            show mis bored_talk at right
            mis "I'll keep that in mind, [povname]."
        "If you don't want one then you don\'t have to.":
            if missallaway_points <= 9:
                $ missallaway_points += 1
            else:
                $ missallaway_points = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased")
            show pov smirk_talk at left
            show mis embarrassed at right
            pov "If you don't want a new car then you don\'t have to, Miss."
            show pov neutral_talk at left
            pov "I think it's pretty cool that you've kept that running for so long."
            show pov smirk_talk at left
            pov "It's uh... vintage?"
            show pov neutral at left
            show mis embarrassed_talk at right
            mis "I do love that car, all its imperfections give it personality."
            mis "Plus the large, bulkiness of it makes me feel like I own the roads."
            show mis neutral_talk at right
            mis "I guess I could look into getting a NEW truck."
    show pov confused at left
    show mis embarrassed_talk at right
    mis "Anyway, about the other night. I just want to clarify a few things."
    show mis sad_talk at right
    mis "It was late, I was a little hot and both-"
    show pov shocked at left
    show mis shocked_talk at right
    mis "Ermm.. tired!"
    show pov embarrassed at left
    show mis embarrassed_talk at right
    mis "Tired."
    mis "It was wrong of me to scold you."

    menu:
        "I appreciated that, Miss.":
            show pov neutral_talk at left
            show mis embarrassed at right
            pov "Thank you, I appreciate it."
        "It's alright, Miss.":
            show pov neutral_talk at left
            show mis embarrassed at right
            pov "It's alright, Miss. No need to apologise or anything."
    if whyamiintrouble_leave == 1:
        if missallaway_points <= 9:
            $ missallaway_points += 1
        else:
            $ missallaway_points = 10
        $ renpy.notify("Your relationship with Miss Allaway has increased")
        show pov bored at left
        show mis smirk_talk at right
        mis "I honestly find it a little funny that you actually fell for the counting trick."
        mis "That hasn't worked with any student above the age of 9."
        show pov bored_talk at left
        show mis neutral at right
        pov "Are you mocking me?"
        show pov bored at left
        show mis neutral_talk at right
        mis "Just a tad."
        show pov bored at left
        show mis smirk_talk at right
        if winc == 0:
            mis "Does your [mumrole] do the counting thing too?"
        else:
            mis "Does your mom do the counting thing too?"
        show pov bored at left
        show mis smirk at right
        pov "..."
        show pov bored_talk at left
        show mis neutral at right
        pov "I'll just take my seat now."
        show pov bored at left
        show mis smirk_talk at right
        mis "Haha, I'm just teasing, [povname]. Please don't report me for ‘bullying'. Hehe."
    else:
        if missallaway_points >= 1:
            $ missallaway_points -= 1
        else:
            $ missallaway_points = 0
        $ renpy.notify("Your relationship with Miss Allaway has decreased")
        show pov shocked at left
        show mis bored_talk at right
        mis "Although! You did give me a crappy attitude about it."
        show pov shocked_talk at left
        show mis bored at right
        pov "What?!"
        show pov angry_talk at left
        pov "I was not giving you cr-"
        show pov angry at left
        show mis confused_talk at right
        mis "Talking back at me, refusing my request to leave university premises, getting involved with violence?"
        show pov sad at left
        show mis angry_talk at right
        mis "This university does not tolerate violence."
        show pov shocked at left
        show mis sad_talk at right
        mis "No matter how hot it is."
        show pov shocked_talk at left
        show mis bored at right
        pov "I- Coach Fistem-! You... what?"
        show pov confused at left
        show mis bored_talk at right
        mis "I'm giving you your first warning, [povname]. Keep your nose clean or I'll clean it for you."
        show pov sad_talk at left
        show mis bored at right
        pov "Ew, what does that even mean?"
        show pov bored at left
        show mis bored_talk at right
        mis "Just sit down and get ready for class."
    $ missallaway_path = 3

    jump lbl_classroom_day_setup
