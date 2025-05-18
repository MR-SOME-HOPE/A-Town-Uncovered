## Dinner with me Mom ##
label lbl_dinner_with_me_mom:
    if winc == 0:
        jump lbl_dinner_with_me_mom_winc0
    show pov embarrassed_talk at left
    with dissolve
    hide btn_mylivingroom_day_mother_idle2
    show mum neutral at right
    with dissolve
    pov "Hey, Mom."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Yes, sweetie?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I was wondering if you would want to... care to..."
    pov "Um, go to dinner? Would you care to want to go to dinner?"
    pov "I was wondering if you want to care to go to dinner... with me that is."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "Why are you stumbling over your words?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I- I was wondering if you want to go out for dinner with me."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Yeah, sure. Dinner sounds nice."
    show pov shocked_talk at left
    show mum neutral at right
    pov "Really?"
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Yeah, of course. Like some Chinese takeout or burgers?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I was actually thinking someplace nice?"
    show pov embarrassed at left
    show mum confused_talk at right
    mum "Like what..?"
    show pov smirk_talk at left
    show mum shocked at right
    pov "Like fancy pants, wine and dine, tuxedo and cocktail night sort of restaurant."
    show pov smirk at left
    show mum shocked_talk at right
    mum "Ohhh! But, [povname]. That's way too expensive for us."
    show pov neutral_talk at left
    show mum sad at right
    pov "Don't worry about that. Leave that up to me."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "No... I can't accept that. Save that money for something more important."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "You are important to me."
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "[povname]. You're making me blush."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "Please, Mom. It'll be nice. It'll be my way of saying thank you for raising me so well."
    show pov smirk at left
    show mum sad_talk at right
    mum "Are you really sure? I don't want to be the reason for you being broke..."
    mum "Just- don't pick somewhere too expensive for goodness sake."
    show pov smirk_talk at left
    show mum sad at right
    pov "I can't settle for anything less than the best in town."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "You're really spoiling me, you know that. That's unhealthy to do."
    show pov smirk_talk at left
    show mum embarrassed at right
    pov "It's not like we're going to do this every night."
    show pov smirk at left
    show mum embarrassed_talk at right
    mum "Hmmm... alright. I accept your invitation."
    show pov neutral_talk at left
    show mum embarrassed at right
    pov "Awesome!"
    show pov confused at left
    show mum confused_talk at right
    mum "Are we going tonight?"
    show pov confused_talk at left
    show mum confused at right
    pov "Mmmm... we'll see. Most likely not, I'll run some errands first."
    show mum neutral at right
    pov "I just thought it'd be a good idea to let you know with plenty of time beforehand."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Oh, definitely."
    show mum embarrassed at right
    mum "..."
    show pov smirk at left
    show mum embarrassed_talk at right
    mum "Oh gosh, I'm blushing so hard. I'll need to go and look for a dress."
    if inventory.has_item(Items.suit):
        show pov neutral_talk at left
        show mum smirk at right
        pov "I've already got a suit, so I'm covered."
        show pov neutral at left
        show mum smirk_talk at right
        mum "You do? I haven't seen you in a suit since you were like, 9 years old."
        mum "You were a lot smaller then."
        show pov neutral_talk at left
        show mum smirk at right
        pov "I remember. You took a lot of photos."
        show pov bored at left
        show mum smirk_talk at right
        mum "How could I not. You looked so funny!"
        show pov bored_talk at left
        show mum neutral at right
        pov "Thanks, Mom."
        show pov neutral_talk at left
        pov "Anyway, I'll let you know when we're going out."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Sounds good."
    else:
        show pov neutral_talk at left
        show mum confused at right
        pov "And I'll need to find myself a suit."
        show pov neutral at left
        show mum confused_talk at right
        mum "You don't have one?"
        show pov confused_talk at left
        show mum confused at right
        pov "I've always rented one."
        show pov neutral at left
        show mum confused_talk at right
        mum "Well, I honestly think you should buy one. You should have at least one, all-purpose suit in your wardrobe."
        show pov neutral_talk at left
        show mum smirk at right
        pov "I'll see what I can find."
        show mum neutral at right
        pov "And I'll let you know when we're going out."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Sounds good."
    $ mum_path = 26
    if gtime == 0:
        jump lbl_mykitchen_day
    else:
        jump lbl_mylivingroom_day

