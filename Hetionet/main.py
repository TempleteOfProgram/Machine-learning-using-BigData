import os, json
from flask import Flask, request
from resources.nodes import insert_all_nodes
from resources.edges import insert_all_edges
from Neo4j.query import (find_query, insert_query)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def find_dummy():
    """
     http://127.0.0.1:5000/
     """
    dummy_relation = "MATCH (x:dummy {name:'dummy'}) -[r]-> (y:dummy)  RETURN x.name, y.name"
    records = find_query(dummy_relation)
    if not records:
        return json.dumps({"error": "Record not found"})
    try:
        for record in records:
            print(record)
            return json.dumps({"success": True})
    except Exception as e:
        return e



@app.route("/disease", methods=['GET'])
def find_ralation():
    """
     http://127.0.0.1:5000/disease?name=diseseName
     """
    name = request.args.get("name")
    if not name:
        return json.dumps({"error": "Disease name not provided"})
    try:
        prefix = """MATCH (a:Disease { name :\""""
        prefix = prefix + name
        postfix = """\"})-[:DrD]->(A:Disease), 
                        (A) -[r:DlA]->(b:Anatomy) -[:AdG]->(c:Gene), (b)-[:AeG]->(d:Gene),(b)-[:AuG]->(e:Gene) 
                        RETURN A, a, b, c, d, e limit 1"""

        postfix0 = """\"})-[:DuG]->(i:Gene), (a)-[:DaG]->(j:Gene), (a)-[:DdG]->(k:Gene)
                        RETURN i, j, k limit 1"""
        edges_query = prefix + postfix
        edges_query0 = prefix + postfix0

        records = find_query(edges_query)
        records0 = find_query(edges_query0)

        To = ""
        for record in records:
            To = record['a']['name']
            print(To, " resembles ", record['A']['name'])
            print(To, " localizes ", record['b']['name'])
            print(To, " up-regulates ", record['e']['name'])
            print(To, " down-regulates ", record['c']['name'])
            print(To, " express ", record['d']['name'])

        for record0 in records0:
            print(To, " up-regulates ", record0['i']['name'])
            print(To, " associates ", record0['j']['name'])
            print(To, " down-regulates ", record0['k']['name'])


        return json.dumps({"success": True})

    except Exception as e:
        print(e)
        return json.dumps({"error": "Exception found"})


@app.route("/add_node", methods=['GET'])
def add_node():
    """
    http://127.0.0.1:5000/add_node?id=nodeID&name=nodeName&kind=nodekind
    :param: id
    :param: name
    :param: kind
    :return:
    """
    id = request.args.get('id')
    name = request.args.get('name')
    kind = request.args.get('kind')

    new_node = f"""CREATE   ( new : {kind} {{ id : "{id}",  name : "{name}", kind : "{kind}" }})"""
    insert_query(new_node)
    return json.dumps({"success": True})




@app.route("/add_edges", methods=['GET'])
def add_edges():
    """
    http://127.0.0.1:5000/add_edges?source=nodesource&metaedge=nodemetaedge&target=nodetarget
    :param: source
    :param: metaedge
    :param: target
    :return:
    """
    source = request.args.get('source')
    metaedge = request.args.get('metaedge')
    target = request.args.get('target')

    new_edge = f"""MATCH(dummy1 : {source}), (dummy2: {source}) WHERE dummy1={source} and dummy2={target}
                   CREATE (dummy1) - [:{metaedge}] -> (dummy2)
                   RETURN dummy1, dummy2 """
    insert_query(new_edge)
    return json.dumps({"success": True})


@app.route("/insert_all_nodes", methods=['GET'])
def insert_all_nodes():
    """
    http://127.0.0.1:5000/insert_all_nodes
    """
    insert_all_nodes()
    return json.dumps({"success": True})



@app.route("/insert_all_edges", methods=['GET'])
def insert_all_edges():
    """
    http://127.0.0.1:5000/insert_all_edges
    """
    insert_all_edges()
    return json.dumps({"success": True})



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, threaded=True)
