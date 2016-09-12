
import csv

#create empty variables
playerlist = []
previousexperience = []
newplayers = []
dragons = {}
sharks = {}
raptors = {}
league = [dragons,sharks,raptors]

#load up information for the guardian letters
times = ['March 17 @ 1 pm','March 17 @ 3 pm','March 18 @ 1 pm']
template = "Dear {},\n\nYour child, {}, has been placed on the {} soccer team. The first practice for the {} is scheduled for {}. \nWe look forward to seeing you there! \n\nSincerely,\nCoach"

#function to split players into group that's played before and group that hasn't.    
def experienced(playerlist):
  for player in playerlist[1:]:
    if player[2] == 'YES':  # item postion 2 in each player's list is previous experience; divides them into 2 groups
      previousexperience.append(player)
    else:
      newplayers.append(player)
  return previousexperience,newplayers      

#function to assign players to teams
def assign(previousexperience):
  for player in previousexperience:
    if player in previousexperience[:3]:  #first 3 go to the Dragons {dictionary of child (key): guardian(s) (item)}
      dragons[player[0]] = player[3]
    elif player in previousexperience[3:6]:  #second 3 go to the Sharks {dictionary of child (key): guardian(s) (item)}
      sharks[player[0]] = player[3]
    elif player in previousexperience[6:]:  #the rest go to the Raptors {dictionary of child (key): guardian(s) (item)}
      raptors[player[0]] = player[3]

#generate the guardian letters
def letter(league,times,template):
  for team in league:  #league is list of teams, which are dictionaries
    if team == league[0]:  #if the team is the first in the list (Dragons),
      for player in team:  #take every player, and insert their info into the letter template and save file
        filename = ('_'.join(list(player.split()))).lower()+'.txt'
        with open(filename,'w') as file:
          file.write(template.format(team[player],player,'Dragons','Dragons',times[0]))
    elif team == league[1]: #if the team is the second in the list (Sharks),
      for player in team: #take every player, and insert their info into the letter template and save file
        filename = ('_'.join(list(player.split()))).lower()+'.txt'
        with open(filename,'w') as file:        
          file.write(template.format(team[player],player,'Sharks','Sharks',times[1]))
    else: #if the team is the rest (Raptors),
      for player in team: #take every player, and insert their info into the letter template and save file
        filename = ('_'.join(list(player.split()))).lower()+'.txt'
        with open(filename,'w') as file:        
          file.write(template.format(team[player],player,'Raptors','Raptors',times[2]))

if __name__ == "__main__":     
  #quick yes/no to run
  if input('Would you like to create the team rosters and guardian letters? Y/n ').upper() == 'Y':
    #import the player info from the csv, store it as playerlist (list of lists)
    with open('soccer_players.csv',newline='') as csvfile:
      csvreader = csv.reader(csvfile,delimiter=',')
      for row in csvreader:
        playerlist.append(row)
    experienced(playerlist)  #divide players into experienced and new
    assign(previousexperience)  #assign experienced players to teams
    assign(newplayers)  #assign new players to teams
    letter(league,times,template) #generate letters for guardians with child's info
    print('Rosters created and letters generated.')
  else:
    print('Okay')    

  