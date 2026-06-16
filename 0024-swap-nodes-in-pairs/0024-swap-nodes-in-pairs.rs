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
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode {val: 0, next: head} ));
        let mut current = &mut dummy;

        while current.as_ref()?.next.is_some() && current.as_ref()?.next.as_ref()?.next.is_some() {
            let mut node1 = current.as_mut()?.next.take();
            let mut node2 = node1.as_mut()?.next.take();

            let next_pair = node2.as_mut()?.next.take();
            node1.as_mut()?.next = next_pair;
            node2.as_mut()?.next = node1;
            current.as_mut()?.next = node2;


            current = &mut current.as_mut()?.next.as_mut()?.next; 

        }
        dummy?.next
    }
}