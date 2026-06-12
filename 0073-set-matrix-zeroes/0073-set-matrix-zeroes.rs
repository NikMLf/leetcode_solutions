impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut indexses: Vec<(usize, usize)> = vec![];
        for i in 0..matrix.len() {
            for j in 0..matrix[0].len() {
                if matrix[i][j] == 0 && !(indexses.contains(&(i, j))) { 
                    for i_ in 0..matrix.len() {
                        if matrix[i_][j] != 0 {
                            indexses.push((i_, j));
                        }
                        matrix[i_][j] = 0;                        
                    }
                    for j_ in 0..matrix[0].len() {
                        if matrix[i][j_] != 0 {
                            indexses.push((i, j_));
                        }
                        matrix[i][j_] = 0;  
                    }
                }
            }
        }
    }
}