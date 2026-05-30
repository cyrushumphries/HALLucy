use std::collections::HashMap;
use crate::buffer::Buffer;

pub trait EngineNode { //traits are comparable to java interfaces (but much more powerful)
    fn id(&self) -> &str;
    fn set_param(&mut self, name: &str, value: f32);
    fn process(&mut self, inputs: &[Buffer], outputs: &mut [Buffer]);
    fn port_info(&self) -> NodePortInfo;
}

//An engineNode has inputs and outputs, grouped in a struct
pub struct NodePortInfo {
    pub inputs: Vec<PortDescriptor>,
    pub outputs: Vec<PortDescriptor>,
}

//A Port has an id, name and a type
pub struct PortDescriptor {
    pub id: String,
    pub name: &'static str,
    pub port_type: PortType,
}

//Available port types are:
#[derive(Clone, Copy)] //adds flexibility on tiny enum, allows "passing around", because an assignment creates a copy and avoids ownership transfer
pub enum PortType {
    Audio,
    Float,
    Event,
}

//The engine graph has nodes and connections between the nodes 
pub struct EngineGraph {
    //map between NodeID and pointer to EngineNode
    pub nodes: HashMap<String, Box<dyn EngineNode>>, //dyn -> Nodes will be of different types but all type will be impelemting the EngineNode Trait
    //Box -> Rust needs all items in a collection to be of dame size, which is impossible with different Node types
    //Box is a fixed size pointer to the heap, nodes will be on the heap, hashmap stores the pointers
    pub connections: Vec<EngineConnection>,
}

//A connection between specific node ports (as a node can have multiple ports)
//from NodeID,PortID to NodeID,PortID
pub struct EngineConnection {
    pub from: (String, String), // NodeId, PortId
    pub to: (String, String),
}