## Effie Main Story Throwaway Conversations Classroom ##
default sexaroundtowneffieclassroom = 0

## Sex Around Town Effie
label lbl_classroom_day_effie_sexworld:
    if sexaroundtowneffieclassroom == 0:
        show pov shocked_talk at left
        with dissolve
        hide btn_classroom_daysexworld_effie_idle2
        show effpo shocked at right
        with dissolve
        show pov shocked_talk at left
        with hpunch
        pov "EFFIE?!"
        show effpo confused at right
        with hpunch
        pov "WHAT ARE YOU DOIN-"
        show pov shocked at left
        show effpo bored_talk at right
        eff "Gosh, [povname]. Why are you yelling?"
        eff "It's way to early for you to be ringing bells in my ear."
        show pov shocked_talk at left
        show effpo bored at right
        pov "I-"
        show effpo confused at right
        pov "You're-"
        show pov shocked at left
        show effpo sad_talk at right
        eff "Dude, you're freaking me out."
        show pov shocked_talk at left
        show effpo confused at right
        pov "You're masturbating out here in the classroom?"
        show pov shocked at left
        eff "..."
        show effpo bored_talk at right
        eff "What are you? The feel-good police?"
        show effpo confused_talk at right
        eff "Class hasn't even started so just chill. You're acting really weird this morning."
        show pov shocked at left
        show effpo smirk_talk at right
        eff "Did someone roll out the wrong side of the bed today?"
        show effpo smirk at right
        pov "..."
        show effpo embarrassed at right
        eff "..."
        show pov shocked at left
        show effpo confused_talk at right
        eff "I- uh, don't really appreciate you watching over my shoulder."
        show effpo bored_talk at right
        eff "There's a thing called privacy."

        $ sexaroundtowneffieclassroom = 1

    else:
        show pov sad_talk at left
        with dissolve
        hide btn_classroom_daysexworld_effie_idle2
        show effpo confused at right
        with dissolve
        pov "Uh-"
        show pov sad at left
        eff "..."
        show effpo confused_talk at right
        eff "Are you okay, [povname]?"
        show pov sad_talk at left
        show effpo shocked at right
        pov "Uh--ghh"
        show pov sad at left
        eff "..."
        show effpo embarrassed_talk at right
        eff "Maybe you just need some coffee. Sounds like you're having a rough morning."

    jump lbl_classroom_day
