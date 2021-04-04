package GraphPackage;

import java.util.HashMap;
import java.util.List;


public class Graph {

	static public  HashMap<Integer, Coordinates> nodesCordinates;
	
	static public HashMap<Integer, List<Integer>> adjacencyList;
	
	
	static {
		//Step 3: Initialization of Graph
		nodesCordinates = new HashMap<>();
		adjacencyList = new HashMap<>();
	}


	public static HashMap<Integer, Coordinates> getNodesCordinates() {
		return nodesCordinates;
	}


	public static void setNodesCordinates(HashMap<Integer, Coordinates> nodesCordinates) {
		Graph.nodesCordinates = nodesCordinates;
	}


	public static HashMap<Integer, List<Integer>> getAdjacencyList() {
		return adjacencyList;
	}


	public static void setAdjacencyList(HashMap<Integer, List<Integer>> adjacencyList) {
		Graph.adjacencyList = adjacencyList;
	}
	
	
}
