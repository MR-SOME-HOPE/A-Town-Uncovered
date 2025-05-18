## Brock Side Story Throwaway Conversations Cafe Inside ##
default cafeinside_spareboxes = 0

## Where's Effie?
label lbl_cafeinside_day_brock_whereseffie:
    if jack_path <= 1:
        show pov neutral_talk at left
        show brow neutral at right
        pov "Hey, I'm just wondering where Effie is?"
        show pov neutral at left
        show brow neutral_talk at right
        idk "Effie's off-duty at the moment. She only works afternoon shifts."
        show pov neutral_talk at left
        show brow neutral at right
        pov "Alright, thanks."

        jump lbl_cafeinside_day_setup

    else:
        show pov neutral_talk at left
        show brow neutral at right
        pov "Hey, I'm just wondering where Effie is?"
        show pov neutral at left
        show brow neutral_talk at right
        bro "Effie's off-duty at the moment. She only works afternoon shifts."
        show pov neutral_talk at left
        show brow neutral at right
        pov "Alright, thanks."

        jump lbl_cafeinside_day_setup

## Seen at Club
label lbl_cafeinside_day_brock_seenatclub:
    show pov neutral_talk at left
    show brow bored at right
    pov "Hey, I've seen you at the fight club before, remember me? I'm the newbie."
    show pov confused_talk at left
    show brow bored at right
    pov "Why are you working here? Aren't you supposed to be at uni?"
    show pov bored at left
    show brow bored_talk at right
    idk "Okay, first off. I have no idea what you're talking about and even if I did; you're breaking rule number uno, ese."
    show pov embarrassed_talk at left
    show brow bored at right
    pov "Right, sorry."
    show pov embarrassed at left
    show brow neutral_talk at right
    bro "The name's Brock. Kinda like the Rock but with a B."
    bro "And to answer your weird and totally not hurtful question; I don't go to the university. I dropped out."
    bro "I mean, if I stayed, I would've graduated two years ago. But I didn't..."
    show pov confused at left
    show brow bored at right
    bro "..."
    show brow bored_talk at right
    bro "The caffeine in the air really hypes me up for the night."
    show brow smirk_talk at right
    bro "Y'know, THE night."
    show pov embarrassed_talk at left
    show brow neutral at right
    pov "Oh, I see."
    show pov neutral at left
    show brow confused_talk at right
    bro "Yup. Well, is there anything I can get for you today?"
    show pov neutral_talk at left
    show brow confused at right
    pov "Not at the moment, that is all."
    $ brock_path = 1
    $ renpy.notify("New Contact: Brock")

    jump lbl_cafeinside_day_setup

## Brock Morning Shift
label lbl_cafeinside_day_brock_morningshift:
    show pov confused_talk at left
    with dissolve
    show brow bored at right
    with dissolve
    pov "Hey, Brock right? Where's Effie?"
    if (27 <= sister_path <= 34):
        show pov neutral at left
        show brow confused_talk at right
        bro "She told me that she'll be taking a short leave to take care of something?"
        bro "I'm not sure, bro. She was a little vague about it."
        show brow neutral_talk at right
        bro "In any case, it's none of my business and I'm here to cover her shift."
        bro "I need me the money anyways."
        show pov neutral_talk at left
        show brow neutral at right
        pov "Alright, Brock. Thanks, dude."
    else:
        show pov confused at left
        show brow bored_talk at right
        bro "I have absolutely no idea, bro. I was called in to take her shift for today."
        show pov confused_talk at left
        show brow bored at right
        pov "Did your manager say what happened to her?"
        show pov sad at left
        show brow bored_talk at right
        bro "My guess is as good as yours bro."
        show pov sad_talk at left
        show brow bored at right
        pov "Alright, thanks."

    if on_coffee_run_blocking and not bought_coffee_run_drinks:
        menu:
            "Office Coffee Orders":
                jump lbl_get_coffee_from_cafe

    jump lbl_cafeinside_day_setup

## Spare Boxes
label lbl_cafeinside_day_brock_spareboxes:
    show pov neutral_talk at left
    with dissolve
    show brow neutral at right
    with dissolve
    pov "Hey, Brock!"
    show pov smirk_talk at left
    show brow confused at right
    pov "Just wonder if you have any spare boxes in the back that I can have."
    show pov bored at left
    show brow neutral_talk at right
    bro "Sorry, little dude. We ain't got many to give out. We're very environmentally friendly."
    show pov confused at left
    show brow bored_talk at right
    bro "Reduce, reuse, recycle."
    show brow embarrassed_talk at right
    bro "We have lots and lots of mason jars though."
    show pov confused_talk at left
    show brow confused at right
    pov "That's not gonna work, I need cardboard boxes."
    show pov confused at left
    show brow smirk_talk at right
    bro "Again, sorry. Can't help you there. How about some christmas cake?"
    show pov embarrassed at left
    bro "I swear these things never expire."
    show pov embarrassed at left
    show brow neutral at right
    pov "Maaybe next time. Thanks."

    $ cafeinside_spareboxes = 1

    jump lbl_cafeinside_day_setup
