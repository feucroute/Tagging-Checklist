import itertools

tags = []
e621 = True
while True:
    print("Are you using these tags on e621? (yes/no)")
    yesNo = input()
    if yesNo == 'no':
        e621 = False
    #===========================================================================
    # Artists
    #===========================================================================
    while True:
        print("How many artists contributed to this image?")
        artistNumber = int(input())
        if artistNumber == 0:
            tags.append('unknown artist')
            break
        elif artistNumber == 1:
            print("What is the artist's name?")
            artistTag = input()
            tags.append(artistTag)
            break
        elif artistNumber > 1:
            tags.append('collaboration')
            for i in range(artistNumber):
                print("What is artist" + str(i + 1) + "'s name?")
                artistTag = input()
                tags.append(artistTag)
            break
        else:
            print("Please input a valid number.")
    
    #===========================================================================
    # Characters
    #===========================================================================
    print("How many characters are in this image?")
    charNumber = int(input())
    charList = []
    tags.append(charList)
    
    #===========================================================================
    # How many characters?
    #===========================================================================
    if charNumber == 0:
        tags.append('zero pictured')
        while True:
            print("Are there any unseen characters? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('unseen character')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When there is clearly another character involved with a scene, but that character is not seen at all, not a faceless male or faceless female, not even a disembodied penis or disembodied hand.")
    if charNumber == 1:
        tags.append('solo')
        for i in range(charNumber):
            charList.append([])
            charList[i].append('char' + str(i + 1))
        while True:
            print("Are there any unseen characters? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('unseen character')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When there is clearly another character involved with a scene, but that character is not seen at all, not a faceless male or faceless female, not even a disembodied penis or disembodied hand.")
    if charNumber == 2:
        tags.append('duo')
        for i in range(charNumber):
            charList.append([])
            charList[i].append('char' + str(i + 1))
        while True:
            print("Is only one character being focused on? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('solo focus')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When images have more than one character but clearly emphasize only one of them.")
        while True:
            print("Are there any unseen characters? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('unseen character')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When there is clearly another character involved with a scene, but that character is not seen at all, not a faceless male or faceless female, not even a disembodied penis or disembodied hand.")
    if charNumber > 2:
        tags.append('group')
        for i in range(charNumber):
            charList.append([])
            charList[i].append('char' + str(i + 1))
            if charNumber >= 10:
                tags.append('large group')
        while True:
            print("Is only one character being focused on? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('solo focus')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When images have more than one character but clearly emphasize only one of them.")
        while True:
            print("Are only two characters being focused on? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('duo focus')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When images have multiple characters but clearly emphasize only two of them.")
        while True:
            print("Are there any unseen characters? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('unseen character')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When there is clearly another character involved with a scene, but that character is not seen at all, not a faceless male or faceless female, not even a disembodied penis or disembodied hand.")
        while True:
            print("Is there a crowd? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('crowd')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When there is a modest to large amount of people appearing in an image, but often the focus lies on what is happening in the front or amidst them, usually on specific characters.")
        while True:
            print("Is there an audience? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('audience')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Any group of people who are watching one or more characters.")
        # TODO: Add group sex
        while True:
            print("Is there a ridiculous amount of characters? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('absolutely everyone')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When images include a lot of characters, whether because of a crossover or from a single franchise. Used best when there are a ridiculous number of characters.")


    #===========================================================================
    # Name
    #===========================================================================
    for i in range(len(charList)):
        print("What is the name of " + charList[i][0] + "?")
        charName = input()
        if charName:
            charList[i][0] = charName
            
    #=======================================================================
    # Copyright / Fan Characters
    #=======================================================================
    for i in range(len(charList)):
        print("Is " + charList[i][0] + " owned by or based off a series/company/game? (yes/no)")
        yesNo = input()
        if yesNo == 'yes':
            print("What series/company/game?")
            copyrightTag = input()
            charList[i].append(copyrightTag)
            print("Is " + charList[i][0] + " a canon character of " + copyrightTag + "? (yes/no)")
            yesNo = input()
            if yesNo == 'no':
                charList[i].append('fan character')
    #=======================================================================
    # Body Type
    #=======================================================================
    for i in range(len(charList)):
        while True:
            print("What is the body type of " + charList[i][0] + "? (type 'list' for a list of body types)")
            bodyTag = input()
            if bodyTag != 'list':
                charList[i].append(bodyTag)
            if bodyTag == 'anthro':
                while True:
                    print("Is " + charList[i][0] + "'s species normally anthro in their universe? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'no':
                        charList[i].append('anthrofied')
                        break
                    if yesNo == 'yes':
                        break
                    if yesNo == '?':
                        print("A feral character, or character that typically walks on all fours, but is now rendered closer to human.")
            if bodyTag == 'feral':
                while True:
                    print("Is " + charList[i][0] + "'s species normally feral in their universe? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'no':
                        charList[i].append('feralized')
                        break
                    if yesNo == 'yes':
                        break
                    if yesNo == '?':
                        print("Non-feral characters or species depicted as feral animals.")
                while True:
                    print("Is " + charList[i][0] + " a busty feral? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('busty feral')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Feral characters depicted with human breasts.")
            if bodyTag == 'human':
                while True:
                    print("Is " + charList[i][0] + "'s species normally human in their universe? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'no':
                        charList[i].append('humanized')
                        charList[i].append('alternate species')
                        break
                    if yesNo == 'yes':
                        break
                    if yesNo == '?':
                        print("A non-human character turned into an everyday, fully human, human.")
            if bodyTag == 'humanoidized':
                while True:
                    print("Is " + charList[i][0] + "'s species normally humanoid in their universe? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'no':
                        charList[i].append('humanoidized')
                        charList[i].append('alternate species')
                        break
                    if yesNo == 'yes':
                        break
                    if yesNo == '?':
                        print("A taur character whose taur appearance isn't their normal form.")
            if bodyTag == 'list':
                print("anthro, feral, semi-anthro, human, humanoid, taur, animal head, animate inanimate, living machine, penis creature, serpentine, tentacle monster, waddling head, eldritch horror, flora fauna, food creature, glitch, goo creature, mineral fauna, monster, object head, robot, undead")
            print("Does " + charList[i][0] + " have another body type? (yes/no)")
            yesNo = input()
            if yesNo == 'no':
                break
        
    #=======================================================================
    # Species
    #=======================================================================
    for i in range(len(charList)):
        while True:
            print("What species is " + charList[i][0] + "?")
            speciesTag = input()
            charList[i].append(speciesTag)
            print("Is " + charList[i][0] + " another species? (yes/no)")
            yesNo = input()
            if yesNo == 'no':
                break
    #=======================================================================
    # Sex / Gender    
    #=======================================================================
    for i in range(len(charList)):
        print("What sex/gender is " + charList[i][0] + "? (male/female/ambiguous gender/dickgirl/cuntboy/herm/maleherm)")
        sexTag = input()
        charList[i].append(sexTag)
        if sexTag == ('dickgirl' or 'cuntboy' or 'herm' or 'maleherm'):
            charList[i].append('intersex')
        while True:
            print("Is " + charList[i][0] + " crossgender? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('crossgender')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When a character of one gender is depicted as another gender.")
        while True:
            print("Can you see " + charList[i][0] + "'s body but not their face? (yes/no)")
            yesNo = input()
            if yesNo == 'yes':
                if 'male' in charList[i]:
                    charList[i].append('faceless male')
                if 'female' in charList[i]:
                    charList[i].append('faceless female')
                if 'ambiguous gender' in charList[i]:
                    charList[i].append('faceless ambiguous')
                if 'intersex' in charList[i]:
                    charList[i].append('faceless intersex')
                    if 'dickgirl' in charList[i]:
                        charList[i].append('faceless dickgirl')
                    if 'cuntboy' in charList[i]:
                        charList[i].append('faceless cuntboy')
                    if 'herm' in charList[i]:
                        charList[i].append('faceless herm')
                    if 'maleherm' in charList[i]:
                        charList[i].append('faceless maleherm')
                break
            if yesNo == 'no':
                break
        while True:
            print("Is " + charList[i][0] + " muscular? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('muscular')
                if 'male' in charList[i]:
                    charList[i].append('muscular male')
                if 'female' in charList[i]:
                    charList[i].append('muscular female')
                if 'ambiguous gender' in charList[i]:
                    charList[i].append('muscular ambiguous')
                if 'intersex' in charList[i]:
                    charList[i].append('muscular intersex')
                    if 'dickgirl' in charList[i]:
                        charList[i].append('muscular dickgirl')
                    if 'cuntboy' in charList[i]:
                        charList[i].append('muscular cuntboy')
                    if 'herm' in charList[i]:
                        charList[i].append('muscular herm')
                    if 'maleherm' in charList[i]:
                        charList[i].append('muscular maleherm')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When a character has any level of musculature above athletic.")
        while True:
            if 'slightly chubby' not in charList[i]:
                print("Is " + charList[i][0] + " overweight? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('overweight')
                    if 'male' in charList[i]:
                        charList[i].append('overweight male')
                    if 'female' in charList[i]:
                        charList[i].append('overweight female')
                    if 'ambiguous gender' in charList[i]:
                        charList[i].append('overweight ambiguous')
                    if 'intersex' in charList[i]:
                        charList[i].append('overweight intersex')
                        if 'dickgirl' in charList[i]:
                            charList[i].append('overweight dickgirl')
                        if 'cuntboy' in charList[i]:
                            charList[i].append('overweight cuntboy')
                        if 'herm' in charList[i]:
                            charList[i].append('overweight herm')
                        if 'maleherm' in charList[i]:
                            charList[i].append('overweight maleherm')
                    while True:
                        print("Is " + charList[i][0] + " obese? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('obese')
                            if 'male' in charList[i]:
                                charList[i].append('obese male')
                            if 'female' in charList[i]:
                                charList[i].append('obese female')
                            if 'ambiguous gender' in charList[i]:
                                charList[i].append('obese ambiguous')
                            if 'intersex' in charList[i]:
                                charList[i].append('obese intersex')
                                if 'dickgirl' in charList[i]:
                                    charList[i].append('obese dickgirl')
                                if 'cuntboy' in charList[i]:
                                    charList[i].append('obese cuntboy')
                                if 'herm' in charList[i]:
                                    charList[i].append('obese herm')
                                if 'maleherm' in charList[i]:
                                    charList[i].append('obese maleherm')
                            while True:
                                print("Is " + charList[i][0] + " morbidly obese? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('morbidly obese')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("'Jabba the Hut fat', 'Hyper fat'. Has trouble walking, or can't walk. Rolls in places you didn't even know existed. There is no limit, real or imagined, that exceeds this tag.")
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Small rolls in the places you would expect. Fat in torso still shouldn't go past the shoulders in most cases.")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Larger than slightly chubby but smaller than obese. Should not go past 'santa fat'.")
        if sexTag == ('male' or 'cuntboy' or 'maleherm'):
            while True:
                print("Is " + charList[i][0] + " manly? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('manly')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A male, cuntboy, or maleherm character who shows some physical and/or behavioral characteristics that denotes their masculinity.")
            while True:
                print("Is " + charList[i][0] + " girly? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('girly')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A male, cuntboy, or maleherm character with a feminine personality, clothing, and sometimes body type, sans breasts.")
        if sexTag == ('female' or 'dickgirl' or 'herm'):
            while True:
                print("Is " + charList[i][0] + " acting like a tomboy? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('tomboy')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A female, dickgirl, or herm character with a masculine personality and/or style of dress.")
                    
    #=======================================================================
    # Focus tags
    #=======================================================================
    if ('solo focus' in tags) or ('duo focus' in tags):
        if 'male' in tags:
            while True:
                print("Is the image focused on only male characters? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('male focus')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("This is used when multiple individuals are in an animation or image yet the main focus clearly goes to just one (or more) male character(s).")
        if 'female' in tags:
            while True:
                print("Is the image focused on only female characters? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('female focus')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("This is used when multiple individuals are in an animation or image yet the main focus clearly goes to just one (or more) female character(s).")
        if 'ambiguous gender' in tags:
            while True:
                print("Is the image focused on only ambiguous characters? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('ambiguous focus')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("This is used when multiple individuals are in an animation or image yet the main focus clearly goes to just one (or more) ambiguous character(s).")
        if 'intersex' in tags:
            while True:
                print("Is the image focused on only intersex characters? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('intersex focus')
                    if 'dickgirl' in tags:
                        while True:
                            print("Is the image focused on only dickgirl characters? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('dickgirl focus')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("This is used when multiple individuals are in an animation or image yet the main focus clearly goes to just one (or more) dickgirl character(s).")
                    if 'cuntboy' in tags:
                        while True:
                            print("Is the image focused on only cuntboy characters? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('cuntboy focus')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("This is used when multiple individuals are in an animation or image yet the main focus clearly goes to just one (or more) cuntboy character(s).")
                    if 'herm' in tags:
                        while True:
                            print("Is the image focused on only herm characters? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('herm focus')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("This is used when multiple individuals are in an animation or image yet the main focus clearly goes to just one (or more) herm character(s).")
                    if 'maleherm' in tags:
                        while True:
                            print("Is the image focused on only maleherm characters? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('maleherm focus')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("This is used when multiple individuals are in an animation or image yet the main focus clearly goes to just one (or more) maleherm character(s).")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("This is used when multiple individuals are in an animation or image yet the main focus clearly goes to just one (or more) intersex character(s).")              
    
    #===========================================================================
    # View
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Can you see " + charList[i][0] + " from behind? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('rear view')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Character(s) or scenes viewed from behind.")
        while True:
            print("Can you see " + charList[i][0] + " from the front? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('front view')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Character(s) or scenes viewed from the front.")
        while True:
            print("Can you see " + charList[i][0] + " from the side? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('side view')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Character(s) or subjects viewed from the side. Sometimes called profile view.")
        while True:
            print("Is " + charList[i][0] + " viewed from about halfway between front view/rear view and side view? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('three-quarter view')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Character(s) or subjects viewed from about halfway between front_view and side_view.")
        while True:
            print("Can we see from " + charList[i][0] + "'s point of view? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('first person view')
                if 'male' in charList[i]:
                    charList[i].append('male pov')
                if 'female' in charList[i]:
                    charList[i].append('female pov')
                if 'intersex' in charList[i]:
                    charList[i].append('intersex pov')
                    if 'dickgirl' in charList[i]:
                        charList[i].append('dickgirl pov')
                    if 'cuntboy' in charList[i]:
                        charList[i].append('cuntboy pov')
                    if 'herm' in charList[i]:
                        charList[i].append('herm pov')
                    if 'maleherm' in charList[i]:
                        charList[i].append('maleherm pov')
                # TODO: penetrative, receiving, dominant, and submissive pov
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When the perspective is from the view of one of the characters, as if you are that character. ")
    while True:
        print("Is the image at a low-angle view? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('low-angle view')
            while True:
                print("Is the image at a worm's-eye view? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append("worm's-eye view")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("")
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("When the view is pointing up, generally at a medium angle.")
    while True:
        print("Is the image at a high-angle view? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('high-angle view')
            while True:
                print("Is the image at a bird's eye view? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append("bird's-eye view")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A bird's-eye view is an elevated view of an object from above, with a perspective as though the observer were a bird.")
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("When the viewpoint of the image is coming from a little higher than where the subject is, like you're standing taller than them.")
    #===========================================================================
    # Age Related                
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " look young? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('young')
                if ('human' not in charList[i]) or ('humanoid' not in charList[i]):
                    while True:
                        print("Is " + charList[i][0] + " a cub? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('cub')
                            break
                        if yesNo == 'no':
                            break  
                        if yesNo == '?':
                            print("A young, underaged, furry character.")  
                while True:
                    print("Does " + charList[i][0] + " appear to be less than one year old? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('baby')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A very young child, especially one newly or recently born.")
                while True:
                    print("Does " + charList[i][0] + " appear to be between one and three years old? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('toddler')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Someone of the ages 1-3.")
                while True:
                    print("Does " + charList[i][0] + " appear to be between three and 12 years old? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('child')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Character whose estimated age is around 3-12 years.")
                while True:
                    print("Does " + charList[i][0] + " appear to be between 13 and 19 years old? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('teenager')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Characters in the age range of thirteen to nineteen.")
                if 'teenager' not in charList[i]:
                    if 'male' in charList[i]:
                        charList[i].append('shota')
                    if 'female' in charList[i]:
                        charList[i].append('loli')
                        if 'big breasts' in charList[i]:
                            charList[i].append('big breasts')
                break
            if yesNo == 'no':
                while True:
                    print("Does " + charList[i][0] + " look at least middle-aged? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        if 'male' in charList[i]:
                            charList[i].append('mature male')
                        if 'female' in charList[i]:
                            charList[i].append('mature female')
                        if 'ambiguous gender' in charList[i]:
                            charList[i].append('mature ambiguous')
                        if 'intersex' in charList[i]:
                            charList[i].append('mature intersex')
                            if 'dickgirl' in charList[i]:
                                charList[i].append('mature dickgirl')
                            if 'cuntboy' in charList[i]:
                                charList[i].append('mature cuntboy')
                            if 'herm' in charList[i]:
                                charList[i].append('mature herm')
                            if 'maleherm' in charList[i]:
                                charList[i].append('mature maleherm')
                        while True:
                            print("Does " + charList[i][0] + " look old or elderly? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('old')
                                if e621 == False:
                                    if 'male' in charList[i]:
                                        charList[i].append('elderly male')
                                    if 'female' in charList[i]:
                                        charList[i].append('elderly female')
                                    if 'ambiguous gender' in charList[i]:
                                        charList[i].append('elderly ambiguous')
                                    if 'intersex' in charList[i]:
                                        charList[i].append('elderly intersex')
                                        if 'dickgirl' in charList[i]:
                                            charList[i].append('elderly dickgirl')
                                        if 'cuntboy' in charList[i]:
                                            charList[i].append('elderly cuntboy')
                                        if 'herm' in charList[i]:
                                            charList[i].append('elderly herm')
                                        if 'maleherm' in charList[i]:
                                            charList[i].append('elderly maleherm')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("The word 'old' describes a character having lived for a long time; no longer young.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A middle-aged character.")
                break
            if yesNo == '?':
                print("When a character appears to be underage. Used to describe those under the age of 19.")
        while True:
            print("Is " + charList[i][0] + " aged up? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('aged up')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Use this when a character looks physically older than is considered canon for them.")
    
    #===========================================================================
    # Size difference
    #===========================================================================
    charCombo = list(itertools.combinations(charList, 2))
    for i in range(len(charCombo)):
        while True:
            print("Is " + charCombo[i][0][0] + " significantly larger than " + charCombo[i][1][0] + "? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('size difference')
                # Larger
                if 'ambiguous gender' in charCombo[i][0]:
                    tags.append('larger ambiguous')
                if 'male' in charCombo[i][0]:
                    tags.append('larger male')
                if 'female' in charCombo[i][0]:
                    tags.append('larger female')
                if 'intersex' in charCombo[i][0]:
                    tags.append('larger intersex')
                    if 'dickgirl' in charCombo[i][0]:
                        tags.append('larger dickgirl')
                    if 'cuntboy' in charCombo[i][0]:
                        tags.append('larger cuntboy')        
                    if 'herm' in charCombo[i][0]:
                        tags.append('larger herm')                    
                    if 'maleherm' in charCombo[i][0]:
                        tags.append('larger maleherm')
                if 'anthro' in charCombo[i][0]:
                    tags.append('larger anthro')
                if 'feral' in charCombo[i][0]:
                    tags.append('larger feral')
                if 'human' in charCombo[i][0]:
                    tags.append('larger human')
                if 'humanoid' in charCombo[i][0]:
                    tags.append('larger humanoid')
                if 'taur' in charCombo[i][0]:
                    tags.append('larger taur')
                # Smaller
                if 'ambiguous gender' in charCombo[i][1]:
                    tags.append('smaller ambiguous')
                if 'male' in charCombo[i][1]:
                    tags.append('smaller male')
                if 'female' in charCombo[i][1]:
                    tags.append('smaller female')
                if 'intersex' in charCombo[i][1]:
                    tags.append('smaller intersex')
                    if 'dickgirl' in charCombo[i][1]:
                        tags.append('smaller dickgirl')
                    if 'cuntboy' in charCombo[i][1]:
                        tags.append('smaller cuntboy')        
                    if 'herm' in charCombo[i][1]:
                        tags.append('smaller herm')                    
                    if 'maleherm' in charCombo[i][1]:
                        tags.append('smaller maleherm')
                if 'anthro' in charCombo[i][1]:
                    tags.append('smaller anthro')
                if 'feral' in charCombo[i][1]:
                    tags.append('smaller feral')
                if 'human' in charCombo[i][1]:
                    tags.append('smaller human')
                if 'humanoid' in charCombo[i][1]:
                    tags.append('smaller humanoid')
                if 'taur' in charCombo[i][1]:
                    tags.append('smaller taur')
                break
            if yesNo == 'no':
                print("Is " + charCombo[i][1][0] + " significantly larger than " + charCombo[i][0][0] + "? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('size difference')
                    # Larger
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('larger ambiguous')
                    if 'male' in charCombo[i][1]:
                        tags.append('larger male')
                    if 'female' in charCombo[i][1]:
                        tags.append('larger female')
                    if 'intersex' in charCombo[i][1]:
                        tags.append('larger intersex')
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('larger dickgirl')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('larger cuntboy')        
                        if 'herm' in charCombo[i][1]:
                            tags.append('larger herm')                    
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('larger maleherm')
                    if 'anthro' in charCombo[i][1]:
                        tags.append('larger anthro')
                    if 'feral' in charCombo[i][1]:
                        tags.append('larger feral')
                    if 'human' in charCombo[i][1]:
                        tags.append('larger human')
                    if 'humanoid' in charCombo[i][1]:
                        tags.append('larger humanoid')
                    if 'taur' in charCombo[i][1]:
                        tags.append('larger taur')
                    # Smaller
                    if 'ambiguous gender' in charCombo[i][0]:
                        tags.append('smaller ambiguous')
                    if 'male' in charCombo[i][0]:
                        tags.append('smaller male')
                    if 'female' in charCombo[i][0]:
                        tags.append('smaller female')
                    if 'intersex' in charCombo[i][0]:
                        tags.append('smaller intersex')
                        if 'dickgirl' in charCombo[i][0]:
                            tags.append('smaller dickgirl')
                        if 'cuntboy' in charCombo[i][0]:
                            tags.append('smaller cuntboy')        
                        if 'herm' in charCombo[i][0]:
                            tags.append('smaller herm')                    
                        if 'maleherm' in charCombo[i][0]:
                            tags.append('smaller maleherm')
                    if 'anthro' in charCombo[i][0]:
                        tags.append('smaller anthro')
                    if 'feral' in charCombo[i][0]:
                        tags.append('smaller feral')
                    if 'human' in charCombo[i][0]:
                        tags.append('smaller human')
                    if 'humanoid' in charCombo[i][0]:
                        tags.append('smaller humanoid')
                    if 'taur' in charCombo[i][0]:
                        tags.append('smaller taur')                
                break
            if yesNo == '?':
                print("Use this for images or animations featuring at least two characters in which one character is noticeably bigger or smaller in body size than the other character.")
    
    #===========================================================================
    # Age difference
    #===========================================================================
    charCombo = list(itertools.combinations(charList, 2))
    for i in range(len(charCombo)):
        while True:
            print("Is " + charCombo[i][0][0] + " significantly older than " + charCombo[i][1][0] + "? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('age difference')
                # Older
                if 'ambiguous gender' in charCombo[i][0]:
                    tags.append('older ambiguous')
                if 'male' in charCombo[i][0]:
                    tags.append('older male')
                if 'female' in charCombo[i][0]:
                    tags.append('older female')
                if 'intersex' in charCombo[i][0]:
                    tags.append('older intersex')
                    if 'dickgirl' in charCombo[i][0]:
                        tags.append('older dickgirl')
                    if 'cuntboy' in charCombo[i][0]:
                        tags.append('older cuntboy')        
                    if 'herm' in charCombo[i][0]:
                        tags.append('older herm')                    
                    if 'maleherm' in charCombo[i][0]:
                        tags.append('older maleherm')
                # Younger
                if 'ambiguous gender' in charCombo[i][1]:
                    tags.append('younger ambiguous')
                if 'male' in charCombo[i][1]:
                    tags.append('younger male')
                if 'female' in charCombo[i][1]:
                    tags.append('younger female')
                if 'intersex' in charCombo[i][1]:
                    tags.append('younger intersex')
                    if 'dickgirl' in charCombo[i][1]:
                        tags.append('younger dickgirl')
                    if 'cuntboy' in charCombo[i][1]:
                        tags.append('younger cuntboy')        
                    if 'herm' in charCombo[i][1]:
                        tags.append('younger herm')                    
                    if 'maleherm' in charCombo[i][1]:
                        tags.append('younger maleherm')
                break
            if yesNo == 'no':
                print("Is " + charCombo[i][1][0] + " significantly older than " + charCombo[i][0][0] + "? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('age difference')
                    # Older
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('older ambiguous')
                    if 'male' in charCombo[i][1]:
                        tags.append('older male')
                    if 'female' in charCombo[i][1]:
                        tags.append('older female')
                    if 'intersex' in charCombo[i][1]:
                        tags.append('older intersex')
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('older dickgirl')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('older cuntboy')        
                        if 'herm' in charCombo[i][1]:
                            tags.append('older herm')                    
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('older maleherm')
                    # Younger
                    if 'ambiguous gender' in charCombo[i][0]:
                        tags.append('younger ambiguous')
                    if 'male' in charCombo[i][0]:
                        tags.append('younger male')
                    if 'female' in charCombo[i][0]:
                        tags.append('younger female')
                    if 'intersex' in charCombo[i][0]:
                        tags.append('younger intersex')
                        if 'dickgirl' in charCombo[i][0]:
                            tags.append('younger dickgirl')
                        if 'cuntboy' in charCombo[i][0]:
                            tags.append('younger cuntboy')        
                        if 'herm' in charCombo[i][0]:
                            tags.append('younger herm')                    
                        if 'maleherm' in charCombo[i][0]:
                            tags.append('younger maleherm')
                break
            if yesNo == '?':
                print("A clear difference exists in the age groups of the individuals interacting. Such age groups may include young children/cubs, teens, fully developed adults, and elders.")
    #===========================================================================
    # Male bits
    #===========================================================================
    for i in range(len(charList)):
        if ('male' in charList[i]) or ('dickgirl' in charList[i]) or ('herm' in charList[i]) or ('maleherm' in charList[i]):
            while True:
                print("Does " + charList[i][0] + " have a visible penis? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('penis')
                    while True:
                        print("What color is " + charList[i][0] + "'s penis?")
                        penisColorTag = input()
                        charList[i].append(penisColorTag + ' penis')
                        print("Is " + charList[i][0] + "'s penis another color? (yes/no)")
                        yesNo = input()
                        if yesNo == 'yes':
                            if 'multicolored penis' not in charList[i]:
                                charList[i].append('multicolored penis')
                                print("Is " + charList[i][0] + "'s penis two distinct colors? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('two tone penis')
                                print("Is " + charList[i][0] + "'s penis rainbow colored? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('rainbow penis')
                        if yesNo == 'no':
                            break
                    while True:
                        print("Is " + charList[i][0] + "'s penis translucent? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('translucent penis')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A penis that has the property of light passing through it. Simply put: if you can see the penis and can see through the penis, either into the background, object, or entity, it is one of these.")
                    while True:
                        print("Does " + charList[i][0] + " have a big penis? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('big penis')
                            while True:
                                print("Does " + charList[i][0] + " have a huge penis? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('huge penis')
                                    while True:
                                        print("Does " + charList[i][0] + " have a hyper penis? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('hyper penis')
                                            charList[i].append('hyper')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("An impossibly large penis in proportion to the body size of its owner, to the point of absurdity.")
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("A character that has a large penis above what is anatomically possible but is still, to some extent, plausible looking. ")
                            break
                        if yesNo == 'no':
                            print("Does " + charList[i][0] + " have a small penis? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('small penis')
                                while True:
                                    print("Does " + charList[i][0] + " have a micropenis? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('micropenis')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("A character that has a near impossibly small penis, generally no longer or thicker than a finger.")
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A character that has a noticeably small penis. Generally no longer than the length of the hand or not much thicker than the thumb.")
                            break
                        if yesNo == '?':
                            print("A character, that has a large penis but is anatomically possible.")
                    while True:        
                        print("Does " + charList[i][0] + " have a noticeably short penis? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('short penis')
                            break
                        if yesNo == 'no':
                            while True:
                                print("Does " + charList[i][0] + " have a noticeably long penis? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('long penis')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("A penis that is especially long in comparison to its thickness and the character's height.")
                            break
                        if yesNo == '?':
                            print("A penis that is especially short in comparison to its thickness and the character's height.")
                    if ('dickgirl' not in charList[i]) and ('herm' not in charList[i]) and ('maleherm' not in charList[i]):
                        if 'faceless male' not in charList[i]:
                            while True:
                                print("Is " + charList[i][0] + " a disembodied penis?")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('disembodied penis')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("When there is a penis in view, but the character that it may be a part of is not. Often this may look like a literal floating penis, but the rest of the character could just be out of the frame.")
                    while True:
                        print("Is " + charList[i][0] + "'s penis erect? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('erection')
                            while True:
                                print("Is " + charList[i][0] + " tenting? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('tenting')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("When an erection causes the underwear, clothing, bed sheet or other crotch covering fabric to pull upward, taking the appearance of a tent.")
                            while True:
                                print("Does " + charList[i][0] + " have morning wood? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('morning wood')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("An involuntary full or partial erection when sleeping or waking up.")
                            while True:
                                print("Does " + charList[i][0] + " have an unwanted erection? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('unwanted erection')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("For posts depicting a character with an erection they do not want.")
                            if 'clothing' in charList[i]:
                                while True:
                                    print("Does " + charList[i][0] + " have an erection under their clothes? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('erection under clothes')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("A tag used for when an image depicts a character that has an erection under their clothing or clearly hints that way through expressions, dialogue or gestures.")
                            break
                        if yesNo == 'no':
                            while True:
                                print("Is " + charList[i][0] + "'s penis half-erect? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('half-erect')
                                    break
                                if yesNo == 'no':
                                    while True:
                                        print("Is " + charList[i][0] + "'s penis flaccid? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('flaccid')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("Used when a penis is visible but not erect. Often it is pointing down, hanging loosely, or just sitting on top of the balls not doing anything in particular.")
                                    break
                                if yesNo == '?':
                                    print("When a character's penis is not fully erect but not quite flaccid either.")
                            break
                        if yesNo == '?':
                            print("A character with a visibly stiff penis or a tent caused by an erect penis.")
                    break
                if yesNo == 'no':
                    while True:
                        print("Is " + charList[i][0] + " tenting? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('tenting')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("When an erection causes the underwear, clothing, bed sheet or other crotch covering fabric to pull upward, taking the appearance of a tent.")
                    while True:
                        print("Can you see " + charList[i][0] + "'s bulge? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('bulge')
                            while True:
                                print("Is " + charList[i][0] + "'s bulge big? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('big bulge')
                                    while True:
                                        print("Is " + charList[i][0] + "'s bulge hyper? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('hyper bulge')
                                            charList[i].append('hyper')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("Clothes bulging from an obviously hyper-sized penis and/or balls.")
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("Big bulges are somewhere in the ballpark of 'larger than a fist, smaller than a head'. Large, but not large enough to make walking difficult.")
                            while True:
                                print("Can you see the outline of " + charList[i][0] + "'s penis? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('penis outline')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("This tag is used when a character's penis is not directly visible, but can be seen as clearly present under clothing, erect or no.")
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Tagged for noticeable presence of penis and/or balls under clothing.")
                    break
                if yesNo == '?':
                    print("The penis (also known as cock, dick, dong and other terms) is the most visible part of the male genitalia.")
        if ('male' in charList[i]) or ('dickgirl' in charList[i]) or ('herm' in charList[i]) or ('maleherm' in charList[i]):
            while True:
                print("Does " + charList[i][0] + " have visible balls? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('balls')
                    while True:
                        print("What color is " + charList[i][0] + "'s balls?")
                        ballColorTag = input()
                        charList[i].append(ballColorTag + ' balls')
                        print("Are " + charList[i][0] + "'s balls another color? (yes/no)")
                        yesNo = input()
                        if yesNo == 'yes':
                            if 'multicolored balls' not in charList[i]:
                                charList[i].append('multicolored balls')
                                print("Are " + charList[i][0] + "'s balls two distinct colors? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('two tone balls')
                                print("Are " + charList[i][0] + "'s balls rainbow colored? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('rainbow balls')
                        if yesNo == 'no':
                            break
                    while True:
                        print("Are " + charList[i][0] + "'s balls translucent? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('translucent balls')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Balls that have the property of light passing through them. Simply put: if you can see the balls and can see through the balls, either into the background, object, or entity, it is one of these.")
                    while True:
                        print("Does " + charList[i][0] + " have big balls? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('big balls')
                            while True:
                                print("Does " + charList[i][0] + " have huge balls? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('huge balls')
                                    while True:
                                        print("Does " + charList[i][0] + " have huge balls? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('hyper balls')
                                            charList[i].append
                                            ('hyper')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("A character, that has unrealistically large balls, generally 3/8th the size of the character and larger. Characters under this tag are commonly capable of sitting on their balls without the support of their feet.")
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("A character, that has large balls significantly above average, generally anything that's not big enough to sit on but too big to be easily held in two hands.")
                            break
                        if yesNo == 'no':
                            while True:
                                print("Does " + charList[i][0] + " have small balls? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('small balls')
                                    while True:
                                        print("Does " + charList[i][0] + " have micro balls? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('micro balls')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("A character that has near impossibly small balls.")
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("A character that has balls smaller than usual. Generally the size of an eyeball, perhaps smaller.")
                            break
                        if yesNo == '?':
                            print("A character, that has large balls significantly above average, generally anything that's not big enough to sit on but too big to be easily held in two hands.")
                    break
                if yesNo == 'no':
                    while True:
                        print("Can you see the outline of " + charList[i][0] + "'s balls? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('ballsack outline')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("If the balls are not visible but their outline is discernible through clothes.")
                    if 'ballsack outline' not in charList[i]:
                        while True:
                            print("Can you see " + charList[i][0] + "'s bulge? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('bulge')
                                while True:
                                    print("Is " + charList[i][0] + "'s bulge big? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('big bulge')
                                        while True:
                                            print("Is " + charList[i][0] + "'s bulge hyper? (yes/no/?)")
                                            yesNo = input()
                                            if yesNo == 'yes':
                                                charList[i].append('hyper bulge')
                                                charList[i].append('hyper')
                                                break
                                            if yesNo == 'no':
                                                break
                                            if yesNo == '?':
                                                print("Clothes bulging from an obviously hyper-sized penis and/or balls.")
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("Big bulges are somewhere in the ballpark of 'larger than a fist, smaller than a head'. Large, but not large enough to make walking difficult.")
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Tagged for noticeable presence of penis and/or balls under clothing. This may be because of tight clothing, or because the genitalia is just too damn large.")
                    break
                if yesNo == '?':
                    print("The Balls (also known as testicles, nuts, ball sack and other terms) are a visible part of the male genitalia that include the pair of the roughly spherical testicle glands as well as the scrotum for tagging convenience.")
                
    #===========================================================================
    # Female bits
    #===========================================================================
    for i in range(len(charList)):
        if ('female' in charList[i]) or ('cuntboy' in charList[i]) or ('herm' in charList[i]) or ('maleherm' in charList[i]):
            while True:
                print("Is " + charList[i][0] + "'s pussy clearly visible? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('pussy')
                    while True:
                        print("What color is " + charList[i][0] + "'s pussy?")
                        pussyTag = input()
                        if pussyTag != '':
                            charList[i].append(pussyTag + ' pussy')
                        print("Is " + charList[i][0] + "'s pussy another color? (yes/no)")
                        yesNo = input()
                        if yesNo == 'yes':
                            if 'multicolored pussy' not in charList[i]:
                                charList[i].append('multicolored pussy')
                                print("Is " + charList[i][0] + "'s pussy two distinct colors? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('two tone pussy')
                                print("Is " + charList[i][0] + "'s pussy rainbow colored? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('rainbow pussy')
                        if yesNo == 'no':
                            break
                    while True:
                        print("Is " + charList[i][0] + "'s clitoris clearly visible? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('clitoris')
                            while True:
                                print("What color is " + charList[i][0] + "'s clitoris?")
                                clitorisTag = input()
                                charList[i].append(clitorisTag + ' clitoris')
                                print("Is " + charList[i][0] + "'s clitoris another color? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    if 'multicolored clitoris' not in charList[i]:
                                        charList[i].append('multicolored clitoris')
                                        print("Is " + charList[i][0] + "'s clitoris two distinct colors? (yes/no)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('two tone clitoris')
                                        print("Is " + charList[i][0] + "'s clitoris rainbow colored? (yes/no)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('rainbow clitoris')
                                if yesNo == 'no':
                                    break
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Part of the pussy or cloaca, female homologue of the penis.")
                    while True:
                        print("Is " + charList[i][0] + "'s clitoral hood clearly visible? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('clitoral hood')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("The skin that covers the clitoris; female homologue of the foreskin.")
                    break
                if yesNo == 'no':
                    while True:
                        print("Does " + charList[i][0] + " have camel toe? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('camel toe')
                            while True:
                                print("Does " + charList[i][0] + " have plump camel toe? (yes/no?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('plump camel toe')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("When a character has a plump labia but can not be seen directly, usually because of an article of clothing or other materials.")
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("When a character's pussy is not directly visible but its outline can be seen through clothing.")
                    break
                if yesNo == '?':
                    print("The pussy (also known as vagina, cunt, vulva, and other terms) is the most visible part of the female genitalia that may also include internal parts as well for tagging convenience.") 
    for i in range(len(charList)):
        if ('female' in charList[i]) or ('dickgirl' in charList[i]) or ('herm' in charList[i]):
            while True:
                print("Is " + charList[i][0] + " flat chested? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('flat chested')
                    break
                if yesNo == 'no':
                    while True:
                        print("Does " + charList[i][0] + " have breasts? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('breasts')
                            while True:
                                print("Is " + charList[i][0] + " a mammal or mammal-like? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    break
                                if yesNo == 'no':
                                    charList[i].append('non-mammal breasts')
                                    break
                                if yesNo == '?':
                                    print("Humanoid breasts on any species of animal that does not, in real life, produce milk. Reptiles, fish, birds, and insects depicted with breasts should be tagged with this.")
                            while True:
                                print("Does " + charList[i][0] + " have small breasts? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('small breasts')
                                    break
                                if yesNo == 'no':
                                    while True:
                                        print("Does " + charList[i][0] + " have medium breasts? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('medium breasts')
                                            break
                                        if yesNo == 'no':
                                            while True:
                                                print("Does " + charList[i][0] + " have big breasts? (yes/no/?)")
                                                yesNo = input()
                                                if yesNo == 'yes':
                                                    charList[i].append('big breasts')
                                                    if 'loli' in charList[i]:
                                                        charList[i].append('oppai loli')
                                                    while True:
                                                        print("Does " + charList[i][0] + " have huge breasts? (yes/no/?)")
                                                        yesNo = input()
                                                        if yesNo == 'yes':
                                                            charList[i].append('huge breasts')
                                                            while True:
                                                                print("Does " + charList[i][0] + " have hyper breasts? (yes/no/?)")
                                                                yesNo = input()
                                                                if yesNo == 'yes':
                                                                    charList[i].append('hyper breasts')
                                                                    charList[i].append('hyper')
                                                                    break
                                                                if yesNo == 'no':
                                                                    break
                                                                if yesNo == '?':
                                                                    print("From too large to physically carry (or occur naturally) and beyond.")
                                                            break
                                                        if yesNo == 'no':
                                                            break
                                                        if yesNo == '?':
                                                            print("Still physically plausible to somewhat unlikely. Equal or exceeds the bearer's head in size.")
                                                    break
                                                if yesNo == 'no':
                                                    break
                                                if yesNo == '?':
                                                    print("Pretty big, but still smaller than the bearer's head. Ranges from D-style up to the size of character's head.")
                                            break
                                        if yesNo == '?':
                                            print("Might be considered 'average-sized' breasts; B to C-cup sizing, dependent on the frame size and shape of the character.")
                                    break
                                if yesNo == '?':
                                    print("Not flat chested, but can be from below average size to just developing. Generally in the range of A-cup sizing.")
                            while True:
                                print("Does " + charList[i][0] + " have multiple pairs of breasts? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('multi breast')
                                    print("How many breasts?")
                                    breastsTag = input()
                                    charList[i].append(breastsTag + ' breasts')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("A character that has more than one pair of breasts on a individual body. They may or may not have nipples as well.")
                            while True:
                                print("Can you only see the underside of " + charList[i][0] + "'s breasts? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('under boob')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("Images or Animations in which only the underside of a female's breasts can be seen.")
                            while True:
                                if 'nipples' not in charList[i]:
                                    print("Can you only see the bare side of " + charList[i][0] + "'s breasts? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('side boob')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("When only the outer side of a bare breast, but not the nipple, is visible.")
                            while True:
                                print("Is " + charList[i][0] + " pressing their breasts against something? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('breast squish')
                                    while True:
                                        print("Is " + charList[i][0] + " pressing their breasts against another's breasts? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('breasts frottage')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("When two or more characters have their breasts pressed against each other.")
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("When a character presses their breasts against something (e.g. a wall, floor, arm, or chest).")
                            while True:
                                print("Is " + charList[i][0] + " holding their own breasts? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('holding breasts')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("Used to denote a character holding their own breasts in an image; not to be confused with breast grab.")
                            while True:
                                print("Is " + charList[i][0] + " resting their breasts on a surface or limb? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('breast rest')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("When breasts are resting on a surface or limb, sometimes flattening out under their own weight.")
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Soft round growths that serve as a secondary sexual characteristic for female or intersex characters. ")
                    break
                if yesNo == '?':
                    print("For non-male characters with no visible breasts (i.e. 'flat as a board'). Not to be confused with small breasts, which are used for female characters with below average to barely visible (but still present) breasts.")
        if ('female' in charList[i]) or ('dickgirl' in charList[i]) or ('herm' in charList[i]):
            while True:
                print("Can you see " + charList[i][0] +  "'s areolae? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('areola')
                    while True:
                        print("What color are " + charList[i][0] + "'s areolae?")
                        areolaColor = input()
                        charList[i].append(areolaColor + ' areola')
                        print("Are " + charList[i][0] + "'s areolae another color? (yes/no)")
                        yesNo = input()
                        if yesNo == 'yes':
                            if 'multicolored areola' not in charList[i]:
                                charList[i].append('multicolored areola')
                                print("Are " + charList[i][0] + "'s areolae two distinct colors? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('two tone areola')
                                print("Are " + charList[i][0] + "'s areolae rainbow colored? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('rainbow areola')
                        if yesNo == 'no':
                            break
                    while True:
                        print("Are " + charList[i][0] + "'s areolae glowing? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('glowing areola')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Areolae that are glowing.")
                    while True:
                        print("Are " + charList[i][0] + "'s areolae puffy? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('puffy areola')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Areolae that are puffy.")
                    while True:
                        print("Does " + charList[i][0] + " have heart-shaped areolae? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('<3 areola')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Areolae that are heart-shaped.")   
                    while True:
                        print("Does " + charList[i][0] + " have big areolae? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('big areola')
                            while True:
                                print("Does " + charList[i][0] + " have huge areolae? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('huge areola')
                                    while True:
                                        print("Does " + charList[i][0] + " have hyper areolae? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('hyper areola')
                                            charList[i].append('hyper')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("Areola that cover most of the breasts or areola larger than huge.")
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("When the areola of a character covers an unusually large portion of the breasts.")
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("This tag is used when the circular area of pigmented skin around the nipples of a character are very pronounced.")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A (usually circular) patch of discolored skin around a character's nipples.")
        if ('female' in charList[i]) or ('dickgirl' in charList[i]) or ('herm' in charList[i]):
            while True:
                print("Can you clearly see " + charList[i][0] + "'s nipples? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('nipples')
                    while True:
                        print("What color are " + charList[i][0] + "'s nipples?")
                        nippleColor = input()
                        charList[i].append(areolaColor + ' nipples')
                        print("Are " + charList[i][0] + "'s nipples another color? (yes/no)")
                        yesNo = input()
                        if yesNo == 'yes':
                            if 'multicolored nipples' not in charList[i]:
                                charList[i].append('multicolored nipples')
                                print("Are " + charList[i][0] + "'s nipples two distinct colors? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('two tone nipples')
                                print("Are " + charList[i][0] + "'s nipples rainbow colored? (yes/no)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('rainbow nipples')   
                        if yesNo == 'no':
                            break                 
                    while True:
                        print("Are " + charList[i][0] + "'s nipples glowing? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('glowing nipples')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A tag used for when the nipple(s) of a creature appear to be glowing; emitting light.")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Images or animations depicting one or more nipples: organs which, while serving no functionality in males, are used for the release of breast milk in females.")
    #===========================================================================
    # Body Parts
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + "'s butt visible or prominently featured? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('butt')
                while True:
                    print("Is " + charList[i][0] + "'s butt big? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('big butt')
                        while True:
                            print("Is " + charList[i][0] + "'s butt huge? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('huge butt')
                                while True:
                                    print("Is " + charList[i][0] + "'s butt hyper? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('hyper butt')
                                        charList[i].append('hyper')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("An impossibly large hyper butt.")
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Images and animations of a character whose rear end is so overwhelmingly massive in size that simply referring to it as a 'big butt' would be an incredible understatement.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Refers to a character whose butt is remarkably large.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Buttocks, booty, rear end, ass, heinie, posterior. This tag is used if a butt is visible or, more usually, prominently featured, regardless of whether it is clothed or not.")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have thick thighs? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('thick thighs')
                while True:
                    print("Does " + charList[i][0] + " have huge thighs? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('huge thighs')
                        while True:
                            print("Does " + charList[i][0] + " have hyper thighs? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('hyper thighs')
                                charList[i].append('hyper')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Thighs that are unrealistically huge.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Thighs that are the same width as the characters torso or bigger.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Thighs is the upper part of the leg where the femur is located. This tag describes characters with thighs that are big in circumference or diameter (thick) in relation to their body size.")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have wide hips? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('wide hips')
                while True:
                    print("Does " + charList[i][0] + " have huge hips? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('huge hips')
                        while True:
                            print("Does " + charList[i][0] + " have hyper hips? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('hyper hips')
                                charList[i].append('hyper')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Unrealistically large hips. Probably more than three times with width of their shoulders.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Hips that are probably around twice the width of their shoulders.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("This tag describes an individual with noticeably larger-than-average hips relative to their body size or shape.")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have a small waist? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('small waist')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A feature where the waist is narrower than the hips and shoulders to a greater than average degree.")
    
    for i in range(len(charList)):
        if 'overweight' not in charList[i]:
            while True:
                print("Is " + charList[i][0] + " slightly chubby? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('slightly chubby')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A little thick here and there. Maybe a small 'gut' but the majority of the body structure is fairly similar to a non-chubby person.")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have abs? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('abs')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Short for the grouping of the abdominal muscles (sometimes also including Obliques).")
    
    for i in range(len(charList)):
        if ('muscular' in charList[i]) and ('slightly chubby' in charList[i]):
            if 'abs' not in charList[i]:
                charList[i].append('musclegut')
        if ('muscular' in charList[i]) and ('overweight' in charList[i]):
            if 'abs' not in charList[i]:
                charList[i].append('musclegut')    
    
    for i in range(len(charList)):
        if ('medium breasts' in charList) or ('big breasts' in charList[i]):   
            if 'wide hips' in charList[i]:
                while True:
                    print("Is " + charList[i][0] + "'s waist slim in comparison to their breasts and hips? (yes/no)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('curvy figure')
                        if ('big breasts' not in charList[i]) and ('wide hips' not in charList[i]):
                            charList[i].append('hourglass figure')
                        if ('big breasts' in charList[i]) and ('wide hips' in charList[i]):
                            charList[i].append('voluptuous')
                            if 'small waist' in charList[i]:
                                charList[i].append('curvaceous')
                        break
                    if yesNo == 'no':
                        break
                    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have a rounded belly? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('belly')
                while True:
                    print("Does " + charList[i][0] + " have a big belly? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('big belly')
                        while True:
                            print("Does " + charList[i][0] + " have a hyper belly? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('hyper belly')
                                charList[i].append('hyper')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("When a character's belly is far bigger than could ever be realistically possible, commonly from obesity, vore, pregnancy, or a variation of inflation.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character's stomach is bigger than normal, either from obesity or pregnancy.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Sometimes also called a 'gut', a 'paunch', or a 'beer belly', etc. This tag is used for when a character's lower abdomen/stomach area is rounded in front, for any reason (pregnancy, overweight, inflation, etc).")
  
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have visible fingers? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('fingers')
                while True:
                    print("How many fingers does " + charList[i][0] + " have?")
                    fingerTag = input()
                    if fingerTag == '1':
                        charList[i].append('1 finger')
                        break
                    else:
                        charList[i].append(fingerTag + ' fingers')
                        break
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("The manipulative digits commonly found on hands.")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have a ponytail? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('ponytail')
                while True:
                    if 'braided hair' in charList[i]:
                        print("Does " + charList[i][0] + " have a braided ponytail? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('braided ponytail')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A variant of the ponytail that, instead of being straight, is instead woven into plaits.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A ponytail is a hairstyle in which most or all of the hair on the head is pulled away from the face, gathered and secured at the back of the head with a hair tie, hair clip or similar device, and allowed to hang freely from that point.")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have pigtails? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('pigtails')
                if 'briaded hair' in charList[i]:
                    while True:
                        print("Does " + charList[i][0] + " have twin braids? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('twin braids')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Hair braided into two braids.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("This tag is used when a character has their hair bunched like a ponytail on both sides of their head.")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have hair on their head? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('hair')
                while True:
                    print("What color is " + charList[i][0] + "'s hair?")
                    hairTag = input()
                    charList[i].append(hairTag + ' hair')
                    print("Is " + charList[i][0] + "'s hair another color? (yes/no)")
                    yesNo = input()
                    if yesNo == 'yes':
                        if 'multicolored hair' not in charList[i]:
                            charList[i].append('multicolored hair')
                            print("Is " + charList[i][0] + "'s hair two distinct colors? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two tone hair')
                            print("Is " + charList[i][0] + "'s hair rainbow colored? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('rainbow hair')
                    if yesNo == 'no':
                        break
                while True:
                    print("Does " + charList[i][0] + " have short hair? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('short hair')
                        break
                    if yesNo == 'no':
                        while True:
                            print("Does " + charList[i][0] + " have long hair? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('long hair')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("When a character's hair extends below their shoulders. Typically more than 2 heads in length.")
                        break
                    if yesNo == '?':
                        print("When a character's hair does not extend past the neck. Typically less than 1.5 heads in length.")
                while True:
                    print("Does " + charList[i][0] + " have big hair? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('big hair')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Hair that is styled and teased to occupy an unusually large amount of space above and around the head")
                while True:
                    print("Does " + charList[i][0] + " have braided hair? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('braided hair')
                        while True:
                            print("Is " + charList[i][0] + "'s hair in a single braid? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('single braid')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("This tag is used when a character's hair is woven into one single plait.")
                        if 'pigtails' in charList[i]:
                            while True:
                                print("Does " + charList[i][0] + " have twin braids? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('twin braids')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("Hair braided into two braids.")
                        while True:
                            print("Does " + charList[i][0] + " have a side braid? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('side braid')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A side braid is a hairstyle that features a single braid positioned on one side of the head.")
                        while True:
                            print("Does " + charList[i][0] + " have dreadlocks? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('dreadlocks')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A type of hairstyle that has twisted, matted ropes of hair.")
                        while True:
                            print("Does " + charList[i][0] + " have drill hair? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('drill hair')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A characteristic hairstyle (predominantly on females) where the curls of the hair resemble the bit of a drill or the shavings from a drill.")                        
                        while True:
                            print("Does " + charList[i][0] + " have straight hair? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('straight hair')
                                break
                            if yesNo == 'no':
                                while True:
                                    print("Does " + charList[i][0] + " have curly hair? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('curly hair')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("When a character's hair is curly... Speaks for itself, really.")
                                break
                            if yesNo == '?':
                                print("When a character's hair is relatively straight and free-flowing. Not curly or messy or anything like that, and usually not styled.")
                        while True:
                            print("Does " + charList[i][0] + " have messy hair? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('messy hair')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Referred to the hair of a character that looks either intentional or not messed up, dishevelled and basically formless.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("This tag is used when all or part of a character's hair is woven into plaits.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Threadlike strands on the heads of humans and many animals, not to be confused with fur.")
  
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have a mane? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('mane')
                while True:
                    print("What color is " + charList[i][0] + "'s mane?")
                    maneTag = input()
                    charList[i].append(maneTag + ' mane')
                    print("Is " + charList[i][0] + "'s mane another color? (yes/no)")
                    yesNo = input()
                    if yesNo == 'yes':
                        if 'multicolored mane' not in charList[i]:
                            charList[i].append('multicolored mane')
                            print("Is " + charList[i][0] + "'s mane two distinct colors? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two tone mane')
                            print("Is " + charList[i][0] + "'s mane rainbow colored? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('rainbow mane')
                    if yesNo == 'no':
                        break
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Long and heavy hair growing about the neck and head of some mammals (such as horses and lions)")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have a visible nose? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                print("What color is " + charList[i][0] + "'s nose?")
                noseTag = input()
                if noseTag != '':
                    charList[i].append(noseTag + ' nose')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("The part of the face or facial region in humans and certain animals that contains the nostrils and the organs of smell and functions as the usual passageway for air in respiration")
    
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have visible, open eyes? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                while True:
                    print("How many eyes does " + charList[i][0] + " have?")
                    eyeTag = int(input())
                    if eyeTag == 1:
                        charList[i].append('1 eye')
                        break
                    if eyeTag >= 3:
                        charList[i].append('multi eye')
                        charList[i].append(str(eyeTag) + ' eyes')
                        break
                    if eyeTag == 2:
                        break
                while True:
                    print("What color is " + charList[i][0] + "'s eyes?")
                    eyeTag = input()
                    charList[i].append(eyeTag + ' eyes')
                    print("Does " + charList[i][0] + "'s eyes have another color? (yes/no)")
                    yesNo = input()
                    if yesNo == 'yes':
                        while True:
                            print("Does " + charList[i][0] + " have heterochromia? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('heterochromia')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Images or animations depicting a character with the medical condition known as heterochromia iridis, a genetic quirk which causes their eyes to contain multiple colors.")
                        while True:
                            print("Does " + charList[i][0] + " have multicolored eyes? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('multicolored eyes')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Images or Animations in which a character's eyes has multiple colors.")
                    if yesNo == 'no':
                        break
                while True:
                    print("Does " + charList[i][0] + " have clearly defined sclera? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        print("What color is " + charList[i][0] + "'s sclera?")
                        scleraTag = input()
                        if scleraTag != 'white':
                            charList[i].append(scleraTag + ' sclera')
                        while True:
                            print("Does " + charList[i][0] + " have pupils? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                break
                            if yesNo == 'no':
                                charList[i].append('no pupils')
                                break
                            if yesNo == '?':
                                print("Images depicting one or more characters with a clearly defined sclera and iris but no visible pupils.")
                        break
                    if yesNo == 'no':
                        while True:
                            print("Does " + charList[i][0] + " have clearly defined irises and pupils? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('no sclera')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Images depicting one or more characters with a clearly defined iris and pupils but no visible sclera.")
                        break
                    if yesNo == '?':
                        print("The tough fibrous outer envelope of tissue covering all of the eyeball except the cornea.")
                while True:
                    print("Does " + charList[i][0] + " have empty eyes? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('empty eyes')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Images depicting one or more characters that possess eyes that are uniformly one color or a gradient.")
                while True:
                    print("Does " + charList[i][0] + " have half-closed eyes? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('half-closed eyes')
                        while True:
                            print("Does " + charList[i][0] + " have bedroom eyes? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('bedroom eyes')
                                charList[i].append('seductive')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("That sensual, seductive-looking glance that a character expresses when they are in a mood for something romantic and/or sexual. ")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Images or animations in which a character has both of eyes somewhat, but not entirely, closed.")
                while True:
                    print("Is one of " + charList[i][0] + "'s eyes closed? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('one eye closed')
                        while True:
                            print("Is " + charList[i][0] + " winking? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('wink')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A wink is an intentional action in which a character closes one eye, leaving the other open.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Images or Animations in which a character has only one of their eyes shut.")
                while True:
                    print("Does " + charList[i][0] + " have heart eyes? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('<3 eyes')
                        charList[i].append('<3')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Use this when seeing heart-shaped eyes or heart-shaped pupils within the eyes.")
                while True:
                    print("Does " + charList[i][0] + " have big eyes? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('big eyes')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character has eyes that are disproportionately big, especially compared with the rest of its facial features.")
                while True:
                    print("Does " + charList[i][0] + " have spiral eyes? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('spiral eyes')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Spiral eyes are eyes that show swirling or spiraling, most prominently associated with hypnosis.")
                break
            if yesNo == 'no':
                while True:
                    print("Is " + charList[i][0] + " eyeless? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('eyeless')
                        break
                    if yesNo == 'no':
                        while True:
                            print("Are " + charList[i][0] + " eyes closed? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('eyes closed')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Images or animations which show a character with their eyes closed. If you can not see the other eye, assume it is closed as well.")
                        break
                    if yesNo == '?':
                        print("For characters who do not have eyes.")
                break
            if yesNo == '?':
                print("The organ of sight, in vertebrates typically one of a pair of spherical bodies contained in an orbit of the skull and in humans appearing externally as a dense, white, curved membrane, or sclera, surrounding a circular, colored portion, or iris, that is covered by a clear, curved membrane, or cornea, and in the center of which is an opening, or pupil, through which light passes to the retina.")
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have tears in their eyes? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('tears')
                while True:
                    print("Is " + charList[i][0] + " crying? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('crying')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Crying, also called sobbing, wailing, weeping, whimpering, bawling, blubbering and QQ-ing, is shedding tears as a response to an emotional state in humans.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Refers to images or animations in which at least one character has tears on their face/ around their eyes, but may not be actively crying. ")
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " wearing makeup? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('makeup')
                while True:
                    print("Is " + charList[i][0] + " applying makeup? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('applying makeup')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character is applying makeup.")    
                while True:
                    print("Is " + charList[i][0] + "'s makeup running? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('running makeup')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When makeup is exposed to wetness, it gets runny. Makeup gets runny commonly when exposed to tears when either a character is crying or any other fashion.")
                while True:
                    print("Is " + charList[i][0] + " wearing eyeshadow? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('eyeshadow')
                        print("What color is " + charList[i][0] + "'s eyeshadow?")
                        eyeshadowTag = input()
                        charList[i].append(eyeshadowTag + ' eyeshadow')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A colored cosmetic, typically in powder form, applied to the eyelids or to the skin around the eyes to accentuate them.")
                while True:
                    print("Is " + charList[i][0] + " wearing eyeliner? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('eyeliner')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Makeup used to outline the eyes.")
                while True:
                    print("Is " + charList[i][0] + " wearing mascara? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('mascara')
                        if 'running makeup' in charList[i]:
                            while True:
                                print("Is " + charList[i][0] + "'s mascara running? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('running mascara')
                                    if 'tears' in charList[i]:
                                        while True:
                                            print("Does " + charList[i][0] + " have mascara tears? (yes/no/?)")
                                            yesNo = input()
                                            if yesNo == 'yes':
                                                charList[i].append('mascara tears')
                                                break
                                            if yesNo == 'no':
                                                break
                                            if yesNo == '?':
                                                print("When a character has tears in their eyes while wearing mascara.") 
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("When mascara is exposed to wetness, it gets runny. Mascara gets runny commonly when exposed to tears when either a character is crying or any other fashion.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A cosmetic applied to thicken, lengthen, and usually darken the eyelashes.")
                while True:
                    print("Is " + charList[i][0] + " wearing lipstick? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('makeup')
                        print("What color is " + charList[i][0] + "'s lipstick?")
                        lipstickTag = input()
                        charList[i].append(lipstickTag + ' lipstick')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("This tag is used when a character has applied lipstick of any color to their lips.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Make-up, also known as Cosmetics, are substances used to enhance the appearance or odor of the human body.")
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have eyebrows? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('eyebrows')
                while True:
                    print("Does " + charList[i][0] + " have a unibrow? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('unibrow')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character's eyebrows are joined together and looks like one instead of two.")
                while True:
                    print("Does " + charList[i][0] + " have thick eyebrows? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('thick eyebrows')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Eyebrows that are bushy or thick")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("The ridge over the eye or the hair growing usually in a line or arch on the skin over it")     
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have colored nails? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('colored nails')
                while True:
                    print("What color are " + charList[i][0] + " nails?")
                    nailTag = input()
                    charList[i].append(nailTag + ' nails')
                    break
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Colored nails are regular nails that have been colored by nail polish to create a temporary layer of paint for fashion purposes.")

    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " covered in fur? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('fur')
                while True:
                    print("What color is " + charList[i][0] + "'s fur?")
                    furTag = input()
                    charList[i].append(furTag + ' fur')
                    print("Is " + charList[i][0] + "'s fur another color? (yes/no)")
                    furYesNo = input()
                    if furYesNo == 'yes':
                        if 'multicolored fur' not in charList[i]:
                            charList[i].append('multicolored fur')
                            print("Is " + charList[i][0] + "'s fur two dictinct colors? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two tone fur')
                            print("Is " + charList[i][0] + "'s fur rainbow colored? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('rainbow fur')
                    if furYesNo == 'no':
                        break
                while True:
                    print("Is " + charList[i][0] + "'s fur dark?")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('dark fur')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body covered in dark-colored fur.")
                while True:
                    print("Is " + charList[i][0] + "'s fur light?")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('light fur')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body covered in light-colored fur.")
                while True:
                    print("Is " + charList[i][0] + "'s fur long? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('long fur')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character with long fur.")
                while True:
                    print("Is " + charList[i][0] + "'s fur short? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('short fur')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character with short fur.")
                while True:
                    print("Is " + charList[i][0] + "'s fur spotted? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('spotted fur')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in spotted fur.")
                while True:
                    print("Is " + charList[i][0] + "'s fur striped? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('striped fur')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in striped fur.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("The thick coat of soft hair covering the skin of a mammal, such as a fox or beaver.")  
        while True:
            print("Is " + charList[i][0] + " covered in feathers? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('feathers')
                while True:
                    print("What color is " + charList[i][0] + "'s feathers?")
                    feathersTag = input()
                    charList[i].append(feathersTag + ' feathers')
                    print("Are " + charList[i][0] + "'s feathers another color? (yes/no)")
                    featheryesNo = input()
                    if featheryesNo == 'yes':
                        if 'multicolored feathers' not in charList[i]:
                            charList[i].append('multicolored feathers')
                            print("Are " + charList[i][0] + "'s feathers two dictinct colors? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two tone feathers')
                            print("Are " + charList[i][0] + "'s feathers rainbow colored? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('rainbow feathers')
                    if featheryesNo == 'no':
                        break
                while True:
                    print("Is " + charList[i][0] + "'s feathers spotted? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('spotted feathers')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in spotted feathers.")
                while True:
                    print("Is " + charList[i][0] + "'s feathers striped? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('striped feathers')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in striped feathers.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print(" One of the light, flat growths forming the plumage of birds, consisting of numerous slender, closely arranged parallel barbs forming a vane on either side of a horny, tapering, partly hollow shaft.")  
        while True:
            print("Is " + charList[i][0] + " covered in scales? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('scales')
                while True:
                    print("What color is " + charList[i][0] + "'s scales?")
                    scalesTag = input()
                    charList[i].append(scalesTag + ' scales')
                    print("Are " + charList[i][0] + "'s scales another color? (yes/no)")
                    scalesyesNo = input()
                    if scalesyesNo == 'yes':
                        if 'multicolored scales' not in charList[i]:
                            charList[i].append('multicolored scales')
                            print("Are " + charList[i][0] + "'s scales two dictinct colors? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two tone scales')
                            print("Are " + charList[i][0] + "'s scales rainbow colored? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('rainbow scales')
                    if scalesyesNo == 'no':
                        break
                while True:
                    print("Is " + charList[i][0] + "'s scales spotted? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('spotted scales')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in spotted scales.")
                while True:
                    print("Is " + charList[i][0] + "'s scales striped? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('striped scales')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in striped scales.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("One of the many small platelike dermal or epidermal structures that characteristically form the external covering of fishes, reptiles, and certain mammals.")  
        while True:
            print("Is " + charList[i][0] + " covered in skin? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                while True:
                    print("What color is " + charList[i][0] + "'s skin?")
                    skinTag = input()
                    charList[i].append(skinTag + ' skin')
                    print("Is " + charList[i][0] + "'s skin another color? (yes/no)")
                    skinyesNo = input()
                    if skinyesNo == 'yes':
                        if 'multicolored skin' not in charList[i]:
                            charList[i].append('multicolored skin')
                            print("Is " + charList[i][0] + "'s skin two dictinct colors? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two tone skin')
                            print("Is " + charList[i][0] + "'s skin rainbow colored? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('rainbow skin')
                    if skinyesNo == 'no':
                        break
                while True:
                    print("Is " + charList[i][0] + "'s skin dark?")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('dark skin')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body covered in dark-colored skin.")
                while True:
                    print("Is " + charList[i][0] + "'s skin light?")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('light skin')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body covered in light-colored skin.")
                while True:
                    print("Is " + charList[i][0] + "'s skin spotted? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('spotted skin')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in spotted skin.")
                while True:
                    print("Is " + charList[i][0] + "'s skin striped? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('striped skin')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in striped skin.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("The membranous tissue forming the external covering or integument of an animal and consisting in vertebrates of the epidermis and dermis.")
        while True:
            print("Is " + charList[i][0] + " covered in some kind of unknown texture? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                while True:
                    print("What color is " + charList[i][0] + "'s body?")
                    bodyTag = input()
                    charList[i].append(bodyTag + ' body')
                    print("Is " + charList[i][0] + "'s body another color? (yes/no)")
                    bodyyesNo = input()
                    if bodyyesNo == 'yes':
                        if 'multicolored body' not in charList[i]:
                            charList[i].append('multicolored body')
                            print("Is " + charList[i][0] + "'s body two dictinct colors? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two tone body')
                            print("Is " + charList[i][0] + "'s body rainbow colored? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('rainbow body')
                    if bodyyesNo == 'no':
                        break
                while True:
                    print("Is " + charList[i][0] + "'s body dark?")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('dark body')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body covered in dark-colored body.")
                while True:
                    print("Is " + charList[i][0] + "'s body light?")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('light body')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body covered in light-colored body.")
                while True:
                    print("Is " + charList[i][0] + "'s body spotted? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('spotted body')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in spotted body.")
                while True:
                    print("Is " + charList[i][0] + "'s body striped? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('striped body')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character or animal, that has its body partially or completely covered in striped body.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A character with a body that is difficult to determine the type of skin, fur or scales that the character has.")
    for i in range(len(charList)):
        while True:
            print("Can we see " + charList[i][0] + "'s tongue? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('tongue')
                # TODO: Other tongue tags
                while True:
                    print("What color is " + charList[i][0] + "'s tongue?")
                    tongueTag = input()
                    if tongueTag != '':
                        charList[i].append(tongueTag + ' tongue')
                    print("Is " + charList[i][0] + "'s tongue another color? (yes/no)")
                    tongueYesNo = input()
                    if tongueYesNo == 'yes':
                        if 'multicolored tongue' not in charList[i]:
                            charList[i].append('multicolored tongue')
                            print("Is " + charList[i][0] + "'s tongue two distinct colors? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two tone tongue')
                            print("Is " + charList[i][0] + "'s tongue rainbow colored? (yes/no)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('rainbow tongue')
                    if tongueYesNo == 'no':
                        break
                while True:
                    print("Is " + charList[i][0] + "'s tongue out? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('tongue out')
                        while True:
                            print("Is " + charList[i][0] + " licking someone or something? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('licking')
                                # TODO: Licking what?
                                # TODO: Blep?
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A character rubbing their tongue against something, be it another character, an object, or even themselves.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Images or Animations in which a character's tongue is protruding out between the lips.")
                while True:
                    print("Does " + charList[i][0] + " have a long tongue? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('long tongue')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A long tongue is a tongue that is noticeably longer than a human's, generally if the tongue is long enough that a character or animal could theoretically touch the top of their own snout or nose with it then it counts.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A character with an exposed tongue, the muscle in the mouth that aids with the consumption of food.")
    #===========================================================================
    # Piercings
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Does " + charList[i][0] + " have any piercings? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('piercing')
                while True:
                    print("Does " + charList[i][0] + " have ear piercings? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('ear piercing')
                        # TODO: Types of ear piercings
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A piercing in the ear.")
                if 'nipples' in charList[i]:
                    while True:
                        print("Does " + charList[i][0] + " have nipple piercings? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('nipple piercing')
                            # TODO: Types of nipple piercings
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("")
                while True:
                    print("Does " + charList[i][0] + " have facial piercings? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('facial piercing')
                        while True:
                            print("Does " + charList[i][0] + " have nose piercings? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('nose piercing')
                                # TODO: Types of nose piercings
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Piercings done somewhere on the nose or nostril.")
                        # TODO: Types of facial piercings
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A piercing on some part of the forward face.")
                while True:
                    print("Does " + charList[i][0] + " have genital piercings? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('genital piercing')
                        # TODO: Types of genital piercing
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A type of piercing that involves any part of the genital area.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Art featuring body piercings.")
    #===========================================================================
    # Looking
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " looking directly at the viewer? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('looking at viewer')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Tagged when at least one character is looking directly at the viewer, through the fourth wall. In other words, it is as if the character is looking at you.")
        while True:
            print("Is " + charList[i][0] + " looking back? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('looking back')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Images or animations in which a character is looking over their shoulders at something/someone else, or the viewer.")
        while True:
            print("Is " + charList[i][0] + " looking pleasured? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('looking pleasured')
                while True:
                    print("Is " + charList[i][0] + " making an ahegao face? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('ahegao')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A particular facial expression that occurs when a character's mouth is open, and eyes are usually rolled back. Often accompanied by dilated_pupils & tongue_out.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When at least one character seems to feel sexual pleasure, often by showing it with a smile or an ecstatic face.")
        if (len(charList) > 1) or ('unseen character' in tags):
            while True:
                print("Is " + charList[i][0] + " looking at another character? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('looking at another')
                    while True:
                        print("Is " + charList[i][0] + " peeping? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('peeping')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Tagged when a character is secretly watching someone. Usually from close proximity, such as through a window or keyhole, or from bushes or other concealed places.")
                    while True:
                        print("Is " + charList[i][0] + " being watched? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('being watched')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Tagged when someone is being watched. Similar to a voyeur, but there is no indication that the watcher is taking pleasure from watching the act, be it sexual or not.")
                    while True:
                        print("Is " + charList[i][0] + " making eye contact with another character? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('eye contact')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Used when at least two characters in an image are looking directly at each other. For situations where a character is looking at the viewer, use looking at viewer instead.")
                    while True:
                        print("Is " + charList[i][0] + " looking at their partner? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('looking at partner')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("When a character is looking at a partner. Used mainly in romantic and/or sexual situations.")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("When one character is looking at another character.")
    #===========================================================================
    # Clothing
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " clothed? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('clothed')
                while True:
                    print("Is " + charList[i][0] + " fully clothed? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('fully clothed')
                        break
                    if yesNo == 'no':
                        while True:
                            print("Is " + charList[i][0] + " partially clothed? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('partially clothed')
                                while True:
                                    print("Are " + charList[i][0] + " pants down? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('pants down')
                                        charList[i].append('pants')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("Images or animations in which a character's pants are worn down far enough to provide full access to their genitalia and buttocks.")
                                while True:
                                    print("Are " + charList[i][0] + " shorts down? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('shorts down')
                                        charList[i].append('shorts')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("Images or animations in which a character's shorts are worn down far enough to provide full access to their genitalia and buttocks.")
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Used to indicate a character is wearing clothes that are pulled aside or partially removed.")
                        break
                    if yesNo == '?':
                        print("Tagged when a character is wearing a full set of clothing (both topwear and bottomwear). Footwear optional.")
                while True:
                    print("Is " + charList[i][0] + " wearing skimpy clothing? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('skimpy')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Characters that are dressed in clothing that is notably tight, revealing (midriff, cleavage), suggestive, or otherwise accentuating a character's sexual proclivity.")
                if 'breasts' in charList[i]:
                    while True:
                        print("Is " + charList[i][0] + " showing cleavage? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('cleavage')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Images or animations depicting cleavage; sometimes called the 'bust line', the gap between a character's breasts, lying over the sternum.")
                while True:
                    print("Is " + charList[i][0] + " crossdressing? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('crossdressing')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character wearing clothing associated with their opposite gender.")                
                while True:
                    print("Is " + charList[i][0] + " bottomless? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('bottomless')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Images or animations depicting a character wearing clothing over the upper half of their body, but not over the lower half. ")
                while True:
                    print("Is " + charList[i][0] + " topless? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('topless')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Images or animations depicting a character who is wearing clothing over the lower half of their body, but not the upper half.")
                if 'feral' in charList[i]:
                    charList[i].append('clothed feral')
                break
            if yesNo == 'no':
                while True:
                    print("Is " + charList[i][0] + " mostly nude? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('mostly nude')
                        break
                    if yesNo == 'no':
                        while True:
                            print("Is " + charList[i][0] + " nude? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('nude')
                                while True:
                                    print("Is " + charList[i][0] + " casually nude? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('casual nudity')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("Used when one or more characters within a post are nude in non-sexual situations.")
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Posts depicting at least one character who isn't wearing any clothing at all. Not even stockings or a hat, or other non-covering clothing.")
                        break
                    if yesNo == '?':
                        print("Tagged when a character is only wearing clothing that doesn't really cover anything of the torso, including groin. Such as hats, gloves, scarves, boots, etc.")
                break
            if yesNo == '?':
                print("Images or animations which show characters wearing clothing.")
    #===========================================================================
    # X on Y
    #===========================================================================
    charCombo = list(itertools.combinations(charList, 2))
    charPermu = list(itertools.permutations(charList, 2))
    for i in range(len(charCombo)):
        while True:
            print("Are " + charCombo[i][0][0] + " and " + charCombo[i][1][0] + " doing romantic/sexual acts with each other? (yes/no)")
            yesNo = input()
            if yesNo == 'yes':
                if 'male' in charCombo[i][0]:
                    if 'male' in charCombo[i][1]:
                        tags.append('male/male')
                    if 'female' in charCombo[i][1]:
                        tags.append('male/female')
                        while True:
                            print("Is " + charCombo[i][1][0] + " pegging " + charCombo[i][0][0] + "? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('pegging')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A female character wearing a strapon and using the sex toy to engage in anal sex with a receiving male character.")
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('male/ambiguous')
                    if 'intersex' in charCombo[i][1]:
                        tags.append('intersex/male')
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('dickgirl/male')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('cuntboy/male')
                        if 'herm' in charCombo[i][1]:
                            tags.append('herm/male')
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('maleherm/male')
                    if ('anthro' not in charCombo[i][0]) and ('anthro' not in charCombo[i][1]):
                        if 'anthro' in charCombo[i][1]:
                            tags.append('male on anthro')
                    if ('feral' not in charCombo[i][0]) and ('feral' not in charCombo[i][1]):
                        if 'feral' in charCombo[i][1]:
                            tags.append('male on feral')
                    if ('human' not in charCombo[i][0]) and ('human' not in charCombo[i][1]):
                        if 'human' in charCombo[i][1]:
                            tags.append('male on human')
                    if ('humanoid' not in charCombo[i][0]) and ('humanoid' not in charCombo[i][1]):
                        if 'humanoid' in charCombo[i][1]:
                            tags.append('male on humanoid')
                    if ('taur' not in charCombo[i][0]) and ('taur' not in charCombo[i][1]):
                        if 'taur' in charCombo[i][1]:
                            tags.append('male on taur')
                if 'female' in charCombo[i][0]:
                    if 'male' in charCombo[i][1]:
                        tags.append('male/female')
                        while True:
                            print("Is " + charCombo[i][0][0] + " pegging " + charCombo[i][1][0] + "? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('pegging')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A female character wearing a strapon and using the sex toy to engage in anal sex with a receiving male character.")
                    if 'female' in charCombo[i][1]:
                        tags.append('female/female')
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('female/ambiguous')
                    if 'intersex' in charCombo[i][1]:
                        tags.append('intersex/female')
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('dickgirl/female')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('cuntboy/female')
                        if 'herm' in charCombo[i][1]:
                            tags.append('herm/female')
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('maleherm/female')
                    if ('anthro' not in charCombo[i][0]) and ('anthro' not in charCombo[i][1]):
                        if 'anthro' in charCombo[i][1]:
                            tags.append('female on anthro')
                    if ('feral' not in charCombo[i][0]) and ('feral' not in charCombo[i][1]):
                        if 'feral' in charCombo[i][1]:
                            tags.append('female on feral')
                    if ('human' not in charCombo[i][0]) and ('anthumanhro' not in charCombo[i][1]):
                        if 'human' in charCombo[i][1]:
                            tags.append('female on human')
                    if ('humanoid' not in charCombo[i][0]) and ('humanoid' not in charCombo[i][1]):
                        if 'humanoid' in charCombo[i][1]:
                            tags.append('female on humanoid')
                    if ('taur' not in charCombo[i][0]) and ('taur' not in charCombo[i][1]):
                        if 'taur' in charCombo[i][1]:
                            tags.append('female on taur')
                if 'ambiguous gender' in charCombo[i][0]:
                    if 'male' in charCombo[i][1]:
                        tags.append('male/ambiguous')
                    if 'female' in charCombo[i][1]:
                        tags.append('female/ambiguous')
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('ambiguous/ambiguous')
                    if 'intersex' in charCombo[i][1]:
                        tags.append('intersex/ambiguous')
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('dickgirl/ambiguous')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('cuntboy/ambiguous')
                        if 'herm' in charCombo[i][1]:
                            tags.append('herm/ambiguous')
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('maleherm/ambiguous')
                    if ('anthro' not in charCombo[i][0]) and ('anthro' not in charCombo[i][1]):
                        if 'anthro' in charCombo[i][1]:
                            tags.append('ambiguous on anthro')
                    if ('feral' not in charCombo[i][0]) and ('feral' not in charCombo[i][1]):
                        if 'feral' in charCombo[i][1]:
                            tags.append('ambiguous on feral')
                    if ('human' not in charCombo[i][0]) and ('human' not in charCombo[i][1]):
                        if 'human' in charCombo[i][1]:
                            tags.append('ambiguous on human')
                    if ('humanoid' not in charCombo[i][0]) and ('humanoid' not in charCombo[i][1]):
                        if 'humanoid' in charCombo[i][1]:
                            tags.append('ambiguous on humanoid')
                    if ('taur' not in charCombo[i][0]) and ('taur' not in charCombo[i][1]):
                        if 'taur' in charCombo[i][1]:
                            tags.append('ambiguous on taur')
                if 'intersex' in charCombo[i][0]:
                    if ('anthro' not in charCombo[i][0]) and ('anthro' not in charCombo[i][1]):
                        if 'anthro' in charCombo[i][1]:
                            tags.append('intersex on anthro')
                    if ('feral' not in charCombo[i][0]) and ('feral' not in charCombo[i][1]):
                        if 'feral' in charCombo[i][1]:
                            tags.append('intersex on feral')
                    if ('human' not in charCombo[i][0]) and ('human' not in charCombo[i][1]):
                        if 'human' in charCombo[i][1]:
                            tags.append('intersex on human')
                    if ('humanoid' not in charCombo[i][0]) and ('humanoid' not in charCombo[i][1]):
                        if 'humanoid' in charCombo[i][1]:
                            tags.append('intersex on humanoid')
                    if ('taur' not in charCombo[i][0]) and ('taur' not in charCombo[i][1]):
                        if 'taur' in charCombo[i][1]:
                            tags.append('intersex on taur')
                if 'dickgirl' in charCombo[i][0]:
                    if 'male' in charCombo[i][1]:
                        tags.append('dickgirl/male')
                    if 'female' in charCombo[i][1]:
                        tags.append('dickgirl/female')
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('dickgirl/ambiguous')
                    if 'intersex' in charCombo[i][1]:
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('dickgirl/dickgirl')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('dickgirl/cuntboy')
                        if 'herm' in charCombo[i][1]:
                            tags.append('dickgirl/herm')
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('maleherm/dickgirl')
                if 'cuntboy' in charCombo[i][0]:
                    if 'male' in charCombo[i][1]:
                        tags.append('cuntboy/male')
                    if 'female' in charCombo[i][1]:
                        tags.append('cuntboy/female')
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('cuntboy/ambiguous')
                    if 'intersex' in charCombo[i][1]:
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('dickgirl/cuntboy')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('cuntboy/cuntboy')
                        if 'herm' in charCombo[i][1]:
                            tags.append('herm/cuntboy')
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('maleherm/cuntboy')
                if 'herm' in charCombo[i][0]:
                    if 'male' in charCombo[i][1]:
                        tags.append('herm/male')
                    if 'female' in charCombo[i][1]:
                        tags.append('herm/female')
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('herm/ambiguous')
                    if 'intersex' in charCombo[i][1]:
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('dickgirl/herm')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('herm/cuntboy')
                        if 'herm' in charCombo[i][1]:
                            tags.append('herm/herm')
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('maleherm/herm')
                if 'maleherm' in charCombo[i][0]:
                    if 'male' in charCombo[i][1]:
                        tags.append('maleherm/male')
                    if 'female' in charCombo[i][1]:
                        tags.append('maleherm/female')
                    if 'ambiguous gender' in charCombo[i][1]:
                        tags.append('maleherm/ambiguous')
                    if 'intersex' in charCombo[i][1]:
                        if 'dickgirl' in charCombo[i][1]:
                            tags.append('maleherm/dickgirl')
                        if 'cuntboy' in charCombo[i][1]:
                            tags.append('maleherm/cuntboy')
                        if 'herm' in charCombo[i][1]:
                            tags.append('maleherm/herm')
                        if 'maleherm' in charCombo[i][1]:
                            tags.append('maleherm/maleherm')
                break
            if yesNo == 'no':
                break
    
    #===========================================================================
    # Penetrating / Penetrated
    #===========================================================================
    charCombo = list(itertools.combinations(charList, 2))
    charPermu = list(itertools.permutations(charList, 2))
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " penetrating another character? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('penetration')
                if 'male' in charList[i]:
                    charList[i].append('male penetrating')
                if 'female' in charList[i]:
                    charList[i].append('female penetrating')
                if 'ambiguous gender' in charList[i]:
                    charList[i].append('ambiguous penetrating')
                if 'intersex' in charList[i]:
                    charList[i].append('intersex penetrating')
                    if 'dickgirl' in charList[i]:
                        charList[i].append('dickgirl penetrating')
                    if 'cuntboy' in charList[i]:
                        charList[i].append('cuntboy penetrating')
                    if 'herm' in charList[i]:
                        charList[i].append('herm penetrating')
                    if 'maleherm' in charList[i]:
                        charList[i].append('maleherm penetrating')
                if 'anthro' in charList[i]:
                    charList[i].append('anthro penetrating')
                if 'feral' in charList[i]:
                    charList[i].append('feral penetrating')
                if 'human' in charList[i]:
                    charList[i].append('human penetrating')
                if 'humanoid' in charList[i]:
                    charList[i].append('humanoid penetrating')
                if 'taur' in charList[i]:
                    charList[i].append('taur penetrating')               
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("All cases where a penis, tail, or object (dildo, aeroplane, etc.) is put into a character's body (anal, vaginal, oral) for sexual purposes.")
        while True:
            print("Is " + charList[i][0] + " being penetrated? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('penetration')
                if 'male' in charList[i]:
                    charList[i].append('male penetrated')
                if 'female' in charList[i]:
                    charList[i].append('female penetrated')
                if 'ambiguous gender' in charList[i]:
                    charList[i].append('ambiguous penetrated')
                if 'intersex' in charList[i]:
                    charList[i].append('intersex penetrated')
                    if 'dickgirl' in charList[i]:
                        charList[i].append('dickgirl penetrated')
                    if 'cuntboy' in charList[i]:
                        charList[i].append('cuntboy penetrated')
                    if 'herm' in charList[i]:
                        charList[i].append('herm penetrated')
                    if 'maleherm' in charList[i]:
                        charList[i].append('maleherm penetrated')
                if 'anthro' in charList[i]:
                    charList[i].append('anthro penetrated')
                if 'feral' in charList[i]:
                    charList[i].append('feral penetrated')
                if 'human' in charList[i]:
                    charList[i].append('human penetrated')
                if 'humanoid' in charList[i]:
                    charList[i].append('humanoid penetrated')
                if 'taur' in charList[i]:
                    charList[i].append('taur penetrated')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("All cases where a penis, tail, or object (dildo, aeroplane, etc.) is put into a character's body (anal, vaginal, oral) for sexual purposes.")     
    
    #===========================================================================
    # X Penetrating Y
    #===========================================================================
    charCombo = list(itertools.combinations(charList, 2))
    charPermu = list(itertools.permutations(charList, 2))
    for i in range(len(charPermu)):
        if ('penetration' in charPermu[i][0]) and ('penetration' in charPermu[i][1]):
            while True:
                print("Is " + charPermu[i][0][0] + " penetrating " + charPermu[i][1][0] + "? (yes/no)")
                yesNo = input()
                if yesNo == 'yes':
                    if 'anthro penetrating' in charPermu[i][0]:
                        if 'anthro penetrated' in charPermu[i][1]:
                            tags.append('anthro penetrating anthro')
                        if 'feral penetrated' in charPermu[i][1]:
                            tags.append('anthro penetrating feral')  
                        if 'human penetrated' in charPermu[i][1]:
                            tags.append('anthro penetrating human')
                        if 'humanoid penetrated' in charPermu[i][1]:
                            tags.append('anthro penetrating humanoid')
                        if 'taur penetrated' in charPermu[i][1]:
                            tags.append('anthro penetrating taur')     
                    if 'feral penetrating' in charPermu[i][0]:
                        if 'anthro penetrated' in charPermu[i][1]:
                            tags.append('feral penetrating anthro')
                        if 'feral penetrated' in charPermu[i][1]:
                            tags.append('feral penetrating feral')  
                        if 'human penetrated' in charPermu[i][1]:
                            tags.append('feral penetrating human')
                        if 'humanoid penetrated' in charPermu[i][1]:
                            tags.append('feral penetrating humanoid')
                        if 'taur penetrated' in charPermu[i][1]:
                            tags.append('feral penetrating taur')  
                    if 'human penetrating' in charPermu[i][0]:
                        if 'anthro penetrated' in charPermu[i][1]:
                            tags.append('human penetrating anthro')
                        if 'feral penetrated' in charPermu[i][1]:
                            tags.append('human penetrating feral')  
                        if 'human penetrated' in charPermu[i][1]:
                            tags.append('human penetrating human')
                        if 'humanoid penetrated' in charPermu[i][1]:
                            tags.append('human penetrating humanoid')
                        if 'taur penetrated' in charPermu[i][1]:
                            tags.append('human penetrating taur')  
                    if 'humanoid penetrating' in charPermu[i][0]:
                        if 'anthro penetrated' in charPermu[i][1]:
                            tags.append('humanoid penetrating anthro')
                        if 'feral penetrated' in charPermu[i][1]:
                            tags.append('humanoid penetrating feral')  
                        if 'human penetrated' in charPermu[i][1]:
                            tags.append('humanoid penetrating human')
                        if 'humanoid penetrated' in charPermu[i][1]:
                            tags.append('humanoid penetrating humanoid')
                        if 'taur penetrated' in charPermu[i][1]:
                            tags.append('humanoid penetrating taur')    
                    if 'taur penetrating' in charPermu[i][0]:
                        if 'anthro penetrated' in charPermu[i][1]:
                            tags.append('taur penetrating anthro')
                        if 'feral penetrated' in charPermu[i][1]:
                            tags.append('taur penetrating feral')  
                        if 'human penetrated' in charPermu[i][1]:
                            tags.append('taur penetrating human')
                        if 'humanoid penetrated' in charPermu[i][1]:
                            tags.append('taur penetrating humanoid')
                        if 'taur penetrated' in charPermu[i][1]:
                            tags.append('taur penetrating taur')                                    
                    break
                if yesNo == 'no':
                    break
    #===========================================================================
    # Stuff being penetrated
    #===========================================================================
    for i in range(len(charList)):
        if 'penetration' in charList[i]:
            while True:
                print("Is " + charList[i][0] + " being penetrated by two objects or penises at the same time? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('double penetration')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A character who is being penetrated by a combination of 2 routes (oral, vaginal, or anal) all at the same time. This can be from any combination of sex and objects.")
            while True:
                print("Is " + charList[i][0] + " being penetrated by three objects or penises at the same time? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('triple penetration')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("This tag refers to a character who is being penetrated by three of any combination of penises or objects.")
            if 'anus' in charList[i]:
                while True:
                    print("Is " + charList[i][0] + "'s anus being penetrated? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('anal penetration')
                        charList[i].append('anal')
                        if 'double penetration' in charList[i]:
                            while True:
                                print("Is " + charList[i][0] + "'s anus being penetrated by two objects or penises? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('double anal')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("This tag refers to a character who is being anally penetrated by 2 objects or penises.")
                        if 'triple penetration' in charList[i]:
                            while True:
                                print("Is " + charList[i][0] + "'s anus being penetrated by three objects or penises? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('triple anal')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("This tag refers to a character who is being anally penetrated by 3 objects or penises.")
                        if 'dildo' in charList[i]:
                            while True:
                                print("Is " + charList[i][0] + "'s anus being penetrated by a dildo? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('dildo in ass')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("When a character has a dildo in their ass.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character who is being penetrated anally. This can be from any combination of sex and objects.")
            if 'pussy' in charList[i]:
                while True:
                    print("Is " + charList[i][0] + "'s pussy being penetrated? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('vaginal penetration')
                        charList[i].append('vaginal')
                        if 'cervix' in charList[i]:
                            while True:
                                print("Is " + charList[i][0] + "'s cervix being penetrated? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('cervical penetration')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("Where a penis or other object penetrates past the cervix and into the womb.")
                        if 'double penetration' in charList[i]:
                            while True:
                                print("Is " + charList[i][0] + "'s pussy being penetrated by two objects or penises? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('double vaginal')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("This tag refers to a character who is being vaginally penetrated by 2 objects or penises.")
                        if 'triple penetration' in charList[i]:
                            while True:
                                print("Is " + charList[i][0] + "'s pussy being penetrated by three objects or penises? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('triple vaginal')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("This tag refers to a character who is being vaginally penetrated by 3 objects or penises.")  
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character whose pussy is being penetrated. Penises are the most common, although tentacles, tails, and strapon dildos all qualify for this tag when used in such a manner, as well as the occasional enlarged clitoris.")
            while True:
                print("Is " + charList[i][0] + "'s mouth being penetrated? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('oral penetration')
                    charList[i].append('oral')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("This tag is used when someone or somethings mouth is being penetrated. Same usage as vaginal_penetration or anal_penetration.")
            if ('oral penetration' in charList[i]) and ('vaginal penetration' in charList[i]) and ('anal penetration' in charList[i]):
                while True:
                    print("Are " + charList[i][0] + "'s mouth, pussy, and anus being penetrated at the same time? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('all three filled')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Tagged when a character is being penetrated orally, vaginally, and anally all at the same time. This can be from any combination of penises or objects.")
            while True:
                print("Can you not tell what of " + charList[i][0] + " being penetrated? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('ambiguous penetration')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Sometimes it's not entirely clear whether the image depicts anal_penetration or vaginal_penetration.")
    #===========================================================================
    # Fingering
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " fingering themself or another character? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('fingering')
                # TODO: Other fingerings?
                while True:
                    print("Is " + charList[i][0] + " fingering themself? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('fingering self')
                        charList[i].append('masturbation')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character is fingering themself.")
                while True:
                    print("Is " + charList[i][0] + " fingering another character? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('fingering partner')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When one character of a post is fingering another character.")
                while True:
                    print("Is " + charList[i][0] + " fingering a pussy? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('vaginal fingering')
                        charList[i].append('vaginal')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character inserting fingers into the pussy (but not all of them, because that would be vaginal_fisting).")
                while True:
                    print("Is " + charList[i][0] + " fingering an anus? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('anal fingering')
                        charList[i].append('anal')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character sexually stimulating either themselves or someone else by inserting one or more fingers into their anus.")
                while True:
                    print("Is " + charList[i][0] + " fingering a urethra? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('urethral fingering')
                        charList[i].append('urethral')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Fingering of the urethra.")
                while True:
                    print("Is " + charList[i][0] + " fingering a nipple? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('nipple fingering')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("fingers are going into the nipple")
                while True:
                    print("Is " + charList[i][0] + " fingering a cloaca? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('cloacal fingering')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character inserting fingers into the cloaca (but not all of them, because that would be cloacal_fisting).")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Inserting the fingers into an orifice. Typically the anus or pussy.")
    #===========================================================================
    # Sucking
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " sucking something? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('sucking')
                if 'breasts' in tags:
                    while True:
                        print("Is " + charList[i][0] + " sucking on someone's breasts? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('breast suck')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Use this when a character is sucking any part of the breasts, including the nipples. This may involve grabbing and squeezing. If things escalate to the point of drinking in lactating milk, then add the tag breastfeeding as well.")
                while True:
                    print("Is " + charList[i][0] + " sucking on a thumb? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('thumb suck')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character is sucking the thumb, often their own. This is usually seen in very young children, but it may happen in older characters in certain circumstances.")
                while True:
                    print("Is " + charList[i][0] + " sucking on someone's balls? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('ball suck')
                        charList[i].append('sex')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("This applies when a character uses their mouth to suck on somebody's balls. Fairly self-explanatory.")
                while True:
                    print("Is " + charList[i][0] + " sucking on toes? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('toe suck')
                        charList[i].append('foot fetish')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character is sucking the toes, seen as a form of foot fetish.")
                while True:
                    print("Is " + charList[i][0] + " sucking on nipples? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('nipple suck')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Use this when characters suck on nipples, be it on another character's body or on themselves.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When a character is sucking something. While this might technically include things like popsicles, most often this will include some sort of body part. Note that for tagging purposes, fellatio should not be tagged with sucking.")
    #===========================================================================
    # Posture
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " standing up? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('standing')
                while True:
                    print("Is " + charList[i][0] + " standing on one leg? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('on one leg')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("The character is standing with one foot in contact with the ground, and the other raised off the ground with the foot supporting no weight.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Images or Animations in which a character is held upright and supported on their legs and feet. This can be applied to both Bipedal and Quadrupedal characters.")
        while True:
            print("Is " + charList[i][0] + " bent over? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('bent over')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When a character is leaning over at a right angle with their back bent and legs straight. Characters who are bent over can sometimes be engaged in sex, such as with the from_behind_position.")
        while True:
            print("Is " + charList[i][0] + " sitting? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('sitting')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Images or Animations which show a character at rest, supported by the buttocks or thighs where the torso is more or less upright.")
        while True:
            print("Is " + charList[i][0] + " crouching? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('crouching')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Resting only on the feet (rather than on the butt or legs) while bent at the knees. Characters who are crouching can be engaged in sexual activity, such as with the doggystyle or cowgirl position.")
        while True:
            print("Is " + charList[i][0] + " kneeling? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('kneeling')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When a character's knee(s) touch the ground or other surface beneath them, usually balancing with their feet.")
        while True:
            print("Is " + charList[i][0] + " on all fours? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('all four')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A position in which both sets of limbs are resting against the ground. Basically the way a non-humanoid or feral animals usually stands.")
        while True:
            print("Is " + charList[i][0] + " lying? (not telling a lie) (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('lying')
                while True:
                    print("Is " + charList[i][0] + " lying on their back? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('on back')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Images or animations in which a character is shown lying on their back, sometimes with their arms and elbows supporting them.")
                while True:
                    print("Is " + charList[i][0] + " lying on their side? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('on side')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Images or Animations in which a character is resting on the narrow width of their body, sometimes supported upright on their arm, or the surface underneath. ")
                while True:
                    print("Is " + charList[i][0] + " lying on their front? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('on front')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character is lying on their belly.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When a character is more or less horizontal and supported along its length by the surface underneath.")
        while True:
            print("Is " + charList[i][0] + "'s ass up? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('ass up')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("An elevated, in relation to the rest of the body, posterior. Commonly used to describe the position in which a character lays their chest on the ground while they raise their ass up into the air, kneeling or even standing with their legs (or hind legs in the case of feral or taur characters), typically in a presenting pose, but not always.")
        while True:
            print("Are more than one of " + charList[i][0] + "'s legs raised? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('legs up')
                while True:
                    print("Are " + charList[i][0] + "'s legs behind their head? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('legs behind head')
                        charList[i].append('flexible')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("As the tag suggests, when a character has their legs behind their head to expose their hindquarters.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Images with this tag contain a character or characters who have their legs above the waist and/or stretched up into the air.")
        while True:
            print("Is " + charList[i][0] + "'s leg raised? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('raised leg')
                while True:
                    print("Does " + charList[i][0] + " have one leg raised? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('one leg up')
                        while True:
                            print("Is " + charList[i][0] + " doing vertical splits? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('vertical splits')
                                charList[i].append('splits')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A form of splits that involves one leg pointing upwards and another leg pointing downwards. A character might achieve this position while standing or while suspended by an outside force such as a partner, or rope.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A position in which a character has one leg up. It can be in positions such as standing or lying on bed. predominantly characterized by the raised_leg being pointed upwards and having an unbent or mostly unbent knee. when done in a standing position this commonly becomes a form of splits.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Images or Animations in which a character's leg is raised up or away from the body, usually revealing genitalia. ")
        while True:
            print("Is " + charList[i][0] + " reclining? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('reclining')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A position in which a person is sitting, but lounging backwards casually, often supported by a raised surface or their arms.")
        while True:
            print("Does " + charList[i][0] + " have their arms crossed? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('crossed arms')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When a character has their arms crossed with one over the other. This can be either a general pose or something related to a unique sexual position or bondage situation.")
        while True:
            print("Does " + charList[i][0] + " have their legs crossed? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('crossed legs')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("When a character has their legs crossed with one over the other. Characters who have their legs crossed can be relaxing, making a pose, or having sex. Sexual positions that can feature a character with their legs crossed include missionary position and cowgirl position.")
        while True:
            print("Does " + charList[i][0] + " have their arm raised? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('raised arm')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Images or Animations in which a character's arm is raised above or away from the body.")
        while True:
            print("Does " + charList[i][0] + " have one hand behind their head? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('hand behind head')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("An image where one or more characters has one hand behind their head.")
        while True:
            print("Does " + charList[i][0] + " have both hands behind their head? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('hands behind head')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("An image where one or more characters have both hands behind their head.")
    #===========================================================================
    # Actions
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " grabbing another's arm? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('arm grab')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Used to denote a character grabbing the arm(s) of another character.")
        while True:
            print("Is " + charList[i][0] + " spreading parts of their body? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('spreading')
                if 'pussy' in charList[i]:
                    while True:
                        print("Is " + charList[i][0] + " spreading their pussy? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('spread pussy')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Where a character is spreading apart the lips of a pussy. This may be a form of presenting or inviting.")
                while True:
                    print("Is " + charList[i][0] + " spreading their legs? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('spread legs')
                        while True:
                            print("Is " + charList[i][0] + " doing splits? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('splits')
                                if 'one leg up' in charList[i]:
                                    while True:
                                        print("Is " + charList[i][0] + " doing vertical splits? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('vertical splits')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("A form of splits that involves one leg pointing upwards and another leg pointing downwards. A character might achieve this position while standing or while suspended by an outside force such as a partner, or rope.")
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Splits (also referred to as the splits) is a physical position in which the legs are in line with each other and extended in opposite directions.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Where a character has their legs spread apart. This may be a form of presenting or inviting.")
                if 'anus' in charList[i]:
                    while True:
                        print("Is " + charList[i][0] + " spreading their anus? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('spread anus')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Where a character is spreading open an anus. This may be a form of presenting or inviting. Not to be confused with gaping_anus.")
                if 'butt' in charList[i]:
                    while True:
                        print("Is " + charList[i][0] + " spreading their butt? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('spread butt')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Where a character is spreading apart one or both of their own or another character's buttocks. This may be a form of presenting or inviting.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Images with this tag feature a character who is, or has someone else, or a device spreading their legs, pussy lips, butt cheeks apart, or their anus open. ")
    #===========================================================================
    # Sex toys
    #===========================================================================
    while True:
        print("Are there sex toys in the image? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('sex toy')
            while True:
                print("Is a character using a sex toy on another? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('toying partner')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("When one character sexually stimulates another character with a sex toy. Do not tag with masturbation.")
            while True:
                print("Are there anal beads in the image? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('anal beads')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sex toy consisting of a number of round beads on a string that are specifically designed to pleasure the anus.")
            while True:
                print("Is there a dildo in the image? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('dildo')
                    # TODO: Kinds of dildos
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A phallic sex toy designed to look and feel like a penis. It is used primarily for penetrative sex and masturbation.")
            while True:
                print("Is there a vibrator in the image? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('vibrator')
                    # TODO: Kinds of vibrators
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Images or animations depicting characters using vibrators, dildos fitted with vibration units, to create additional stimulation during masturbation.")
            while True:
                print("Is there a butt plug in the image? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('buttplug')
                    while True:
                        print("Is there a buttplug tail in the image? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('buttplug tail')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A type of butt plug that has an artificial tail (most commonly equine, feline, or vulpine) attached to the actual plug, so that when it is inserted into a character's anus, they appear to have a tail. ")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sex toy specifically designed to be inserted into the anus. The shape of the toy makes it difficult for the plug to be accidentally dislodged and can be 'worn' for long periods of time.")
            while True:
                print("Is there a penetrable sex toy in the image? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('penetrable sex toy')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A penetrable_sex_toy (Fleshlight, Tenga, breeding_mount) is a synthetic device designed to simulate sex. It can be shaped to look or feel like a pussy, anus, or something else entirely.")
            while True:
                print("Is there a Sybian in the image? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('sybian')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A mechanical sex toy designed for penetrative masturbation. It consists of a large round saddle-like device that can vibrate and be fitted with a variety of dildos and other sex toys. The character mounts and straddles it vaguely the same as if horseriding, hence why it is sometimes called a Sybian saddle.")
            while True:
                print("Is there a strapped in toy in the image? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('strapped in toy')
                    while True:
                        print("Is there a strapped in dildo in the image?")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('strapped in dildo')
                            charList[i].append('dildo')
                            break
                        if yesNo == 'no':
                            break
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A special harness with a sex toy built onto it that penetrates one of the orifices, and cannot be pulled out except for taking off the harness. ")
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("An object or device designed for genital or anal stimulation. The most common type is the dildo, an artificial penis, but there are many other varieties available.")
    
    #===========================================================================
    # Masturbation
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " masturbating? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('masturbation')
                while True:
                    print("Is " + charList[i][0] + " fisting themself? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('autofisting')
                        charList[i].append('fisting')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("The insertion of a character's entire hand into their own anus, pussy, or cloaca.")
                while True:
                    print("Is " + charList[i][0] + " masturbating anally? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('anal masturbation')
                        charList[i].append('anal')
                        while True:
                            print("Is " + charList[i][0] + " rimming their own anus? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('autorimming')
                                charList[i].append('oral masturbation')
                                charList[i].append('oral')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character masturbating by sexually stimulating their own anus, whether through anal fingering or with a sex toy.")
                while True:
                    print("Is " + charList[i][0] + " penetrating themself using their penis or tail? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('autopenetration')
                        charList[i].append('penetration')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("All cases where a character's penis or tail or is inserted into their own body (anal, vaginal, cloaca, urethral, cervical).")
                while True:
                    print("Is " + charList[i][0] + " giving themself a footjob? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('autofootjob')
                        charList[i].append('foot fetish')
                        while True:
                            print("Is " + charList[i][0] + " giving themself a two-footed footjob? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('two-footed autofootjob')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("The act of giving oneself a footjob, with both feet.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("The act of giving oneself a footjob.")
                if ('dickgirl' in charList[i]) or ('herm' in charList[i]):
                    while True:
                        print("Is " + charList[i][0] + " titfucking themself? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('autotitfuck')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A character using their own penis to titfuck themselves, considered to be a form of masturbation.")
                while True:
                    print("Is " + charList[i][0] + " using their tail to masturbate? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('tail masturbation')
                        while True:
                            print("Is " + charList[i][0] + " giving themself a tailjob? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('autotailjob')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("The same as a tailjob, only used for when a character does it to themselves.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A form of masturbation that involves a character's own tail.")
                if ('female' in charList[i]) or ('cuntboy' in charList[i]) or ('herm' in charList[i]) or ('maleherm' in charList[i]):
                    while True:
                        print("Is " + charList[i][0] + " masturbating vaginally? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('vaginal masturbation')
                            charList[i].append('vaginal')
                            while True:
                                print("Is " + charList[i][0] + " performing cunnilingus on themself? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('autocunnilingus')
                                    charList[i].append('oral masturbation')
                                    charList[i].append('oral')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("A form of masturbation where a character's mouth or tongue is used to stimulate their own pussy and clitoris. ")
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Self-stimulation of the pussy.")
                if ('sex toy' in tags) or ('improvised sex toy' in tags):
                    while True:
                        print("Is " + charList[i][0] + " using a sex toy to masturbate? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('toying self')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("This tag is added when a character is using a sex toy to masturbate.")
                if ('male' in charList[i]) or ('dickgirl' in tags) or ('herm' in tags) or ('maleherm' in tags):
                    while True:
                        print("Is " + charList[i][0] + " masturbating their penis? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('penile masturbation')
                            if 'multi penis' in charList[i]:
                                while True:
                                    print("Is " + charList[i][0] + " masturbating by rubbing their penises together? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        charList[i].append('autofrottage')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("A form of masturbation where a character with more than one penis rubs them together.")
                            while True:
                                print("Is " + charList[i][0] + " licking their own penis? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('auto penis lick')
                                    charList[i].append('oral masturbation')
                                    charList[i].append('oral')
                                    charList[i].append('licking')
                                    charList[i].append('tongue out')
                                    charList[i].append('tongue')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("This tag is used when a character in the post is licking their own penis.")
                            while True:
                                print("Is " + charList[i][0] + " giving themself a tonguejob? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('autotonguejob')
                                    charList[i].append('tongue out')
                                    charList[i].append('tongue')
                                    charList[i].append('long tongue')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("Penile masturbation where a character's long and likely prehensile tongue stimulates their own penis.")
                            while True:
                                print("Is " + charList[i][0] + " using their mouth to stimulate their own penis? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('autofellatio')
                                    charList[i].append('oral masturbation')
                                    charList[i].append('oral')
                                    while True:
                                        print("Is " + charList[i][0] + " being forced to perform oral on themself? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            charList[i].append('forced autofellatio')
                                            charList[i].append('forced')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("A character being forced to perform oral on themselves.")
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("")
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Self-stimulation of the penis with the hands.")
                while True:
                    print("Is " + charList[i][0] + " fingering themself? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('fingering self')
                        charList[i].append('fingering')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character is fingering themself.")
                while True:
                    print("Is " + charList[i][0] + " masturbating with other characters? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        tags.append('group masturbation')
                        while True:
                            print("Is a group of characters circlejerking? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('circlejerk')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A group of males masturbating ('jerking off') together (with or without interpersonal contact).")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When two or more characters are masturbating together without stimulating each other.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("All cases where a character is sexually stimulating themselves (penis, balls, anus, pussy, urethra, or cloaca).")
    
    
    
    #===========================================================================
    # Sex acts
    #===========================================================================
    if len(charList) >= 2:
        while True:
            print("Are any characters having sex?")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('sex')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Images or animations depicting any kind of sexual activity between two or more characters of any description.") 
    if 'sex' in tags:
        if 'clothed' in tags:
            while True:
                print("Are clothed characters having sex? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('clothed sex')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("This tag is added when there is a character in the post who is having sex and is not nude.")
        if 'group' in tags:
            while True:
                print("Are more than two characters engaging in sexual activities at the same time? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('group sex')
                    while True:
                        print("Is there a threesome? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            tags.append('threesome')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Images or animations depicting three characters, of any combination of genders, engaging in mutual sexual activity.")
                    if len(charList) >= 4:
                        while True:
                            print("Is there a foursome? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('foursome')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A post that depicts four characters engaged in sexual activity. The characters can be of any gender.")
                        while True:
                            print("Is a group of characters actively having sex with one character? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('gangbang')
                                while True:
                                    print("Is one character actively having sex with a group of people? (yes/no/?)")
                                    yesNo = input()
                                    if yesNo == 'yes':
                                        tags.append('reverse gangbang')
                                        break
                                    if yesNo == 'no':
                                        break
                                    if yesNo == '?':
                                        print("A type of gangbang where one character is having sex with a group of characters.")
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A form of group sex where three or more individuals are having sex with a single character, either sequentially or all at once.")
                    if len(charList) >= 5:
                        while True:
                            print("Is there an orgy with at least five characters? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('orgy')
                                if 'large group' in tags:
                                    while True:
                                        print("Is there an orgy with at least ten characters? (yes/no/?)")
                                        yesNo = input()
                                        if yesNo == 'yes':
                                            tags.append('mass orgy')
                                            break
                                        if yesNo == 'no':
                                            break
                                        if yesNo == '?':
                                            print("Tagged for large orgies that have minimum of ten participants.")
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Five or more characters having sex freely among each other in various combinations, often through 'chains' of partners.")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Images or animations depicting more than two characters engaging in sexual activities simultaneously. The 'group sex' tag specifically refers to groups of people all having sex in the same place, but not necessarily all together.") 
        if ('male' in tags) or ('dickgirl' in tags) or ('herm' in tags) or ('maleherm' in tags):
            while True:
                print("Is a character giving another a handjob? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('handjob')
                    if len(charList) >= 3:
                        while True:
                            print("Is a character giving a handjob to two different characters at the same time? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('double handjob')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("The act of giving a handjob to two different characters at once by a single character with one penis in each hand.")
                        while True:
                            print("Are multiple characters giving a handjob to one character? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('collaborative handjob')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("When multiple characters are giving a handjob to one character at the same time.")
                    if len(charList) > 3:
                        while True:
                            print("Is a character giving a hanjob to more than two different characters at the same time? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('multi handjob')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Single character giving a handjob to more than two characters at once. Usually only possible with multiple_limbs.")
                    while True:
                        print("Is a character giving a two-handed hanjob? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            tags.append('two-handed handjob')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("When a character gives another character a handjob using both hands.")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Manual stimulation of someone else's penis by hand.")
            while True:
                print("Is a character giving another a footjob? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('footjob')
                    tags.append('foot fetish')
                    if len(charList) >= 3:
                        while True:
                            print("Is a character giving a footjob to more than one penis? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('double footjob')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("When a character is giving a footjob to more than one penis.")
                    while True:
                        print("Is a character using two feet to give a footjob? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            tags.append('two-footed footjob')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A single character using two feet to stimulate one penis.")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("When feet are used to stimulate another character's penis. Like a handjob, but with feet.")
            while True:
                print("Are two characters performing forttage? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('frottage')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sexual act, common in male/male imagery, in which two characters press and rub their erect penises together.")
        if ('female' in tags) or ('cuntboy' in tags) or ('herm' in tags) or ('maleherm' in tags):
            while True:
                print("Is a character using their foot on another's pussy for sexual stimulation? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('vaginal footjob')
                    tags.append('foot fetish')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Using a foot on another character's pussy for the purpose of sexual stimulation.")
            while True:
                print("Are two characters performing tribadism? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('tribadism')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Scissoring, tribbing; A sexual act, common in female/female imagery, in which two characters press and rub their pussy and clitoris together.")
        while True:
            print("Are two characters in from behind position? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('from behind position')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Sexual intercourse in which the penetrating character is situated behind the receiver.")
        while True:
            print("Are two characters in amazon position? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('amazon position')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A position which is essentially the bottom-on-top version of the piledriver or anvil position. The top is on their back with their legs brought up towards their chest, while the bottom straddles the bent legs and rides the penis, typically facing the top.")
        while True:
            print("Are two characters in an unusual position? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('unusual position')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Tagged for unusual sex positions that can only be described as unique or bizarre.")
        while True:
            print("Are two characters in cradle position? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('cradle position')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("This is a sex position in which a character is cradling another individual while doing some lewd activity, often involving giving them a handjob. While this usually includes breastfeeding (or some other kind of nipple suckling), lactation isn't required for the tag.")
        while True:
            print("Are two characters in deck chair position? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('deck chair position')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A sex position where both partners are reclining or lying down, in opposite directions.")
        while True:
            print("Are two characters in reverse amazon position? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('reverse amazon position')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("The top is on their back with their legs brought up towards their chest (or resting on top of the bottom's thighs), while the bottom straddles the bent legs and rides the penis, facing away from the top.")
        while True:
            print("Are two characters in t square position? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('t square position')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("This tag refers to one of two similar sex positions in which the top and bottom are positioned at a 90 degree angle.")
        while True:
            print("Are two characters in waterfall position? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                tags.append('waterfall position')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("A variant of the cowgirl position, where the penetrating partner's lower body is on a heightened surface, such as a bed or a couch.")
        if 'oral' in tags:
            if 'cloaca' in tags:
                while True:
                    print("Is a character performing oral on another with a cloaca?")
                    yesNo = input()
                    if yesNo == 'yes':
                        tags.append('cloacalingus')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Slang term for performing oral on a cloaca. Can be a male cloaca or a female cloaca, but this tag should not be used for fellatio on males that have a cloaca.")
            if ('female' in tags) or ('cuntboy' in tags) or ('herm' in tags) or ('maleherm' in tags):
                while True:
                    print("Is a character performing cunnilingus on another? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        tags.append('cunnilingus')
                        tags.append('vaginal')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A form of oral sex where a character's pussy or clitoris is stimulated using another character's mouth.") 
                if len(charList) >= 3:
                    while True:
                        print("Are two or more characters performing cunnilingus on the same character? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            tags.append('collaborative cunnilingus')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("When 2 or more characters are performing cunnilingus on the same character.")
            if ('male' in tags) or ('dickgirl' in tags) or ('herm' in tags) or ('maleherm' in tags):
                while True:
                    print("Is a character performing fellatio (not irrumatio) on another? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        tags.append('fellatio')
                        if len(charList) >= 3:
                            while True:
                                print("Are two or more characters performing fellatio on the same character? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    tags.append('coolaborative fellatio')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("2 or more characters performing fellatio on the same character (even if on multi_penis characters).")
                        if len(charList) >= 2:    
                            while True:
                                print("Is a character performing fellatio on more than one penis at the same time")
                                yesNo = input()
                                if yesNo == 'yes':
                                    tags.append('double fellatio')
                                    tags.append('double oral')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("A character performing fellatio on more than one penis at the same time (includes multi_penis characters).")
                        if 'knotting' in tags:
                            while True:
                                print("Is a characters knot expanded in another's mouth during fellatio? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    tags.append('oral knotting')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("The insertion or expansion of the knot (usually a canine penis) during fellatio. Oral knotting is usually depicted by internal shots, or balls deep in combination with clearly bulging cheeks.")
                        if 'beak' in tags:
                            while True:
                                print("Is a character with a beak performing fellatio on another character? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    tags.append('beakjob')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("The beakjob tag is for cases where a character with a beak is giving fellatio.")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A form of oral sex where an individual uses their mouth and/or throat to stimulate the penis of another.")
                while True:
                    print("Is a character performing irrumatio (not fellatio) on another? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        tags.append('irrumatio')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A form of oral sex where an individual thrusts their penis into the mouth and/or throat of another.")
            if 'group sex' in tags:
                while True:
                    print("Are a group of characters in a daisy chain? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        tags.append('daisy chain')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A type of sex position which describes a group of characters each performing oral on the next.")
                if 'oral' in tags:
                    while True:
                        print("Are a group of characters in a spitroast? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            tags.append('spitroast')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A sex position where a character is orally and anally/vaginally penetrated at the same time. Usually this happens during a threesome.")
                    while True:
                        print("Are a group of characters in a reverse spitroast? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            tags.append('reverse spitroast')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Sex involving 3 or more characters, in which a middle character is penetrating another character while orally pleasuring a third one.")
            while True:
                print("Are two characters in 69 position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('69 position')
                    if 'standing' in tags:
                        while True:
                            print("Are two characters in standing 69 position? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('standing 69')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("A 69_position where one of the participants is standing, and supporting the other participant upside_down.")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sex position in which two characters align themselves so that each character's mouth is near the other's genitals, with one or both parties performing oral sex. ")
            while True:
                print("Is a character snout fucking another? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('snout fuck')
                    if 'beak' in tags:
                        while True:
                            print("Is a character, with a beak, snout fucking another? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('beak fuck')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("For use with sharp, pointy bird/squid beaks and the like")
                    while True:
                        print("Is a character, with a muzzle, snout fucking another? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            tags.append('muzzle fuck')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Use for dogs, cats, and the like, as opposed to beaks")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("When a character is rimming or performing cunnilingus on another character to the extreme point where part or all of the character's face is entering the pussy or anus.")
        if 'from behind position' in tags:
            if 'all fours' in tags:
                while True:
                    print("Are two characters in doggystyle position? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        tags.append('doggystyle')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Any sex position in which a person crouches on all fours and is stimulated sexually.")
                while True:
                    print("Are two characters in mounting position? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        tags.append('mounting')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Mounting is similar to doggystyle in that one character is down on all fours and being taken from behind. However, the character performing the penetration lays their body trunk on their partners back-or, if there is a significant size difference, parallel to the ground-rather than holding their body erect.")
            while True:
                print("Are two characters in chair position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('chair position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sex position where the Top is sitting up and the Bottom is sitting on top of them while facing away. Commonly also known as reverse mastery or lap dance position. ")
            while True:
                print("Are two characters in bodyguard position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('bodyguard position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A standing sex position where both partners are facing in the same direction.")
            while True:
                print("Are two characters in perching position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('perching position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A position where the top has, ideally, both feet off the ground and is perched on top of the bottom's rear and potentially using the bottom's rear or legs as support for their feet.")
            while True:
                print("Are two characters in jockey position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('jockey position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Rear entry sex position wherein the receiving partner is lying prone on front, while the penetrating partner does so while kneeling or crouching on top.")
            while True:
                print("Are two characters in wheelbarrow position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('wheelbarrow position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sexual position similar to doggystyle but with the Top holding the Bottom's legs off of the ground (like a wheelbarrow).")
            while True:
                print("Are two characters in speed bump position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('speed bump position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Rear entry sex position wherein the receiving partner is lying prone on front, while the penetrating partner lies on top.")
        if 'on top' in tags:
            while True:
                print("Are two characters in cowgirl position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('cowgirl position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sexual position in which the recipient of penetration is positioned on_top of the giver, facing toward their head while they lay on their back.")  
            while True:
                print("Are two characters in reverse cowgirl position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('reverse cowgirl position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("The cowgirl position, but with the bottom (the partner being penetrated, even though they're above the top) facing away from the top.")
            while True:
                print("Are two characters in mastery position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('mastery position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A face-to-face sexual position where the penetrated partner is seated on top of the penetrating partner, who is in turn seated or lightly reclining, such as on the edge of a bed, in a chair, or atop a stool.") 
            while True:
                print("Are two characters in lotus position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('lotus position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Position where one partner (commonly male) in a seated position crosses his legs in front of them. Their partner then sits in their lap facing them, with either or both of their arms and legs around the other person.")
        if 'on back' in tags:
            while True:
                print("Are two characters in missionary position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('missionary position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A vanilla sex position where one character lays on their back while spreading their legs to allow another character to penetrate them face-to-face. Also tagged for non-penetrative sex done in this position, such as grinding and tribadism.")
            while True:
                print("Are two characters in table lotus position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('table lotus position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Lotus_position in which the receiving partner is lying on their back on a surface (such as a table, kitchen counter, bed) with their bottom level to the giving partner's waist.")
            while True:
                print("Are two characters in reverse missionary position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('reverse missionary position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A variant of the missionary position where the penetrating character is on the bottom instead of on top. If the penetrated character is sitting up, use cowgirl_position.")
            while True:
                print("Are two characters in bent spoon position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('bent spoon position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Sex position similar to spoon position, but with both partners lying on their back instead of on their side.")
        if 'standing' in tags:
            while True:
                print("Are two characters in stand and carry position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('stand and carry position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Sex that occurs when one party is carrying the other while standing. Some times done while against a wall. Often involves a leg_grab.") 
            while True:
                print("Are two characters in reverse wheelbarrow position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('reverse wheelbarrow position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A variant of the wheelbarrow position where the penetrated partner is facing upwards, towards their partner.")
        if 'legs up' in tags:
            while True:
                print("Are two characters in anvil position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sex position in which the person being penetrated has both legs up in front of their partner as they are being penetrated.") 
        if 'group sex' in tags:
            while True:
                print("Are a group of characters in train position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('train position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("The train position refers to a specific position where the participants form a line, front to back, and penetrate whoever is in front of them (anally or vaginally) much like the linked boxcars on a train. However, the last one being penetrated can be penetrated vaginally, anally, or orally.")
            while True:
                print("Are a group of characters in sandwich position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('sandwich position')
                    if 'bisexual' in tags:
                        while True:
                            print("Are a group of characters in a bisexual sandwich? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                tags.append('bisexual sandwich')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("Top: Male character, penetrating 'Middle', Middle: Male character, penetrating 'Bottom', Bottom: Female character being penetrated by 'Middle'")
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A type of sex position involving three participants: both penetrating partners are on the ends, both facing the middle partner. The one being penetrated is always between them in the middle, being penetrated by both (front and back partner). Penetration is always vaginal, anal or both at once, NOT oral. ")
            while True:
                print("Are a group of characters in triangle position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('triangle position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("The triangle position is a situation in which 3 characters of random genders engage in a position in which 1 (usually a male) is lying on their back whilst another character is sitting on or kneeling over their face and the last character sitting on or kneeling over their genitals")
            while True:
                print("Are a group of characters in 169 position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('169 position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A threesome position where two partners perform the 69 position while one of them is penetrated by a third.")
            while True:
                print("Are a group of people in 1691 position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('1691')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("1691 is a 4some position where two people '69' while two other people, one on either side, perform a sexual act to one of the two who are '69ing'.")
            while True:
                print("Are a group of characters in eiffel tower position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('eiffel tower position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("When one character is being penetrated orally and vaginally or anally at the same time, and the two penetrating participants are high-fiving or simply holding hands in a way to imitate a tower.")
            while True:
                print("Are a group of characters in totem pole position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('totem pole position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sexual position with the same premise as the chair position, except it involves a sequence of three (or more) individuals. The participants sit at each other's lap while being penetrated (either anally or vaginally), stacking themselves like a totem pole.")
        if 'raised leg' in tags:
            while True:
                print("Are two characters in leg glider position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('leg glider position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sex position where the Top is upright and the Bottom is usually on their side (or less commonly on back), with one leg raised up and the other leg either spread out or straddled by the Top.")
        if 'spooning' in tags:
            while True:
                print("Are two characters in spoon position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('spoon position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sexual position where both partners lie on their sides, the receiving partner having their back to the penetrating partner.")
        if 'arm grab' in tags:
            while True:
                print("Are two characters in prison guard position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('prison guard position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A position where the individual doing the penetration thrusts into their bent-over partner from behind while pulling their partner's arms back by the wrists.")
        if 'crouching' in tags:
            while True:
                print("Are two characters in piledriver position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('piledriver position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("The position is executed with the bottom partner lying neck down and bottom up with their legs bent over head, while the top partner stands above and inserts their penis or strapon straight downwards.")
            while True:
                print("Are two characters in reverse piledriver position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('reverse piledriver position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("When the bottom partner lies with their neck down and their bottom up with their legs bent over their head, and the top partner stands above and faces away from the bottom partner.")
            while True:
                print("Are two characters in squat position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('squat position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("A sex position in which one character is penetrated anally or vaginally from behind by another while they are crouching.")
        if 'kneeling' in tags:
            while True:
                print("Are two characters in arch position? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    tags.append('arch position')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Sex position where the receiver is in partial bridge position resting on the shoulders, with the partner in the kneeling position.")
    #===========================================================================
    # Fluids
    #===========================================================================
    while True:
        print("Is there precum in the image? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('precum')
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("Relatively small amounts of fluid that leak from the tip of the penis when a character is close to orgasm.")    
    
    if 'cum' not in tags:
        while True:
            print("Is there cum in the image? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('cum')
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("An informal spelling of 'come', which is a slang term for semen, a sperm-containing fluid released from the penis through the process of ejaculation, during the orgasm. ")
    while True:
        print("Is there pussy juice in the image? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('pussy juice')
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("Vaginal secretions; fluid naturally produced within the pussy. A sign of intense arousal, this fluid lubricates sexual intercourse. Usually seen within, on, or near a pussy and usually colorless.")
    while True:
        print("Is there saliva in the image? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('saliva')
            for i in range(len(charList)):
                while True:
                    print("Is " + charList[i][0] + " drooling? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('drooling')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Drooling, also known as driveling, slobbering, or, in a medical context, ptyalism, is when saliva flows outside the mouth.")
            while True:
                print("Is there a saliva string? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('saliva string')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("This tag is for images and animations that show a strand of saliva connecting a character's tongue to something else (for example, after a French kiss or oral sex).")
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("It is the watery and usually frothy substance produced in the mouths of humans and most other animals.")
    
    for i in range(len(charList)):
        while True:
            print("Is there cum inside of " + charList[i][0] + "? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('cum inside')
                if ('female' in charList[i]) or ('cuntboy' in charList[i]) or ('herm' in charList[i]) or ('maleherm' in charList[i]):
                    while True:
                        print("Is there cum in " + charList[i][0] + "'s pussy? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('cum in pussy')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("When a character has cum in their pussy. This may be during the actual orgasm or just after sex.")
                while True:
                    print("Is there cum in " + charList[i][0] + "'s ass? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('cum in ass')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Use this when a character has cum inside their anus, either during or directly after anal sex. If the cum is shown dripping out, then the tags cum drip and cum from ass also apply.")
                while True:
                    print("Is there cum in " + charList[i][0] + "'s mouth? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('cum in mouth')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character has cum in their mouth. This tag is frequently used with fellatio and autofellatio.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("Depictions of cum within an orifice such as a pussy, anus, mouth, etc. Often evident from semen leaking from the orifice, or seen in internal view.")
    
    #===========================================================================
    # Orgasms
    #===========================================================================
    for i in range(len(charList)):
        while True:
            print("Is " + charList[i][0] + " having an orgasm? (yes/no/?)")
            yesNo = input()
            if yesNo == 'yes':
                charList[i].append('orgasm')
                while True:
                    print("Is " + charList[i][0] + " ejaculating fluids? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('ejaculation')
                        if ('female' in charList[i]) or ('cuntboy' in charList[i]) or ('herm' in charList[i]) or ('maleherm' in charList[i]):
                            while True:
                                print("Is " + charList[i][0] + " in the process of ejaculating pussy juice? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('pussy ejaculation')
                                    charList[i].append('pussy juice')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("Squirting, gushing; the phenomenon where a character, at the beginning of a particularly powerful orgasm, ejects a liquid substance originating from the urethra and/or paraurethral ducts within the pussy.")
                        if ('male' in charList[i]) or ('dickgirl' in charList[i]) or ('herm' in charList[i]) or ('maleherm' in charList[i]):
                            while True:
                                print("Is " + charList[i][0] + " in the process of externally ejaculating cum? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('cumshot')
                                    charList[i].append('cum')
                                    if 'multi penis' in charList[i]:
                                        while True:
                                            print("Did " + charList[i][0] + " shoot two cumshots? (yes/no/?)")
                                            yesNo = input()
                                            if yesNo == 'yes':
                                                charList[i].append('double cumshot')
                                                break
                                            if yesNo == 'no':
                                                break
                                            if yesNo == '?':
                                                print("One character, two cumshots.")
                                        while True:
                                            print("Did " + charList[i][0] + "shoot multiple cumshots? (yes/no/?)")
                                            yesNo = input()
                                            if yesNo == 'yes':
                                                charList[i].append('multi cumshot')
                                                break
                                            if yesNo == 'no':
                                                break
                                            if yesNo == '?':
                                                print("Cumshots from multiple dicks")
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("A character in the process of ejaculating cum (the emphasis here is on shot).")
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Umbrella tag for all kinds of ejaculation, such as cumshot and pussy_ejaculation.")
                if ('male' in charList[i]) or ('dickgirl' in charList[i]) or ('herm' in charList[i]) or ('maleherm' in charList[i]):
                    while True:
                        print("Did " + charList[i][0] + " cum prematurely? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('premature ejaculation')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("An embarrassing condition which leads characters to reach orgasm far too quickly, bringing an abrupt end to the sex act without satisfying either partner.")
                    while True:
                        print("Did " + charList[i][0] + " cum when their partner didn't want to? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('unwanted cumshot')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A character ejaculating in a manner undesired by their partner.")
                    while True:
                        print("Did " + charList[i][0] + " ejaculate with direct stimulation of their penis? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('hands-free')
                            charList[i].append('cum')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("A character ejaculating without direct stimulation of their penis.")
                    while True:
                        print("Did " + charList[i][0] + " cum while being penetrated? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('cum while penetrated')
                            charList[i].append('cum')
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Anything that depicts a character ejaculating during anal penetration, whether via sex or use of a sex toy. Also applies to herms ejaculating while penetrated vaginally.")
                    while True:
                        print("Did " + charList[i][0] + "'s cum splatter? (yes/no/?)")
                        yesNo = input()
                        if yesNo == 'yes':
                            charList[i].append('cum splatter')
                            charList[i].append('cum')
                            while True:
                                print("Did " + charList[i][0] + " have a cum explosion? (yes/no/?)")
                                yesNo = input()
                                if yesNo == 'yes':
                                    charList[i].append('cum explosion')
                                    break
                                if yesNo == 'no':
                                    break
                                if yesNo == '?':
                                    print("An explosion of cum")
                            break
                        if yesNo == 'no':
                            break
                        if yesNo == '?':
                            print("Used when a character ejaculates so vigorously that the cum splatters out of the orifice or object that's being penetrated.")
                while True:
                    print("Did " + charList[i][0] + " have a wet dream? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('wet dream')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("When a character has an involuntary orgasm in their sleep.")
                while True:
                    print("Did " + charList[i][0] + " have a spontaneous orgasm? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('spontaneous orgasm')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("A character ejaculating without any apparent direct penile, vaginal, anal, or oral stimulation.")
                while True:
                    print("Did " + charList[i][0] + " have a forced orgasm? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('forced orgasm')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Pictures or animations where a character is made to orgasm against their will.")
                while True:
                    print("Did " + charList[i][0] + " have multiple orgasms? (yes/no/?)")
                    yesNo = input()
                    if yesNo == 'yes':
                        charList[i].append('multiple orgasms')
                        break
                    if yesNo == 'no':
                        break
                    if yesNo == '?':
                        print("Used to denote when an individual has multiple orgasms over a contiguous span of sexual activity, especially without a significant refractory period between orgasms.")
                if len(charList) >= 2:
                    if 'simultaneous orgasms' not in tags:
                        while True:
                            print("Are two or more characters having orgasms at the same time? (yes/no/?)")
                            yesNo = input()
                            if yesNo == 'yes':
                                charList[i].append('simultaneous orgasms')
                                break
                            if yesNo == 'no':
                                break
                            if yesNo == '?':
                                print("When two (or more) characters having sex together reach orgasm at the same time.")
                break
            if yesNo == 'no':
                break
            if yesNo == '?':
                print("The release of sexual tension through rhythmic and intensely pleasurable contractions of the muscles in and around the erogenous zones.")
    while True:
        print("Did any characters recently just finish having sex? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('after sex')
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("Images or animations which infers the characters shown have just had sex. Usually, cum is found on the characters who have had intercourse.")
    #===========================================================================
    # Sexual Themes
    #===========================================================================
    # TODO
    
    #===========================================================================
    # Medium
    #===========================================================================
    while True:
        print("Is this image a sketch? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('sketch')
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("A freehand drawing, not usually intended as a finished work. Most often, sketches are used to develop composition for an image and will be refined later through some variety of inking or lineart.")
    while True:
        print("Is this image line art? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('line art')
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("Line art is any image that consists of distinct straight and curved lines placed against a (usually plain) background, without gradations in shade (darkness) or hue (color) to represent two-dimensional or three-dimensional objects. Line art can use lines of different colors, although line art is usually monochromatic.")
    while True:
        print("Is this image monochrome? (yes/no/?)")
        yesNo = input()
        if yesNo == 'yes':
            charList[i].append('monochrome')
            while True:
                print("Does this image only use the colors black and white? (yes/no/?)")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('black and white')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("Monochrome Images or Animations which consist of only the colors Black and White. Usually seen on earlier versions of colored images.")
            while True:
                print("")
                yesNo = input()
                if yesNo == 'yes':
                    charList[i].append('')
                    break
                if yesNo == 'no':
                    break
                if yesNo == '?':
                    print("")
            break
        if yesNo == 'no':
            break
        if yesNo == '?':
            print("This tag is used for images or animations whose entire composition is only or almost only composed of just lines and shades of a single hue. The term is sometimes mixed up with restricted palette when the hues used are similar.")
    break
print(tags)