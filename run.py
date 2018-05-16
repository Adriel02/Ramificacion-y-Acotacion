# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ob = search.GPSProblem('O', 'B', search.romania)
dn = search.GPSProblem('D', 'N', search.romania)

print "Ramificacion y acotacion -->", search.branch_and_bound_graph_search(dn).path()
print "Ramificacion y acotacion con heuristica -->", search.branch_and_bound_Heuristic(dn).path()
