

# def AStarSearch(tree, heuristic, start, goal):
#     cost = {start: 0}  # total cost for nodes visited
#     closed = []  # closed nodes
#     opened = [[start, heuristic[start]]]  # opened nodes

#     '''find the visited nodes'''
#     while True:
#         fn = [i[1] for i in opened]  # fn = f(n) = g(n) + h(n)
#         chosen_index = fn.index(min(fn))
#         node = opened[chosen_index][0]  # current node
#         closed.append(opened[chosen_index])
#         del opened[chosen_index]
#         if closed[-1][0] == goal:  # break the loop if the goal node has been found
#             break
#         for item in tree[node]:
#             if item[0] in [closed_item[0] for closed_item in closed]:
#                 continue
#             cost.update({item[0]: cost[node] + item[1]})  # add nodes to cost dictionary
#             fn_node = cost[node] + heuristic[item[0]] + item[1]  # calculate f(n) of current node
#             temp = [item[0], fn_node]
#             opened.append(temp)  # store f(n) of current node in array opened

#     '''find optimal sequence'''
#     trace_node = goal  # correct optimal tracing node, initialize as the goal node
#     optimal_sequence = [goal]  # optimal node sequence
#     for i in range(len(closed) - 2, -1, -1):
#         check_node = closed[i][0]  # current node
#         if trace_node in [children[0] for children in tree[check_node]]:
#             children_costs = [temp[1] for temp in tree[check_node]]
#             children_nodes = [temp[0] for temp in tree[check_node]]

#             '''check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
#             change the correct optimal tracing node to current node'''
#             if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
#                 optimal_sequence.append(check_node)
#                 trace_node = check_node
#     optimal_sequence.reverse()  # reverse the optimal sequence

#     return closed, optimal_sequence

# ======================================================================================================================================
import networkx as nx

def AStarSearch(G, heuristic, start, goal):
    cost = {start: 0}  # total cost for nodes visited
    closed = []  # closed nodes
    opened = [[start, heuristic[start]]]  # opened nodes

    '''find the visited nodes'''
    while True:
        fn = [i[1] for i in opened]  # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # current node
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == goal:  # break the loop if the goal node has been found
            break
        if isinstance(G, dict):  # check if G is a dictionary
            neighbors = [item[0] for item in G[node]]
        else:  # if G is not a dictionary, it should be a NetworkX graph object
            neighbors = list(G.neighbors(node))
        for neighbor in neighbors:
            if neighbor in [closed_item[0] for closed_item in closed]:
                continue
            if isinstance(G, dict):  # check if G is a dictionary
                edge_data = {'weight': [item[1] for item in G[node] if item[0] == neighbor][0]}
            else:  # if G is not a dictionary, it should be a NetworkX graph object
                edge_data = G.get_edge_data(node, neighbor)
            cost.update({neighbor: cost[node] + edge_data['weight']})  # add nodes to cost dictionary
            fn_node = cost[node] + heuristic[neighbor] + edge_data['weight']  # calculate f(n) of current node
            temp = [neighbor, fn_node]
            opened.append(temp)  # store f(n) of current node in array opened
    '''find optimal sequence'''
    trace_node = goal  # correct optimal tracing node, initialize as the goal node
    optimal_sequence = [goal]  # optimal node sequence
    for i in range(len(closed) - 2, -1, -1):
        check_node = closed[i][0]  # current node
        if isinstance(G, dict):  # check if G is a dictionary
            children_costs = [item[1] for item in G[check_node] if item[0] == trace_node]
            children_nodes = [item[0] for item in G[check_node]]
        else:  # if G is not a dictionary, it should be a NetworkX graph object
            edge_data = G.get_edge_data(check_node, trace_node)
            children_costs = [edge_data['weight']]
            children_nodes = list(G.neighbors(check_node))
        '''check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
        change the correct optimal tracing node to current node'''
        if trace_node in children_nodes and cost[check_node] + children_costs[0] == cost[trace_node]:
            optimal_sequence.append(check_node)
            trace_node = check_node
    optimal_sequence.reverse()  # reverse the optimal sequence

    return closed, optimal_sequence

