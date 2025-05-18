## The Town is Crazy ##
label lbl_the_town_is_crazy:
    if winc == 0:
        jump lbl_the_town_is_crazy_winc0
    show pov angry_talk at left
    with dissolve
    show mum sad at right
    with dissolve
    pov "Mom, we need to talk. I have no idea what is going on in this town."
    show pov confused_talk at left
    show mum sad at right
    pov "Have you been noticing what the fuck is going on around here? It's abnormal and weird."
    show pov angry at left
    show mum sad_talk at right
    mum "[povname], slow down."
    show pov angry_talk at left
    show mum sad at right
    pov "And you! What was up with you and Dad this morning?"
    pov "Why were you acting like such a whore in front of me!?"
    show pov sad_talk at left
    pov "And- and- w-why the hell is Dad so.. not Dad? Y'know?"
    show pov angry_talk at left
    pov "Like he's so chill and doesn't give a shit anymore."
    show pov confused_talk at left
    pov "He's not being a fucking prick anymore? What happened to him?"
    show pov angry_talk at left
    pov "Did something happen while I was gone?"
    show pov angry at left
    show mum sad_talk at right
    mum "Honey-"
    show pov angry_talk at left
    show mum sad at right
    pov "Mom... be honest with me."

    menu:
        "Are you brainwashed?":
            show pov angry_talk at left
            show mum sad at right
            pov "Are you brainwashed?"
            show pov angry at left
            show mum sad_talk at right
            mum "No, sweetie. I'm not brainwashed."
            show pov angry_talk at left
            show mum sad at right
            pov "Lies! That's what someone who HAS been brainwashed would say."
        "Are you really my mom?":
            show pov angry_talk at left
            show mum sad at right
            pov "Are you really my mom?"
            show pov sad at left
            show mum sad_talk at right
            mum "Of course I am, sweetie. Don't you recognise me?"
            show pov angry_talk at left
            show mum sad at right
            pov "No! No, I don't recognise you. My mom isn't a straight up whore."
        "Am I dead? Is this heaven?":
            show pov sad_talk at left
            show mum sad at right
            pov "Am I dead? Is this heaven?"
            show pov angry at left
            show mum sad_talk at right
            mum "No, sweetie. This isn't heaven, you're not dead."
            show pov angry_talk at left
            show mum sad at right
            pov "How can I believe you? Don't fuck with my head."
    show pov angry at left
    show mum angry_talk at right
    mum "[povname]! Shut up for a second and listen to me!"
    show mum bored_talk at right
    mum "I was in a call with your dad just now - your real dad."
    show pov confused_talk at left
    show mum angry at right
    pov "My real dad? What are you saying? I'm adopted?"
    show pov confused at left
    show mum sad_talk at right
    mum "No, that's not what I mean. Your real dad: the dad you grew up with."
    show pov sad_talk at left
    show mum sad at right
    pov "I don't get what you're saying. If there's a ‘real dad', then that means there's a- ‘fake dad'?"
    show pov sad at left
    show mum sad_talk at right
    mum "It's hard to explain without sounding like a crazy person. Believe me when I say that you're in real danger."
    mum "You can't stay here. You have to go back to where you came from."
    show pov shocked_talk at left
    show mum sad at right
    pov "But.. Mom? W-What? Back to our old home? Why can't I stay here?"
    show pov sad_talk at left
    show mum sad at right
    pov "Are you saying that we're moving back?"
    show pov confused at left
    show mum sad_talk at right
    mum "We're not moving. Only YOU are going back to where you came from."
    show pov angry at left
    show mum sad at right
    pov "..."
    show pov angry_talk at left
    show mum angry at right
    pov "What the hell are you talking about? Why are you so cryptic?"
    show pov angry at left
    show mum angry_talk at right
    mum "If you really want an explanation. You'll have to trust me okay?"
    show pov bored at left
    show mum sad_talk at right
    mum "Will you trust me?"

    menu:
        "Yes.":
            #if mum_points <= 9:
            #    $ mum_points += 1
            #else:
            #    $ mum_points = 10
            #$ renpy.notify("Your relationship with Mom has increased")
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Yes, of course."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "Good, because you can't trust anyone else in this place except for me, and your father."
            show pov bored_talk at left
            show mum neutral at right
            pov "Got it."
            show pov confused at left
            show mum bored_talk at right
            mum "Now listen, I'll explain everything you need to know."
        "No.":
            show pov angry_talk at left
            show mum angry at right
            pov "Actually, I don't think I will."
            show pov angry at left
            show mum angry_talk at right
            mum "This is your mother we're talking about. Or at least partially your mother."
            show pov angry_talk at left
            show mum sad at right
            pov "What?!"
            show pov angry at left
            show mum sad_talk at right
            mum "Please, just listen, I'll explain everything you need to know."
    show pov confused at left
    show mum bored_talk at right
    mum "This isn't your universe."
    show mum bored at right
    pov "..."
    show mum confused_talk at right
    mum "You must've found yourself accessing this parallel universe through one of the gateways found in town."
    show pov confused_talk at left
    show mum confused at right
    pov "Umm..."
    show pov confused_talk at left
    show mum bored at right
    pov "I don't know how to... react to this?"
    show pov smirk_talk at left
    show mum angry at right
    pov "Are you sure I'm not dreaming? That's not at all possible."
    show pov sad at left
    show mum sad_talk at right
    mum "It's true, think about it, it's the only explanation that's somewhat sensible to you right now."
    show pov confused at left
    show mum bored_talk at right
    mum "This world is exactly like your world except our society runs and functions more on sex and lust than yours does."
    show pov confused_talk at left
    show mum bored at right
    pov "Yeah, I pretty much figured that out."
    show pov confused at left
    show mum smirk_talk at right
    mum "It sounds good doesn't it?"

    menu:
        "It does.":
            show pov embarrassed_talk at left
            show mum smirk at right
            pov "Honestly, it sounds like heaven."
        "It doesn't.":
            show pov sad_talk at left
            show mum confused at right
            pov "It doesn't actually... too much of it makes it lose its specialty."
    show pov sad at left
    show mum sad_talk at right
    mum "Either way, you need to get out of this town and get back to your own town."
    mum "To your own universe!"
    show pov shocked at left
    mum "If you stay here long enough, no. If you stay here any longer, you're going to be killed."
    mum "Sacrificed."
    show pov sad_talk at left
    show mum sad at right
    pov "Sacrificed?"
    show pov sad at left
    show mum sad_talk at right
    mum "You heard me. Slit right across your throat."
    show pov angry_talk at left
    show mum sad at right
    pov "What the fuck... what kind of world is this where someone who do such a barbaric thing?"
    show pov confused at left
    show mum sad_talk at right
    mum "It's the town's annual ritual."
    show pov confused_talk at left
    show mum sad at right
    pov "What happens during it?"
    show pov angry at left
    show mum sad_talk at right
    mum "It's when a young male is chosen to be a sacrifice for the town."
    show mum confused_talk at right
    mum "It's to guarantee a strong, united, lustful year for everyone."
    show pov sad at left
    show mum sad at right
    mum "..."
    show mum sad_talk at right
    mum "Your dad told me that you were this year's sacrifice."
    show pov sad_talk at left
    show mum sad at right
    pov "What..? No.. I, I just got here, how can I all of a sudden be chosen to be fucking murdered."
    show pov confused at left
    show mum bored_talk at right
    mum "You see, that's where your real dad comes in."
    mum "As you should know, when there are parallel universes, there are multiple selves."
    show mum confused_talk at right
    mum "Technically, I'm not your mother, but I also am."
    show mum sad_talk at right
    mum "Technically, you're not my real son, and yet, you also are."
    show pov shocked at left
    mum "Your dad in this world is your actual dad and your dad back in your world is from this world."
    show pov angry_talk at left
    show mum sad at right
    pov "Wait- What?! How could that be?"
    show pov angry at left
    show mum sad_talk at right
    mum "I'm not really the one you should be asking about that."
    show pov angry_talk at left
    show mum sad at right
    pov "Well? Where's Dad? When can I talk to him? Why didn't he talk to me this morning?"
    show pov angry at left
    show mum sad_talk at right
    mum "He was shocked, dumbfounded. He didn't know what to do when he saw you in the kitchen."
    show pov confused at left
    show mum sad_talk at right
    mum "He told me that he told you, well, the ‘you' from this world to run away and hide in your world."
    show pov confused_talk at left
    show mum sad at right
    pov "I think I understand."
    show pov sad at left
    show mum sad_talk at right
    mum "I know it's confusing but just believe me when I say that you're not safe here."
    show pov bored at left
    show mum sad_talk at right
    mum "You need to get back the way you came in."

    menu:
        "Into your vagina?":
            show pov smirk_talk at left
            show mum embarrassed at right
            pov "Into your vagina?"
            show pov embarrassed at left
            show mum confused_talk at right
            mum "Even at a time like this, you have time to joke around, don't you?"
            show pov sad at left
            show mum sad_talk at right
            mum "[povname]. As much as I'd let you fuck me, now's not the time, the ritual is about to start at sunset."
            show pov confused at left
            show mum confused_talk at right
            mum "Seriously, do you remember going into the beach or the pond at the park?"
            show mum bored_talk at right
            mum "Those are the only two gateways known in this town."
        "In the pond?":
            show pov confused_talk at left
            show mum neutral at right
            pov "Into the pond at the park?"
            show pov confused at left
            show mum neutral_talk at right
            mum "That must be it, there are only two known gateways in this town and that's through the pond and the beach."
        "I'm not sure where.":
            show pov sad_talk at left
            show mum confused at right
            pov "I'm not 100 percent sure what the gateway is."
            show pov confused at left
            show mum bored_talk at right
            mum "Well, the only two known gateways in this town are bodies of water, the pond and the beach."
    show pov confused_talk at left
    show mum bored at right
    pov "There's one at the beach?"
    show pov confused at left
    show mum confused_talk at right
    mum "Why do you think our beach is empty but your beach is packed with nudists?"
    show pov confused_talk at left
    show mum embarrassed at right
    pov "That explains it."
    show pov sad at left
    show mum sad_talk at right
    mum "Enough chit-chat, [povname]. You have to leave now before she comes for yo-"
    play music "audio/music/hellraiser_texture.ogg"

    scene bg girlatthedoor_1
    with hpunch
    idk "[povname]."
    show bg girlatthedoor_2
    idk "You're coming with me."
    show bg girlatthedoor_3
    with hpunch
    "{i}*Thwoomp!*{/i}"
    show bg girlatthedoor_4
    $ renpy.pause(0.7, hard=True)
    show bg girlatthedoor_5
    $ renpy.pause(0.5, hard=True)
    show bg girlatthedoor_6
    $ renpy.pause(0.5, hard=True)
    show bg girlatthedoor_7
    $ renpy.pause()
    $ main_story = 35
    stop music fadeout 5.0

    scene black
    with fade
    $ renpy.pause ()

    jump lbl_park_night_setup

