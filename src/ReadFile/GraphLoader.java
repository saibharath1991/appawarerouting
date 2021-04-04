package ReadFile;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

import GraphPackage.Coordinates;
import GraphPackage.Graph;

public class GraphLoader {

	static int xcounter=1;
	
	static int ycounter=1;
	//Step 1: Done in MATLAB - Generate ERDOS RENYI GRAPH
	public static void main(String [] args) throws Exception {
		
		String file = "src/erdosgraph/input.txt";
		Scanner reader = new Scanner(new FileReader(file));
			
		//Step 2: Load the output from MATLAB
		int currentTracker = 0;
		while(true) {
			if(!reader.hasNext())
				break;
			String line =reader.nextLine();
			
			if(line.contains("print Adj")) {
				currentTracker = 1;
				continue;
			}
			else if(line.contains("x co-ordinates")) {
				currentTracker = 2;
				continue;
			}
			else if(line.contains("y-co-ordinates")) {
				currentTracker = 3;
				continue;
			}
			
			if(currentTracker==1) {
				buildAdjacencyList(line);
			}
			else if(currentTracker==2) {
				buildXCoordinateList(line);
			}
			else if(currentTracker==3) {
				buildYCoordinateList(line);
			}
			
			
		}
		
		reader.close();
		System.out.println("Printing the adjacency list");
		printAdjacencyList();
		
		//filterAdjacencyList();
		//Create nodes in mininet
		Mininet.create(Graph.adjacencyList,Graph.nodesCordinates);
		
	}

	private static void filterAdjacencyList() {
		
		
		
				Set<Integer> filterNodes =Graph.adjacencyList.keySet();
				
				filterNodes.stream()
					.filter(f -> f.intValue() > 100)
						.forEach(j -> {
							Graph.adjacencyList.remove(j);
						});

				for(Integer i: Graph.adjacencyList.keySet())
				{
					List<Integer> adjNodes =Graph.adjacencyList.get(i);
					
					adjNodes.stream()
						.filter(f -> f.intValue() > 100)
							.forEach(j -> {
								Graph.adjacencyList.remove(i,j);
							});
				}
			
					
					
				
		
		}
	
	
	private static void printAdjacencyList() {
		System.out.println(Graph.getAdjacencyList());
		System.out.println(Graph.getNodesCordinates());
		
	}

	private static void buildYCoordinateList(String line) {
		if(line==null) {
			return;
		}
		try {
			double number = Double.parseDouble(line);
			Coordinates cord = Graph.getNodesCordinates().get(ycounter);
			cord.setY(number);
			Graph.getNodesCordinates().put(ycounter, cord);
			ycounter++;
		}
		catch(Exception e) {
			return;
		}
		
	}

	private static void buildXCoordinateList(String line) {
		if(line==null) {
			return;
		}
		try {
			double number = Double.parseDouble(line);
			Graph.getNodesCordinates().put(xcounter, new Coordinates(number));
			xcounter++;
		}
		catch(Exception e) {
			return;
		}
	}

	private static void buildAdjacencyList(String line) {
		Integer node1 =-1;
		Integer node2=-1;
		if(!line.contains("("))
			return;
		else if(!line.contains(")"))
			return;
		String[] compos = line.split(" ");
		for(String item: compos) {
			if(item.length()<=2)
				continue;
			if(item.contains("(")) {
				String[] splitItem = item.split(",");
				String firstString = splitItem[0];
				
				int index1=firstString.indexOf('(');
				String substring=firstString.substring(index1+1, firstString.length());
				node1=Integer.parseInt(substring);
			
				String secondString = splitItem[1];
				int index2=secondString.indexOf(')');
				String secondSubstring=secondString.substring(0, index2);
				node2=Integer.parseInt(secondSubstring);
				
				if(node1!=-1 && node2!=-1) {
					
					addInAdj(node1,node2);
					//addInAdj(node2,node1);
				}
			}
			
		}
		
	}

	private static void addInAdj(Integer node1, Integer node2) {

		System.out.println("Adding "+ node1+ "," + node2);
		List<Integer> isPresent = Graph.getAdjacencyList().get(node1);
		
		if(isPresent==null || isPresent.isEmpty()) {
			List<Integer> integerList = new ArrayList<Integer>();
			integerList.add(node2);

			Graph.getAdjacencyList()
					.put(node1,integerList);	
		}
		else {
			isPresent.add(node2);
			Graph.getAdjacencyList()
			.put(node1,isPresent);
		}
}
}
