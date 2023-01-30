import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#create graph
def create_tsp_graph(distanceList, h):
    G = nx.Graph()
    for i in range(h):
        G.add_node(i)
    for i in range(h):
        for j in range(h):
            if i != j:
                G.add_edge(i, j, weight=distanceList[i][j])
    return G

#define lin_kernighan
def lin_kernighan(distanceList, h):
    # Initialize the solution with the greedy algorithm.
    current_solution = np.arange(h)
    np.random.shuffle(current_solution)
    best_solution = current_solution.copy()

    # Start the loop.
    while True:
        # Initialize the improvement flag.
        improved = False

        # Try reversing every possible sub-sequence.
        for i in range(h - 2):
            for j in range(i + 2, h):
                if j - i == 1:
                    continue

                # Reverse the sub-sequence and check the gain.
                new_solution = current_solution.copy()
                new_solution[i:j] = np.flip(new_solution[i:j])

                gain = (distanceList[current_solution[i - 1], current_solution[j - 1]]
                        + distanceList[current_solution[i], current_solution[j]]
                        - distanceList[new_solution[i - 1], new_solution[j - 1]]
                        - distanceList[new_solution[i], new_solution[j]])

                # If the gain is positive, update the solution.
                if gain > 0:
                    current_solution = new_solution
                    improved = True
                    if current_solution[0] != 0:
                        current_solution = np.roll(current_solution, -current_solution.tolist().index(0))

        # If no improvement was found, return the best solution.
        if not improved:
            total_distance = 0
            for i in range(h-1):
                total_distance += distanceList[best_solution[i], best_solution[i+1]]
            total_distance += distanceList[best_solution[h-1],best_solution[0]]
            return best_solution, total_distance
        else:
            if current_solution.tolist() != best_solution.tolist():
                best_solution = current_solution.copy()

# example usage

#coordinates
cities= [(15,53),(25,52),(20,40),(10,30),(43,63),(11,22),(30,65),(19,45),(75,20),(55,85),(45,95),(100,30),(39,26)]
#cities
h = len(cities)
distanceList = []
#dinamic distance calculator 
def distance(i,j):
    for i in range(h):
        for j in range(h):
            if i !=j :
                x1, y1 = cities[i]
                x2, y2 = cities[j]
                result = round(np.sqrt((x1 - x2)**2 + (y1 - y2)**2))
                distanceList.append(result) 
            elif i == j:
                x1, y1 = cities[i]
                x2, y2 = cities[j]
                result = round(np.sqrt((x1 - x1)**2 + (y1 - y1)**2))
                distanceList.append(result)             


distance(cities,cities)
distanceList = np.array(distanceList).reshape(h,h)



result, total_distance = lin_kernighan(distanceList, h)
print("Best Solution:", result)
print("Total Distance :", total_distance)
G = create_tsp_graph(distanceList, h)
nx.draw(G,s,with_labels=True)
plt.show()