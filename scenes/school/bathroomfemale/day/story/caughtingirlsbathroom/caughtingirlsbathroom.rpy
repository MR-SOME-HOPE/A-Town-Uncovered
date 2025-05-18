## Caught in Girls' Bathroom ##
label lbl_caught_in_girls_bathroom:

    scene bg schoolbathroomfemale_day
    with fade
    show pov shocked at left
    with dissolve
    with hpunch
    mis "[povname]?!"
    show mis angry_talk at right
    with dissolve
    mis "What the hell are you doing in the female bathrooms?!"

    menu:
        "I thought this was the male bathroom.":
            show pov embarrassed_talk at left
            show mis angry at right
            pov "I honestly thought this was the male bathrooms."
            show pov embarrassed at left
            show mis angry_talk at right
            mis "I honestly think that's a poor excuse for being a Peeping Tom."
            show pov angry_talk at left
            show mis bored at right
            pov "I'm not a Peeping Tom!"
            show pov embarrassed at left
            show mis angry_talk at right
            mis "Says the boy guiltily in the bathroom that is clearly for girls only."
        "I'm meeting someone here.":
            show pov embarrassed_talk at left
            show mis angry at right
            pov "I was meant to meet someone here."
            show pov embarrassed at left
            show mis angry_talk at right
            mis "Uh-huh? And why did you think this was an acceptable place to meet up?"
            show pov embarrassed_talk at left
            show mis angry at right
            pov "I- I don't think it is now."
            show pov embarrassed at left
            show mis angry_talk at right
            mis "It never was, [povname]."
        "I was looking for you.":
            show pov embarrassed_talk at left
            show mis angry at right
            pov "I was looking for you."
            show pov embarrassed at left
            show mis angry_talk at right
            mis "You must be joking or something because that is the stupidest excuse I heard thus far."
            show pov embarrassed_talk at left
            show mis angry at right
            pov "I swear, I needed to talk to you about something important!"
            show pov embarrassed at left
            show mis angry_talk at right
            mis "Well, guess what? I have a better place for us to converse."
    show pov embarrassed at left
    show mis angry at right
    pov "..."
    show pov bored at left
    show mis angry_talk at right
    mis "Detention, today. During lunch break."
    mis "And don't you dare try and skip out on it!"
    show pov bored_talk at left
    show mis angry at right
    pov "Fine... fine. I'll be there."
    show pov bored at left
    show mis angry_talk at right
    mis "Now get your butt out of here before I-"
    show pov confused at left
    show mis angry_talk at right
    mis "Uh- yeah, get out, [povname]."
    if gtime == 0:
        show pov bored at left
        hide mis angry_talk at right
        pov "{i}Great, now I have to stay for the day. I guess I'll attend class to pass the time.{/i}"
    $ townmap_enabled = 0
    $ missallaway_path = 5

    jump lbl_schoolbathroomfemale_day
