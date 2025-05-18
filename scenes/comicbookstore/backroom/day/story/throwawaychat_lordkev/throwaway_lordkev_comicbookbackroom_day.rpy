## Throwaway Lord Kev Comic Book Back Room Day Conversation ##
label lbl_comicbookbackroom_day_lordkev:
    show btn_comicbookbackroom_day_crugeon_idle2
    show btn_comicbookbackroom_day_davendithas_idle2
    show btn_comicbookbackroom_day_lordkev_idle2
    $ renpy.pause(0.001)
    hide btn_comicbookbackroom_day_lordkev_idle2
    jump lbl_comicbookbackroom_day_lordkev_convo

label lbl_comicbookbackroom_day_lordkev_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 6 or date == 11 or date == 22 or date == 31:
            jump lbl_comicbookbackroom_day_lordkev_1
        elif date == 7 or date == 18 or date == 21:
            jump lbl_comicbookbackroom_day_lordkev_2
        elif date == 10 or date == 17 or date == 23:
            jump lbl_comicbookbackroom_day_lordkev_3
        elif date == 8 or date == 20 or date == 24:
            jump lbl_comicbookbackroom_day_lordkev_4
        elif date == 9 or date == 16 or date == 26:
            jump lbl_comicbookbackroom_day_lordkev_5
        elif date == 1 or date == 19 or date == 25:
            jump lbl_comicbookbackroom_day_lordkev_11
        elif date == 2 or date == 15 or date == 28:
            jump lbl_comicbookbackroom_day_lordkev_12
        elif date == 3 or date == 14 or date == 27:
            jump lbl_comicbookbackroom_day_lordkev_13
        elif date == 5 or date == 13 or date == 30:
            jump lbl_comicbookbackroom_day_lordkev_14
        elif date == 4 or date == 12 or date == 29:
            jump lbl_comicbookbackroom_day_lordkev_15
    elif gtime == 1:
        if date == 2 or date == 19 or date == 22 or date == 31:
            jump lbl_comicbookbackroom_day_lordkev_6
        elif date == 1 or date == 18 or date == 30:
            jump lbl_comicbookbackroom_day_lordkev_7
        elif date == 4 or date == 20 or date == 28:
            jump lbl_comicbookbackroom_day_lordkev_8
        elif date == 3 or date == 11 or date == 23:
            jump lbl_comicbookbackroom_day_lordkev_9
        elif date == 6 or date == 12 or date == 24:
            jump lbl_comicbookbackroom_day_lordkev_10
        elif date == 5 or date == 13 or date == 21:
            jump lbl_comicbookbackroom_day_lordkev_11
        elif date == 9 or date == 14 or date == 25:
            jump lbl_comicbookbackroom_day_lordkev_12
        elif date == 8 or date == 17 or date == 26:
            jump lbl_comicbookbackroom_day_lordkev_13
        elif date == 7 or date == 16 or date == 29:
            jump lbl_comicbookbackroom_day_lordkev_14
        elif date == 10 or date == 15 or date == 27:
            jump lbl_comicbookbackroom_day_lordkev_15

