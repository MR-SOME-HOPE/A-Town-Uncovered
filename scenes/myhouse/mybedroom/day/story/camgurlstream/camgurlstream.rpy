## Sister Camgurl Stream ##
label lbl_camgurl_stream:
    if gtime == 1 and day == 2:
        if sister_path == 5:
            jump lbl_first_camgurl_stream
        elif sister_path == 14:
            jump lbl_second_camgurl_stream
        elif sister_path == 23:
            jump lbl_third_camgurl_stream
        else:
            scene bg firstcamgurlstream_0_3
            if gtime == 1 and day == 2:
                pov "I've either missed it or she decided not to stream today..."
    else:
        scene bg firstcamgurlstream_0_3
        pov "I don't think now is when she usually streams."
        pov "From what I remember, she streams on a Wednesday Afternoon."

    jump lbl_mybedroom_desk
