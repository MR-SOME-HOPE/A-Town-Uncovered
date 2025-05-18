## Post Detention ##
label lbl_post_detention:

    scene bg classroom_dayempty
    with fade
    show pov confused at left
    with dissolve
    show mis confused_talk at right
    with dissolve
    mis "Oh, [povname]. Before you go."
    show pov embarrassed at left
    show mis embarrassed_talk at right
    mis "I just want you to know that I really don't think you're a bad kid. You were just in the wrong place at the wrong time."
    show mis confused_talk at right
    mis "I expect not to see you here in detention again in the future."
    show pov smirk_talk at left
    show mis confused at right
    pov "I can't promise you that, Miss. I'm pretty known for being in the wrong place at the wrong time."
    show pov neutral at left
    show mis confused_talk at right
    mis "You would describe yourself as unlucky?"
    show pov embarrassed_talk at left
    show mis neutral at right
    pov "Not unlucky. Just a guy with a very eventful life."
    show pov embarrassed at left
    show mis neutral_talk at right
    mis "I'm sure you'll come across something worthy of your end-of-year paper, then."
    show pov embarrassed_talk at left
    show mis confused at right
    pov "Speaking of which; I'm still having trouble with it."
    show pov sad_talk at left
    pov "I still don't have anything to talk write about."
    show pov embarrassed at left
    show mis confused_talk at right
    mis "I can't really just hand it to you on a platter, [povname]. This is your final assignment we're talking about."
    show mis neutral_talk at right
    mis "I want you to keep trying; and put some brain power into it."
    show pov neutral at left
    show mis smirk_talk at right
    mis "Here's the deal: once you get a topic in mind, then I can help you from there."
    show pov embarrassed at left
    show mis confused_talk at right
    mis "But for now, we're literally working with nothing."
    show pov embarrassed_talk at left
    show mis neutral at right
    pov "Alright, just thought I'd throw it out there."
    show pov neutral at left
    show mis neutral_talk at right
    mis "Once we get a foundation, I'll help you build the walls and all the intricacies."
    show pov neutral_talk at left
    show mis neutral at right
    pov "Thanks, Miss Allaway."
    show pov smirk_talk at left
    show mis bored at right
    pov "Can I call you by your first name  - I feel like we've gotten so clos-"
    show pov embarrassed at left
    show mis bored_talk at right
    mis "No."
    show pov embarrassed_talk at left
    show mis bored at right
    pov "I understand, respect."
    show pov embarrassed at left
    show mis neutral_talk at right
    mis "I think that's enough chatter for today, [povname]."
    show pov confused at left
    show mis confused_talk at right
    mis "Class is about to start again."

    menu:
        "Sorry about everything.":
            show pov embarrassed_talk at left
            show mis neutral at right
            pov "Sorry about everything."
            if skill_cha >= 4:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ renpy.notify("Your relationship with Miss Allaway has increased")
                show pov embarrassed at left
                show mis neutral_talk at right
                mis "It's alright, just keep your finger out of your nose and stay in university."
                show pov smirk_talk at left
                show mis neutral at right
                pov "Heh, thought you preferred that I didn't stay in university past class hours."
                show pov smirk at left
                show mis embarrassed_talk at right
                mis "Oh, you know what I mean."
                show pov smirk_talk at left
                show mis neutral at right
                pov "I'll be off then, Miss."
                show pov smirk at left
                show mis neutral_talk at right
                mis "Take care of yourself, [povname]."
            else:
                show pov embarrassed at left
                show mis confused_talk at right
                mis "It's alright, just keep out of trouble."
                show pov embarrassed_talk at left
                show mis neutral at right
                pov "I'll do my best."
                show pov embarrassed at left
                show mis neutral_talk at right
                mis "I'll see you in class, [povname]."
                show pov embarrassed_talk at left
                show mis neutral at right
                pov "You too, Miss."
        "It was nice spending time with you.":
            show pov smirk_talk at left
            show mis confused at right
            pov "It was nice spending time with you."
            if skill_cha >= 7:
                if missallaway_points <= 8:
                    $ missallaway_points += 2
                else:
                    $ missallaway_points = 10
                $ renpy.notify("Your relationship with Miss Allaway has increased by 2")
                show pov smirk at left
                show mis confused_talk at right
                mis "Even if it was detention?"
                show pov smirk_talk at left
                show mis confused at right
                pov "Even if we were trapped in a horror movie."
                show mis embarrassed at right
                pov "Any time with you is time well spent."
                show pov smirk at left
                show mis embarrassed_talk at right
                mis "You're really a filter-free person, aren't you?"
                mis "Take care of yourself, [povname]. I'll see you when I see you."
            else:
                show pov smirk at left
                show mis confused_talk at right
                mis "Don't get it the wrong way, [povname]. It was detention."
                show pov embarrassed_talk at left
                show mis confused at right
                pov "But still."
                show pov embarrassed at left
                show mis bored_talk at right
                mis "But still nothing, I suggest you quit it with these games."
                mis "I'm your teacher - for one - and it is still highly inappropriate."
                show pov smirk_talk at left
                show mis bored at right
                pov "I like a challenge."
                show pov embarrassed at left
                show mis bored_talk at right
                mis "Well, expect the impossible."
                mis "Goodbye, [povname]."
        "See you, Miss Allaway.":
            show pov neutral_talk at left
            show mis neutral at right
            pov "See you, Miss Allaway."
            if skill_cha >= 1 and skill_luc >= 3:
                if missallaway_points <= 9:
                    $ missallaway_points += 1
                else:
                    $ missallaway_points = 10
                $ renpy.notify("Your relationship with Miss Allaway has increased")
                show pov neutral at left
                show mis neutral_talk at right
                mis "Goodbye, [povname]. Take care of yourself."
                show mis smirk_talk at right
                mis "Stay out of trouble, okay? For me."
                show pov smirk_talk at left
                show mis smirk at right
                pov "I'll do my best, I can't guarantee that trouble will stay out of me."
                show pov smirk at left
                show mis smirk_talk at right
                mis "You're quite the silver tongued fox, aren't you?"
            else:
                show pov neutral at left
                show mis neutral_talk at right
                mis "Goodbye, [povname]."
                mis "Stay out of trouble, okay?"
                show pov neutral_talk at left
                show mis neutral at right
                pov "Sure thing, Miss. I can do that."
                show pov neutral at left
                show mis neutral_talk at right
                mis "Good, good. Alright, off you go."
    $ townmap_enabled = 1
    $ missallaway_path = 6

    jump lbl_schoolhallway1_day_setup
