## Zariah Main Story Throwaway Conversations School Hallway 1 ##
default sexaroundtownzariah = 0

## Sex Around Town Zariah
label lbl_schoolhallway1_day_zariah_sexworld:
    if sexaroundtownzariah == 0:
        show pov sad_talk at left
        with dissolve
        hide btn schoolhallway1_day_zariah_idle
        show zar neutral at right
        with dissolve
        pov "Hey, Zariah."
        show pov sad at left
        show zar embarrassed_talk at right
        zar "Hey, [povname]."
        show zar confused_talk at right
        zar "You feeling alright? Your head is swaying around in circles."
        show pov sad_talk at left
        show zar confused at right
        pov "I may or may not feel a little light-headed..."
        show pov sad at left
        show zar smirk_talk at right
        zar "You should probably sit down then. Catch your breath, rest up-"
        show pov shocked at left
        zar "A quickie blowjob may help, get some blood rushing to your head."
        show pov embarrassed_talk at left
        show zar confused at right
        pov "I- I- what?"
        show zar smirk at right
        pov "That's the wrong 'head'-"
        show pov confused at left
        show zar smirk_talk at right
        zar "Mmmm, nope. I know what I'm talking about, just look at me."
        show pov bored at left
        zar "I'm a doctor."
        show pov bored_talk at left
        show zar smirk at right
        pov "... Okay, now I know you're just fucking around."
        show pov bored at left
        show zar smirk_talk at right
        zar "Bazinga."
        show pov sad at left
        show zar confused_talk at right
        zar "But seriously, get some rest. Avoid rough sex, you might faint."
        show pov shocked at left
        show zar embarrassed_talk at right
        zar "Almost did that myself on stage last week during my set."
        zar "But dude had intense urges, can't fault him."
        show pov embarrassed_talk at left
        show zar neutral at right
        pov "... Right. Gotcha. Thanks for the tip, Z."

        $ sexaroundtownzariah = 1

    else:
        show pov sad at left
        with dissolve
        hide btn schoolhallway1_day_zariah_idle
        show zar smirk_talk at right
        with dissolve
        zar "How's the head, [povname]?"
        show zar confused_talk at right
        zar "Still looking a little loopy, I see."
        show zar neutral_talk at right
        zar "Well as I suggested, I'd stay off the rough stuff for now."
        zar "Don't wanna pass out mid-climax."

    jump lbl_schoolhallway1_day
