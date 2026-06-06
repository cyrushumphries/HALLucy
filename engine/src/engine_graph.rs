use std::collections::HashMap;
use crate::node_trait::{EngineNode, PortDescriptor};
use crate::nodes::audio;

//The engine graph has nodes and connections between the nodes 
pub struct EngineGraph {
    //map between NodeID and pointer to EngineNode
    pub nodes: HashMap<String, Box<dyn EngineNode>>, //dyn -> Nodes will be of different types but all type will be impelemting the EngineNode Trait
    //Box -> Rust needs all items in a collection to be of dame size, which is impossible with different Node types
    //Box is a fixed size pointer to the heap, nodes will be on the heap, hashmap stores the pointers
    pub connections: Vec<EngineConnection>,
    pub port_map: HashMap<(String, String), PortDescriptor>,
}

//A connection between specific node ports (as a node can have multiple ports)
//from NodeID,PortID to NodeID,PortID
pub struct EngineConnection {
    pub from: (String, String), // NodeId, PortId
    pub to: (String, String),
}


impl EngineGraph {
    pub fn new() -> Self {
        Self {
            nodes: HashMap::new(),
            connections: Vec::new(),
            port_map: HashMap::new(),
        }
    }


    pub fn create_node_by_name(
        id: String,
        category: &str,
        name: &str,
    ) -> Box<dyn EngineNode> {
        match (category, name) {
            ("audio", "Oscillator") => Box::new(audio::oscillator::Oscillator::new(id)),

            _ => panic!("Unknown node type: {category}::{name}"),
        }
    }

    //ports param not needed i think
    pub fn add_node_by_name(
        &mut self,
        id: String,
        category: String,
        name: String,
        ports: Vec<PortDescriptor>,
    ) {
        let node = Self::create_node_by_name(id.clone(), &category, &name);
        self.nodes.insert(id.clone(), node);

        for port in ports {
            self.port_map.insert((id.clone(), port.id.clone()), port);
        }
    }


    pub fn delete_node(&mut self, id: &str) {
        self.nodes.remove(id);
        self.connections.retain(|c| c.from.0 != id && c.to.0 != id);
        self.port_map.retain(|(n, _), _| n != id);
    }

    pub fn connect(
        &mut self,
        from_node: String,
        from_port: String,
        to_node: String,
        to_port: String,
    ) {
        self.connections.push(EngineConnection {
            from: (from_node, from_port),
            to: (to_node, to_port),
        });
    }

    pub fn disconnect(
        &mut self,
        from_node: &str,
        from_port: &str,
        to_node: &str,
        to_port: &str,
    ) {
        self.connections.retain(|c| {
            !(c.from.0 == from_node &&
              c.from.1 == from_port &&
              c.to.0 == to_node &&
              c.to.1 == to_port)
        });
    }

    pub fn set_param(&mut self, node_id: &str, name: &str, value: f32) {
        if let Some(node) = self.nodes.get_mut(node_id) {
            node.set_param(name, value);
        }
    }
}