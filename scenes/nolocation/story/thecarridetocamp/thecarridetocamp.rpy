## The Car Ride To Camp
label lbl_the_car_ride_to_camp:
    ## In the car ride in the morning
    scene bg thecarridetocamp_0
    with fade

    sis "{i}*Yawn*{/i}"
    sis "When you said morning- you really meant like at the break of dawn."

    mum "I didn’t wanna waste good day light, hon."
    mum "You can sleep, we’ll be there soon."

    pov "Where is it?"

    mum "It’s up on the lookout."
    mum "There’s actually a really nice camping area near there and it’s close to a lot of nice places that we can visit and do!"
    mum "Oh man, I never got a chance to go camping when I was young so you guys are lucky to get this opportunity."
    mum "Camping wasn’t really a thing. The closest thing we did was stay in a traditional home out in rural areas."
    mum "But who would call that camping?"

    if winc == 0:
        pov "You know what, [missus]. You’re right."
    else:
        pov "You know what, mom. You’re right."
    pov "We ARE lucky to have this opportunity."
    if winc == 0:
        pov "I want you to know that I’m excited for this and that it’ll be a great household weekend."
    else:
        pov "I want you to know that I’m excited for this and that it’ll be a great family weekend."

    mum "That’s it, baby!"
    mum "That’s exactly what I love to hear."

    sis "{i}*Snore*{/i}"

    pov "I’m sure she’s excited too, on the inside."
    pov "She’s conserving her energy for the camp itself."

    mum "Hehe, right."
    mum "Don’t worry, she’ll learn to love it quickly."
    mum "I’m confident in that."
    mum "You can sleep too, [povname]. We’ll be there soon."

    ## SCENE END

    $ mumsiscamp_path = 3

    jump lbl_setting_up_camp