### NO WINC ###
label lbl_dinner_with_me_mom_winc0:
    show pov embarrassed_talk at left
    with dissolve
    hide btn_mylivingroom_day_mother_idle2
    show mum neutral at right
    with dissolve
    pov "Hey, [missus]."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Yes, sweetie?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I was wondering if you would want to... care to..."
    pov "Um, go to dinner? Would you care to want to go to dinner?"
    pov "I was wondering if you want to care to go to dinner... with me that is."
    show pov embarrassed at left
    show mum confused_talk at right
    mum "Why are you stumbling over your words?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I- I was wondering if you want to go out for dinner with me."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Yeah, sure. Dinner sounds nice."
    show pov shocked_talk at left
    show mum neutral at right
    pov "Really?"
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Yeah, of course. Like some Chinese takeout or burgers?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I was actually thinking someplace nice?"
    show pov embarrassed at left
    show mum confused_talk at right
    mum "Like what..?"
    show pov smirk_talk at left
    show mum shocked at right
    pov "Like fancy pants, wine and dine, tuxedo and cocktail night sort of restaurant."
    show pov smirk at left
    show mum shocked_talk at right
    mum "Ohhh! But, [povname]. That's way too expensive for us."
    show pov neutral_talk at left
    show mum sad at right
    pov "Don't worry about that. Leave that up to me."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "No... I can't accept that. Save that money for something more important."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "You are important to me."
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "[povname]. You're making me blush."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "Please, [missus]. It'll be nice. It'll be my way of saying thank you for raising me so well."
    show pov smirk at left
    show mum sad_talk at right
    mum "Are you really sure? I don't want to be the reason for you being broke..."
    mum "Just- don't pick somewhere too expensive for goodness sake."
    show pov smirk_talk at left
    show mum sad at right
    pov "I can't settle for anything less than the best in town."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "You're really spoiling me, you know that. That's unhealthy to do."
    show pov smirk_talk at left
    show mum embarrassed at right
    pov "It's not like we're going to do this every night."
    show pov smirk at left
    show mum embarrassed_talk at right
    mum "Hmmm... alright. I accept your invitation."
    show pov neutral_talk at left
    show mum embarrassed at right
    pov "Awesome!"
    show pov confused at left
    show mum confused_talk at right
    mum "Are we going tonight?"
    show pov confused_talk at left
    show mum confused at right
    pov "Mmmm... we'll see. Most likely not, I'll run some errands first."
    show mum neutral at right
    pov "I just thought it'd be a good idea to let you know with plenty of time beforehand."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Oh, definitely."
    show mum embarrassed at right
    mum "..."
    show pov smirk at left
    show mum embarrassed_talk at right
    mum "Oh gosh, I'm blushing so hard. I'll need to go and look for a dress."
    if inventory.has_item(Items.suit):
        show pov neutral_talk at left
        show mum smirk at right
        pov "I've already got a suit, so I'm covered."
        show pov neutral at left
        show mum smirk_talk at right
        mum "You do? I haven't seen you in a suit since you were like, 9 years old."
        mum "You were a lot smaller then."
        show pov neutral_talk at left
        show mum smirk at right
        pov "I remember. You took a lot of photos."
        show pov bored at left
        show mum smirk_talk at right
        mum "How could I not. You looked so funny!"
        show pov bored_talk at left
        show mum neutral at right
        pov "Thanks, [missus]."
        show pov neutral_talk at left
        pov "Anyway, I'll let you know when we're going out."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Sounds Good."
    else:
        show pov neutral_talk at left
        show mum confused at right
        pov "And I'll need to find myself a suit."
        show pov neutral at left
        show mum confused_talk at right
        mum "You don't have one?"
        show pov confused_talk at left
        show mum confused at right
        pov "I've always rented one."
        show pov neutral at left
        show mum confused_talk at right
        mum "Well, I honestly think you should buy one. You should have at least one, all-purpose suit in your wardrobe."
        show pov neutral_talk at left
        show mum smirk at right
        pov "I'll see what I can find."
        show mum neutral at right
        pov "And I'll let you know when we're going out."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Sounds good."
    $ mum_path = 26
    if gtime == 0:
        jump lbl_mykitchen_day
    else:
        jump lbl_mylivingroom_day
