init python:
    def add_points(arg_character,arg_amount):
        ### Takes the 'char_points' string from arg_character and actually access Ren'pys 'store' where saved variables are stored to get the actual char_points to work with.
        tempvar_pointsvalue = getattr(store,arg_character)

        if tempvar_pointsvalue >= 10:
            #If points are max no change.
            pass
        elif tempvar_pointsvalue + arg_amount >= 10:
            #If points will be max or over set the store 'char_points' to 10
            setattr(store,arg_character,10)
        else:
            #If points will not max, just add current points and new points and then set the store's 'char_points' to that value.
            setattr(store,arg_character,tempvar_pointsvalue + arg_amount)

        #Takes the supplied 'char_points' and splits it into char and points as a list
        tempvar_charname = arg_character.split("_")

        #Uses the 'char' that is the first index of the list and returns a formated version.
        tempvar_formatedname = format_name(tempvar_charname[0])

        #Choose which notification to use, when the points are more than 1 will show the exact amount, otherwise just goes with 'increased.'
        if arg_amount > 1:
            renpy.notify("Relationship with %s increased by %d." % (tempvar_formatedname,arg_amount))
        else:
            renpy.notify("Relationship with %s increased." % (tempvar_formatedname))
        renpy.pause(1.5,hard=True)



    def subtract_points(arg_character,arg_amount):
        ### clone of the add_points, just deals with removing points.
        tempvar_pointsvalue = getattr(store,arg_character)
        if tempvar_pointsvalue <= 0:
            pass
        elif tempvar_pointsvalue - arg_amount <= 0:
            setattr(store,arg_character,10)
        else:
            setattr(store,arg_character,tempvar_pointsvalue - arg_amount)
        tempvar_charname = arg_character.split("_")
        tempvar_formatedname = format_name(tempvar_charname[0])
        if arg_amount > 1:
            renpy.notify("Relationship with %s decreased by %d." % (tempvar_formatedname,arg_amount))
        else:
            renpy.notify("Relationship with %s decreased" % (tempvar_formatedname))
        renpy.pause(1.5,hard=True)


    def format_name(arg_unformattedname):
        tempvar_name = ""
        ### Because some of the variable name's are not just the name, but a title and name, or a title must check the name and return a correctly formated name.
        ### Will have to update as new characters with titles or title + name are added.
        if arg_unformattedname == "lordkevlamin":
            tempvar_name = "Lord Kevlamin"
        elif arg_unformattedname == "nursehollick":
            tempvar_name = "Nurse Hollick"
        elif arg_unformattedname == "missallaway":
            tempvar_name = "Miss Allaway"
        elif arg_unformattedname == "coachfistem":
            tempvar_name = "Coach Fistem"
        elif arg_unformattedname == "principallashley":
            tempvar_name = "Miss Lashley"
        elif arg_unformattedname == "effiesdad":
            tempvar_name = "Effie's Dad"
        elif arg_unformattedname == "grundlesam":
            tempvar_name = "Grundle Sam"
        elif arg_unformattedname == "jacobsdad":
            tempvar_name = "Jacob's Dad"
        elif arg_unformattedname == "eloise":
            tempvar_name = "Eloise"
        elif arg_unformattedname == "edward":
            tempvar_name = "Edward"
        elif arg_unformattedname == "mum":
            if winc == 1:
                tempvar_name = "Mom"
            else:
                tempvar_name = store.missus
        elif arg_unformattedname == "sister":
            tempvar_name = store.sister
        elif arg_unformattedname == "dad":
            if winc == 1:
                tempvar_name = "Dad"
            else:
                tempvar_name = store.dadname
        else:
            tempvar_name = arg_unformattedname.capitalize()

        return str(tempvar_name)

    def hardpause(arg_delay):
        ## wrapper function, to make sure hard=True isn't forgotten.
        renpy.pause(arg_delay,hard=True)

    def add_contact(arg_name):
        ## simple function to notify of Contact being unlocked, includes pause incase multiple are added at once.
        renpy.notify("New Contact: %s" % (arg_name))
        renpy.pause(1.5,hard=True)

    def nyi():
        renpy.notify("Content under construction, not yet implemented.")
        renpy.pause(1.0,hard=True)
