import datetime
import feedbackManager as fm


def musicReturn(song,customer,rating,comments):
    newLine = False

    #reading the file
    with open("Rental.txt", "r") as f:
        f.readline()
        lines = f.readlines()  

    #writing a new version of the file to append any new changes to
    with open("Rental.txt", "w") as f:
        
        f.write("RecordID,RentalDate,ReturnDate,RentalCustomerID\n")
        
        for line in lines:
            
            line = line.strip().split(",")
            
            #if entry matches songID and it is currently being rented
            if line[0] == song and line[2] == "":
                
                #if the song is being rented by the same user who is returning the song
                if line[3] == customer:
                    
                    line[2] = str(datetime.date.today())
                    newLine = ",".join(line)
                else:
                    print("This song has been rented by a different customer!")
            
            # writing the line back without any changes
            else:
                line = ",".join(line)
                f.write(line+"\n")

        #if a line has been changed
        if newLine is not False:
            f.write(newLine + "\n")
            print("Song",song, "returned")

            
            fm.add_feedback(song,rating,comments,"Music_Feedback.txt")

        #if no changes were made
        else:
            print("Song not found or already returned")
    
    