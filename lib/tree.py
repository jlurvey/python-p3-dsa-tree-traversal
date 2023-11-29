class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    def depth_first(node):
        if node is None:
           return None
        
        if node['id'] == id:
           return node
        
        for child in node ['children']:
           result = depth_first(child)
           if result: 
              return result
        
        return None
    
    return depth_first(self.root)
    
