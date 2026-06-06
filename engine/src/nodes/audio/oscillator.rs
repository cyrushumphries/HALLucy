use crate::node_trait::{EngineNode, NodePortInfo, PortDescriptor, PortType};
use crate::buffer::Buffer;

pub struct Oscillator {
    id: String,
    freq: f32,
}

impl Oscillator {
    pub const NAME: &'static str = "Oscillator";
    pub const CATEGORY: &'static str = "audio";

    pub fn new(id: String) -> Self {
        Self { id, freq: 440.0 }
    }
}

impl EngineNode for Oscillator {
    fn id(&self) -> &str {
        &self.id
    }

    fn set_param(&mut self, name: &str, value: f32) {
        if name == "freq" {
            self.freq = value;
        }
    }

    fn port_info(&self) -> NodePortInfo {
        NodePortInfo {
            inputs: vec![
                PortDescriptor {
                    id: "freq".into(),
                    name: "freq",
                    port_type: PortType::Float,
                }
            ],
            outputs: vec![
                PortDescriptor {
                    id: "out".into(),
                    name: "out",
                    port_type: PortType::Audio,
                }
            ],
        }
    }

    fn process(&mut self, _inputs: &[Buffer], _outputs: &mut [Buffer]) {
        // DSP here
    }
}
