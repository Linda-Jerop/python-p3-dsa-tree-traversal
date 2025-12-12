class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    """
    Traverse the tree using depth-first search to find a node by its id.
    
    This method searches through the tree structure to find and return the 
    first node that has a matching 'id' attribute. If no matching node is 
    found, it returns None.
    
    Args:
        id: The id string to search for in the tree nodes
        
    Returns:
        The node dictionary with the matching id, or None if not found
    """
    # Initialize an empty list to store the final result
    # This will hold the node we're looking for once found
    result = []
    
    # Initialize the list of nodes we need to visit with the root node
    # This acts as our queue/stack for traversing the tree
    nodes_to_visit = [self.root]
    
    # Continue traversing while there are still nodes to visit
    # This loop will process each node one at a time
    while len(nodes_to_visit) > 0:
      # Step 1: Remove the first node from the nodes_to_visit list
      # pop(0) removes and returns the element at index 0 (the first element)
      node = nodes_to_visit.pop(0)
      
      # Step 2: Check if this node's id matches the id we're searching for
      # If it matches, add the entire node to our result list
      if node.get('id') == id:
        result.append(node)
      
      # Step 3: Add this node's children to the BEGINNING of nodes_to_visit
      # This is what makes it depth-first: we explore children before siblings
      # By adding children to the beginning, we visit them next (LIFO - Last In, First Out)
      nodes_to_visit = node['children'] + nodes_to_visit
    
    # Return the first (and only) node in the result list if found
    # If result is empty, this returns None (default for list access)
    # We use result[0] if result else None to safely return None when list is empty
    return result[0] if result else None
