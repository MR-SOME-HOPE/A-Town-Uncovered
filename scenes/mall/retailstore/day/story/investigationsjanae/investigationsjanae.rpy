label lbl_investigations_janae:
    default investigations_janae = 0
    if investigations_janae != 0:
        pov "{i}She doesn't have the books I need.{/i}"
    else:
        $ investigations_janae = 1
        show pov embarrassed_talk at left
        with dissolve
        show jan neutral at right
        with dissolve
        pov "Hi, Janae?"
        show pov embarrassed at left
        show jan neutral_talk at right
        jan "Yes indeed!"
        jan "How can I help you?"
        show pov shocked at left
        show jan confused_talk at right
        jan "Hey, aren’t you that kid from the news-?"
        show pov embarrassed_talk at left
        show jan confused at right
        pov "Yes, yes I am... Although it’s not exactly something I’m proud of."
        show pov embarrassed at left
        show jan embarrassed_talk at right
        jan "Hey, we all have had a rough night that ended unexpectedly, right?"
        show jan neutral_talk at right
        jan "But that’s all beside the point. So, how can I help you?"
        show pov neutral_talk at left
        show jan neutral at right
        pov "Well, actually I was hoping to know if you sold books about something, in particular."
        show pov neutral at left
        show jan neutral_talk at right
        jan "Well, we have a little bit of everything here."
        show jan confused_talk at right
        jan "What exactly are you looking for?"
        show pov bored_talk at left
        show jan shocked at right
        pov "History about the town or urban myths of the town."
        show pov bored at left
        show jan shocked_talk at right
        jan "Huh. Now that's odd. You have to be one of the very few people who ask me about that topic."
        show pov shocked_talk at left
        show jan shocked at right
        pov "Really?"
        show pov shocked at left
        show jan embarrassed_talk at right
        jan "Yeah. Besides you, the only other person who has asked me about books about the town, is that nice girl Effie!"
        show pov confused_talk at left
        show jan confused at right
        pov "Effie?"
        show pov bored at left
        show jan confused_talk at right
        jan "Yeah, she is about your age, I believe."
        show pov embarrassed at left
        show jan neutral_talk at right
        jan "Really cool to talk with? Ponytail?"
        show pov embarrassed_talk at left
        show jan neutral at right
        pov "Yes, that's her. She is a friend of mine."
        show pov embarrassed at left
        show jan neutral_talk at right
        jan "She usually comes from time to time, asking if we have books about that and other occult stuff."
        show pov embarrassed at left
        show jan bored_talk at right
        jan "We sometimes have documentaries about paranormal stuff and the like, in the dvd’s section. But we mostly have novels and adult erotica in the book section."
        show pov smirk_talk at left
        show jan bored at right
        pov "So nothing of use for me, huh?"
        show pov smirk at left
        show jan smirk_talk at right
        jan "I’ll tell you what I keep telling her:"
        jan "You’ll have more luck with stuff like that from Sam, in the next store over."
        show pov confused at left
        show jan shocked_talk at right
        jan "He is a bit odd; but really sweet once you get to know him."
        show jan bored_talk at right
        jan "Plus he knows a lot about this sort of stuff."
        show pov confused_talk at left
        show jan smirk at right
        pov "Huh, well, worth the shot."
        show pov neutral_talk  at left
        show jan embarrassed at right
        pov "Thanks, Janae."
        show pov neutral at left
        show jan embarrassed_talk at right
        jan "No problem!"
        show pov confused at left
        show jan neutral at right
        jan "Oh, and for what it’s worth..."
        show pov shocked at left
        show jan smirk_talk at right
        jan "You have a rather cute ass~"
        show pov embarrassed_talk at left
        show jan smirk at right
        pov "Umm, thank you, I guess?"
        show pov embarrassed at left
        show jan smirk_talk at right
        jan "Don’t be a stranger!"

    jump lbl_retailstore_day
