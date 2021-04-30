from itertools import permutations
import math
from draw import draw_path
from test import test_path

class password():
    def __init__(self, rule):
        self.rule = rule
        # Longest distance
        self.longest_length = 0.0
        # List of longest path. The longest path is not unique. 
        self.longest_path = []
        # Your code goes here:
        self.adjacent = {'13': '2', '31': '2', '19': '5', '91': '5', '17': '4', '71': '4', '28': '5', '82': '5', '37': '5', '73': '5', '39': '6', '93': '6' }

        

    # Find the longest path
    def find_longest_path(self):
        # Your code goes here:
        # dictionary of coordinates
        coordinate = {}
        for x in range(1,10):
            coordinate[str(x)] = ((x-1)//3, (x-1)%3) 
        # p is each path
        p = permutations(coordinate.keys(), 9)
        for i in p:
            flag = True
            # creates a list of strings out of the permutations
            i = ''.join(i)
            dist = 0
            # runs for rule 1
            if self.rule == 1:
                for key in self.adjacent:
                    if key in i:
                        # not a valid rule
                        flag = False
                        break
                    # supposed to do distance but does not work correctly
                if flag == True: 
                    dist = 0
                    for j in range(0, 8):
                        
                        v1= coordinate[i[j]]
                        v2= coordinate[i[j+1]]

                        dist = dist+self.distance(v1,v2)

                    if(dist == self.longest_length):
                        self.longest_path.append(i)
                    elif(dist > self.longest_length):
                        self.longest_length = dist
                        self.longest_path = []
                        self.longest_path.append(i)
                            
            if self.rule == 2:
                for key in self.adjacent: 
                # if value index is greater than key index remove
                    # if i.index(key) < i.index(key.values()):
                    place = self.adjacent[key]
                    if key in i and i.index(key[0]) < i.index(place):
                        flag = False
                        break
                if flag == True: 
                    dist = 0
                    for j in range(0, 8):
                        
                        v1= coordinate[i[j]]
                        v2= coordinate[i[j+1]]

                        dist = dist+self.distance(v1,v2)

                    if(dist == self.longest_length):
                        self.longest_path.append(i)
                    elif(dist > self.longest_length):
                        self.longest_length = dist
                        self.longest_path = []
                        self.longest_path.append(i)

                

            #     # find index of key
            #     # find index of value
           
                            
                   
  
    # Calculate distance between two vertices
    # Format of a coordinate is a tuple (x_value, y_value), for example, (1,2), (0,1)
    def distance(self, vertex1, vertex2):
        return math.sqrt((vertex1[0]-vertex2[0])**2 + (vertex1[1]-vertex2[1])**2)

    # Print and save the result
    def print_result(self):
        print("The longest length using rule " + str(self.rule) + " is:")
        print(self.longest_length)
        print()
        print("All paths with longest length using rule " + str(self.rule) + " are:") 
        print(self.longest_path)
        print()
        with open('results_rule'+str(self.rule)+'.txt', 'w') as file_handler:
            file_handler.write("{}\n".format(self.longest_length)) 
            for path in self.longest_path:
                file_handler.write("{}\n".format(path)) 

    # test the result 
    def test(self):
        test_path(self.longest_length, self.longest_path, self.rule)

    # draw first result
    def draw(self):
        if len(self.longest_path) > 0:
            draw_path(self.longest_path[0], self.rule)

if __name__ == "__main__":

    for rule in range(1,3):
        # Initialize the object using rule 1 or rule 2
        run = password(rule)
        # Find the longest path
        run.find_longest_path()
        # Print and save the result
        run.print_result()
        # Draw the first longest path
        run.draw()
        # Verify the result 
        run.test()