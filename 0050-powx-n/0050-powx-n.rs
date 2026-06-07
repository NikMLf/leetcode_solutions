impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        let mut n_long = n as i64;
        let mut current_x = if n_long < 0 { 1.0 / x } else { x };
        let mut current_n = n_long.abs();
        
        let mut result = 1.0;
        
        while current_n > 0 {
            if current_n % 2 == 1 {
                result *= current_x;
            }
            current_x *= current_x;
            current_n /= 2;
        }
        
        result
    }
}