use pyo3::prelude::*;
use hallucy_engine::*;

#[pyclass]
pub struct RustEngine {
    graph: EngineGraph,
}

#[pymethods]
impl RustEngine {
    #[new]
    fn new() -> Self {
        Self { graph: EngineGraph::new() }
    }

    fn add_node_by_name(py_graph: &mut EngineGraph, id: String, category: String, name: String, ports: Vec<PortDescriptor>) {
        py_graph.add_node_by_name(id, category, name, ports);
    }
}

