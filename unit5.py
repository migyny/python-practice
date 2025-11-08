###############################    Session1          ###############################
#------------------------------  Problem set 1      --------------------------------
# class Cat:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed




# cat1 = Cat("Felix", "Breed1")
# cat2 = Cat("Kokos", "Egyptian Cat")

# print(cat2.name,cat2.breed)
# print(cat1.name,cat1.breed)
#------------------------------
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next= None


# x=Node(2)
# print(x.value,x.next)
# y=Node(4)
# print(y.value)

# x.next=y

# print(x.next.value)

# y= None

# print(x.next.value)


#1

# class Pokemon:
#     def __init__(self, name, types, evolution = None):
#         self.name = name
#         self.types = types
#         self.is_caught = False
#         self.evolution = evolution

#     def print_pokemon(self):
#         print({
#             "name": self.name,   
#             "types": self.types, 
#             "is_caught": self.is_caught 
#         })

#     def catch(self):
#         self.is_caught = True
#     def choose(self):
#         if self.is_caught == True:
#             print(self.name + "I choose you!")
#         else:
#             print(self.name +"is wild! Catch them if you can!")

#     def add_type(self,new_type):
#         self.types.append(new_type)
    
# def get_evolutionary_line(starter_pokemon):
#     curr = starter_pokemon
#     lst = []
#     while curr != None:
#         lst.append(curr.name)
#         curr = curr.evolution
#     return lst
        


# def get_by_type(my_pokemon, pokemon_type):
#     lst=[]
#     for pokemon in my_pokemon:
#         if pokemon_type in pokemon.types:
#             lst.append(pokemon.name)

#     return lst
                  
		

# my_pokemon = Pokemon("Pikachu", "Electric")

# print(my_pokemon.name,my_pokemon.types)

# #2
# squirtle = Pokemon("Squirtle", ["water"])
# squirtle.print_pokemon()

# #3
# squirtle.is_caught = True
# squirtle.print_pokemon()

# #4
# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()

# #5
# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()

# #6
# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()

# #7

# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)

# #8
# charizard = Pokemon("Charizard", ["fire", "flying"])
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)

# #9

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
          

# def print_linked_list(head):
#     curr = head
#     while curr.next is not None:
#           print(curr.value + " -> " , end='')
#           curr= curr.next
#     print(curr.value)


# node_one= Node("a")
# node_two = Node("b")

# print(node_one.value) 
# print(node_one.next) 
# print(node_two.value)
# print(node_two.next) 

# node_one.next = node_two
# print(node_one.value)
# print(node_one.next.value)
# print(node_two.value)

# #11

# node_1 = Node("Mario")
# node_2 = Node("Luigi")
# node_3 = Node("Wario")
# node_4 = Node("Toad")
# node_1.next = node_2
# node_2.next=node_3
# node_3.next=node_4

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)

# #12
# print_linked_list(node_1)


#----------------------
#1

# class Card():
#     def  __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
#     def print_card(self):
#         print(f"{self.rank} of {self.suit}")
	
#     def is_valid(self):
#         suits = ["Hearts","Spades","Clubs","Diamonds"]
#         ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
#         if self.suit in suits and self.rank in ranks:
#             return True
#         return False
    
#     def get_value(self):
#         match(self.rank): 
#             case "Ace": return 1
#             case "Jack" : return 11
#             case "Queen" : return 12
#             case "King" : return 13
#             case _ : return int(self.rank)
#         return None
    
# class Hand:
#     def __init__(self):
#         self.cards = []
     
#     def add_card(self, card):
#         self.cards.append(card)
	    
#     def remove_card(self, card):
#         self.cards

        
	
		
# card = Card("Sapdes","8")
# print(card.suit,card.rank)
# card1 = Card("Clubs","Ace")
# card1.print_card()
# card1.suit = "Hearts"
# card1.print_card()

# #4
# my_card = Card("Hearts", "7")
# print(my_card.is_valid())

# second_draw = Card("Spades", "Joker")
# print(second_draw.is_valid())

# #5

# card = Card("Hearts", "7")
# print(card.get_value())

# card_two = Card("Spades", "Jack")
# print(card_two.get_value())

# #6


###############################    Session2          ###############################
#------------------------------  Problem set 1      --------------------------------

class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        