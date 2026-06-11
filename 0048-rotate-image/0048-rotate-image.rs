impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let mut res: Vec<Vec<i32>> = vec![vec![0; matrix[0].len()]; matrix.len()];
        let mut i: usize = 0;
        let mut j: usize;

        while i < matrix.len() {
            j = 0;
            while j < matrix[0].len() {
                res[j][i] = matrix[i][j];
                j += 1;
            }
            i += 1;
        }
        for i in 0..res.len() {
            res[i].reverse();
        }

        *matrix = res;

    }
}