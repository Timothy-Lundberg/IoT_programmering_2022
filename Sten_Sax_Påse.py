# Anton Yemortaji
# Erik Axelsson
# Timothy Lundberg



import random
   
def user_choice():
    # Ber användaren om deras val och konverterar till lowercase
    user_hand = input("Sten, Sax eller påse?: ").lower()
    # Returnerar värdet
    return user_hand

def pc_choice():
    # Slumpar ett tal mellan 1-3
    pc_value = random.randint(1, 3)
    # Anknyter ett värde till pc_hand
    if pc_value == 1:
        pc_hand = "sten"
         
    elif pc_value == 2:
        pc_hand = "sax"
        
    else:
         pc_hand = "påse"
              
    return pc_hand     

       
def play():
    # Anropar funktionen pc_choice
    pc_hand = pc_choice()
    # Anropar funktionen user_choice
    user_hand = user_choice()
    # Printar ut datorns hand och användarens hand
    print("*"* 128 + f"\n\t\t\t\t\tDatorn     VS    User\n\n \t\t\t\t\t{pc_hand}              {user_hand}")
    # Kollar om det blir oavgjort    
    if pc_hand == user_hand:
        print("\n\t\t\t\t\t      Oavgjort!\n"+ "*" * 128)
    # Bestämmer vem som vinnaren är
    elif pc_hand == "sten" and user_hand == "sax":
        pc_hand = "winner"
    
    elif pc_hand == "sax" and user_hand == "påse":
        pc_hand = "winner"
    
    elif pc_hand == "påse" and user_hand == "sten":
        pc_hand = "winner"
    
    elif user_hand == "sten" and pc_hand == "sax":
        user_hand = "winner"
    
    elif user_hand == "sax" and pc_hand == "påse":
        user_hand = "winner"
    
    elif user_hand == "påse" and pc_hand == "sten":
        user_hand = "winner"
    # Om användaren vinner så...        
    if user_hand == "winner":
        print("\n\t\t\t\t\t   Grattis du vann!\n"+ "*" * 128)
    # Om datorn vinner så...
    elif pc_hand == "winner":
        print("\n\t\t\t\t\t   Du förlorade\n"+ "*" * 128)

   
     
keep_going = True
# While sats som körs till keep_going blir False    
while keep_going:
    # Frågar om användaren vill spela 
    user_command = input("Vill du spela? Ja eller Nej: ").lower()
    # Om ja så körs spelet
    if user_command == "ja":
            play()
    # Om nej så avslutas programmet        
    elif user_command == "nej":
            keep_going = False
          
    
    

        


    
   



    