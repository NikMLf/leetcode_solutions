impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        if s.len() == 0 {
            return 0;
        }
        let chars: Vec<char> = s.chars().collect();
        let mut max:usize = 0;
        let mut start: usize = 0;
        let mut stop: usize = 1;
        while stop < s.len() {
            let current_char = chars[stop];
            let mut found_dup = false;
            let mut dup_idx = 0;

            for i in start..stop {
                if chars[i] == current_char {
                    found_dup = true;
                    dup_idx = i;
                    break;
                }
            }

            if found_dup {
                start = dup_idx + 1;
            }

            if stop - start > max {
                max = stop - start;
            }

            stop += 1;

        }
        max as i32 + 1

    }
}