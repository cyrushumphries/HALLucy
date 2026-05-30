use pyo3::prelude::*;
use musicvfx_engine::*;

#[pyclass]
pub struct RustEngine {
    graph: EngineGraph,
}