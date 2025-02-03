import math

def inventoryPruning(choice):
    
    #if we are pruning by lowest rating.
    if choice == 1:
        ratings = {}
        finals =[]
        
        with open("Music_Feedback.txt", "r") as f:
            f.readline()
    
            for line in f:
                line = line.strip()
                
                if not line:  
                    continue
                
                #changing the total ratings and number of ratings recorded line by line
                line = line.split(',')
                
                #first instance of a song
                if line[0] not in ratings:
                    ratings[line[0]] = [int(line[1]),1]
                #song already seen. ratings[0] stores total of the ratings while ratings [1] stores the number of ratings
                else:
                    ratings[line[0]][0] += int(line[1])
                    ratings[line[0]][1] +=1

            # using the total rating / number of ratings to find the average rating for each song
            for x in ratings:
                finals.append([x, ratings[x][0]/ ratings[x][1]])


            #finding song with the lowest rating.
            worst = ["",math.inf]
            for x in finals:
                if x[1] <worst[1]:
                    worst[1] = x[1]
                    worst[0] = x[0]

            print("We suggest you remove song:",worst[0], "with an average rating of" ,str(worst[1])+"/5.")
            
            # printing the full song info so it can be easily found and pruned
            with open("Music_Info.txt",'r') as f:
                for line in f:
                    line = line.strip()
                
                    if not line:  
                        continue
                
                    line = line.split(',')
                    if line[0] == worst[0]:
                        print("RecordID,,ArtistTitle,Medium,Genre,PurchaseDate")
                        print(line)


    # if we are pruning by lowest number of rentals
    elif choice == 2:
        #dictionary used to store the rent count for each song.
        rentNumbers = {}
        with open("Rental.txt", "r") as f:
            f.readline()
    
            for line in f:
                line = line.strip()
                
                if not line:  
                    continue 
                line = line.split(',')


                # changing the rent count for the song on each line
                if line[0] not in rentNumbers:
                    rentNumbers[line[0]] = 1
                else:
                    rentNumbers[line[0]] +=1

            # process of finding the lowest rating.
            lowest = ["",math.inf]
            for x in rentNumbers:
                if rentNumbers[x] < lowest[1]:
                    lowest = [x,rentNumbers[x]]

            print("We suggest you remove song:",lowest[0], "with only",lowest[1],"rents.")
            
            # printing the full song info so it can be easily found and pruned
            with open("Music_Info.txt",'r') as f:
                for line in f:
                    line = line.strip()
                
                    if not line:  
                        continue
                
                    line = line.split(',')
                    if line[0] == lowest[0]:
                        print("RecordID,,ArtistTitle,Medium,Genre,PurchaseDate")
                        print(line)

