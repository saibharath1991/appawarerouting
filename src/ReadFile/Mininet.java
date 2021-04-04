package ReadFile;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import GraphPackage.Coordinates;

public class Mininet {

	public static void create(HashMap<Integer, List<Integer>> adjacencyList,
			HashMap<Integer, Coordinates> nodesCordinates
			) throws Exception {
		// Create the mininet nodes
		
	//	Path path = Paths.get("./erdos_mininet.py");
		
		
	//	BufferedWriter br=new BufferedWriter(new FileWriter("./erdos_mininet.py"));
		BufferedWriter br=new BufferedWriter(new FileWriter("./sample_sshd.py"));
		
		String header = "from mininet.topo import Topo";
		br.append(header + "\n");
		
		
		String className="class MyTopo( Topo ):\n\t\"Erdos topology experiment\"\n";
		
		br.append(className);
		
		String methodName="\n\tdef build (self): \n\t\t\"custom topology \"\n";
		
		br.append(methodName);
		
		br.flush();
		
		Set<Integer> visitedNodes = new HashSet<Integer>();
		Set<Integer> income = new HashSet<Integer>();
		Set<Integer> expense = new HashSet<Integer>();
		
		//Visit every node
		for(Integer k: adjacencyList.keySet()) {
			
			if(k > 1)
				continue;
			//Get its adjavency List
			List<Integer> adjList = adjacencyList.get(k);
			
			for(Integer adjNode : adjList) {
				
				if(adjNode > 5)
					continue;
				if(!visitedNodes.contains(adjNode)) {
					
					String createNodes="";
					
					if(!expense.contains(k)) {
						if(!income.contains(k))
						 createNodes = createNodes.concat("\n\t\tmH_"+k+" = self.addHost('h"+k+"')");
						
						 Integer switchKNumber = k * 10 + 1;
						 createNodes = createNodes.concat("\n\t\tmS_"+k+"_"+switchKNumber+" = self.addSwitch('s"+switchKNumber+"')");
						createNodes = createNodes.concat("\n\t\tself.addLink(mH_"+k+", mS_"+k+"_"+switchKNumber+")");
							
					}
					
					if(!income.contains(adjNode)) {
						if(!expense.contains(adjNode)) 
						 createNodes = createNodes.concat("\n\t\tmH_"+adjNode+" = self.addHost('h"+adjNode+"')");
						
					 Integer  switchKNumber = adjNode * 10 + 2;
						 createNodes = createNodes.concat("\n\t\tmS_"+adjNode+"_"+switchKNumber+" = self.addSwitch('s"+switchKNumber+"')");
						createNodes = createNodes.concat("\n\t\tself.addLink(mS_"+adjNode+"_"+switchKNumber+", mH_"+adjNode+")");
						
					
					}
					
					 Integer switchKNumber = k * 10 + adjNode;
					 Integer switchAdjNumber = adjNode * 10 + k;
					 
					// createNodes = createNodes.concat("\n\t\tmS_"+k+"_"+adjNode+" = self.addSwitch('s"+switchKNumber+"')");
					// createNodes = createNodes.concat("\n\t\tself.addLink(mH_"+k+", mS_"+k+"_"+adjNode+")");
					 
					// createNodes = createNodes.concat("\n\t\tmS_"+adjNode+"_"+k+" = self.addSwitch('s"+switchAdjNumber+"')");
					// createNodes = createNodes.concat("\n\t\tself.addLink(mS_"+adjNode+"_"+k+", mH_"+adjNode+")");
			
					 expense.add(k);
					income.add(adjNode);
					
					// createNodes = createNodes.concat("\n\t\tself.addLink(mS_"+k+"_"+adjNode+", mS_"+adjNode+"_"+k+")");
					
					createNodes = createNodes.concat("\n\t\tself.addLink(mS_"+k+"_"+(k*10+1)+", mS_"+adjNode+"_"+(adjNode * 10 +2)+")");
					
					
					br.append(createNodes);
					br.flush();
				}
			}
			
			visitedNodes.add(k);
		}
		
		String trailer="\n\ntopos = { 'mytopo': ( lambda: MyTopo() ) }";
		br.append(trailer);
		br.close();
	}

}
