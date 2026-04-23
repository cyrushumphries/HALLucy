use std::collections::HashMap;
use crate::buffer::Buffer;

pub trait EngineNode {
    fn id(&self) -> &str;
    fn set_param(&mut self, name: &str, value: f32);
    fn process(&mut self, inputs: &[Buffer], outputs: &mut [Buffer]);
    fn port_info(&self) -> NodePortInfo;
}

pub struct NodePortInfo {
    pub inputs: Vec<PortDescriptor>,
    pub outputs: Vec<PortDescriptor>,
}

pub struct PortDescriptor {
    pub id: String,
    pub name: &'static str,
    pub port_type: PortType,
}

#[derive(Clone, Copy)] //adds flexibility on tiny enum, allows "passing around", because an assignment creates a copy and avoids ownership transfer
pub enum PortType {
    Audio,
    Float,
    Event,
}

pub struct EngineGraph {
    pub nodes: HashMap<NodeId, Box<dyn EngineNode>>,
    pub connections: Vec<EngineConnection>,
}

pub struct EngineConnection {
    pub from: (String, String), // NodeId, PortId
    pub to: (String, String),
}