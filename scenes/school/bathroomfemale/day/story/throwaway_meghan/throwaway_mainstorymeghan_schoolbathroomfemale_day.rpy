## Meghan Main Story Throwaway Conversations School Bathroom Female ##

## Sex Around Town Meghan
label lbl_schoolbathroomfemale_day_meghan_sexworld:
    if sexaroundtownmeghan == 0:
        show pov shocked_talk at left
        with dissolve
        hide btn_schoolbathroom_day_meghansexworld_idle2
        show megsw confused at right
        with dissolve
        pov "Whoa- uh"
        show pov shocked at left
        show megsw confused_talk at right
        meg "Ahem-? Excuse me?"
        show pov embarrassed_talk at left
        show megsw confused at right
        pov "You look- uhm... I like what you're weari-"
        show pov embarrassed at left
        show megsw bored_talk at right
        meg "This is the girls' bathroom?"
        show pov shocked at left
        show megsw angry_talk at right
        meg "Get the fuck out!"
        show pov embarrassed_talk at left
        show megsw angry at right
        pov "Look, haang on a sec-cerooni."
        pov "I know I shouldn't be in here but I panicked."
        pov "Everyone out there are... having sex."
        show pov sad_talk at left
        pov "Like- this is still school, right?"
        show pov shocked at left
        show megsw angry_talk at right
        meg "And this is the girl's bathroom."
        meg "I won't fuck you off again, so for the last time, fuck off."

        $ sexaroundtownmeghan = 1

        jump lbl_schoolbathroomfemale_day

    else:
        show pov sad at left
        with dissolve
        hide btn_schoolbathroom_day_meghansexworld_idle2
        show megsw bored_talk at right
        with dissolve
        meg "Go away, [povname]."
        show pov confused at left
        meg "I don't care nor do I want to buy whatever you're selling."
        show pov sad_talk at left
        show megsw bored at right
        pov "I didn't even say-"
        show pov sad at left
        show megsw confused_talk at right
        meg "Ah- ah- husshhhhhhh..."

        jump lbl_schoolbathroomfemale_day
