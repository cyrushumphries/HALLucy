use pyo3::prelude::*;
use hallucy_engine::*;

#[pyclass]
pub struct RustEngine {
    graph: EngineGraph,
}