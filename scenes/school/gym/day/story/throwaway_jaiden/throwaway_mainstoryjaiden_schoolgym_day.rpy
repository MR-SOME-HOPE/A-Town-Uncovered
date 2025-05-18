## Jaiden Main Story Throwaway Conversations Schoolgym ##
default sexaroundtownjaiden = 0

## Sex Around Town Jaiden
label lbl_schoolgym_day_jaiden_sexworld:
    if sexaroundtownjaiden == 0:
        show pov shocked_talk at left
        with dissolve
        show jain confused at right
        with dissolve
        pov "Jaiden! Care to explain why you have absolutely no clothes on?!"
        show pov shocked at left
        show jain bored_talk at right
        jai "Why are you yelling, maggot?!"
        show pov shocked_talk at left
        show jain confused at right
        pov "Why don't you have clothes on!"
        show pov shocked at left
        show jain angry_talk at right
        jai "I'm fucking excercising, maggot!"
        show jain confused_talk at right
        jai "Why would I sweat in my clothes, that's just stupid."
        show pov sad_talk at left
        show jain confused at right
        pov "Aren't you embarrassed or something? If a teacher sees you, you could be expelled or-"
        show pov sad at left
        show jain confused_talk at right
        jai "Calm the hell down, [povname]."
        show pov shocked at left
        jai "Read the school handbook again and you'll see that bare-skin is clearly allowed as uniform."
        show pov sad at left
        jai "I'm just standing here; and looking at you is already making me break into sweat."
        jai "Now if you'll excuse me, I've got a set to do. I'm limited on rest times."
        show pov shocked at left
        show jain confused_talk at right
        jai "Oh by the way, you haven't seen Jacob, have you? I told him that I'd show him my dick-squatting techniques."
        show jain smirk_talk at right
        jai "That guy's trying to bulk up, but it can't hurt to have a great-looking butt."

        $ sexaroundtownjaiden = 1

    else:
        show pov sad at left
        with dissolve
        show jain neutral_talk at right
        with dissolve
        jai "Hey, I'm a little busy at the moment."
        show pov confused at left
        show jain smirk_talk at right
        jai "Unless you can keep up with my pace."
        show jain confused_talk at right
        jai "Hopefully I can beat my record time today."
        show pov shocked at left
        show jain smirk_talk at right
        jai "It helps to not flick the bean for a few days, makes cumming a lot faster and intense."

    if gtime == 0:
        jump lbl_schoolgym_day
    else:
        jump lbl_schoolyard_day
