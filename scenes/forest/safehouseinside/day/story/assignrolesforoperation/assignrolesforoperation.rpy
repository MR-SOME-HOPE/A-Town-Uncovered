## Assign Roles for Operation
default operation_flyer = "lockpick"

label lbl_assign_roles_for_operation:
    scene bg forestsafehouseinside_day
    with fade

    ## SPRITES with pov, eff, jac

    show pov smirk_talk at left
    with dissolve
    pov "Hey, Effie, Jacob."
    show pov confused_talk at left
    pov "Where’s the other two?"

    ## Cole and Edward show up

    show pov confused at left
    show col shocked_talk at Position(xpos=1000)
    show edw neutral at Position(xpos=1400)
    with dissolve
    col "Whoaa- this place is-"
    col "This place!"
    show pov embarrassed at left
    show col neutral_talk at Position(xpos=1000)
    col "Wow!"
    show pov neutral at left
    show edw embarrassed at Position(xpos=1400)
    col "Look at this place."
    show col neutral_talk at Position(xpos=1000)
    col "Thank you so much for inviting me into your team, [povname]."
    show col smirk_talk at Position(xpos=1000)
    col "Do I call you captain?"
    show pov embarrassed_talk at left
    show col smirk at Position(xpos=1000)
    show edw bored at Position(xpos=1400)
    pov "Hey, Cole."
    show pov embarrassed at left
    show col embarrassed at Position(xpos=1000)
    show edw bored_talk at Position(xpos=1400)
    edw "And hey, Edward."
    show pov neutral_talk at left
    show edw smirk at Position(xpos=1400)
    pov "Hey, Edward."
    show pov neutral at left
    show col neutral at Position(xpos=1000)
    show edw shocked_talk at Position(xpos=1400)
    edw "Alright, skipping the small talk, [povname]. I have devised a plan that is fool proof."
    show pov smirk at left
    show col neutral_talk at Position(xpos=1000)
    show edw smirk at Position(xpos=1400)
    col "We watched a lot of heist movies."
    show col smirk at Position(xpos=1000)
    show edw smirk_talk at Position(xpos=1400)
    edw "You watched a lot of heist movies, I was busy working on the actual plan."
    show pov embarrassed at left
    show col smirk_talk at Position(xpos=1000)
    show edw bored at Position(xpos=1400)
    col "Sure, sure. Whatever makes you feel more superior, little man."
    show col smirk at Position(xpos=1000)
    show edw bored_talk at Position(xpos=1400)
    edw "Ugh- anyway. This plan requires 3 roles; the distractor, the lookout, and the lockpicker."
    show edw neutral_talk at Position(xpos=1400)
    edw "It’s pretty straightforward, nothing too creative is needed."
    show edw confused_talk at Position(xpos=1400)
    edw "We’re breaking into the dean’s office, not a high security bank."
    show pov confused at left
    show col bored at Position(xpos=1000)
    show edw neutral_talk at Position(xpos=1400)
    edw "Anyway, the distractor will keep Lashley talking down in the hallway on the ground floor level."
    show edw smirk_talk at Position(xpos=1400)
    edw "I’ve kept track of her bathroom habits and she tends to go about 5 minutes after the first period has started."
    show col confused at Position(xpos=1000)
    show edw confused_talk at Position(xpos=1400)
    edw "This is our moment to strike."
    edw "The lookout will simply look out on the staircase to make sure everything is in the clear and will signal the lockpicker if things look dire."
    show pov shocked at left
    show col bored at Position(xpos=1000)
    show edw shocked_talk at Position(xpos=1400)
    edw "The lock-picker will pick her office door lock and then run in to look for the confiscated flyers."
    show pov embarrassed at left
    show col smirk at Position(xpos=1000)
    show edw confused_talk at Position(xpos=1400)
    edw "They should be stashed in one of her draws."
    show pov confused at left
    show col bored at Position(xpos=1000)
    show edw confused at Position(xpos=1400)
    show eff bored_talk at Position(xpos=1600)
    with dissolve
    eff "Who knows how to lock-pick?"

    ## If MC knows how to lockpick
    if know_lockpick == 1:
        $ operation_flyer = "lockpick"
        show pov confused_talk at left
        show col smirk at Position(xpos=1000)
        show edw shocked at Position(xpos=1400)
        show eff smirk at Position(xpos=1600)
        show jac shocked at Position(xpos=1800)
        with dissolve
        pov "I do."
        show pov embarrassed at left
        show eff smirk_talk at Position(xpos=1600)
        eff "Great, then you’re the designated lockpicker and flyer grabber."
        show eff confused_talk at Position(xpos=1600)
        eff "Any objections?"
        show pov neutral_talk at left
        show col neutral at Position(xpos=1000)
        show eff bored at Position(xpos=1600)
        pov "No, no need. I can do it."
        show pov neutral at left
        show edw neutral at Position(xpos=1400)
        show eff smirk_talk at Position(xpos=1600)
        show jac neutral at Position(xpos=1800)
        eff "Great."
        show eff smirk at Position(xpos=1600)
        show jac smirk_talk at Position(xpos=1800)
        jac "Cole and I can be distractors. We can sure talk a lot and I’m pretty sure she likes me."
        show col smirk_talk at Position(xpos=1000)
        show jac neutral at Position(xpos=1800)
        col "Bro, $10 you can’t get her to laugh at one of your flirtatious jokes."
        show col confused at Position(xpos=1000)
        show jac neutral_talk at Position(xpos=1800)
        jac "You’re on. I can make her laugh so much, you’d be paying me to tell you my secrets."
        show col smirk_talk at Position(xpos=1000)
        show jac neutral at Position(xpos=1800)
        col "That’s so stupid."
        col "Deal."
        show col smirk at Position(xpos=1000)
        show eff shocked_talk at Position(xpos=1600)
        show jac  at Position(xpos=1800)
        eff "Alright, I’ll stick with [povname] and help him look in her office."
        show edw neutral at Position(xpos=1400)
        show eff neutral_talk at Position(xpos=1600)
        eff "Would you be okay on lookout, Edward?"
        show col neutral_talk at Position(xpos=1000)
        edw "Easiest job in the gang."
        show pov embarrassed at left
        show col neutral at Position(xpos=1000)
        show edw bored_talk at Position(xpos=1400)
        edw "Just don’t fuck up, Jacob."
        show col neutral at Position(xpos=1000)
        show jac shocked_talk at Position(xpos=1800)
        jac "And Cole?!"
        show col bored at Position(xpos=1000)
        show edw smirk_talk at Position(xpos=1400)
        show eff bored at Position(xpos=1600)
        show jac shocked at Position(xpos=1800)
        edw "Nope, just you."
        show edw bored at Position(xpos=1400)
        show jac bored_talk at Position(xpos=1800)
        jac "Spain without the ‘s’."

    else:
        $ operation_flyer = "distract"
        show pov embarrassed at left
        show col smirk at Position(xpos=1000)
        show edw shocked at Position(xpos=1400)
        show eff smirk_talk at Position(xpos=1600)
        show jac shocked at Position(xpos=1800)
        eff "…"
        eff "No one? Then I guess that role is up to anyone."
        show eff bored_talk at Position(xpos=1600)
        eff "Well, then one of us has to."
        show pov neutral at left
        show edw embarrassed_talk at Position(xpos=1400)
        show eff bored at Position(xpos=1600)
        edw "I can learn, it shouldn’t be that hard."
        edw "Child’s play really."
        show col confused at Position(xpos=1000)
        show jac bored at Position(xpos=1800)
        edw "I’ve learnt way harder skills."
        show pov smirk at left
        show eff smirk_talk at Position(xpos=1600)
        eff "Okay, okay. You don’t need to brag about it, you haven’t even started."
        show edw embarrassed at Position(xpos=1400)
        show eff shocked_talk at Position(xpos=1600)
        eff "I’ll help Edward look around the office so we can grab the flyers quicker."
        show pov neutral at left
        show eff neutral_talk at Position(xpos=1600)
        show jac confused at Position(xpos=1800)
        eff "[povname]. Would you down to distract Lashley?"
        eff "You and her seem to get along well."
        show pov embarrassed_talk at left
        show eff smirk at Position(xpos=1600)
        pov "I don’t know if that’s how I’d describe it but sure."
        show pov embarrassed at left
        show col smirk_talk at Position(xpos=1000)
        col "I’ll back you up, dude."
        col "Talking is my game, but I’ll let you lead the waltz."
        show col bored at Position(xpos=1000)
        show eff bored at Position(xpos=1600)
        show jac confused_talk at Position(xpos=1800)
        jac "It’s a weird waltz when 3 people are involved."
        show col bored_talk at Position(xpos=1000)
        show edw smirk at Position(xpos=1400)
        show jac shocked at Position(xpos=1800)
        col "You’re just mad that you’re on lookout duty."
        show col smirk at Position(xpos=1000)
        show jac angry at Position(xpos=1800)
        col "The least important role."
        show pov embarrassed_talk at left
        show col bored at Position(xpos=1000)
        show eff neutral at Position(xpos=1600)
        show jac shocked_talk at Position(xpos=1800)
        jac "Oh- whatever."
        jac "I’d use the time too catch up on some sleep if I didn’t have confidence in your distraction ability."
        show pov shocked at left
        show col smirk_talk at Position(xpos=1000)
        show edw shocked at Position(xpos=1400)
        show eff shocked at Position(xpos=1600)
        show jac shocked at Position(xpos=1800)
        col "Wanna bet? Bitch?"
        show col bored at Position(xpos=1000)
        show jac confused_talk at Position(xpos=1800)
        jac "$2?"
        show col smirk at Position(xpos=1000)
        show edw smirk at Position(xpos=1400)
        show eff bored at Position(xpos=1600)
        show jac smirk_talk at Position(xpos=1800)
        jac "No. $5!"
        show pov confused at left
        show col bored_talk at Position(xpos=1000)
        show edw neutral at Position(xpos=1400)
        show eff  at Position(xpos=1600)
        show jac shocked at Position(xpos=1800)
        col "Pennies."
        show col neutral at Position(xpos=1000)
        show eff angry_talk at Position(xpos=1600)
        show jac bored at Position(xpos=1800)
        eff "Guys! Not the time."

    show pov shocked at left
    show edw shocked_talk at Position(xpos=1400)
    show jac confused at Position(xpos=1800)
    show eff confused at Position(xpos=1600)
    edw "Okay, so we got our roles sorted out."
    show edw confused_talk at Position(xpos=1400)
    edw "We need to be at school first thing in the morning."
    show pov neutral at left
    show col bored at Position(xpos=1000)
    show edw shocked_talk at Position(xpos=1400)
    edw "Everyone know what they’re doing? It’s pretty simple."
    show col neutral at Position(xpos=1000)
    show edw confused_talk at Position(xpos=1400)
    show jac shocked at Position(xpos=1800)
    edw "No questions, right?"
    show jac shocked_talk at Position(xpos=1800)
    show eff bored at Position(xpos=1600)
    jac "Ah-"
    show pov embarrassed at left
    show edw smirk_talk at Position(xpos=1400)
    show jac shocked at Position(xpos=1800)
    show eff smirk at Position(xpos=1600)
    edw "Alright cool!"
    show pov embarrassed at left
    show edw bored_talk at Position(xpos=1400)
    show jac angry at Position(xpos=1800)
    edw "Meeting adjourned."
    show col smirk_talk at Position(xpos=1000)
    show edw bored at Position(xpos=1400)
    col "Shouldn’t the leader say that…"
    show col neutral_talk at Position(xpos=1000)
    col "No?"
    show col shocked_talk at Position(xpos=1000)
    col "Okay…"
    show pov neutral at left
    show col neutral_talk at Position(xpos=1000)
    col "Oh yeah, how do I get back from here?"

    scene black
    with fade
    $ renpy.pause()
    "Back at forest entrance..."

    scene bg forest_day
    with fade

    $ main_story = 154

    jump lbl_forest_day_setup
