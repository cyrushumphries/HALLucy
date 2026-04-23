pub struct Buffer {
    pub samples: Vec<f32>,
}

impl Buffer {
    pub fn new(size: usize) -> Self {
        Self {
            samples: vec![0.0; size],
        }
    }

    pub fn clear(&mut self) {
        for s in &mut self.samples {
            *s = 0.0;
        }
    }
}
