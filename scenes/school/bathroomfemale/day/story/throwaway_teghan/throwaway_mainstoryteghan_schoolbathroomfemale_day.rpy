## Teghan Main Story Throwaway Conversations School Bathroom Female ##
default sexaroundtownteghan = 0

## Sex Around Town Teghan
label lbl_schoolbathroomfemale_day_teghan_sexworld:
    if sexaroundtownteghan == 0:
        show pov shocked at left
        with dissolve
        hide btn_schoolbathroom_day_teghansexworld_idle2
        show tegsw smirk_talk at right
        with dissolve
        teg "Yo yo! It's the [povname]-myster."
        show tegsw confused_talk at right
        teg "Nice of you to pop up in the girls' bathroom toilets again."
        show pov embarrassed at left
        show tegsw smirk_talk at right
        teg "You don't seem to be the least bit worried about getting caught, you perv."
        show pov embarrassed at left
        show tegsw smirk at right
        pov "Ah- uh- errm... y- yeah? I guess?"
        show pov shocked at left
        show tegsw smirk_talk at right
        teg "Do you need something or you here for a quick get off."
        show pov embarrassed_talk at left
        show tegsw confused at right
        pov "I- uhm.. ha! Uhhh- no..? yeah..? I d-don't know?"
        show pov embarrassed at left
        show tegsw confused_talk at right
        teg "What is up with you, man?"
        teg "Pussy got your tongue?"
        show pov embarrassed_talk at left
        show tegsw confused at right
        pov "W-Why are you wearing... that?"
        pov "At school, may I add."
        show pov embarrassed at left
        show tegsw neutral_talk at right
        teg "Oh, it was Meghan's idea. She figured we'd look, and I quote-"
        show tegsw smirk_talk at right
        teg "'Fucking spicy'."
        show tegsw smirk_talk at right
        teg "To which I agree with. Don't 'cha think?"
        show pov embarrassed at left
        show tegsw confused at right
        pov "Y-yeah? Absolutely- spicy."
        show pov shocked at left
        show tegsw confused_talk at right
        teg "Um, [povname]? You've got a little drool."
        show pov embarrassed at left
        teg "Right there in the corner of your mouth."
        teg "Are you okay?"
        show pov embarrassed_talk at left
        show tegsw confused at right
        pov "I'm- going to go wash up- in the not girls' bathroom."
        show pov embarrassed at left
        show tegsw neutral_talk at right
        teg "Laters, Drool McCool."

        $ sexaroundtownteghan = 1

        jump lbl_schoolbathroomfemale_day

    else:
        show pov embarrassed at left
        with dissolve
        hide btn_schoolbathroom_day_teghansexworld_idle2
        show tegsw neutral_talk at right
        with dissolve
        teg "Yo, Sorry, can't talk."
        show pov shocked at left
        teg "Discussing orgy plans with the girls."
        show pov embarrassed_talk at left
        show tegsw embarrassed at right
        pov "Can- I come?"
        show pov sad at left
        show tegsw embarrassed at right
        teg "Sorry, it's really Meghan's orgy, invite only."

        jump lbl_schoolbathroomfemale_day
