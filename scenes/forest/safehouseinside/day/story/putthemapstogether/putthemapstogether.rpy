## Put The Maps Together
label lbl_put_the_maps_together:
    scene bg forestsafehouseinside_day
    with fade
    ## At the hideout, everyone’s present.
    ## SPRITES
    show pov neutral at left
    show edw neutral at Position(xpos=1200)
    show jac shocked at Position(xpos=1600)
    with dissolve
    edw "Alright, we got the flyers."
    show edw smirk_talk at Position(xpos=1200)
    edw "Now we need to figure out this mysterious location."
    show edw confused_talk at Position(xpos=1200)
    edw "I don’t know much about the printing process but printing mistakes don’t usually involve different and unfinished sections."
    edw "I mean yes, the printer could’ve ran out of ink, but this is definitely a different kind of unfinished."
    show pov confused at left
    show jac smirk_talk at Position(xpos=1600)
    jac "I have a hunch."
    show edw confused at Position(xpos=1200)
    show jac embarrassed_talk at Position(xpos=1600)
    jac "Just a hunch but it might be too obvious."
    jac "I’ve seen this done in the movies before but there’s no way this could be the answer."
    show pov smirk_talk at left
    show jac confused at Position(xpos=1600)
    pov "What are you talking about, dude?"
    show pov confused at left
    show edw bored at Position(xpos=1200)
    show jac confused_talk at Position(xpos=1600)
    jac "Here, hand them over."
    show edw confused at Position(xpos=1200)
    jac "I need a bright light source though."

    ## Jacob stacks the flyer maps on top of each other and holds it up against the ceiling light bulb.
    ## CG
    scene bg putthemapstogether_1
    with fade

    eff "Oh-"

    col "My."

    edw "Shit."

    pov "Wait- that’s actually it?"
    pov "It actually is the answer."

    jac "I knew it!"
    jac "It’s so stupid and obvious that it was the answer all along."
    jac "Only an idiot would actually consider trying this."

    eff "Oh my God, Jacob! You idiotic genius."

    pov "It was literally right in front of us the whole time."

    col "Where is that."

    jac "That’s definitely the same street as the comic book store."
    jac "Wait-"
    jac "That’s the comic book store building."
    jac "The location is right next to it- in… the alley?"
    jac "What?"

    col "In the alleyway."

    eff "Are you sure?"

    jac "Oh- what? Now you’re questioning my genius?"
    jac "I’m literally solving the case right before your eyes and you’re questioning me."
    jac "So rude."

    eff "I’m not, I’m just suspicious of that being the actual location."
    eff "Are you sure it’s not the building next to Hendai’s?"

    jac "What? The adult store. I mean, it’s in the gap in between both buildings so it MUST be the alleyway."

    pov "I trust Jacob."
    pov "If Jacob says it’s the alleyway then the alleyway is where we shall check."

    col "Ew. But fine. I’m down to check that place out."

    edw "You better be right, Jacob."

    jac "Thanks, [povname]."

    col "Do you mind if we do it some other day though."

    eff "Actually yeah, I was just about to say. I have some assignments that I really can’t hand in late."

    col "I have clients I needed to meet up with."

    pov "Fine. We’ll meet up another time. I guess I’ll just head home."
    pov "Good job today, Jacob."
    pov "Proud of you, dude."

    jac "A point to Team Jacob."
    jac "Suck my ass, Edward."

    edw "What are you talking about?"

    scene black
    with fade
    $ renpy.pause()
    "Back at the forest entrance..."

    scene bg forest_day
    with fade

    $ main_story = 156

    jump lbl_forest_day_setup
