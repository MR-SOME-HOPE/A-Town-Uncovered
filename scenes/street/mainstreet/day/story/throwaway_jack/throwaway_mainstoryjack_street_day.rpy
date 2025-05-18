## Jack Main Story Throwaway Conversations Street ##
default sexaroundtownjack = 0

## Sex Around Town Jack
label lbl_street_day_jack_sexworld:
    if sexaroundtownjack == 0:
        ## Sprite Start
        show pov neutral_talk at left
        with dissolve
        hide btn street_day_jack_idle
        show jack bored at right
        with dissolve
        pov "Jack."
        show pov neutral at left
        show jack bored_talk at right
        jack "Cunt."
        show pov smirk_talk at left
        show jack bored at right
        pov "Fuck-nugget."
        show pov smirk at left
        show jack smirk_talk at right
        jack "Still a cunt."
        show pov bored at left
        show jack bored_talk at right
        jack "The fuck do you want?"
        show pov bored_talk at left
        show jack bored at right
        pov "You look pretty fucked up-"
        show pov confused_talk at left
        show jack angry at right
        pov "Care to fill me on why the whole town is having an orgy?"
        show pov neutral at left
        show jack angry_talk at right
        jack "If anyone sounds fucked up, it's you."
        show pov angry_talk at left
        show jack bored at right
        pov "I'm asking a genuinely reasonable question."
        show pov confused_talk at left
        show jack angry at right
        pov "I wouldn't ask you in the first place if I wasn't so fucking confused."
        show pov angry at left
        show jack angry_talk at right
        jack "Look, do me a favour and make like a tree."
        show pov confused at left
        show jack bored_talk at right
        jack "I don't care, and I don't care."
        show pov angry at left
        show jack bored_talk at right
        jack "Now, if you'll excuse me, I'm was in the middle of an important call."
        show pov confused at left
        show jack bored at right
        jack "..."
        show pov confused at left
        show jack bored_talk at right
        jack "{i}*On the phone*{/i} Yeah, no. It's no one. Just some lunatic trying to sell me literal bullshit."

        $ sexaroundtownjack = 1

    else:
        show pov bored_talk at left
        with dissolve
        hide btn street_day_jack_idle
        show jack bored at right
        with dissolve
        pov "Jack."
        show pov confused at left
        show jack angry_talk at right
        jack "Look, I told you to leave me alone."
        show pov shocked at left
        show jack angry_talk at right
        jack "Go back to your mom's pussy since that's where you belong."
        show pov confused at left
        show jack angry at right
        pov "{i}I don't know how to take that insult...{/i}"

    jump lbl_street_day
