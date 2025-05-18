## Tension in the Room
label lbl_the_tension_in_the_room:
    scene bg classroom_day
    with fade

    clasm1 "Come on, man. It was just a dream."

    clasm2 "N-No man, the town is going to shit!"
    clasm2 "I lived on the same street as the guy whose family got kidnapped, and I keep hearing weird sounds at night!"
    clasm2 "I swear I saw someone at my window, late at night!"

    clasf1 "Jessica, it’s okay!"
    clasf1 "Erica is back. She must have went through something horrible. That’s why she didn’t respond when you tried talking to her!"

    clasf2 "She couldn’t stop begging me to fuck her, Lisa!"
    clasf2 "The old Erica was the biggest virgin around."
    clasf2 "I don’t know what they did to her, but that girl isn’t Erica anymore!"

    #-As more people mutter about several different topics, you are staring at the Polaroid in your hand-
    pov "…"

    scene bg classroom_day
    with hpunch
    show pov shocked at left
    show eff confused_talk at right
    eff "Geez, I knew things would be tense after what happened but I didn’t think it would be this bad."
    show pov shocked_talk at left
    show eff confused at right
    pov "Effie!"
    show pov embarrassed at left
    show eff confused_talk at right
    eff "I swear, it feels like an execution room in here."
    show pov embarrassed_talk at left
    show eff confused at right
    pov "Didn't see you there-!"
    show pov embarrassed at left
    show eff confused_talk at right
    eff "[povname]?"
    eff "Dude, are you okay?"
    show eff confused at right
    pov "Hmm?"
    show eff confused_talk at right
    eff "Dude, what happened to you?"
    eff "You look like shit!"
    eff "No offense."
    show pov embarrassed_talk at left
    show eff confused at right
    pov "Just… Bad dreams and paranoia…"
    show pov embarrassed at left
    show eff confused_talk at right
    eff "Well, you are not the only one."
    show pov sad at left
    show eff confused_talk at right
    eff "Everyone in school is to some degree, especially with the whole 'Erica coming back' deal adding fuel to the fire."
    show eff sad_talk at right
    eff "Do you want to talk about it?"
    show pov sad_talk at left
    show eff sad at right
    pov "I… Rather not…"
    show pov sad at left
    show eff confused_talk at right
    eff "Damn, must have been quite the nightmare, huh?"
    show pov sad_talk at left
    show eff confused at right
    pov "You have no idea."
    show pov sad at left
    show eff confused_talk at right
    eff "Well…"
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "How about we go for some drinks to the mall or something?"
    show eff smirk_talk at right
    eff "Maybe some a artificially sweetened drink could help you relax?"
    show pov sad_talk at left
    show eff confused at right
    pov "I am not really in the mood for it, Effie…"
    show pov sad at left
    show eff smirk_talk at right
    eff "Well, how about a movie?"
    show pov embarrassed at left
    show eff neutral_talk at right
    eff "I can get Jacob and the three of us could watch something to pass the time."
    show eff embarrassed_talk at right
    eff "The whole town is going crazy and all, but we can at least try and make the most of it, don’t you think?"
    show pov sad_talk at left
    show eff embarrassed at right
    pov "I uh-"
    show pov shocked at left
    show eff shocked at right
    show mis neutral_talk
    with dissolve
    mis "Good morning, students."
    mis "We have a lot of material to cover, thanks to all the chaos that happened. So please sit down and turn your textbooks to page-"

    scene bg chalkboard_day
    with fade
    show mis embarrassed_forward_1
    with dissolve
    mis "…"
    show mis embarrassed_talk_forward_1
    mis "You know what?"
    mis "Let’s take it easy today, alright?"
    mis "I want you all to write an essay of what it is you are feeling right now."
    show mis smirk_talk_forward_1
    mis "Please be extra specific with your words and then we are going to pass them to the front and we are going to help calm each other down from this crazy experience."
    show mis embarrassed_talk_forward_1
    mis "Does that sound good?"
    show mis neutral_talk_forward_1
    mis "Definitely better than the essays and research projects I had booked in my program, right?"
    show mis neutral_forward_1
    clas "{i}*Muffled muttering with uncertainty*{/i}"
    show mis neutral_talk_forward_1
    mis "Good! In that case, you guys have 30 minutes to finish and then we’ll start sharing, alright?"
    show mis confused_talk_forward_1
    mis "[povname], would you be so kind as to come with me for a moment?"

    $ main_story = 72

    jump lbl_allaway_is_worried
