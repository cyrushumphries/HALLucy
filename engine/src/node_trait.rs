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