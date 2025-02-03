def musicSearch(method,request):
    returned = []


    # Open the file
    with open("Music_Info.txt", "r") as mus:
        mus.readline()  # Skips the header line
        for line in mus:  
            line = line.strip()  
            if not line:  
                continue
            line = line.split(',')

            #searching by song name
            if method == 1 and request.lower() in line[2].lower():
                returned.append(line)

            #searching by artist name
            elif method == 2 and request.lower() in line[1].lower():
                returned.append(line)

            #searching by medium of storage
            elif method == 3 and request.lower() in line[3].lower():
                returned.append(line)

            #searching by genre
            elif method == 4 and request.lower() in line[4].lower():
                returned.append(line)

    #checking if the song is available
    with open("Rental.txt","r") as ren:
        ren.readline()
        
        #checking each song that is outputted by the search
        for x in range(len(returned)):
            unav = False
            
            #checking each line in the rental database to see if it is currently being rented
            for line in ren:
                line = line.strip()
                if not line:  
                    continue
                line = line.split(',')
                
                #if song id matches the line entry's song id.
                if returned[x][0] == line[0]:

                    if line[2] == "":
                        unav = True
                    else:
                        pass
            
            #adds availablility status onto the search results for each song.
            if unav is True:
                returned[x].append("UNAVAILABLE")
            else:
                returned[x].append("AVAILABLE")

    # if no songs matched the search
    if returned == []:
        print("No songs found.")
    
    #if songs were found from search
    else:
        for x in returned:
            print(x)