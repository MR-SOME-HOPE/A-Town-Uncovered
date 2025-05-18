## Edward Main Story Throwaway Conversations Schoolyard ##
default sexaroundtownedward = 0

## Sex Around Town Edward
label lbl_schoolyard_day_edward_sexworld:
    if sexaroundtownedward == 0:
        show pov embarrassed_talk at left
        with dissolve
        show edw confused at right
        with dissolve
        pov "Hey, Edward."
        show pov sad_talk at left
        pov "You... who-"
        pov "What is going on here? You seem to be the guy to tell it to me straight."
        show pov sad at left
        show edw confused_talk at right
        edw "I have no idea what you're talking about."
        show pov embarrassed at left
        edw "I'm just out here like every other morning testing my invention."
        show pov shocked_talk at left
        show edw bored at right
        pov "Look around you, man! Open your eyes."
        show pov shocked at left
        show edw bored_talk at right
        edw "That's a little racist... don't you think?"
        show pov sad_talk at left
        show edw bored at right
        pov "I didn't mean it like that! Just-"
        show pov shocked_talk at left
        show edw confused at right
        pov "Look over there! Those two are just having sex! Out in the open."
        pov "At fucking uni!"
        show pov shocked at left
        edw "..."
        show edw confused_talk at right
        edw "Did you watch a North Korean propaganda video, [povname]?"
        show pov angry at left
        edw "Because you're acting like you've been brain-washed."
        show pov angry_talk at left
        show edw confused at right
        pov "What does a North Korean prop-"
        show pov bored at left
        show edw confused_talk at right
        edw "Hmmm, it really does seem like you have though."
        show pov confused at left
        edw "Y'see, that's the difference between us and them."
        show pov bored at left
        show edw smirk_talk at right
        edw "Two words, 'free'-'dom'."
        show pov sad at left
        edw "Hehehe, next thing you'll say is that we shouldn't be allowed to have different haircuts."

        $ sexaroundtownedward = 1

    else:
        show pov confused at left
        with dissolve
        show edw confused_talk at right
        with dissolve
        edw "Hey, [povname]. I'm a little busy at the moment."
        edw "Can you not interfere with my pussy magnet."
        show edw bored at right
        edw "..."
        show edw embarrassed_talk at right
        edw "It's a work in progress. Seems to be attracting more dicks and assholes than anything."

    jump lbl_schoolyard_day
