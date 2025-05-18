##[Dining room, night- “An Awkward Diner Situation”  - main_story =86]

##-show begins at night when the player is instructed to go to the dining room-

##-show shows the family sitting with food on the table, waiting for Dad to show up-
label lbl_an_awkward_dinner_situation:
    show black
    with fade

    scene bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_confused_talk
    show dad anawkwarddinnersituation_empty
    show povnose anawkwarddinnersituation
    show sisnose anawkwarddinnersituation
    with dissolve
    sis "I still don’t think this is a good idea…"
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show povexpression anawkwarddinnersituation_confused
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_confused
    mum "I know, honey, I know."
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_bored
    mum "Look, just focus on eating. Don’t take anything he says too personal if he does say anything and I’ll handle the rest, okay?"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_embarrassed
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_sad_talk
    sis "I just want to make sure it’s on the record that I was against all this if he does make a show or this turns out to be a disaster."
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_embarrassed_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_sad
    pov "Noted. Though I don’t think that helps a lot right now."

    #-The conversation is brought to an end as the front door opens and dad comes in-
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_bored
    dad "I’m home!"

    #Me, Sis & mum "…
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_angry
    "..."
    dad "Wow, it smells terrific all the way from here!"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookpov
    dad "Feels like the good old days, doesn’t it?"
    show povexpression anawkwarddinnersituation_shocked
    show eyespov anawkwarddinnersituation_looksis
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_angry_talk
    sis "Why you pompous prick-"
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_shocked
    mum "Shh!"

    ##-Dad shows into the show and proceeds to go and sit on the table-
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_standing
    with dissolve
    dad "Nothing like coming home from a hard working day of routine."
    if winc == 0:
        dad "Been a while since I managed to come home to a nice meal with my household, hasn’t it?"
    else:
        dad "Been a while since I managed to come home to a nice meal with my family, hasn’t it?"
    show eyespov anawkwarddinnersituation_looksis
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_angry
    show dad anawkwarddinnersituation_standing
    with dissolve
    dad "Sorry about that everyone. Getting used to the new job and tasks has been quite the huge problem for me."
    dad "Especially when it comes to the stress."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_angry
    pov "I see…"
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_smirk_talk
    show dad anawkwarddinnersituation_idle
    with dissolve
    sis "Fascinating…"
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_smirk
    mum "Yeah…"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_bored
    dad "…"
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_idle
    dad "Well, I see the mood here has also been quite dim lately."
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_bored
    dad "How about we start eating, then?"

    #-The family begins to eat with the quiet but tense atmosphere, Sister still looks displeased and will make no attempt at starting a conversation though-
    show bg anawkwarddinnersituation_pov_eats_sis_idle_mum_eats
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_confused
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    dad "So, [povname]..."
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_eats
    show povexpression anawkwarddinnersituation_confused_talk
    show eyessis anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_idle
    pov "Yeah?"
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_eats
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_bored_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    dad "How are things at university?"
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_idle
    dad "Have you been focusing on your studies?"
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_eats
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_bored_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    pov "Y-Yeah…"
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_eats
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored_talk
    show eyessis anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_idle
    pov "Thing’s been good, I suppose."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_eats
    show povexpression anawkwarddinnersituation_bored
    dad "Good, I expect you to be aiming for the top of your class in order to pay up for the little stunt you pulled off."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_eats
    dad "You better be focusing on your books in order to keep yourself under our roof."
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_smirk_talk
    show eyessis anawkwarddinnersituation_lookmum
    show dad anawkwarddinnersituation_idle
    pov "Yeah, thanks, I know…"
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_sad
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_eats
    mum "H-How about we change the subject?"
    mum "I think [povname] has had enough of a lecture for now."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_idle
    dad "Well, he better keep it together."
    if winc == 0:
        dad "I’ve had… trouble at work because of it, so I feel justified in the need to remind him that his actions affect the whole household."
    else:
        dad "I’ve had… trouble at work because of it, so I feel justified in the need to remind him that his actions affect the whole family."
    show povexpression anawkwarddinnersituation_bored_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_sad
    pov "I’m well aware. Thanks…"
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_eats
    mum "I-In anyway, how's the dinner?"
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_surprised
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_surprised
    show dad anawkwarddinnersituation_idle
    mum "[povname] helped me make it, so I managed to get it out in time!"
    show sisexpression anawkwarddinnersituation_surprised_talk
    show dad anawkwarddinnersituation_eats
    sis "Oh, it’s great, [missus]!"
    sis "No complaints here."
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_embarrassed_talk
    show sisexpression anawkwarddinnersituation_embarrassed
    show dad anawkwarddinnersituation_idle
    pov "Yeah, happy I could help out."
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_eats
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_neutral_talk
    show sisexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_eats
    pov "It came out really good!"
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_eats
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_confused
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_idle
    dad "It's fine, I guess."

    #-There is a bit of a moment of silence after Dad said that-
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show povexpression anawkwarddinnersituation_confused
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_eats
    "..."
    mum "Just... F-Fine?"
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_sad
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_idle
    mum "I see…"
    mum "I g-guess I’ll try to make it better next time, then…"
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_eats
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_shocked
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_angry
    dad "Good."

    #-By now Sister is visibly angry due to his comments while the Mc wears a scowl himself-
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show povexpression anawkwarddinnersituation_shocked_talk
    show eyessis anawkwarddinnersituation_lookmum
    show dad anawkwarddinnersituation_eats
    pov "…"
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_shocked
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_angry_talk
    show dad anawkwarddinnersituation_idle
    sis "-prick…"
    show povexpression anawkwarddinnersituation_shocked
    show sisexpression anawkwarddinnersituation_angry
    dad "Did you say something, [sister]?"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_angry_talk
    show dad anawkwarddinnersituation_eats
    sis "N-No…"
    sis "Nothing at all. Just trying to get a bit of something off my teeth…"
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_idle
    dad "I see."
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_embarrassed
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    mum "U-Um, didn’t you say you wanted to bring something up with [povname]?"
    show povexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_idle
    dad "Ah yes, I was just getting to that if you could just give me a few minutes to finish up my plate, I would have gotten to it."
    if winc == 0:
        dad "Figured it'd be nice to take a moment with the household before getting straight to business."
    else:
        dad "Figured it'd be nice to take a moment with the family before getting straight to business."

    #-Missus is visibly shaken up by this-
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_surprised
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_eats
    mum "I…"
    mum "I-I’m sorry…"
    show povexpression anawkwarddinnersituation_embarrassed_talk
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_confused_talk
    show dad anawkwarddinnersituation_idle
    pov "Don’t be, [missus], I was just about to ask the same thing."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_eats
    pov "What was it you wanted to ask? Better just spit it out now."
    show povexpression anawkwarddinnersituation_confused
    show eyessis anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_idle
    dad "Right. Say [povname], do you happen to have a job?"
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_confused_talk
    show dad anawkwarddinnersituation_eats
    pov "A job?"
    pov "Well, yeah. Kind of."
    show povexpression anawkwarddinnersituation_smirk_talk
    show sisexpression anawkwarddinnersituation_bored
    pov "I assumed you know by now, but I do work part time at the mall and-"
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_surprised
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_shocked
    show dad anawkwarddinnersituation_idle
    dad "So I was right: nothing important."
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored_talk
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_eats
    pov "W-Well, I wouldn’t call it that-"
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_eats
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_idle
    dad "Doesn’t matter."
    dad "There is a position open for an intern in the company and I will be having you apply."

    #-The rest of the family now turn to look with surprise-
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show povexpression anawkwarddinnersituation_shocked_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_shocked
    pov "Uhh… What?"
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_shocked
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_confused
    dad "You heard me. I moved some strings there, to allow you to apply."
    dad "I want you to get first-hand experience on what a real job is like."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_confused
    show eyessis anawkwarddinnersituation_lookpov
    show dad anawkwarddinnersituation_eats
    dad "Plus, this way I get to keep you in my sights and ensure you are out of others way with your shenanigans."
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_confused_talk
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_idle
    pov "Do I get any say on this?"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookfood
    dad "I don’t remember asking your opinion."
    dad "So, no."
    show eyespov anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_eats
    mum "I-I remind you, [povname] is still in education. He can’t just drop that to become a full-time intern at a company!"
    show bg anawkwarddinnersituation_pov_eats_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_confused
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_confused_talk
    show dad anawkwarddinnersituation_idle
    sis "Plus, don’t you need to fit a certain amount of criteria to even apply as an intern?"
    sis "What makes you so sure he would even be accepted in the first place?"
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_bored
    show sisexpression anawkwarddinnersituation_confused
    dad "As I just said, I moved some strings and managed to get you basically in already."
    show bg anawkwarddinnersituation_pov_eats_sis_idle_mum_eats
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk
    show sisexpression anawkwarddinnersituation_smirk
    dad "And don’t flatter yourself, you will mainly be doing pencil pusher work and moving around the office with papers and coffee."
    show dad anawkwarddinnersituation_eats
    dad "We’ve had an influx of work, so the fact that interns are needed for this sort of thing is a priority."
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show povexpression anawkwarddinnersituation_smirk_talk
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_eats
    pov "I-I’m still not about to just drop my studies for this."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_eats
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_idle
    dad "It is a part time thing, for the most part."
    dad "It will be after a school day, however. The days you do have to work, you will be staying there until night."
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_smirk_talk
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    pov "Because that is supposed to make it better?"
    show povexpression anawkwarddinnersituation_confused_talk
    pov "What about coursework and all my other stuff? I can’t just drop it all because you-"
    show bg anawkwarddinnersituation_pov_eats_sis_idle_mum_eats
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_idle
    dad "It’s a temporary arrangement. Don’t be such a crybaby."
    show povexpression anawkwarddinnersituation_smirk
    show sisexpression anawkwarddinnersituation_surprised
    dad "Besides, what could be so important in your life right now to have you ignore an opportunity like this?"
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_lookmum
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_eats
    dad "The opportunity to gain a position in a big company and make something of yourself?"
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk_talk
    show eyessis anawkwarddinnersituation_lookpov
    show dad anawkwarddinnersituation_idle
    pov "Maybe I don’t need a  position in a big company to make something of myself?"
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show povexpression anawkwarddinnersituation_bored_talk
    show eyessis anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_eats
    pov "And I thought you told me to be focusing on studies."
    show povexpression anawkwarddinnersituation_bored
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_idle
    dad "I am still expecting you to, but since all you do afterwards is run around and waste time, you may as well prove yourself useful to me."
    show bg anawkwarddinnersituation_pov_eats_sis_idle_mum_eats
    show povexpression anawkwarddinnersituation_smirk_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_eats
    pov "And what if I don’t want to prove myself useful to you?"
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_shocked
    show dad anawkwarddinnersituation_idle
    dad "You would regret it… Deeply."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_shocked
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_angry_talk
    show dad anawkwarddinnersituation_eats
    sis "Don’t you threaten him!"
    show sisexpression anawkwarddinnersituation_angry
    show dad anawkwarddinnersituation_idle
    dad "You stay out of it, missy!"
    dad "You are already on a thin line for not having a proper job to begin with."
    show eyespov anawkwarddinnersituation_lookfood
    show eyessis anawkwarddinnersituation_lookmum
    dad "You refuse to speak about it, so how do I know you are not whoring yourself off on the streets?!"
    show povexpression anawkwarddinnersituation_angry
    show sisexpression anawkwarddinnersituation_confused_talk
    sis "T-That’s…"
    show eyespov anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_eats
    mum "Alright, everyone calm down - right this instant!"
    if winc == 0:
        mum "Look, mister, you are not just going to come here and talk bad about the two of them after being missing for months. So, easy, or you are sleeping outside!"
    else:
        mum "Look, mister, you are not just going to come here and talk bad about the children after being missing for months. So, easy, or you are sleeping outside!"
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_idle
    mum "Do. Not. Test me…"
    show eyespov anawkwarddinnersituation_lookfood
    dad "Alright, alright, no need to bite my head off, jeez."
    dad "But you have to admit it is a huge opportunity for [povname]."
    dad "Are you really going to tell me it’s wise to let it go to waste because he prefers to waste time with those friends of his?"
    show eyespov anawkwarddinnersituation_lookmum
    show eyessis anawkwarddinnersituation_lookmum
    show dad anawkwarddinnersituation_eats
    mum "However [povname] decides to spend his time is not a waste and I will not allow you to talk down to him like that!"
    mum "{i}*Sigh*{/i}"
    show eyespov anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_idle
    mum "That being said, it is a big opportunity for him. But your way of informing him about it, is terrible!"
    show povexpression anawkwarddinnersituation_sad
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_eats
    mum "And don’t you dare talk like that about [sister] again either!"
    mum "She is a grown adult and she doesn’t need to tell you anything if she is not comfortable with it!"
    mum "You are going to respect her boundaries, or with the lord as my witness, I’ll fix that attitude of yours the hard way!"
    show povexpression anawkwarddinnersituation_sad
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_sad_talk
    show dad anawkwarddinnersituation_idle
    sis "Thanks, [missus]…"
    show povexpression anawkwarddinnersituation_sad_talk
    show sisexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_eats
    pov "Yeah…"
    show povexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_idle
    dad "Alright, alright, woman!"
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_confused
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_shocked
    dad "I told you before, I get it."
    dad "Well, back on the important topic."
    show eyespov anawkwarddinnersituation_lookmum
    show eyessis anawkwarddinnersituation_lookfood
    dad "You will be taking this job, mister."
    dad "You still haven’t received your punishment for your actions, from me. And that’s the end of the discussion."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_eats
    pov "Peachy."
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_idle
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_idle
    dad "Watch that attitude when you are at work."
    dad "You are already getting a load off, by working only part-time, like a good for nothing, rather than experiencing the full day of work."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_eats
    show eyespov anawkwarddinnersituation_looksis
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_neutral
    show dad anawkwarddinnersituation_eats
    dad "But maybe acting like a man and seeing what the real world is like, will force you to grow up."
    show bg anawkwarddinnersituation_pov_eats_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookfood
    show sisexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_idle
    dad "Become a whole other person, even."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_eats
    show povexpression anawkwarddinnersituation_smirk_talk
    show dad anawkwarddinnersituation_eats
    pov "Right…"
    pov "So, I have no choice in the matter here, do I?"
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_idle
    dad "The paperwork is done, so no."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_eats
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_eats
    pov "Fan-freaking-tastic."
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_bored_talk
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_shocked
    show dad anawkwarddinnersituation_idle
    pov "Anything else you are signing me up for against my will?"
    show bg anawkwarddinnersituation_pov_eats_sis_idle_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_smirk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_confused
    dad "Keep that up, and I’ll send you to the military. Though I doubt you’ll be of much use, even there."
    dad "Where being a man actually matters."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_angry
    show dad anawkwarddinnersituation_eats
    mum "Enough!"
    mum "{i}*sigh*{/i}"
    mum "I swear you are going to give me a migraine or something!"
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_embarrassed
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_idle
    mum "[povname], just try it for a couple of days."
    mum "You are a grown man, so I won’t force you to stay if you don’t like it, but at least try it so your father will stop with this nonsense."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_eats
    pov "…"
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_sad_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_idle
    pov "Fine…"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_sad_talk
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_shocked
    show dad anawkwarddinnersituation_eats
    pov "But only because you asked me to."
    show bg anawkwarddinnersituation_pov_eats_sis_idle_mum_idle
    show povexpression anawkwarddinnersituation_bored
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_idle
    mum "Thank you."
    show bg anawkwarddinnersituation_pov_idle_sis_idle_mum_idle
    show sisexpression anawkwarddinnersituation_angry
    dad "Good, it’s about time you learn some respect here."
    dad "Bending over to your superiors, like a good bitch; you’ll do fine in the job."
    show povexpression anawkwarddinnersituation_angry_talk
    show sisexpression anawkwarddinnersituation_shocked
    show dad anawkwarddinnersituation_eats
    pov "OKAY, YOU KNOW WHAT-!"

    #-The Mc and Dad stand up from the table ready to escalate things further-
    show povexpression anawkwarddinnersituation_angry
    show sisexpression anawkwarddinnersituation_angry
    show dad anawkwarddinnersituation_idle
    mum "ENOUGH, BOTH OF YOU!"
    show dad anawkwarddinnersituation_standing
    with hpunch
    dad "YOU HAVE SOMETHING TO SAY, BOY?!"
    dad "BE READY TO FACE THE CONSEQUENCES OF WHATEVER IS ABOUT TO COME OUT OF YOUR MOUTH!"
    show povexpression anawkwarddinnersituation_angry_talk
    pov "OH, DON’T WORRY, I’VE BEEN SAVING UP A GOOD CHUNK OF WHAT I HAVE IN MIND TO SAY TO YOU FOR A WHILE!"
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_angry
    show eyessis anawkwarddinnersituation_lookmum
    mum "DON’T YOU TWO DARE!"
    show sisexpression anawkwarddinnersituation_angry_talk
    sis "THAT’S IT!"

    #-Sister stands up from the table about to cry-
    show povexpression anawkwarddinnersituation_bored
    sis "I CAN’T TAKE IT ANYMORE! WHY DID WE EVEN AGREE TO THIS IN THE FIRST PLACE?!"
    sis "THIS WHOLE DINNER WAS A MISTAKE! AND THIS JACKASS STILL HAS THE BALLS TO INSULT US TO OUR FACES AND DEMAND STUFF FROM US!?"
    show sisexpression anawkwarddinnersituation_sad
    mum "Sweetie, no-"
    show sisexpression anawkwarddinnersituation_confused
    dad "WATCH YOUR TONGUE, NOW! YOU ARE LUCKY YOU ARE STILL ABLE TO LEAVE UNDER MY ROOF, TO BEGIN WITH!"
    show povexpression anawkwarddinnersituation_angry_talk
    show eyessis anawkwarddinnersituation_lookpov
    show sisexpression anawkwarddinnersituation_angry
    pov "SHE IS MORE WELCOME HERE THAN YOU, YOU ASSHOLE!"
    show povexpression anawkwarddinnersituation_angry
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_angry_talk
    sis "THIS MAN TREATS US LIKE SHIT FOR OUR WHOLE STAY HERE, AND NOW WANTS US TO JUST SHUT UP AND TAKE THE BULLSHIT COMING OUT OF HIS MOUTH?"
    show eyessis anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_idle
    with dissolve
    sis "WELL, I WANT NO PART OF IT!"
    sis "IT’S ALREADY ENOUGH OF A PAIN HAVING TO DEAL WITH HIS LIES AND BULLSHIT -- WHILE HE IS NOT HERE -- TO ALSO HAVE TO LISTEN TO HIM!"
    show eyespov anawkwarddinnersituation_looksis
    show eyessis anawkwarddinnersituation_lookmum
    show sisexpression anawkwarddinnersituation_angry_talk
    show dad anawkwarddinnersituation_eats
    sis "I’m sorry, [missus], but fuck this and fuck him!"
    sis "I’m out!"

    #-Sister leaves the show and not before long she slams the door to her room-
    scene black
    $ renpy.pause(0.5,hard=True)
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle ## SISTER NEEDS TO BE EATING TO HIDE BEHIND THE 'sisgone' IMAGE

    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_angry
    show dad anawkwarddinnersituation_idle
    show sisgone anawkwarddinnersituation
    show povnose anawkwarddinnersituation
    with dissolve ## Hides the Sister
    dad "THAT’S RIGHT! GO AND HIDE IN THE ROOM I PAID FOR YOU, YOU WORTHLESS GOOD FOR NOTHING-"

    mum "SHUT! UP!"
    mum "One more thing, I swear to God, one more thing out of your mouth and you won’t step a foot inside this house for as long as I live and breathe!"
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    show dad anawkwarddinnersituation_eats
    dad "…"
    show povexpression anawkwarddinnersituation_smirk
    show dad anawkwarddinnersituation_idle
    mum "Good… You still are sensible enough to know not to cross my limit."
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_shocked
    mum "[povname], you are giving this whole thing of working at The Robotics Company a chance."
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show povexpression anawkwarddinnersituation_angry_talk
    show dad anawkwarddinnersituation_eats
    pov "You are taking his side?!"
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show povexpression anawkwarddinnersituation_shocked
    show dad anawkwarddinnersituation_idle
    mum "Quiet!"
    mum "You are taking it only for the sake of the opportunity, but if your father tries to be a smart-ass or crosses the line with you, I want you to head straight home and let me know."
    show povexpression anawkwarddinnersituation_confused
    dad "What’s the whole point of this being to help him grow up, if you are going to keep babying him?!"
    show bg anawkwarddinnersituation_pov_idle_sis_eats_mum_idle
    show eyespov anawkwarddinnersituation_lookfood
    mum "I told you to keep quiet!"
    mum "I’m getting so sick of you. I am this close to getting a lawyer on the matter and start talking about divorce. Is that what you want?!"
    show eyespov anawkwarddinnersituation_lookmum
    dad "…"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_eats
    mum "You already spend all of your time out. For all I know, you are fucking whatever sloozy your limp dick manages to convince of a pity fuck."
    show povexpression anawkwarddinnersituation_confused
    show dad anawkwarddinnersituation_idle
    mum "So you better keep your mouth shut before you are living the single life in your late 40’s."
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_shocked
    dad "Why you-"
    show povexpression anawkwarddinnersituation_shocked_talk
    mum "I’M NOT PLAYING GAMES HERE!"
    mum "I’M GETTING SO SICK OF YOU, I’M STARTING TO WONDER WHAT I EVEN SAW IN YOU IN THE FIRST PLACE!"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_shocked
    mum "So shut your mouth before I kick you out…"
    show eyespov anawkwarddinnersituation_lookmum
    dad "…"
    show povexpression anawkwarddinnersituation_confused
    mum "[povname], I’ll make sure this doesn’t take up all your time, but I do want you to give it a shot."
    show povexpression anawkwarddinnersituation_surprised
    mum "As he said, it is your punishment; but I see it's fair you also get the chance to make something good out of all of this."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_eats
    mum "Even if it’s just temporary."
    show eyespov anawkwarddinnersituation_lookmum
    show dad anawkwarddinnersituation_idle
    mum "Once I decide it’s enough, you can let it go and go back to normal."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_sad
    show dad anawkwarddinnersituation_eats
    mum "I’m not gonna let this affect your studies either."
    show dad anawkwarddinnersituation_idle
    mum "Your father has made enough of a mess already as it is, but he is not about to ruin your education."
    show eyespov anawkwarddinnersituation_lookmum
    mum "So please, do this for me."
    show povexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    mum "You’ll be busy with other stuff around the office, so you won’t be tolerating your father either."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_embarrassed
    show dad anawkwarddinnersituation_idle
    mum "I won’t even ask you to carpool or anything."
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    mum "Much less get along."
    mum "Does that sound fair to you?"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored_talk
    show dad anawkwarddinnersituation_idle
    pov "I…"

    #-Missus gives the Mc a begging look-
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    mum "Please..."
    show povexpression anawkwarddinnersituation_sad_talk
    show dad anawkwarddinnersituation_idle
    pov "…"
    pov "I’ll give it a shot… Just…"
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored_talk
    show dad anawkwarddinnersituation_eats
    pov "Just keep this asshole away from me and [sister]."
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_embarrassed
    show dad anawkwarddinnersituation_idle
    mum "I will, I promise."
    mum "Now go to your room. Take your plate along if you are still hungry."
    show eyespov anawkwarddinnersituation_lookfood
    show povexpression anawkwarddinnersituation_bored
    show dad anawkwarddinnersituation_eats
    mum "I’m going to yell to your father a lot now, so you may want to use headphones for a bit."

    #-Missus turns back to look at Dad with hatred in her eyes-
    show eyespov anawkwarddinnersituation_lookmum
    show povexpression anawkwarddinnersituation_embarrassed_talk
    show dad anawkwarddinnersituation_idle
    pov "Okay… Night, [missus]…"
    pov "Call me if you need help…"
    show povexpression anawkwarddinnersituation_embarrassed
    mum "Oh, don’t worry, I will not."

    $ main_story = 86
    $ gtime = 3

    scene bg myhallway_night
    with fade

    jump lbl_myhallway_night_setup
