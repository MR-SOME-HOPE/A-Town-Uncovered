## New Friends ##
label lbl_new_friends:
    show pov neutral at left
    with dissolve
    show jac neutral_talk at right
    with dissolve
    idk "Aye! New kid, what's up!"
    show pov bored_talk at left
    show jac neutral at right
    pov "Uhh.. what's up."
    show pov bored at left
    show jac smirk_talk at right
    ## 20 Years Old
    jac "Nice to meet you, dude. The name's Jacob. But everyone calls me BJ."
    show pov confused_talk at left
    show jac smirk at right
    pov "BJ?"

    menu:
        "Like the yellow dinosaur from Barney?":
            pov "Like the yellow dinosaur from Barney?"

            jump lbl_new_friends_1
        "Like a blowjob?":
            pov "LIke a blowjob?"

            jump lbl_new_friends_1
        "Like Billie Jean?":
            pov "Don't tell me your name is Billie Jean?!"

            jump lbl_new_friends_1

label lbl_new_friends_1:
    show pov bored at left
    show jac smirk_talk at right
    jac "It stands for Benny n Jer's. Y'know, because all the girls wanna be licking deez nu-"

    scene bg classroom_day
    show pov bored at left
    show eff neutral_talk at Position(xpos=1300)
    show jac bored at right
    idk "Alright boy, settle down. Keep that three incher in your pants, no one wants to see it."
    show pov neutral at left
    show jac bored_talk at right
    show eff neutral at Position(xpos=1300)
    jac "Aw, c'mon Effie. There's no need for you to embarrass me like that."
    show jac bored at right
    show eff bored_talk at Position(xpos=1300)
    eff "You've embarrassed yourself enough, I couldn't stand watching any second longer."
    eff "Who the hell introduces themselves like that anyway? Jesus, man."
    show jac bored at right
    show eff neutral_talk at Position(xpos=1300)
    ## 20 Years Old
    eff "Hey, I'm Effie, if you didn't catch that. This piece of crap next to me is Jacob. Everyone just calls him Jacob."
    eff "Sometimes you'll hear ‘asshole'."
    show pov neutral_talk at left
    show jac neutral at right
    show eff neutral at Position(xpos=1300)
    pov "Hey, Nice to meet you. I'm [povname]."
    show pov neutral at left
    show jac neutral at right
    show eff neutral_talk at Position(xpos=1300)
    eff "Welcome to your new school!"
    show jac neutral_talk at right
    show eff neutral at Position(xpos=1300)
    jac "Yeah, welcome to the final year of hell, dude! SOS my friend, SO-fuckin-S. Test after test, exam after exam."
    show jac smirk_talk at right
    show eff bored at Position(xpos=1300)
    jac "I bet you lab rats get treated better than us."
    show jac neutral at right
    show eff bored_talk at Position(xpos=1300)
    eff "You're being dramatic."
    show jac bored_talk at right
    show eff bored at Position(xpos=1300)
    jac "Easy for you to say, you're like the smartest student in the whole grade."

    menu:
        "I know who I'll be sitting next to this year.":
            jump lbl_new_friends_2
        "Fuckin' Nerd!":
            jump lbl_new_friends_3

