## Chieghan Main Story Throwaway Conversations School Bathroom Female ##
default sexaroundtownchieghan = 0

## Sex Around Town Chieghan
label lbl_schoolbathroomfemale_day_chieghan_sexworld:
    if sexaroundtownchieghan == 0:
        show pov embarrassed_talk at left
        with dissolve
        hide btn_schoolbathroom_day_chieghansexworld_idle2
        show chisw neutral at right
        with dissolve
        pov "Heeeey... Chieghan..."
        pov "What's up with the... outfit?"
        show pov embarrassed at left
        show chisw neutral_talk at right
        chi "It is uniform, [povname]."
        show chisw smirk_talk at right
        chi "Do you know Flowerfluff Girl?"
        chi "I feel like one."
        show pov embarrassed_talk at left
        show chisw smirk at right
        pov "It looks- great. Like fuck-"
        show pov embarrassed at left
        show chisw neutral_talk at right
        chi "Ahahaha, thank you, [povname]."
        show pov shocked at left
        chi "You look funny, your face is so red like tomato."
        show pov embarrassed_talk at left
        show chisw confused at right
        pov "I- am feeling a lot of emotions right now."
        show pov confused at left
        show chisw confused_talk at right
        chi "Emotion? Is that like 'hard'?"
        show pov confused_talk at left
        show chisw confused at right
        pov "'Hard'?"
        show pov shocked at left
        show chisw confused_talk at right
        chi "Like your penis. I can see it in your pants."
        show chisw confused at right
        pov "..."
        show chisw neutral_talk at right
        chi "'Hard'."
        show pov embarrassed_talk at left
        show chisw neutral at right
        pov "I shouldn't really be in the girls' lav anyway."
        show pov embarrassed at left
        show chisw neutral_talk at right
        chi "You definitely shouldn't be here."
        chi "Goodbye, [povname]. I will see you and your penis around. Okay?"

        $ sexaroundtownchieghan = 1

        jump lbl_schoolbathroomfemale_day

    else:
        show pov embarrassed at left
        with dissolve
        hide btn_schoolbathroom_day_chieghansexworld_idle2
        show chisw neutral_talk at right
        with dissolve
        chi "Hi, [povname]."
        show chisw confused_talk at right
        chi "You're sweating a lot. Get some water."
        show pov embarrassed_talk at left
        show chisw confused at right
        pov "Yeah, I will, it's just uh- there's a lot to take in."
        show pov bored at left
        show chisw confused_talk at right
        chi "Yeah, you need to definitely take in a lot of water."

        jump lbl_schoolbathroomfemale_day
