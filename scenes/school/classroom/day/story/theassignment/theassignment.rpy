## The Assignment ##
label lbl_the_assignment:

    scene black
    with fade
    "After class..."

    scene bg classroom_day
    with fade
    show pov neutral at left
    with dissolve
    show mis neutral_talk at right
    with dissolve
    mis "[povname], can I steal you for a second?"
    show pov neutral_talk at left
    show mis neutral at right
    pov "Sure."
    show pov neutral at left
    show mis neutral_talk at right
    mis "How are you feeling about the assignment?"

    menu:
        "Pretty Confident.":
            jump lbl_the_assignment_confident
        "Alright.":
            jump lbl_the_assignment_alright
        "Screwed.":
            jump lbl_the_assignment_screwed

label lbl_the_assignment_confident:
    if missallaway_points <= 9:
        $ missallaway_points += 1
    else:
        $ missallaway_points = 10
    $ renpy.notify("Your relationship with Miss Allaway has increased")
    show pov neutral_talk at left
    show mis neutral at right
    pov "I'm feeling pretty confident about it."
    show pov neutral at left
    show mis neutral_talk at right
    mis "That's great to hear, I love a person with confidence. I only ask because I'm unfamiliar with your writing abilities."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Oh, yeah of course. No, I'm feeling good about this."

    jump lbl_the_assignment_1

label lbl_the_assignment_alright:
    show pov neutral_talk at left
    show mis neutral at right
    pov "I'm feeling alright about it."
    show pov neutral at left
    show mis neutral_talk at right
    mis "That's good. I only ask because I'm unfamiliar with your writing abilities."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Oh, yeah of course. I'm not the best writer but I'll definitely give it all I got."

    jump lbl_the_assignment_1

label lbl_the_assignment_screwed:
    if missallaway_points <= 9:
        $ missallaway_points += 1
    else:
        $ missallaway_points = 10
    $ renpy.notify("Your relationship with Miss Allaway has increased")
    show pov sad_talk at left
    show mis neutral at right
    pov "I'm totally screwed if I was completely honest."
    show pov sad at left
    show mis neutral_talk at right
    mis "You shouldn't worry too much, as I said earlier, you have the WHOLE year ahead of you to get it done."
    show pov neutral at left
    mis "You can always book a one-on-one session with me during out of class time if you want."
    mis "I'll be more than happy to help you succeed."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Thanks, Miss. I'll definitely consider it."

    jump lbl_the_assignment_1

label lbl_the_assignment_1:
    show pov neutral at left
    show mis neutral_talk at right
    mis "Do you have an idea on what you want to do your piece on?"
    show pov bored_talk at left
    show mis neutral at right
    pov "I'm not quite sure to be honest."
    show pov bored at left
    show mis bored_talk at right
    mis "Nothing in the news catches your attention?"
    show pov bored_talk at left
    show mis bored at right
    pov "I haven't really gotten around to checking what's been happening in the world lately."
    show pov neutral at left
    show mis neutral_talk at right
    mis "By all means, take your time with it."
    mis "There might not be something right now but something might come up next week, or even next month."
    mis "I just advise you to decide on something early on so that you have plenty of time to gather information and research for it."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Alright."
    show pov neutral at left
    show mis neutral_talk at right
    mis "Alright, [povname], that's all. I'll see you tomorrow."
    $ main_story = 8
    $ gtime += 1
    $ townmap_enabled = 0
    $ renpy.notify("New Objective: Get Assignment Done")
    $ renpy.pause(3,hard=False)
    $ renpy.notify("New Contact: Miss Allaway")

    jump lbl_classroom_day_setup
