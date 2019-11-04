# Machine-learning-using-BigData

# Neo4J:
1. Hetionet : Integrating Biology into a Public Neo4j Database

Cypher Commands : 
1. Delete relationship: 
    - f""" MATCH()-[r:"RELATION_NAME"]-() DELETE r """ 
    
2. Create relationship:
    - f"""MATCH (a:"nodeName1"), (b:"nodeName2")where nodeName1.attribute="value"
            and nodeName2.attribute="value" CREATE (a)-[r:"RelationName"]->(b)
            RETURN type(r), r.name""" 
            
3. Create node: 
    - f"""CREATE ( Disease : Disease{{ id : "{line[0]}", name : "{line[1]}", kind : "{line[2]}" }})""" 
    
4. Find relationship of a noe: 
    - f"""MATCH p=()-[r:"relationshipName"]->()
        RETURN p LIMIT 25""" 
        
5. Delete all relationship of a node: 
    - f"""MATCH ()-[r:"relationshipName"]-() delete r
 
# Cassandra:

    
    
# Hadoop:
1. hdfs namenode -formate
2. start-all.cmd
3. resource-manager: all map-reduce programs that are executed in the system
	http://localhost:8088/cluster
4. namenode UI:
	http://localhost:50070/dfshealth.html#tab-overview
5. copy file to hadoop directory:
	hadoop fs -mkdir "filename" 
        
        
        
