label lbl_last_hour_of_school:
    scene bg chalkboard_day
    with fade
    show pov embarrassed at left
    show eff bored_talk at Position(xpos=1300)
    show col smirk at Position(xpos=1600)
    show jac neutral at Position(xpos=1800)
    eff "Well, that wasn’t too bad."
    show eff bored at Position(xpos=1300)
    show col smirk_talk at Position(xpos=1600)
    col "At least it was quick."
    show pov embarrassed_talk at left
    show eff bored at Position(xpos=1300)
    show col smirk at Position(xpos=1600)
    show jac shocked at Position(xpos=1800)
    pov "So, just one more hour of uni and we can go back home, right?"
    show pov embarrassed at left
    show eff bored_talk at Position(xpos=1300)
    show col shocked at Position(xpos=1600)
    eff "Ugh, I can't. I gotta help out Brock and the manager with cleaning up the coffee shop."
    show eff embarrassed_talk at Position(xpos=1300)
    eff "If there is even one piece of broken glass left behind after his final inspection then he is going to have a hissy-fit."
    show pov shocked at left
    show eff shocked at Position(xpos=1300)
    show col confused at Position(xpos=1600)
    show jac neutral_talk at Position(xpos=1800)
    jac "Want me to go help out? It’s not like I am doing anything."
    show eff embarrassed_talk at Position(xpos=1300)
    show col embarrassed at Position(xpos=1600)
    show jac neutral at Position(xpos=1800)
    eff "Nah, it’s cool."
    eff "I doubt the manager is going to be okay with me bringing others to clean up the store anyway."
    show eff shocked at Position(xpos=1300)
    show col shocked at Position(xpos=1600)
    show jac neutral_talk at Position(xpos=1800)
    jac "Want us to walk you there? I mean, it's on the way, so it wouldn’t be a big deal."
    show pov embarrassed at left
    show eff confused at Position(xpos=1300)
    show jac smirk_talk at Position(xpos=1800)
    jac "Right, [povname]?"
    show pov neutral_talk at left
    show eff embarrassed at Position(xpos=1300)
    show jac neutral at Position(xpos=1800)
    pov "Not at all!"
    show pov neutral at left
    show eff embarrassed_talk at Position(xpos=1300)
    show col smirk at Position(xpos=1600)
    eff "Sure, why not? "
    show eff neutral_talk at Position(xpos=1300)
    eff "Thanks guys I appreciate the help."
    eff "I am sure my dad isn’t going to mind if he sees that I was escorted to work by friends."
    show pov embarrassed_talk at left
    show eff embarrassed at Position(xpos=1300)
    pov "It's the least we can do."
    show pov neutral at left
    show jac smirk_talk at Position(xpos=1800)
    jac "Yeah! All for one, one for all and shit! Whoop whoop!"
    show mis bored_talk_forward_1
    with dissolve
    mis "To your seats everyone! Time to settle down."
    hide pov neutral at left
    hide eff shocked at Position(xpos=1300)
    with dissolve
    hide col bored at Position(xpos=1600)
    hide jac neutral at Position(xpos=1800)
    with dissolve
    mis "Now, I want to do this quickly and get you all home early."
    mis "I understand you are all frightened by the circumstances around the town, but we still need to stick to the curriculum."
    mis "So, lets try and make this hour count and pay attention. Now open your books to Chapter 4."

    scene black
    with fade
    $ renpy.pause()
    "After class.."

    scene bg chalkboard_day
    with fade
    show mis bored_talk_forward_1
    with dissolve
    mis "Alright! Now, please remember what we just saw and use it to fill in pages 67 to 82 in your textbooks by Monday."
    show mis confused_talk_forward_1
    mis "This will all come in the test but simplified due to the situation in the town so don’t be too scared."
    show mis neutral_talk_forward_1
    mis "With that out of the way I am free to let you all go, so try and have a calm break, alright?"
    show mis confused_talk_forward_1
    mis "Please be careful going home and make sure to inform your parents and legal guardians of the emergency PTA meeting taking place by the end of the week!"

    if missallaway_path >= 24:
        show mis confused_talk_forward_1
        mis "Oh [povname], can you wait a moment?"
        show mis bored_talk_forward_1
        mis "I have some issues to talk to you about, regarding your coursework."

        scene bg classroom_day
        with fade
        show pov confused_talk at left
        with dissolve
        show mis embarrassed_talk at right
        with dissolve
        pov "Uh… So what exactly is wrong with it?"
        pov "Last I checked, you didn’t even leaved-"

        scene bg lasthourofclass_1
        with hpunch
        #"You are interrupted as Allaway pulls you into her arms and hides her face on your shoulder."

        pov "Woah there!"
        pov "Miss A-Allaway, are you sure we should be doing this here?"
        pov "What if someone comes in?!"
        mis "…"
        pov "Miss Allaway?"
        mis "{i}*Sobs*{/i}"
        mis "I… I was so scared, [povname]."
        mis "Please… Just a little while longer…"
        pov "…"
        pov "As much as you need…"

    $ main_story = 62

    jump lbl_crossroads_of_the_day
