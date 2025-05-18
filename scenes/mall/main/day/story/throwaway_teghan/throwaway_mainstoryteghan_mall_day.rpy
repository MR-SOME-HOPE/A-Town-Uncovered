## Teghan Main Story Throwaway Conversations Mall ##

## Sex Around Town Teghan
label lbl_mall_day_teghan_sexworld:
    if sexaroundtownteghan == 0:
        show pov shocked at left
        with dissolve
        hide btn_schoolbathroom_day_teghansexworld_idle2
        show tegsw smirk_talk at right
        with dissolve
        teg "Yo yo! It's the [povname]-myster."
        show tegsw neutral_talk at right
        teg "Always rad to run into you outside of uni."
        teg "You should try some bubble tea, this shit's the bomb."
        show pov embarrassed at left
        show tegsw smirk_talk at right
        teg "Chieghan knows what's up."
        show pov embarrassed_talk at left
        show tegsw neutral at right
        pov "I-uh will try it sometime... Wh-?"
        show tegsw confused at right
        pov "What are you wearing...?"
        show pov embarrassed at left
        show tegsw confused_talk at right
        teg "Oh, this?"
        show tegsw neutral_talk at right
        teg "Meghan wanted us to try having a signature uniform look."
        teg "She said it will make us look extra hi-fashion and in sync."
        show tegsw confused_talk at right
        teg "Chieghan said something about Flowerfluff Girls?"
        show tegsw smirk_talk at right
        teg "I don't know what the fuck she's on but I dig it."
        teg "And I don't care what nobody says."
        show pov embarrassed_talk at left
        show tegsw confused at right
        pov "... It's very... revealing?"
        show pov shocked_talk at left
        pov "Not that I'm complaining but... so... everything is... not hidden."
        show pov embarrassed at left
        show tegsw confused_talk at right
        teg "You're talking as if we're supposed to be wearing 20 layers of clothes."
        show pov sad at left
        show tegsw smirk_talk at right
        teg "Don't be a prude."

        $ sexaroundtownmeghan = 1

        jump lbl_mall_day

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

        jump lbl_mall_day