### NO WINC ###
label lbl_the_town_is_crazy_winc0:
    show pov angry_talk at left
    with dissolve
    show mum sad at right
    with dissolve
    pov "[missus], we need to talk. I have no idea what is going on in this town."
    show pov confused_talk at left
    show mum sad at right
    pov "Have you been noticing what the fuck is going on around here? It's abnormal and weird."
    show pov angry at left
    show mum sad_talk at right
    mum "[povname], slow down."
    show pov angry_talk at left
    show mum sad at right
    pov "And you! What was up with you and [dadname] this morning?"
    pov "Why were you acting like such a whore in front of me!?"
    show pov sad_talk at left
    pov "And- and- w-why the hell is [dadname] so.. not [dadname]? Y'know?"
    show pov angry_talk at left
    pov "Like he's so chill and doesn't give a shit anymore."
    show pov confused_talk at left
    pov "He's not being a fucking prick anymore? What happened to him?"
    show pov angry_talk at left
    pov "Did something happen while I was gone?"
    show pov angry at left
    show mum sad_talk at right
    mum "Honey, D-"
    show pov angry_talk at left
    show mum sad at right
    pov "[missus]... be honest with me."

    menu:
        "Are you brainwashed?":
            show pov angry_talk at left
            show mum sad at right
            pov "Are you brainwashed?"
            show pov angry at left
            show mum sad_talk at right
            mum "No, sweetie. I'm not brainwashed."
            show pov angry_talk at left
            show mum sad at right
            pov "Lies! That's what someone who HAS been brainwashed would say."
        "Are you really my [mumrole]?":
            show pov angry_talk at left
            show mum sad at right
            pov "Are you really my [mumrole]?"
            show pov sad at left
            show mum sad_talk at right
            mum "Of course I am, sweetie. Don't you recognise me?"
            show pov angry_talk at left
            show mum sad at right
            pov "No! No, I don't recognise you. My [mumrole] isn't a straight up whore."
        "Am I dead? Is this heaven?":
            show pov sad_talk at left
            show mum sad at right
            pov "Am I dead? Is this heaven?"
            show pov angry at left
            show mum sad_talk at right
            mum "No, sweetie. This isn't heaven, you're not dead."
            show pov angry_talk at left
            show mum sad at right
            pov "How can I believe you? Don't fuck with my head."
    show pov angry at left
    show mum angry_talk at right
    mum "[povname]! Shut up for a second and listen to me!"
    show mum bored_talk at right
    mum "I was in a call with your [dadrole] just now, your real [dadrole]."
    show pov confused_talk at left
    show mum angry at right
    pov "My real [dadrole]? What are you saying? I'm not real?"
    show pov confused at left
    show mum sad_talk at right
    mum "No, that's not what I mean. Your real [dadrole]: the [dadrole] you grew up with."
    show pov sad_talk at left
    show mum sad at right
    pov "I don't get what you're saying. If there's a ‘real [dadrole]', then that means there's a- 'fake [dadrole]'?"
    show pov sad at left
    show mum sad_talk at right
    mum "It's hard to explain without sounding like a crazy person. Believe me when I say that you're in real danger."
    mum "You can't stay here. You have to go back to where you came from."
    show pov shocked_talk at left
    show mum sad at right
    pov "But.. [missus]? W-What? Back to our old home? Why can't I stay here?"
    show pov sad_talk at left
    show mum sad at right
    pov "Are you saying that we're moving back?"
    show pov confused at left
    show mum sad_talk at right
    mum "We're not moving. Only YOU are going back to where you came from."
    show pov angry at left
    show mum sad at right
    pov "..."
    show pov angry_talk at left
    show mum angry at right
    pov "What the hell are you talking about? Why are you so cryptic?"
    show pov angry at left
    show mum angry_talk at right
    mum "If you really want an explanation. You'll have to trust me okay?"
    show pov bored at left
    show mum sad_talk at right
    mum "Will you trust me?"

    menu:
        "Yes.":
            #if mum_points <= 9:
            #    $ mum_points += 1
            #else:
            #    $ mum_points = 10
            #$ renpy.notify("Your relationship with [missus] has increased")
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Yes, of course."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "Good, because you can't trust anyone else in this place except for me, and your [dadrole]."
            show pov bored_talk at left
            show mum neutral at right
            pov "Got it."
            show pov confused at left
            show mum bored_talk at right
            mum "Now listen, I'll explain everything you need to know."
        "No.":
            show pov angry_talk at left
            show mum angry at right
            pov "Actually, I don't think I will."
            show pov angry at left
            show mum angry_talk at right
            mum "This is your [mumrole] we're talking about. Or at least partially your [mumrole]."
            show pov angry_talk at left
            show mum sad at right
            pov "What?!"
            show pov angry at left
            show mum sad_talk at right
            mum "Please, just listen, I'll explain everything you need to know."
    show pov confused at left
    show mum bored_talk at right
    mum "This isn't your universe."
    show mum bored at right
    pov "..."
    show mum confused_talk at right
    mum "You must've found yourself accessing this parallel universe through one of the gateways found in town."
    show pov confused_talk at left
    show mum confused at right
    pov "Umm..."
    show pov confused_talk at left
    show mum bored at right
    pov "I don't know how to... react to this?"
    show pov smirk_talk at left
    show mum angry at right
    pov "Are you sure I'm not dreaming? That's not at all possible."
    show pov sad at left
    show mum sad_talk at right
    mum "It's true, think about it, it's the only explanation that's somewhat sensible to you right now."
    show pov confused at left
    show mum bored_talk at right
    mum "This world is exactly like your world except our society runs and functions more on sex and lust than yours does."
    show pov confused_talk at left
    show mum bored at right
    pov "Yeah, I pretty much figured that out."
    show pov confused at left
    show mum smirk_talk at right
    mum "It sounds good doesn't it?"

    menu:
        "It does.":
            show pov embarrassed_talk at left
            show mum smirk at right
            pov "Honestly, it sounds like heaven."
        "It doesn't.":
            show pov sad_talk at left
            show mum confused at right
            pov "It doesn't actually... too much of it makes it lose its specialty."
    show pov sad at left
    show mum sad_talk at right
    mum "Either way, you need to get out of this town and get back to your own town."
    mum "To your own universe!"
    show pov shocked at left
    mum "If you stay here long enough, no. If you stay here any longer, you're going to be killed."
    mum "Sacrificed."
    show pov sad_talk at left
    show mum sad at right
    pov "Sacrificed?"
    show pov sad at left
    show mum sad_talk at right
    mum "You heard me. Slit right across your throat."
    show pov angry_talk at left
    show mum sad at right
    pov "What the fuck... what kind of world is this where someone who do such a barbaric thing?"
    show pov confused at left
    show mum sad_talk at right
    mum "It's the town's annual ritual."
    show pov confused_talk at left
    show mum sad at right
    pov "What happens during it?"
    show pov angry at left
    show mum sad_talk at right
    mum "It's when a young male is chosen to be a sacrifice for the town."
    show mum confused_talk at right
    mum "It's to guarantee a strong, united, lustful year for everyone."
    show pov sad at left
    show mum sad at right
    mum "..."
    show mum sad_talk at right
    mum "Your [dadrole] told me that you were this year's sacrifice."
    show pov sad_talk at left
    show mum sad at right
    pov "What..? No.. I, I just got here, how can I all of a sudden be chosen to be fucking murdered."
    show pov confused at left
    show mum bored_talk at right
    mum "You see, that's where your real [dadrole] comes in."
    mum "As you should know, when there are parallel universes, there are multiple selves."
    show mum confused_talk at right
    mum "Technically, I'm not your [mumrole], but I also am."
    show mum sad_talk at right
    mum "Technically, you're not my real [povmumrole], and yet, you also are."
    show pov shocked at left
    mum "Your [dadrole] in this world is your actual [dadrole] and your [dadrole] back in your world is from this world."
    show pov angry_talk at left
    show mum sad at right
    pov "Wait- What?! How could that be?"
    show pov angry at left
    show mum sad_talk at right
    mum "I'm not really the one you should be asking about that."
    show pov angry_talk at left
    show mum sad at right
    pov "Well? Where's [dadname]? When can I talk to him? Why didn't he talk to me this morning?"
    show pov angry at left
    show mum sad_talk at right
    mum "He was shocked, dumbfounded. He didn't know what to do when he saw you in the kitchen."
    show pov confused at left
    show mum sad_talk at right
    mum "He told me that he told you, well, the ‘you' from this world to run away and hide in your world."
    show pov confused_talk at left
    show mum sad at right
    pov "I think I understand."
    show pov sad at left
    show mum sad_talk at right
    mum "I know it's confusing but just believe me when I say that you're not safe here."
    show pov bored at left
    show mum sad_talk at right
    mum "You need to get back the way you came in."

    menu:
        "Into your vagina?":
            show pov smirk_talk at left
            show mum embarrassed at right
            pov "Into your vagina?"
            show pov embarrassed at left
            show mum confused_talk at right
            mum "Even at a time like this, you have time to joke around, don't you?"
            show pov sad at left
            show mum sad_talk at right
            mum "[povname]. As much as I'd let you fuck me, now's not the time, the ritual is about to start at sunset."
            show pov confused at left
            show mum confused_talk at right
            mum "Seriously, do you remember going into the beach or the pond at the park?"
            show mum bored_talk at right
            mum "Those are the only two gateways known in this town."
        "In the pond?":
            show pov confused_talk at left
            show mum neutral at right
            pov "Into the pond at the park?"
            show pov confused at left
            show mum neutral_talk at right
            mum "That must be it, there are only two known gateways in this town and that's through the pond and the beach."
        "I'm not sure where.":
            show pov sad_talk at left
            show mum confused at right
            pov "I'm not 100 percent sure what the gateway is."
            show pov confused at left
            show mum bored_talk at right
            mum "Well, the only two known gateways in this town are bodies of water, the pond and the beach."
    show pov confused_talk at left
    show mum bored at right
    pov "There's one at the beach?"
    show pov confused at left
    show mum confused_talk at right
    mum "Why do you think our beach is empty but your beach is packed with nudists?"
    show pov confused_talk at left
    show mum embarrassed at right
    pov "That explains it."
    show pov sad at left
    show mum sad_talk at right
    mum "Enough chit-chat, [povname]. You have to leave now before she comes for yo-"
    play music "audio/music/hellraiser_texture.ogg"

    scene bg girlatthedoor_1
    with hpunch
    idk "[povname]."
    show bg girlatthedoor_2
    idk "You're coming with me."
    show bg girlatthedoor_3
    with hpunch
    "{i}*Thwoomp!*{/i}"
    show bg girlatthedoor_4
    $ renpy.pause(0.7, hard=True)
    show bg girlatthedoor_5
    $ renpy.pause(0.5, hard=True)
    show bg girlatthedoor_6
    $ renpy.pause(0.5, hard=True)
    show bg girlatthedoor_7
    $ renpy.pause()
    $ main_story = 35
    stop music fadeout 5.0

    scene black
    with fade
    $ renpy.pause ()

    jump lbl_park_night_setup