label lbl_new_friends_2:
    if effie_points <= 9:
        $ effie_points += 1
    else:
        $ effie_points = 10
    $ renpy.notify("Your relationship with Effie has increased")
    show pov neutral_talk at left
    show jac neutral at right
    show eff neutral at Position(xpos=1300)
    pov "Haha! Looks like I know who I'll be sitting next to all year."
    show pov neutral at left
    show jac neutral at right
    show eff neutral_talk at Position(xpos=1300)
    eff "It's really nothing, I just work hard is all."
    show pov neutral_talk at left
    show jac neutral at right
    show eff neutral at Position(xpos=1300)
    pov "Still, it sounds like you have your life on track so far." # Do you know what you want to do after high school?"
    # show pov neutral at left
    # show jac neutral at right
    # show eff neutral_talk at Position(xpos=1300)
    # eff "I know it sounds boring and a lot of hard work but I wanna get into dentistry."
    # show pov neutral_talk at left
    # show jac neutral at right
    # show eff neutral at Position(xpos=1300)
    # pov "Not a medical doctor? I heard dentists are people who failed to become actual medical doctors. No offence."
    # show pov neutral at left
    # show jac neutral at right
    # show eff neutral_talk at Position(xpos=1300)
    # eff "Haha! None taken. I personally don't have the stomach for all that blood and guts. Dealing with crooked and chipped teeth are enough for me."
    # eff "Besides, it's more because of the money than anything else."
    # show pov neutral_talk at left
    # show jac neutral at right
    # show eff neutral at Position(xpos=1300)
    # pov "Well, props to you for reaching that high."
    # show pov neutral at left
    # show jac neutral at right
    # show eff neutral_talk at Position(xpos=1300)
    # eff "Thanks. I really appreciate that."
    # show pov neutral_talk at left
    # show jac neutral at right
    # show eff neutral at Position(xpos=1300)
    # pov "What about you, Jacob?"
    # show pov neutral at left
    # show jac neutral_talk at right
    # show eff neutral at Position(xpos=1300)
    # jac "I'll probably turn into a pornstar."
    # show pov bored at left
    # show jac neutral at right
    # show eff bored at Position(xpos=1300)
    # pov "..."
    # eff "..."
    # pov "..."
    # eff "..."
    # show jac bored at right
    # show eff bored at Position(xpos=1300)
    # jac "..."
    # show pov neutral_talk at left
    # show jac neutral at right
    # show eff bored at Position(xpos=1300)
    # pov "Dope."

    jump lbl_new_friends_end

label lbl_new_friends_3:
    if effie_points >= 1:
        $ effie_points -= 1
    else:
        $ effie_points = 0
    $ renpy.notify("Your relationship with Effie has decreased")
    show pov smirk_talk at left
    show jac bored at right
    show eff angry at Position(xpos=1300)
    pov "Ha, fuckin' nerd."
    show pov sad at left
    show jac bored at right
    show eff angry_talk at Position(xpos=1300)
    eff "Wow, rude much? I don't know whether or not that was meant to be a joke but just a heads up;"
    eff "That's not how you make a first impression."
    show jac bored_talk at right
    show eff angry at Position(xpos=1300)
    jac "C'mon Effie, being a nerd isn't all that bad. The richest people in the world are the biggest nerds of them all."
    show jac bored at right
    show eff angry at Position(xpos=1300)
    eff "Hmmm..."
    show jac neutral at right
    show eff bored_talk at Position(xpos=1300)
    eff "I'll let it slide this first time. I'm usually cool about these things."
    eff "I'll just assume you're nervous and have a hard time meeting new people."
    show pov sad_talk at left
    show jac neutral at right
    show eff bored at Position(xpos=1300)
    pov "Sorry, I don't know why I said that... I didn't mean to mock you."
    show pov neutral at left
    show jac neutral at right
    show eff neutral_talk at Position(xpos=1300)
    eff "Hey, it's cool, we're cool. I'll go easy on you because you're new. It's best to have some friends to rely on."
    show pov neutral_talk at left
    show jac neutral at right
    show eff neutral at Position(xpos=1300)
    pov "Thanks."
    show pov neutral at left
    show jac embarrassed_talk at right
    show eff neutral at Position(xpos=1300)
    jac "Phew, a little awkward but issue avoided nevertheless. I can feel us becoming closer already"

    jump lbl_new_friends_end

label lbl_new_friends_end:
    show pov neutral at left
    show jac neutral_talk at right
    show eff neutral at Position(xpos=1300)
    jac "Haha, but yeah, [povname], if you need anything or you wanna hang out. You know who to call."
    show jac neutral at right
    show eff neutral_talk at Position(xpos=1300)
    eff "Same here."
    eff "Class is about to start, let's get to our seats."
    show jac smirk_talk at right
    show eff bored at Position(xpos=1300)
    jac "Yes, ma'am."
    $ main_story = 6
    $ renpy.notify("New Contacts: Jacob, Effie")

    jump lbl_english_teacher
