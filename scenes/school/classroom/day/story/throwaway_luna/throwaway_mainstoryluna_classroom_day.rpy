## Luna Main Story Throwaway Conversations Classroom ##

## Sex Around Town Luna
label lbl_classroom_day_luna_sexworld:
    if sexaroundtownluna == 0:
        show pov embarrassed_talk at left
        with dissolve
        show lun neutral at right
        hide btn_classroom_day_luna_idle2
        with dissolve
        pov "Hey... Luna.."
        show pov embarrassed at left
        show lun neutral_talk at right
        lun "Oh hey, [povname]."
        show pov embarrassed_talk at left
        show lun confused at right
        pov "... How... is it going?"
        show pov embarrassed at left
        show lun confused_talk at right
        lun "I'm... good...?"
        lun "Why... are we... talking... like this...?"
        show pov embarrassed_talk at left
        show lun confused at right
        pov "Sorry, I'm just sort of- uneasy at the moment."
        show pov sad_talk at left
        show lun smirk at right
        pov "I'm seeing abnormalities everywhere... literally everywhere."
        show pov embarrassed at left
        show lun neutral_talk at right
        lun "That sounds exciting!"
        show pov embarrassed_talk at left
        show lun neutral at right
        pov "I mean, in a way you can. But I have no idea what is real or not."
        show pov sad_talk at left
        show lun smirk at right
        pov "And that really fucks with you."
        show pov embarrassed at left
        show lun embarrassed_talk at right
        lun "I'm very familiar with what you're feeling, [povname]. Don't worry."
        lun "I frequently get sleep paralysis and y'know how they are."
        show pov shocked at left
        show lun sad_talk at right
        lun "No matter how much you want to, you can't move. And you just have to let the dark figure fuck you silly."
        show pov shocked_talk at left
        show lun sad at right
        pov "Excuse me but wh-"
        show pov shocked at left
        show lun embarrassed_talk at right
        lun "Have you experienced that? Cumming so hard whilst in sleep paralysis?"
        show lun shocked_talk at right
        lun "Your body tenses so fucking hard and your muscles spazz out."
        show lun embarrassed_talk at right
        lun "Call me crazy but I love it. I feel closer to the unknown."
        show pov embarrassed_talk at left
        show lun shocked at right
        pov "I- have to go."
        show pov embarrassed at left
        show lun embarrassed_talk at right
        lun "Alright, I guess I'll see you around? Don't be a stranger in the night."
        show lun smirk_talk at right
        lun "Unless-"
        show pov embarrassed_talk at left
        show lun embarrassed at right
        pov "Bye!"

        $ sexaroundtownluna = 1

    else:
        show pov embarrassed at left
        with dissolve
        show lun neutral_talk at right
        hide btn_classroom_day_luna_idle2
        with dissolve
        lun "Hey, [povname]."
        show pov shocked at left
        show lun confused_talk at right
        lun "Have you seen a ghost? You're as white as freshly squeezed jizz."
        show pov sad at left
        show lun smirk_talk at right
        lun "But like seriously, if you have seen a ghost, call me."
        show pov shocked at left
        show lun neutral_talk at right
        lun "I'm gonna give them my body."

    jump lbl_schoolhallway2_day