## Morning Exclusive
label lbl_comicbookbackroom_day_lordkev_1:
    show pov confused at left
    with dissolve
    show lor bored_talk at right
    with dissolve
    lor "Good morning, what offering have you brought with you today?"
    show pov confused_talk at left
    show lor shocked at right
    pov "Offering? Screw your offering, man."
    show pov bored at left
    show lor angry_talk at right
    lor "But I'm your ruler."
    show pov bored_talk at left
    show lor angry at right
    pov "You're a dictator of the back of Hendai's."
    show pov smirk at left
    show lor angry_talk at right
    lor "That's better than what you'll ever be."
    show pov smirk_talk at left
    show lor angry at right
    pov "You keep telling yourself that."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_2:
    show pov confused at left
    with dissolve
    show lor neutral_talk at right
    with dissolve
    lor "Good afternoon!"
    show pov confused_talk at left
    show lor confused at right
    pov "It's still the morning."
    show pov bored at left
    show lor confused_talk at right
    lor "Oh? I swear it's the afternoon."
    show pov bored_talk at left
    show lor confused at right
    pov "Mmmmmm-morning."
    show pov smirk_talk at left
    show lor bored at right
    pov "Not even your high power can change the time of day."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_3:
    show pov confused at left
    with dissolve
    show lor neutral_talk at right
    with dissolve
    lor "Ah, [povname]! Great to see someone with competence around here."
    show pov confused_talk at left
    show lor neutral at right
    pov "What's up with the other guys?"
    show pov bored at left
    show lor bored_talk at right
    lor "Davendithas isn't speaking with me."
    show pov confused_talk at left
    show lor confused at right
    pov "Does he ever?"
    show pov confused at left
    show lor confused_talk at right
    lor "And Crugeon? I mean, just look at him."
    show pov confused_talk at left
    show lor bored at right
    pov "That's a little harsh."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_4:
    show pov neutral_talk at left
    with dissolve
    show lor angry at right
    with dissolve
    pov "Hey, King dude!"
    show pov neutral at left
    show lor angry_talk at right
    lor "It's Lord Kevlamin."
    show pov neutral_talk at left
    show lor angry at right
    pov "Excuse me, Lord dude."
    show pov neutral at left
    lor "..."
    show pov confused_talk at left
    pov "... Giving me the silent treatment?"
    show pov confused at left
    lor "..."
    show pov bored_talk at left
    pov "Why you gotta be so serious all the time?"

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_5:
    show pov confused at left
    with dissolve
    show lor bored_talk at right
    with dissolve
    lor "[povname], do you dispise me?"
    show pov confused_talk at left
    show lor bored at right
    pov "Does saying yes banish me from ever coming here?"
    show pov neutral at left
    show lor bored_talk at right
    lor "I do believe that will be the case."
    show pov smirk_talk at left
    show lor bored at right
    pov "... As much as I want to say yes..."
    show pov confused_talk at left
    pov "I don't have that big a hatred for you."
    show pov bored at left
    show lor confused_talk at right
    lor "Don't get too sweet with me, peasant. It's highly suspect."

    jump lbl_comicbookbackroom_day

## Afternoon Exclusive
label lbl_comicbookbackroom_day_lordkev_6:
    show pov confused at left
    with dissolve
    show lor embarrassed_talk at right
    with dissolve
    lor "Afternoon, [povname]. Were you followed?"
    show pov confused_talk at left
    show lor shocked at right
    pov "What-? Why would I be followed?"
    show pov confused at left
    show lor angry_talk at right
    lor "I'm afraid that that information is highly above of your pay grade."
    show pov confused_talk at left
    show lor angry at right
    pov "Pay grade? What the hell are you talking about."
    show pov confused at left
    show lor shocked_talk at right
    lor "You know what? I've said to much. Begone."
    lor "And forget everything that happened between us just now."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_7:
    show pov confused at left
    with dissolve
    show lor bored_talk at right
    with dissolve
    lor "I don't want to waste my time talking to you. Begone, peasant!"
    show pov confused_talk at left
    show lor shocked at right
    pov "Well, that's a nice way to treat a fellow Harem Protector player."
    show pov confused at left
    show lor angry_talk at right
    lor "..."
    show pov bored at left
    show lor embarrassed_talk at right
    lor "Apologies, forgive my selfishness. What is it that you seek?"
    show pov smirk_talk at left
    show lor bored at right
    pov "Do you have an attractive sister that looks nothing like you?"
    show pov smirk at left
    lor "..."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_8:
    show pov smirk_talk at left
    with dissolve
    show lor bored at right
    with dissolve
    pov "Who's dick did you have to suck to get the title of Lord?"
    show pov shocked at left
    show lor bored_talk at right
    lor "Your mom's."
    show pov shocked at left
    show lor smirk at right
    pov "..."
    show pov smirk_talk at left
    pov "Well damn, I didn't see that coming."
    pov "Proud of you, Kevin. Sticking up for yourself and having decent-ish comebacks."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_9:
    show pov smirk_talk at left
    with dissolve
    show lor confused at right
    with dissolve
    pov "I saw your girlfriend last night."
    pov "She stopped by at my house and begged for me."
    pov "Sorry that I'm the one that had to tell you."
    show pov smirk at left
    show lor confused_talk at right
    lor "I don't have a girlfriend."
    show pov smirk_talk at left
    show lor angry at right
    pov "Aaaand there's the punch line."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_10:
    show pov confused_talk at left
    with dissolve
    show lor confused at right
    with dissolve
    pov "Why is the window boarded up again?"
    show pov smirk_talk at left
    pov "It's not like you guys are running some really crafty stuff in here."
    show pov confused at left
    show lor confused_talk at right
    lor "If we were, you wouldn't be one to know about it."
    show pov shocked_talk at left
    show lor bored at right
    pov "Does that mean you are?"
    show pov shocked at left
    show lor bored_talk at right
    lor "That is for me to know and for you to not know about."

    jump lbl_comicbookbackroom_day

