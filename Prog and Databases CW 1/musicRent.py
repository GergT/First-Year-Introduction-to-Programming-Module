import subscriptionManager as sm
import datetime 

def musicRent(song,customer):
    songAvailable = True
    exists = False
    
    #Setting the maximum number of songs based upon user's subscription level.
    subscriptions = sm.load_subscriptions()
    if sm.check_subscription(customer, subscriptions):
        if subscriptions[customer]['SubscriptionType'] == 'Premium':
            maxSubs = 7
        else:
            maxSubs = 2

    with open("Rental.txt",'r+') as f:
        
        f.readline()

        for line in f:
            line = line.strip()  
            
            if not line:  
                continue
            line = line.split(',')
            
            #checking if the song can be rented with no errors
            if line[0] == song:
                exists = True
            
                if line[2] == "":
                    songAvailable = False
            
            if line[2] == "" and line[3] == customer:
                maxSubs -=1
        
        #renting the song if no errors
        if maxSubs > 0 and songAvailable and exists:
            today = datetime.date.today()
            f.write("\n"+str(song)+","+str(today)+","+""+","+str(customer))
            print("Song rented successfully")
        
        #printing any errors
        elif not songAvailable :
            print("Song already being rented")     
        
        elif maxSubs <=0:
            print("Customer has already rented too many songs")
        
        elif not exists:
            print("Song does not exist")
        


#musicRent()