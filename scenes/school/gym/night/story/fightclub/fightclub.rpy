## Fight Club ##
label lbl_fight_club:
    default fightclub_seen = 0
    show pov bored at left
    with dissolve
    show jack bored_talk at Position(xpos=1300)
    with dissolve
    show coa bored at right
    with dissolve
    jack "Hey boss, look who showed up."
    show jack bored at Position(xpos=1300)
    pov "..."
    show coa bored_talk at right
    idk "Is this the kid you were talking about earlier?"
    show pov angry at left
    show jack bored_talk at Position(xpos=1300)
    show coa bored at right
    jack "That's the one. Can't believe he showed up. He's either really stupid or wants his ass kicked."
    show jack bored at Position(xpos=1300)
    pov "..."
    show coa bored_talk at right
    idk "I guess you're the quiet type. Don't worry, we turn little boys like you into men around here."

    menu:
        "Who are you?":
            show pov confused_talk at left
            show coa bored at right
            pov "Who are you?"

            jump lbl_fight_club_2
        "What's going on here?":
            show pov confused_talk at left
            show coa bored at right
            pov "What's going on here?"

            jump lbl_fight_club_2
        "Are you all going to gang up on me?":
            show pov confused_talk at left
            show coa bored at right
            pov "Are you all going to gang up on me?"

            jump lbl_fight_club_2

label lbl_fight_club_2:
    show pov bored at left
    show coa angry_talk at right
    idk "Hey, shut it with the questions for a second, I'm asking the questions around here."
    show coa bored_talk at right
    idk "Jack, can you leave us for a second?"
    hide jack bored
    idk "What's your name?"
    show pov bored_talk at left
    show coa bored at right
    pov "I'm [povname]."
    show pov confused at left
    show coa bored_talk at right
    coa "I'm Coach Fistem to you, [povname]. Why did you come here?"

    menu:
        "I was told to come here.":
            show pov bored_talk at left
            show coa angry at right
            pov "I was told to come here by that guy over there."
            show pov angry at left
            show coa angry_talk at right
            coa "Oh, really? Is that so. That's the only reason? You're here becomes some fucking guy invited you? Whoopee!"

            jump lbl_fight_club_3
        "I found my own way here.":
            show pov bored_talk at left
            show coa angry at right
            pov "I found my own way here."
            show pov angry at left
            show coa angry_talk at right
            coa "Did fucking Jesus lead the way here? Did the fucking lights in here make you think that something holy was happening? Shut up with that bullshit."

            jump lbl_fight_club_3
        "I don't even know.":
            show pov bored_talk at left
            show coa angry at right
            pov "I don't even know myself."
            show pov angry at left
            show coa angry_talk at right
            coa "You know why? Because no one fucking told you why! That's why!"

            jump lbl_fight_club_3

label lbl_fight_club_3:
    show pov bored at left
    show coa angry_talk at right
    coa "You're here for one sole purpose."
    show pov sad at left
    show coa angry_talk at right
    coa "You're here to beat the shit out of other people before they beat the shit out of you."
    show coa angry at right
    pov "..."
    show pov bored at left
    show coa angry_talk at right
    coa "What? You think I was going to give you some bullshit-ass speech like Rocko Balboba? Fuck off, I love that movie..."
    show coa bored_talk at right
    coa "But I'm not that kind of guy."
    coa "Say, have you seen the film, ‘Fight Club' starring Brad Fitt?"

    menu:
        "Yeah.":
            $ fightclub_seen = 1
            show pov bored_talk at left
            show coa bored at right
            pov "Yeah."
            show pov bored at left
            show coa bored_talk at right
            coa "Same rules apply. Except we got rid of rule number 1 because it was a pussy rule to begin with."

            jump lbl_fight_club_end
        "No.":
            $ fightclub_seen = 0
            show pov bored_talk at left
            show coa angry at right
            pov "No."
            show pov bored at left
            show coa angry_talk at right
            coa "One! You DO NOT talk about fight club!"
            show pov sad at left
            coa "Two! If either you or the other guy pussies out or gets fucked up. The fight ends."
            coa "Three! Two faggots to one fight."
            coa "Comprende?"
            show pov sad_talk at left
            show coa angry at right
            pov "Yes?"
            show pov sad at left
            show coa angry_talk at right
            coa "Good!"

            jump lbl_fight_club_end

label lbl_fight_club_end:
    show pov angry at left
    coa "Now show me how tough your flimsy-looking arms really are."
    show coa bored_talk at right
    $ jack_path = 2
    $ renpy.notify("New Contact: Coach Fistem")

    jump lbl_schoolgym_night_setup
