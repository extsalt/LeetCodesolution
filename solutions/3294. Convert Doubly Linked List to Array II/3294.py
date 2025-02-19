class Solution:
  def toArray(self, node: 'Optional[Node]') -> List[int]:
    ans = []
    curr = node

    while curr.prev:
      curr = curr.prev

    while curr:
      ans.append(curr.val)
      curr = curr.next

    return ans
