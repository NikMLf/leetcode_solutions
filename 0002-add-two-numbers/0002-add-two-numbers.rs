// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut res: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut current_res = &mut res;
        let mut current_l1 =  & l1;
        let mut current_l2 = & l2;
        let mut i: i32 = 0;
        while current_l1.is_some() || current_l2.is_some() || i != 0 {
            let mut sum: i32 = i;
            if let Some(node) = current_l1 {
                let val1 = node.val;
                sum += val1;
                current_l1 = &node.next;
            }

            if let Some(node) = current_l2 {
                let val2 = node.val;
                sum += val2;
                current_l2 = &node.next;
            }

            if let Some(node) = current_res {
                node.next = Some(Box::new(ListNode::new(sum % 10)));
                current_res = &mut node.next;
            }
            i = sum / 10;
            
        }
        res.unwrap().next

    }
}