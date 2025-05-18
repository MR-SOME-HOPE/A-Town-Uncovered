## Questioning Erica
label lbl_questioning_erica:
    scene black
    with fade
    $ renpy.pause()
    "After checking room 344 and 343..."

    scene bg hospitalroom_day
    with fade
    show pov neutral_talk at left
    show eff bored
    show col bored at right
    with dissolve
    pov "Room 334! There we are."
    show pov neutral at left
    show eff bored
    show col bored_talk at right
    col "Why didn’t we just talk to the receptionist to save time."
    show eff bored_talk
    show col bored at right
    eff "We’re here. Just- let’s talk to Erica."
    show pov neutral_talk at left
    show eff shocked
    show col shocked at right
    pov "Hey, Eri-"

    ## CG of Erica by the window sill, exposed and playing with herself. She looks in your direction.
    scene bg questioningerica_1
    with fade

    eff "Hi- Erica."

    col "Hey, girl~"

    eff "Cole."

    eri "C-Cole? Effie?!"
    eri "Uhhh- sorry I don’t know who you are."
    eri "I don’t think we’ve met."

    pov "I’m [povname]."

    eri "You go to the same school?"

    pov "Yes, I do."

    eri "Sweet."
    eri "I’m Erica."

    pov "Oh, speaking of sweet. We brought chocolates."

    eri "Nawww, you’re too kind. Just leave them by the pile of other chocolates. I don’t wanna get too fat, hahaha~"

    eff "So true, girl. Make sure you eat ours first though, it’s a lot better than those cheap brands."

    pov "Hey, we don’t wanna take up a lot of your time."

    eri "No, please! I’m so bored in here."
    eri "I’m really tired…"
    eri "I need to bathe myself in vitamin D if you know what I mean."

    col "HELL YE-"

    eff "Can- we ask you some questions about your… disappearance."
    eff "I understand it might be a bit of a sensitive topic."

    eri "Pfft, not as sensitive as my clit right now."
    eri "That shit can’t get enough stimulation I swear to God, what a selfish bitch."

    eff "Alright."
    eff "Let’s just get straight into it."

    eri "Hit me."

    eff "Okay."

    eri "No, literally, spank me… slap me… hard!"

    eff "Erica. What can you tell us about where you were during your disappearance?"

    eri "..."
    eri "...."
    eri "{i}*Deep breath*{/i}"
    eri "It was… dark."
    eri "Like literally."
    eri "That place I was in did NOT have sunlight."
    eri "I know what a lightbulb looks like but the sun?"
    eri "I forgot what that shit looked like after a while."
    eri "I started to feel like I was in an apocalyptic bunker, safe from the dangers of the outside and I found the place I was in to be…"
    eri "A safe haven of sorts. I was comfortable and happy to be there…"

    eff "*Whisper* [povname], she literally said bunker."

    col "A bunker you say."

    eri "I- I guess it was kinda like a bunker, it was underground I think."
    eri "Or at least it may as well be underground."
    eri "There were a lot of religious symbolism around the place."
    eri "But- it felt like a heaven and hell sort of deal."
    eri "I did NOT feel like I was praising a God or a devil."
    eri "We were taught to praise… a feeling."
    eri "If that makes sense."
    eri "I don’t know, I just knew that as long as I let them do what they did to me, I felt good, happy, and satisfied."

    pov "As long as you let them do things to you?"
    pov "Who’s them?"

    eri "My captors…"

    eff "This kinda sounds like a stockholm syndrome situation."

    col "For real. This sounds insane and so sad…"

    pov "Are you okay, Erica?"

    eri "I’m good. Don’t worry about me."
    eri "Playing with myself like this helps a lot, but don’t let the fun police outside see me."
    eri "They tie me up and force me to do no hands ejaculation."
    eri "I mean don’t get me wrong, that’s fun as hell but really hard after they inject me with stuff-"
    eri "It- exhausts me because I have to work extra hard to cum."

    col "Totally understandable."
    col "Don’t worry, Erica, you’re safe with us."

    eri "Thanks, big guy."

    eff "Can we ask what you last remember before you were returned at the school?"
    eff "Because everyone was shocked to find you’ve just shown up out of no where."

    eri "I can’t remember what I saw."
    eri "But only because I was blindfolded."
    eri "I thought we were playing again but this time was different."
    eri "They blinded me but I remember feeling a cold body carrying me."
    eri "It was’t warm bodied like I was used to."
    eri "It was cold- and they felt… strong."
    eri "Y’know?"
    eri "All I can do is remember what I felt because my physical touch has been trained to be heightened."
    eri "My other senses have taken a hit."
    eri "Sorry that doesn’t help much."

    eff "No, no. That’s very helpful, Erica."
    eff "Thank you."

    eri "I’m glad I could help, Effie."
    eri "You look great by the way. I almost didn’t recognize you with your side bangs."
    eri "You know she used to have straight bangs like a doofus?"
    eri "Cole you pretty much look the same, but hey!"
    eri "You’ve always been a handsome guy."

    col "Back at cha, Erica."

    eff "We won’t take anymore of your time Erica."
    eff "It was really nice seeing you."

    eri "Please visit me again, I’m so bored!"
    eri "Every guy that tried to fuck me gets carried away by Bruno!"
    eri "FUCK YOU BRUNO!"

    "Bruno" "Yeah, yeah, yeah. You know the rules, Erica!"

    eri "Man, fuck that guy. Mr Fun-Police."

    pov "Sorry to hear."
    pov "We’ll try to make time when we can, right guys?"

    col "Of course. We missed you."

    eff "Yeah, you’ll always have a place with us."

    eri "Seriously. I need to be FUCKED SO BAD!"

    "Bruno" "DON’T MAKE ME COME OVER THERE!"

    pov "Let’s go before we get into some sorta trouble."

    col "It’s only trouble if we act on it."

    eff "Cole, don’t take advantage of her. She’s clearly not herself."

    col "I only hear what she’s saying and-"

    eff "Let’s go, Cole."

    col "Aight, I got ladies waiting in line anyway."

    pov "Sure, sure. Let’s get you to them."
    pov "For the mean time, let’s head back to the HQ."
    pov "Can you text the others, Effie?"

    eff "Yeah, alright."

    pov "Cool. We need to discuss all we’ve learnt from Erica and Davendithas’ family."

    ## SCENE END

    $ main_story = 169

    scene black
    with fade
    $ renpy.pause()
    "After texting everyone to meet at the safehouse..."

    jump lbl_decipher_the_intel
