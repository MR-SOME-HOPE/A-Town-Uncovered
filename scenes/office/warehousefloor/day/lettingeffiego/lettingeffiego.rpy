## Letting Effie Go
label lbl_letting_effie_go:
    
    #-You sat there on the ground in disbelief, heavy breathing-

    scene bg lettingeffiego_1

    jac "[povname]."
    jac "[povname]! We gotta go-"
    jac "We can’t stay here."
    jac "We have to head back and figure out what to do next."
    jac "[povname]!"
    jac "Are you listening to me?!"
    jac "[povname]!!"

    $ main_story = 122.5

    $ gtime = 3

    jump lbl_letting_effie_go_pt2
