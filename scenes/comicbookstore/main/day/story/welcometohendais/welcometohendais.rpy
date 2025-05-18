## Welcome to Hendai's ##
label lbl_welcome_to_hendais:
    show pov neutral at left
    with dissolve
    show jac neutral_talk at right
    with dissolve
    jac "Hey! You made it."
    show pov neutral_talk at left
    show jac neutral at right
    pov "Yup, here I am."
    show pov neutral at left
    show jac neutral_talk at right
    jac "Welcome to Hendai's. My home away from home."
    show pov confused_talk at left
    show jac neutral at right
    pov "Hendai's huh?"
    show pov confused at left
    show jac smirk_talk at right
    jac "Oh, don't get mistaken, Hendai's not a play on hentai. The owner's name really is Hendai. Hendai Tanaka."
    show pov confused_talk at left
    show jac neutral at right
    pov "Where is he?"
    show pov confused at left
    show jac neutral_talk at right
    jac "He's not here right now. He's actually never here 95 percent of the time."
    show pov confused_talk at left
    show jac neutral at right
    pov "Hendai. The owner of Hendai's. Doesn't manage his own store?"
    show pov confused at left
    show jac neutral_talk at right
    jac "That's business for you."
    show pov confused_talk at left
    show jac neutral at right
    pov "Then who runs this place and stops me from just stealing things?"
    hide jac neutral
    show pov confused at left
    show hit neutral_talk at Position(xpos=1300)
    show jac neutral at right
    idk "That would be me."
    show pov neutral at left
    show jac smirk_talk at right
    show hit bored at Position(xpos=1300)
    jac "Hey, babe. How's it going?"
    show jac smirk at right
    show hit bored_talk at Position(xpos=1300)
    idk "Can you please not call me that."
    show jac smirk_talk at right
    show hit bored at Position(xpos=1300)
    jac "But I like the nickname ‘babe' for you"
    show jac smirk at right
    show hit neutral_talk at Position(xpos=1300)
    idk "Who's the new guy? I haven't seen him around before."
    show pov neutral_talk at left
    show jac neutral at right
    show hit neutral at Position(xpos=1300)
    pov "Hey, I'll introduce myself before Jacob embarrasses me. I'm [povname]."
    show pov neutral at left
    show jac neutral at right
    show hit neutral_talk at Position(xpos=1300)

## 19 Years Old
    hit "I'm Hitomi. Welcome to Hendai's. I hope you like this place, we have a lot of different types of reading material for you."

    menu:
        "Porno stuff.":
            show pov neutral_talk at left
            show jac neutral at right
            show hit neutral at Position(xpos=1300)
            pov "Jacob told me that one can get some pornographic stuff here."
            show pov neutral at left
            show jac neutral at right
            show hit neutral_talk at Position(xpos=1300)
            hit "Oh well, yes, that is true. We do sell pornographic material as well."
            hit "The sex shop next door decided to stop selling printed material so now we receive them."
            show jac smirk at right
            show hit neutral_talk at Position(xpos=1300)
            hit "My grandfather, the owner of this store said that it would bring in new customers."
            show jac smirk at right
            show hit confused_talk at Position(xpos=1300)
            hit "As long as I don't sell it to minors, they're free to look 'without me knowing'."
            show jac neutral at right
            show hit bored_talk at Position(xpos=1300)
            hit "I know they look, we all know they look."
            show pov neutral_talk at left
            show jac bored at right
            show hit neutral at Position(xpos=1300)
            pov "I assume Jacob buys a lot of them?"
            show pov neutral at left
            show jac smirk_talk at right
            show hit bored at Position(xpos=1300)
            jac "You wouldn't believe my collection."

            jump lbl_welcome_to_hendais_2
        "Nice to meet you.":
            show pov neutral_talk at left
            show jac neutral at right
            show hit neutral at Position(xpos=1300)
            pov "Thanks, Hitomi. It's really nice to meet you."
            show pov neutral at left
            show jac neutral at right
            show hit neutral_talk at Position(xpos=1300)
            hit "It's very nice to meet you too."

            jump lbl_welcome_to_hendais_2

label lbl_welcome_to_hendais_2:
    show pov neutral at left
    show jac neutral_talk at right
    show hit neutral at Position(xpos=1300)
    jac "Are the boys back there?"
    show pov neutral at left
    show jac neutral at right
    show hit neutral_talk at Position(xpos=1300)
    hit "Yeah, they are, go right ahead."
    show pov bored at left
    show jac smirk_talk at right
    show hit neutral at Position(xpos=1300)
    jac "C'mon, [povname]. Follow me to the back room."

    menu:
        "Sure.":
            show pov neutral_talk at left
            show jac smirk at right
            pov "Sure, lead the way good sir."

            jump lbl_welcome_to_hendais_end
        "No thanks.":
            show pov bored_talk at left
            show jac smirk at right
            pov "No thanks, I don't trust that so called ‘back room'."
            show pov sad at left
            show jac smirk_talk at right
            show hit smirk at Position(xpos=1300)
            jac "Alright, guess I'll just have to push you in."

            jump lbl_welcome_to_hendais_end

label lbl_welcome_to_hendais_end:
    $ main_story = 19
    $ renpy.notify("New Contacts: Hitomi")

    jump lbl_comicbookbackroom_day_setup
