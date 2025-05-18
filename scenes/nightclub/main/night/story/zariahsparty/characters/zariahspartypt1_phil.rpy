## PHIL
label lbl_zariahs_party_phil:
    show pov neutral_talk at left
    with dissolve
    show phi bored at right
    hide btn zariahs_party_phil_idle
    with dissolve
    if zariahs_party_talking_phil == 0:
        pov "Hey Phil."
        show pov shocked at left
        show phi bored_talk at right
        phi "Wait, you gaywad got invited to the rave too?!"
        show pov confused at left
        show phi bored_talk at right
        phi "Man, why are the people that Zariah invited just dorks?!"
        show pov bored at left
        show phi bored_talk at right
        phi "You know what, just for that I’ll make sure to keep the dork entrance to a minimum."
        phi "Gotta make sure the babe to nerd ratio is leaning toward the babe side."
        show pov bored_talk at left
        show phi bored at right
        pov "I’m kinda surprised to hear that you know what a ratio is, but that’s neither here nor there."
        pov "So, Zariah hired you as a bouncer?"
        show pov bored at left
        show phi bored_talk at right
        phi "Yeah, it’s pretty lit."
        phi "I was just posting for my followers online that not only are they coming to listen to whatever Zariah is playing but they also get to do a meet and greet with the Philster on the gate."
        show pov smirk_talk at left
        show phi bored at right
        pov "Not even gonna comment on the “Philster” part."
        pov "So Zariah is paying you in social media boost?"
        show pov smirk at left
        show phi neutral_talk at right
        phi "Yeah, I mean, my account is pretty famous already, but I guess I can always introduce my profile to even more babes out there thanks to Zariah."
        phi "Plus, I get to keep nerds and gaywads out and watch them cry to get in, so that’s always a plus."
        show pov embarrassed_talk at left
        show phi bored at right
        pov "Figured you would say something like that."
        show pov smirk at left
        show phi bored_talk at right
        phi "Yeah you are just lucky I didn’t catch you before coming in and that Zariah told me not to mess with you or the other nerds."
        phi "No way I would let you in otherwise."
        show pov bored_talk at left
        show phi bored at right
        pov "Yeah, another thing I figured you would say."
        pov "So you are just gonna stay here the whole party?"
        show pov bored at left
        show phi bored_talk at right
        phi "Someone’s gotta do it and it lets me get first look and pick off whatever babe wants to come in."
        phi "They have to play on my good side if they want to get in, after all."
        show pov smirk_talk at left
        show phi bored at right
        pov "I suppose it’s useless to tell you to try and not let it get to your head, eh?"
        show pov smirk at left
        show phi bored_talk at right
        phi "I know you are jealous of my position, gaylord."
        show phi bored_talk at right
        phi "Sorry, but you kinda need a tough physique to do this job, not to mention a certain charm."
        show pov bored at left
        phi "Try not to drool too much once you see the ocean of chicks hanging off me."
        show pov bored_talk at left
        show phi bored at right
        pov "Right…"
        pov "Well, I’m gonna get back inside."
        pov "You know, where the party is actually gonna be?"
        show pov shocked at left
        show phi bored_talk at right
        phi "Yeah, whatever gaylord."
        phi "God, first the wimpy four eyes geek and now you."
        phi "You better not scare away the chicks with your nerd gaywad energy."
        show pov smirk_talk at left
        show phi bored at right
        pov "Have fun out here!"
        pov "I’m sure you’ll find ways to amuse yourself while we party."
        pov "Later!"
        show pov smirk at left
        show phi bored_talk at right
        phi "Tch, Gaylordwad..."
        $ zariahs_party_talking_phil = 1
    else:
        show phi bored_talk at right
        phi "Quit bothering me, Gaylordwad."

    jump lbl_nightclubdancefloor_zariahs_party_setup
