import java.util.HashSet;
import java.util.List;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if(source == destination) {
            return true;
        }

        Map<Integer, List<Integer>> adj = new HashMap<>();
        for(int[] edge: edges) {
            int node1 = edge[0];
            int node2 = edge[1];
            adj.computeIfAbsent(node1, k -> new ArrayList<>()).add(node2);
            adj.computeIfAbsent(node2, k -> new ArrayList<>()).add(node1);
        }

        HashSet<Integer> visited = new HashSet<>();
        return dfs(source, destination, visited, adj);
    }

    private boolean dfs(
        int node, 
        int destination, 
        Set<Integer> visited, 
        Map<Integer, List<Integer>> adj
    ) {
        if(node == destination) {
            return true;
        }
        visited.add(node);
        if(!adj.containsKey(node)) {
            return false;
        }
        for(int ngb: adj.get(node)) {
            if(!visited.contains(ngb) && dfs(ngb, destination, visited, adj)) {
                return true;
            }
        }
        return false;
    }
}