destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# print(get_destination_index("Los Angeles, USA")) 2
# print(get_destination_index("Paris, France")) 0

def get_traveler_location(traveler):
#find destination of traveler from list (index 1) and compare to destination index list
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

print(test_destination_index)

attractions = [[] for destination in destinations]
print(attractions)

#add new attraction
def add_attraction(destination, attraction):
#find index of destination from get_destination_index()
  try:
     destination_index = get_destination_index(destination)
     attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return 

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print(attractions)

#search for attractions relating to traveler destination and interest
def find_attractions(destination, interests):
#find attractions in each city
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
#loop through attractions
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
#loop through interests to see if interest matches attraction available
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])
# print(la_arts)

#Gather all traveler info and separate into each category
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

#output info for the traveler
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for attractions in traveler_attractions:
    interests_string += attractions
  return interests_string

#test
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)