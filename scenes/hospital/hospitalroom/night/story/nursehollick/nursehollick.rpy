## Nurse Hollick ##
label lbl_nurse_hollick:
    show pov bored at left
    with dissolve
    show nursw neutral_talk at right
    with dissolve
    idk "So, [povname], is it?"
    show pov bored_talk at left
    show nursw neutral at right
    pov "Yes, that's me."
    show pov bored at left
    show nursw neutral_talk at right
    nur "I'm Nurse Hollick. Pleased to meet you."
    show pov bored_talk at left
    show nursw neutral at right
    pov "Pleasure's mine."
    show pov confused at left
    show nursw neutral_talk at right
    nur "Great, now that we've formally met each other. I need you to undress for me."

    menu:
        "I'm here for a head check-up.":
            show pov confused_talk at left
            show nursw neutral at right
            pov "I'm only here for a head check-up. Well, Violette, the girl that came in with me, she forced me to get a check-up."
            pov "According to her I bumped my head on the concrete path near the park and she's worried that there might be some internal damage?"
            show pov confused at left
            show nursw neutral_talk at right
            nur "Right, don't worry about that. I've already been informed about your reason for being here."
            show pov embarrassed_talk at left
            show nursw neutral at right
            pov "So yeah. Should I just sit on the bed?"
            show pov bored at left
            show nursw neutral_talk at right
            nur "No silly, you should just strip for me like I told you to. Maybe that fall has also affected your hearing."
            show pov bored_talk at left
            show nursw neutral at right
            pov "Funny."
            pov "I swear my head is fine. I didn't hit my head on anything, I dove into the pond to save a girl and nearly drowned."
            show pov bored at left
            show nursw neutral_talk at right
            nur "Even more reason for you to take your clothes off."
            show pov confused_talk at left
            show nursw neutral at right
            pov "W-what? Why?"
            if violetteboobjobpark == 1:
                if nursehollick_points <= 9:
                    $ nursehollick_points += 1
                else:
                    $ nursehollick_points = 10
                $ renpy.notify("Your relationship with Nurse Hollick has increased")
                show pov embarrassed at left
                show nursw smirk_talk at right
                nur "So I can take a look at you properly. The blondie told me about the boob job incident."
                show pov embarrassed_talk at left
                show nursw neutral at right
                pov "That's a little tmi to be sharing to you..."
                show pov embarrassed at left
                show nursw neutral_talk at right
                nur "Don't worry, you can trust me, I'm a nurse."
                nur "It's not healthy to be edging like that. I'll have to check to see if it's okay."
                show pov embarrassed_talk at left
                show nursw neutral at right
                pov "If you insist..."

                jump lbl_nurse_hollick_2
            else:
                show pov angry at left
                show nursw neutral_talk at right
                nur "That blondie was right, you ARE stubborn."
                show pov sad at left
                show nursw smirk_talk at right
                nur "Maybe a little anaesthesia would do the trick."
                show pov embarrassed_talk at left
                show nursw neutral at right
                pov "No, no. It's cool. I can strip."
                show pov embarrassed at left
                show nursw bored_talk at right
                nur "Do it slowly..."
                show nursw neutral_talk at right
                nur "I'm joking, chop-chop, we haven't got all night."

                jump lbl_nurse_hollick_2
        "Sure?":
            if nursehollick_points <= 9:
                $ nursehollick_points += 1
            else:
                $ nursehollick_points = 10
            $ renpy.notify("Your relationship with Nurse Hollick has increased")
            
            show pov confused_talk at left
            show nursw neutral at right
            pov "Umm.. sure?"
            show pov confused at left
            show nursw neutral_talk at right
            nur "Good boy."

            jump lbl_nurse_hollick_2

label lbl_nurse_hollick_2:

    scene black
    with fade

    scene bg hospitalroom_night_lightson_closed
    with fade
    show povn embarrassed_talk at left
    with dissolve
    show nursw neutral at right
    with dissolve
    pov "Do I get a hospital gown or something?"
    show povn embarrassed at left
    show nursw bored_talk at right
    nur "Seriously? This is a hospital, we've seen more than just genitals before."
    nur "Lay down and let me do my job."
    
    $ main_story = 26

    jump lbl_hospitalroom_night_setup_1
