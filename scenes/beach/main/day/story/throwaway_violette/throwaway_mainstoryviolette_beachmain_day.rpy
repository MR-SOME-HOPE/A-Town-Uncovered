## Violette Main Story Throwaway Conversations Beach Main ##
default beach_ajob = 0

## Sexworld
label lbl_beachmain_daysexworld_violette_1:
    pov "{i}Where's Violette? I saw her last night?{/i}"
    pov "{i}I guess if no one's at the beach, you don't have to tend to it?{/i}"

    jump lbl_beachmain_day_setup

## A Job
label lbl_beachmain_day_violette_ajob:
    show povn neutral_talk at left
    with dissolve
    show vio neutral at right
    with dissolve
    pov "Hey, Violette."
    show povn neutral at left
    show vio smirk_talk at right
    vio "Hey, [povname]. Decided to take a load off today?"
    show povn embarrassed at left
    show vio confused at right
    pov "Actually, I was wondering if there's a job for me here."
    pov "One that pays that is. Figured I'd try and ask you just in case."
    show povn embarrassed at left
    show vio confused_talk at right
    vio "Do you have a lifeguard certificate? Or any training, at the very least?"
    show povn embarrassed_talk at left
    show vio bored at right
    pov "Um..."
    show povn embarrassed at left
    show vio confused_talk at right
    vio "This isn't a job that any soul can do. You understand that, right?"
    show povn sad_talk at left
    show vio smirk at right
    pov "I know, I know. I figured I'd roll the dice anyways."
    show povn embarrassed_talk at left
    pov "Plus the benefits look... titillating."
    show povn embarrassed at left
    show vio neutral_talk at right
    vio "I tell you what: come back to me when you've gotten done the bare minimum amount of training, and I can then take you on as my trainee."
    show vio confused_talk at right
    vio "That is, if you're that serious about being a lifeguard."
    show povn embarrassed_talk at left
    show vio smirk at right
    pov "I kinda need something like... now. I guess I'll look elsewhere."
    show povn neutral at left
    show vio neutral_talk at right
    vio "Alrighty. Don't be a stranger though."

    $ beach_ajob = 1

    jump lbl_beachmain_day_setup

## Buukakki Followers Are Everywhere - Violette
label lbl_buukakki_followers_are_everywhere_violette:
    ## SPRITE START NO BG NEEDED
    show pov smirk_talk at left
    show vio neutral at right
    pov "Hey, Violette."
    show pov embarrassed at left
    show vio embarrassed_talk at right
    vio "Sorry, I’m kinda busy getting these clothed-weirdos off the beach."
    show pov embarrassed_talk at left
    show vio confused at right
    pov "That’s actually what I wanted to talk to you about."
    show pov embarrassed at left
    show vio bored_talk at right
    vio "Look, I know they’re disturbing your relaxation and fun."
    show pov shocked at left
    show vio smirk_talk at right
    vio "I’m working on it, [povname]. I can’t exactly throw them off the beach, there’s too many of them and they’re literally running away from me."
    show pov confused at left
    show vio shocked_talk at right
    vio "I called the police station but they are kinda busy with a few other things at the moment."
    show vio bored_talk at right
    vio "Not enough heads to go around keeping this town safe apparently."
    show pov shocked_talk at left
    show vio bored at right
    pov "Sorry to hear."
    show pov embarrassed at left
    show vio smirk_talk at right
    vio "Yeah, thanks."
    show vio shocked_talk at right
    vio "I’m exhausted chasing these fuckers around."
    show vio bored_talk at right
    vio "Without any reinforcements, they’re just walking around rampant."
    show pov sad at left
    show vio sad_talk at right
    vio "{i}*Sigh*{/i}"
    show pov confused at left
    show vio embarrassed at right
    vio "Sorry, [povname]. This is my top priority right now, I’m getting plenty of complaints already and yours isn’t helping."
    show pov confused_talk at left
    show vio bored at right
    pov "I wasn’t-"
    show pov shocked at left
    show vio bored_talk at right
    vio "Gotta go."

    $ buukakkifollowers_violette = 1

    call lbl_buukakki_followers_are_everywhere_check

    jump lbl_beachmain_day_setup
