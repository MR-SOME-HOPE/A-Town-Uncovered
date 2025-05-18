## Cole Main Story Throwaway Conversations School Cafeteria ##
default sexaroundtowncole = 0

## Sex Around Town Cole
label lbl_schoolcafeteria_day_cole_sexworld:
    if sexaroundtowncole == 0:
        show pov embarrassed_talk at left
        with dissolve
        show col neutral at right
        hide btn_schoolcafeteria_day_cole_idle2
        with dissolve
        pov "Cole..."
        show col smirk at right
        pov "I'm sure a... logicial... rational... man such as yourself can help me out here."
        show pov embarrassed at left
        show col smirk_talk at right
        col "What's up, [povname]?"
        show pov sad_talk at left
        show col confused at right
        pov "Why is- everyone... literally fucking around?"
        show pov embarrassed at left
        show col smirk_talk at right
        col "Hahahaha, you're funny. That's what I like about you."
        show col neutral_talk at right
        col "Always bringing out the humour where humour isn't found."
        col "In any case, I've got a meeting with someone in a bit."
        show pov embarrassed_talk at left
        show col neutral at right
        pov "Right."
        show pov shocked at left
        show col smirk_talk at right
        col "You seem to be good with the ladies, should I lick her ass or ease my way in with a titty?"
        show pov embarrassed_talk at left
        show col smirk at right
        pov "W-what?"
        show pov shocked at left
        show col smirk_talk at right
        col "Well, y'know. It's good to make a good first impression with a potential business partner"
        show pov shocked_talk at left
        show col confused at right
        pov "Um..."
        menu:
            "Ass.":
                show pov embarrassed_talk at left
                show col smirk at right
                pov "Ass."
                show pov shocked at left
                show col smirk_talk at right
                col "Good thinking. Shows that I'm super casual and not too married to her as a partner."
                show col neutral_talk at right
                col "Thanks, bud. See you around."
            "Titty.":
                show pov embarrassed_talk at left
                show col smirk at right
                pov "Titty."
                show pov embarrassed at left
                show col smirk_talk at right
                col "I hear you, keep things strictly professional. Good point."
                show col neutral_talk at right
                col "Thanks, man. I knew I could count on you."
            "I don't know...":
                show pov sad_talk at left
                show col confused at right
                pov "I don't know..!"
                show pov shocked_talk at left
                show col shocked at right
                pov "I don't know anything!"
                show pov sad at left
                show col embarrassed_talk at right
                col "Okay, dude. Calm down, I didn't mean to touch a soft spot."
                col "I'll see you later, okay?"

        $ sexaroundtowncole = 1

    else:
        show pov embarrassed at left
        with dissolve
        show col neutral_talk at right
        hide btn_schoolcafeteria_day_cole_idle2
        with dissolve
        col "Hey, man. Sorry, can't talk."
        col "I'm waiting to meet up with someone."
        show col smirk_talk at right
        col "I suggest you do the same, you look a little pale."
        col "Get that blood flowing into your head if you get my Tokyo-drift."

    jump lbl_schoolcafeteria_day
