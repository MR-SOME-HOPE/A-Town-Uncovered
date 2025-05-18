## Convincing Xina
label lbl_convincing_xina:
    # At Eloise’s POV
    scene black
    $ renpy.pause()
    "In the other dimension..."
    $ renpy.pause()

    elo "You must be."

    xin "Exactly."

    scene bg officesurveillanceroom_daynight
    with fade
    show elo sad flip at left
    show xin bored_talk at right
    with dissolve
    xin "I am you."

    show elo sad_talk flip
    show xin bored
    elo "But..."
    elo "You’re so different..."
    elo "How?"

    show elo sad flip
    show xin embarrassed_talk
    xin "*Chuckles*"
    xin "It’s a miracle you haven’t cracked like I did."

    show xin embarrassed
    elo "..."
    show elo sad_talk flip
    show xin shocked
    elo "Why, El?"
    elo "Why did you do it?"

    show elo sad flip
    xin "..."
    show xin sad_talk
    xin "I had my reasons."
    show xin sad
    xin "..."
    show xin sad_talk
    xin "I thought..."
    xin "I thought I’d be happy."
    xin "But this?"
    xin "This isn’t how it’s meant to be."
    xin "I was trying to create a utopia."
    xin "To share the lifestyle of my world with yours."
    xin "But..."
    xin "All I see is destruction of people’s humanity."
    xin "It’s... so... different to how I imagined it would work out."

    show xin sad
    elo "..."

    show xin embarrassed_talk
    xin "All these years, working and scheming, and planning and plotting."
    xin "And the results are... dud."

    show elo embarrassed_talk flip
    show xin sad
    elo "Things just don’t work out the way you want."

    show elo embarrassed flip
    show xin embarrassed_talk
    xin "I know what you’re saying."

    show elo sad_talk flip
    show xin embarrassed
    elo "We have to, El."

    show elo embarrassed flip
    show xin sad_talk
    xin "We have to pull the runes apart."
    show xin sad
    xin "*Sniff*"
    show xin sad_talk
    xin "I’m sorry, El."
    xin "I’m sorry we had to go through this."

    show elo sad_talk flip
    show xin sad
    elo "I-"
    elo "I don’t know if I can forgive you."
    elo "What you did was monstrous."

    show elo sad flip
    show xin sad_talk
    xin "I know."
    show xin sad
    xin "*Sniff*"
    show xin sad_talk
    xin "Then let’s at least make it right."

    show elo sad flip
    elo "Mhmm."
    show elo sad_talk flip
    elo "Let’s."

    $ main_story = 131

    jump lbl_the_rune_separation
