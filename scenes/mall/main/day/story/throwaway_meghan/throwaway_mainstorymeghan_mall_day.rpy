## Meghan Main Story Throwaway Conversations Mall ##
default sexaroundtownmeghan = 0

## Sex Around Town Meghan
label lbl_mall_day_meghan_sexworld:
    if sexaroundtownmeghan == 0:
        show pov shocked_talk at left
        with dissolve
        hide btn_schoolbathroom_day_meghansexworld_idle2
        show megsw confused at right
        with dissolve
        pov "Whoa- uh"
        show pov shocked at left
        show megsw bored_talk at right
        meg "{i}*Sigh*{/i} What do you want, [povname]."
        show pov embarrassed_talk at left
        show megsw confused at right
        pov "You look- uhm... I like what you're weari-"
        show pov embarrassed at left
        show megsw smirk_talk at right
        meg "Yeah, thanks."
        show pov confused at left
        show megsw bored_talk at right
        meg "Now can you move your stupid-looking face?"
        show pov bored at left
        show megsw smirk_talk at right
        meg "I'm trying to spot some hot-ass guys to fuck."
        show pov sad_talk at left
        show megsw confused at right
        pov "Can you just tell me what the hell is going on today?"
        pov "Is today some special day or something?"
        show pov shocked_talk at left
        pov "Everyone's just having sex out in the open like it's nothing."
        show pov shocked at left
        show megsw bored_talk at right
        meg "Go be the abstinance police somewhere else, loser. This isn't the 1700s."
        show pov sad_talk at left
        show megsw bored at right
        pov "{i}*Sigh*{/i} Alright, I hear you loud and clear."
        show pov bored_talk at left
        show megsw angry at right
        pov "{i}*Cough*{/i} bitch."

        $ sexaroundtownmeghan = 1

        jump lbl_mall_day

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

        jump lbl_mall_day
