## Come Read Comics ##
label lbl_come_read_comics:
    show pov neutral at left
    with dissolve
    show jac neutral_talk at right
    with dissolve
    jac "Hey dude! Remember me?"
    show pov neutral_talk at left
    show jac neutral at right
    pov "Oh hey, dude. BJ right? The ol' Big Dick Mcgee."
    show pov neutral at left
    show jac bored_talk at right
    jac "Hmm, yeah. I think we should just stick with Jacob."
    show pov neutral_talk at left
    show jac bored at right
    pov "Good call."
    show pov neutral at left
    show jac neutral_talk at right
    jac "What are you up to today?"

    menu:
        "Wander around town.":
            show pov neutral_talk at left
            show jac neutral at right
            pov "I'm probably just gonna wander around town; find something to occupy myself with."
            show pov neutral at left
            show jac neutral_talk at right
            jac "Oh, really? You should come down to the comic book store with me!"

            jump lbl_come_read_comics_2
        "No plans.":
            show pov neutral_talk at left
            show jac neutral at right
            pov "No plans yet, yourself?"
            show pov neutral at left
            show jac neutral_talk at right
            jac "I'm gonna head down to the comic book store in a bit."

            jump lbl_come_read_comics_2

label lbl_come_read_comics_2:
    show pov neutral_talk at left
    show jac neutral at right
    pov "Comic book store? How vintage."
    show pov neutral at left
    show jac smirk_talk at right
    jac "Yeah, dude. It's actually a pretty sweet store. They have the latest comics, Marvle comics, manga, figurines, not to mention the X rated shit."
    show pov neutral_talk at left
    show jac smirk at right
    pov "What like porno mags? I haven't looked at a porno magazine in like, forever."
    show pov smirk_talk at left
    pov "In my world, there's this thing called the internet."
    show pov smirk at left
    show jac smirk_talk at right
    jac "Yeah, no shit it sounds ancient but c'mon man. Internet porn are such throwaways. Don't you want to own something that you'll cherish and remember?"
    jac "30 years from now, you'll look back on this day and remember that today was the day you got Issue 127 of ‘Fuck Bitches Pay Weekly'."
    jac "What do you say?"

    menu:
        "I'll stop by for a while.":
            show pov neutral_talk at left
            show jac neutral at right
            pov "If I'm not too busy today, I guess I'll stop by for a while. It might be a good hang out place to go to after uni."
            pov "Otherwise, I'll definitely come by some other time!"
            show pov neutral at left
            show jac neutral_talk at right
            jac "Awesome dude! Don't be a stranger. I'll introduce you to my friends there."
            show pov neutral_talk at left
            show jac neutral at right
            pov "Awesome, can't wait to see them."
            show pov neutral at left
            show jac neutral_talk at right
            jac "The comic book store is south-west from here. Right next to the beach. I'll see you there!"

            jump lbl_come_read_comics_end
        "It doesn't sound like my scene.":
            show pov bored_talk at left
            show jac neutral at right
            pov "It doesn't really sound like my type of scene to be honest."
            pov "No offence."
            show pov neutral at left
            show jac neutral_talk at right
            jac "Don't worry, it's cool. None taken, man. But trust me when I say you're missing out on some awesome stuff."
            jac "Well anyways, if you're ever curious and feel like stopping by anytime you're ready."
            jac "The comic book store is south-west from here. Right next to the beach."

            jump lbl_come_read_comics_end

label lbl_come_read_comics_end:
    show pov neutral_talk at left
    show jac neutral at right
    pov "Alright, Jacob. I'll see you 'round."
    $ main_story = 18
    $ townmap_enabled = 1
    $ renpy.notify("New Objective: Meet Jacob at the Comic Book Store")

    jump lbl_schoolhallway1_day_setup
