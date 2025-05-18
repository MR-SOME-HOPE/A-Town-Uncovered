## We Have to Burn the Truck ##
label lbl_we_have_to_burn_the_truck:

    scene bg allawaytruck_1
    with vpunch
    $ renpy.pause(0.5,hard=True)

    scene bg allawaytruck_1
    $ renpy.pause(0.5,hard=True)

    scene bg allawaytruck_2
    $ renpy.pause(0.5,hard=True)
    $ renpy.pause(0.5,hard=True)

    scene bg allawaytruck_2
    $ renpy.pause(0.5,hard=True)

    scene bg allawaytruck_1
    pov "Allaway, slow down!"

    scene bg allawaytruck_2
    pov "The drugs are with Jack! They won't find anything if they pull us over!"

    scene bg allawaytruck_1
    mis "I heard the radio, [povname]!"

    scene bg allawaytruck_6
    mis "They are looking for us! They saw us at the hospital - they know we have something!"
    mis "We have to get out of town; leave no trace!"
    mis "My parents have a cabin in the mountains. We can stay there for a few months, before they think to look there and-"

    scene bg allawaytruck_7
    pov "Allaway, calm down!"
    mis "Don't tell me to be calm!"
    pov "Listen, the only reason the police are looking for us is because you're speeding like the devil is after us!"

    scene bg allawaytruck_6
    pov "We have to hide the truck someplace the police won't find it."
    pov "We don't have to destroy it."
    mis "I am not taking any risks!"

    scene bg allawaytruck_7
    pov "But it's your father's truck!"
    mis "Don't you think I know that?!"

    scene bg allawaytruck_3
    mis "..."
    mis "I-I am not going to be able to rest easy if I know the police are looking for my truck..."

    scene bg allawaytruck_4
    mis "And with the condition it's in, I doubt it will take them long..."
    pov "The most they can do is give you a ticket."

    scene bg allawaytruck_5
    mis "Unless Jack has bought off the entire hospital staff, someone is going to notice eventually!"
    mis "Sooner or later they are going to connect the dots with us, I don't want to risk it!"

    scene bg allawaytruck_3
    pov "Are you sure about this?"
    mis "..."

    scene bg allawaytruck_4
    mis "No..."
    mis "But what choices do we have?"

    scene bg allawaytruck_5
    pov "Sadly, not many..."
    mis "..."

    scene bg allawaytruck_3
    pov "I am with you, with whatever you choose."
    pov "We started this together-"

    scene bg allawaytruck_4
    mis "And we'll end together..."
    mis "..."

    scene bg allawaytruck_5
    mis "Let's burn this rust bucket."

    jump lbl_truck_burning
