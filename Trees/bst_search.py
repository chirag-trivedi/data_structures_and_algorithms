def search(root, key):
    if root is None:
        return None

    curr = root

    while curr is not None:
        if curr.val == key:
            return curr

        elif curr.val > key:
            curr = curr.left

        elif curr.val < key:
            curr = curr.right

    return None

# Time Complexity O(h)
# Space Complexity O(1)