## Interchangable
label lbl_comicbookbackroom_day_lordkev_11:
    show pov bored at left
    with dissolve
    show lor bored_talk at right
    with dissolve
    lor "What is it that you desire, peasant!"
    show pov bored_talk at left
    show lor bored at right
    pov "I really don't like it when you call me peasant."
    show pov bored at left
    show lor confused_talk at right
    lor "What are you then?"
    show pov neutral_talk at left
    show lor confused at right
    pov "Knight. I'd like to be a knight."
    show pov angry at left
    show lor smirk_talk at right
    lor "That's proposterous, a peasant can't be a knight."
    show pov bored_talk at left
    show lor shocked at right
    pov "Whatever, Lord Calories."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_12:
    show pov neutral at left
    with dissolve
    show lor neutral_talk at right
    with dissolve
    lor "Hello, [povname]."
    show pov confused at left
    show lor neutral at right
    pov "..."
    show pov confused_talk at left
    show lor confused at right
    pov "Not peasant?"
    show pov bored at left
    show lor neutral_talk at right
    lor "You're still a peasant, a peasant with a name."
    show pov bored_talk at left
    show lor neutral at right
    pov "I don't know why I'm talking to you right now."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_13:
    show pov confused at left
    with dissolve
    show lor angry_talk at right
    with dissolve
    lor "Ready to feel the full force of pain?!"
    show pov confused_talk at left
    show lor smirk at right
    pov "You wanna play Harem Protector?"
    show pov confused at left
    show lor smirk_talk at right
    lor "That is exactly what I'm talking about!"
    show pov embarrassed_talk at left
    show lor neutral at right
    pov "No, I mean- I wasn't asking yo-"
    show pov bored_talk at left
    show lor confused at right
    pov "Just- keep it in your pants, man."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_14:
    show pov neutral_talk at left
    with dissolve
    show lor bored at right
    with dissolve
    pov "Hi, Lord Kev, how's lordship duty?"
    show pov neutral at left
    show lor bored_talk at right
    lor "It has been fairly quiet."
    show pov confused at left
    show lor confused_talk at right
    lor "Too quiet. I'm thinking of starting a war."
    show pov shocked at left
    show lor smirk_talk at right
    lor "In the streets."
    show pov confused_talk at left
    show lor bored at right
    pov "Like a gang war? I think you should... stay here and not be stupid..er."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_lordkev_15:
    show pov neutral_talk at left
    with dissolve
    show lor confused at right
    with dissolve
    pov "Are you gonna give me some of those cheesy chips?"
    show pov embarrassed at left
    show lor confused_talk at right
    lor "You want these chips... the ones that I touched with these hands."
    lor "The hands that were lovingly suckled on with my chapped yet vuluptuous lips."
    show pov confused_talk at left
    show lor confused at right
    pov "Vuluptuous is quite an overstate-"
    show pov shocked at left
    show lor angry_talk at right
    lor "No, you can't get your hands on my saliva moistened chips."
    show pov sad_talk at left
    show lor smirk at right
    pov "I think I want to barf."

    jump lbl_comicbookbackroom_day
