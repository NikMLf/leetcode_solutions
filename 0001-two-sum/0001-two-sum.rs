impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut indexs: [i32; 2] = [0, 1];
        while indexs[0] < nums.len() as i32 - 1 {
            if nums[indexs[0] as usize] + nums[indexs[1] as usize] == target {break;}
            if indexs[1] == nums.len() as i32 - 1 {
                indexs[0] += 1;
                indexs[1] = indexs[0] + 1
            } else {
                indexs[1] += 1;
            }
        }
        let res: Vec<i32> = indexs.to_vec();
        res
    }
}