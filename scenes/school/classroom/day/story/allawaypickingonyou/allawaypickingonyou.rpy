## Allaway Picking on You ##
label lbl_allaway_picking_on_you:
    default allawaypickingonyou_int = 0
    default allawaypickingonyou_luc = 0

    scene black
    with fade
    "During class..."

    scene bg chalkboard_day
    with fade
    show mis neutral_talk_forward_1
    with dissolve
    mis "And that's how our main protagonist acted."
    mis "Can anyone have a stab at what the author's moral teaching is through our protagonists' actions?"
    show mis neutral_forward_1
    pov "{i}Oh... damn, I sorta dozed off a little...{/i}"
    eff "I can, Miss Allaway!"
    show mis neutral_talk_forward_1
    mis "[povname]? Would you like to give it a go?"
    show mis neutral_forward_1
    pov "Uh..."

    menu:
        "Use your knowledge":
            if skill_int >= 4:
                $ skill_int -= 4
                $ renpy.notify("You used 4 Intelligence Points")
                pov "The author is conveying to the audience that although love triumphs over wealth, wealth among the corrupt corrupts ultimately."
                pov "As exemplified near the end of the text, the antagonist redeems themself through corrupt love which contrasts against the protagonist's actions of choosing the love of wealth."
                show mis neutral_talk_forward_1
                mis "Thank you, [povname]. That was perfect, great explanation."
                $ allawaypickingonyou_int += 1
            else:
                show mis confused_forward_1
                pov "The author is conveying to the audience that wealth triumphs over love, and in the end, the corrupted corrupts ultimate wealth."
                pov "As exemplified near the end of the text, the antagonist fails to redeem themself through love's corruption which mimics the protagonist's actions of choosing the wealth of love."
                show mis confused_talk_forward_1
                mis "Uh- good try but... I think you need to re-read the last section of the book again. You may have misunderstood the message somewhere along the way."
        "Bullshit an answer":
            if skill_luc >= 4:
                $ skill_luc -= 4
                $ renpy.notify("You used 4 Luck Points")
                show mis embarrassed_forward_1
                pov "I think that the author is... conveying to... us, the audience that even though love triumphs over wealth?"
                pov "T-that... uh... wealth and the corruption corrupts the wealthy... uh- corrupted?"
                pov "..."
                pov "A-and... as mentioned near the end of the book, the dude- the antagonist redeems themself through..."
                pov "Love? Love and corruption! Yeah..."
                pov "Which compared to the protagonist's love for wealth... is black and white?"
                show mis embarrassed_talk_forward_1
                mis "Thank you, [povname]. That was... a great explanation."
                $ allawaypickingonyou_luc += 1
            else:
                show mis confused_forward_1
                pov "I think that the author is... trying to tell... us, the audience that even though wealth triumphs over love?"
                pov "T-that... uh... wealth among the corrupted corrupts... ultimately?"
                pov "..."
                pov "A-and... as mentioned near the end of the book, the dude- the antagonist failed at redeeming themself through..."
                pov "Love? Wait-no love's corruption...! Yeah..."
                pov "Which compared to the protagonist's wealth of love... is closely similar?"
                show mis confused_talk_forward_1
                mis "Uh- good try but... I think you need to re-read the last section of the book again. You may have misunderstood the message somewhere along the way."
    show mis neutral_talk_forward_1
    mis "Alright, so on the theme of wealth and corruption. Can anyone point out a good example of where to refer to when our protagonist had to choose between those two?"
    show mis smirk_forward_1
    eff "I've got a good place, Miss-"
    show mis neutral_talk_forward_1
    mis "[povname]! You have your vocal cords warmed up, why don't you give this one a go as well?"
    show mis neutral_forward_1
    pov "... Sure..."

    menu:
        "Use your knowledge":
            if skill_int >= 4:
                $ skill_int -= 4
                $ renpy.notify("You used 4 Intelligence Points")
                show mis neutral_forward_1
                pov "It was around chapter 8, or maybe chapter 9 where the protagonist faced against the leader of the rebellion."
                pov "Out of the possible few scenarios that are scattered mostly near the end of the text, that is the most important turn around for that particular character."
                show mis neutral_talk_forward_1
                mis "Excellent, [povname]! You've nailed it right on the head."
                mis "I'm hoping everyone else is taking notes!"
                $ allawaypickingonyou_int += 1
            else:
                show mis confused_forward_1
                pov "It was actually around chapter 2, or maybe chapter 3 where the protagonist faced against a flashback vision of himself in the mirror."
                pov "Out of the many scenes that are littered mostly near at the beginning of the text, that is the most important self-discovery moment for that character."
                show mis confused_talk_forward_1
                mis "Um... good example but that's not really what I was asking for."
                show mis embarrassed_talk_forward_1
                mis "Still, a good scene to jot down. Everyone?"
        "Bullshit an answer":
            if skill_luc >= 4:
                $ skill_luc -= 4
                $ renpy.notify("You used 4 Luck Points")
                show mis embarrassed_forward_1
                pov "It was around... uh... chapter 8? Give or take a few chapters. It's been a while since I've read the book."
                pov "It's the part where the protagonist faced against that dude? The leader of the rebels... or whatever they're called."
                pov "I'm guessing... out of the possible few scenes in the text... that are scattered near the end of the text that is..."
                pov "T-that that is possibly the most important turn around?"
                pov "For that particular character... uh- yeah..."
                show mis neutral_talk_forward_1
                mis "Excellent, [povname]! You've nailed it right on the head."
                show mis smirk_talk_forward_1
                mis "I'm hoping everyone else is taking notes!"
                $ allawaypickingonyou_luc += 1
            else:
                show mis confused_forward_1
                pov "It was around... uh... chapter 2? Give or take a few chapters. It's been a while since I've read the book."
                pov "It's the part where the protagonist faced against... themself..? In the mirror...? I think that's what happened?"
                pov "I'm guessing... out of many of the scenes in the text... that are scattered near the beginning of the text that is..."
                pov "T-that that is possibly the most important self-discovery moment?"
                pov "For that particular character... uh- yeah..."
                show mis confused_talk_forward_1
                mis "Um... good example but that's not really what I asked for."
                show mis embarrassed_talk_forward_1
                mis "Still, a good scene to jot down. Everyone?"
    show mis neutral_talk_forward_1
    mis "Alright, looks like I can squeeze in one more question before you're all saved by the bell."
    mis "Which character most represents the author's depiction of what love is?"
    show mis neutral_forward_1
    eff "Please, Miss Allaway! I've got a really good quote for thi-"
    show mis smirk_talk_forward_1
    mis "Ahem, [povname]? Be a dear and- I mean... care to share with the class what you think?"
    show mis confused_forward_1
    pov "I really think Effie should get this one... she seems pretty eager..."
    show mis confused_talk_forward_1
    mis "[povname]? Are you trying to tell me that you don't know the answer...?"
    show mis confused_forward_1
    pov "No.. I'm just saying that Effie voluntarily wants to-"
    show mis bored_talk_forward_1
    mis "[povname]? Time's running out. Stop stalling, mister."
    show mis confused_forward_1
    eff "..."
    pov "..."
    show mis neutral_forward_1

    menu:
        "Use your knowledge":
            if skill_int >= 4:
                $ skill_int -= 4
                $ renpy.notify("You used 4 Intelligence Points")
                pov "The old woman that the protagonist meets is the author's main physical depiction for the theme of love."
                pov "Not necessarily romantic love like what the antagonist feels with their partner but more of familial love that she had with her grandchildren."
                pov "She said something along the lines of ‘To relive a life through the eyes of another is an eternal fantasy that forgets who you are'."
                pov "The author suggests that love is subjective to each one person and to falsely care for the wrong person, it blinds you from what you value in life."
                show mis neutral_talk_forward_1
                mis "Amazing memory, [povname]. Thank you for sharing with the class, once again."
                $ allawaypickingonyou_int += 1
            else:
                pov "The grandchildren that the old woman talks about is the author's main physical depiction for the theme of love."
                show mis confused_forward_1
                pov "They had a strong family love for each other and the it highlights what the author is trying to convey through their own life."
                pov "The old woman said something along the lines of ‘grandchildren can be a handful for only a brief moment in time'."
                pov "The author suggests that love starts off small to begin with but grows over time."
                show mis confused_talk_forward_1
                mis "Uh... close? But there's a much better example, I'm sure. Good try though and don't get me wrong, you may use that but it's not the strongest example."
        "Bullshit an answer":
            if skill_luc >= 4:
                $ skill_luc -= 4
                $ renpy.notify("You used 4 Luck Points")
                pov "I think the old woman that the protagonist meets... you know the one?"
                show mis embarrassed_forward_1
                pov "I think she is the author's main character to resemble the meaning of love."
                pov "Not necessarily romantic love... but more... uh- family love?"
                pov "That she had with her grandchildren... yeah.."
                show mis neutral_forward_1
                pov "She said something along the lines of ‘To relive a life through the eyes of another...' something something ‘...is an eternal fantasy that forgets you'? "
                pov "No! ‘...forgets who you are'!"
                pov "I'm guessing that the author is trying to tell us that love is... subjective? To each one person that is."
                pov "And to falsely love... and care for the wrong person, it blinds you from... uhm... what you value... in life?"
                show mis neutral_talk_forward_1
                mis "Amazing memory, [povname]. Thank you for sharing with the class, once again."
                $ allawaypickingonyou_luc += 1
            else:
                pov "The grandchildren? You know? The ones that the old woman talks about?"
                show mis confused_forward_1
                pov "I think they are the author's main character to resemble the meaning of love."
                pov "They had strong family love for each... other? Uh- sure..."
                pov "She said something along the lines of ‘grandchildren can be a handful for only a brief moment... in time'."
                pov "I'm guessing that the author is trying to tell us that love..."
                pov "Uhm... starts off small? To begin with. But it grows over time."
                pov "Yeah, let's go with that."
                show mis confused_talk_forward_1
                mis "Uh... close? But there's a much better example, I'm sure. Good try though and don't get me wrong, you may use that but it's not the strongest example."
    show mis neutral_forward_1
    "{i}Riiiinnnggg!{/i}"
    show mis neutral_talk_forward_1
    mis "Oh! There's the bell. Class dismissed."
    show mis smirk_talk_forward_1
    mis "[povname], can you stay back for a second, I wanna speak with you."
    show mis bored_forward_1
    jac "Oooooh! Someone's in trouble!"
    show mis bored_talk_forward_1
    mis "Jacob, enough of that, get your butt out of here."
    show mis bored_forward_1
    jac "Haha, see you, Miss. Good luck, [povname]."
    show mis neutral_forward_1
    eff "Yeah, good luck."

    jump lbl_offer_tutoring
