## Effie Main Story Throwaway Conversations Cafe Inside ##
default cafe_ajob = 0

## Free Drink
label lbl_cafeinside_day_effie_free_drink:
    show pov neutral at left
    with dissolve
    show effw neutral_talk at right
    call lbl_cafeinside_counter_check
    with dissolve

    eff "Meet me outside - I'm getting the drink ready."
    show pov neutral_talk at left
    show effw neutral at right
    pov "Alright."

    jump lbl_cafeinside_day

## Meet Effie at her House
label lbl_cafeinside_day_effie_meet_effie_house:
    show pov neutral at left
    with dissolve
    show effw neutral_talk at right
    call lbl_cafeinside_counter_check
    with dissolve

    eff "Hey, [povname], hope you enjoyed the drink. I'm still working."
    eff "Meet me outside my house after sunset. I want to show you something."
    show pov neutral_talk at left
    show effw neutral at right
    pov "Where is it, again?"
    show pov neutral at left
    show effw neutral_talk at right
    eff "It's at the end of this street, you can't miss it."
    show pov neutral_talk at left
    show effw neutral at right
    pov "Alright, see you then."

    jump lbl_cafeinside_day

## A Job
label lbl_cafeinside_day_effie_job:
    show pov smirk_talk at left
    with dissolve
    show effw neutral at right
    call lbl_cafeinside_counter_check
    with dissolve

    pov "I was wondering if you have a job opening here."
    show pov embarrassed at left
    show effw bored_talk at right
    eff "Oh sorry, [povname]. I'm not authorized to give out jobs."
    eff "And I wouldn't get my hopes up on it, the roster's pretty filled with casual employees already."
    show pov embarrassed_talk at left
    show effw neutral at right
    pov "Oh, cool cool cool. I'll keep looking, thanks."
    show pov embarrassed at left
    show effw confused_talk at right
    eff "Have you tried the mall?"
    show pov embarrassed_talk at left
    show effw neutral at right
    pov "I'll definitely look there."

    $ cafe_ajob = 1

    jump lbl_cafeinside_day_setup

## Effie Sexworld
label lbl_cafeinside_day_effie_sexworld:
    if sexaroundtowncafe == 0:
        show pov shocked at left
        with dissolve
        show effs neutral_talk at right
        call lbl_cafeinside_counter_check
        with dissolve

        eff "What's up, [povname]? What can I get for you today?"
        show effs neutral at right
        pov "..."
        show effs confused_talk at right
        eff "[povname]? You alright, dude?"
        show pov shocked_talk at left
        show effs confused at right
        pov "Y-you're wearing nothing but an apron?"
        show pov shocked at left
        show effs confused_talk at right
        eff "Well, yeah? You've seen me in uniform already, remember? Our milkshake date?"
        show pov shocked at left
        show effs confused at right
        pov "..."
        show pov shocked at left
        show effs confused_talk at right
        eff "Is everything alright?"
        show pov embarrassed_talk at left
        show effs confused at right
        pov "Yeah.. I'm just a bit.. um- I think I'll be going now."
        show pov embarrassed at left
        show effs confused_talk at right
        eff "Umm? Okay? Do you want me to get you some water?"
        show pov embarrassed_talk at left
        show effs embarrassed at right
        pov "No no, it's okay. Don't worry about me."
        pov "See ya, Effie."
        show pov sad at left
        show effs embarrassed_talk at right
        eff "Take care, [povname]."
        $ sexaroundtowncafe += 1
    else:
        show pov embarrassed at left
        with dissolve
        show effs sad_talk at right
        call lbl_cafeinside_counter_check
        with dissolve

        eff "Uhh.. hey again? Are you really sure you're okay?"
        eff "Don't be passing out in here, I'm not trained to deal with that."
        show pov embarrassed_talk at left
        show effs sad at right
        pov "No.. don't worry. I'm fine. Just getting my bearings."
        show pov sad at left
        show effs sad_talk at right
        eff "If you say so."

    jump lbl_cafeinside_day
