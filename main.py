class RedoDictionary():
    def __init__(self):
        self._dict = {}

        self._stack_redo = []
        self._stack_undo = []
        
    def add(self, key, value):
        if key in self._stack_undo:
            self._stack_undo.append(('add', key, None, None))

        self._stack_undo.append(('add', key, value, None))
        self._dict[key] = value
        
    def get(self, key):
        return self._dict[key]
        
    def remove(self, key):
        removed_value = self._dict[key]
        self._stack_undo.append(('remove', key, removed_value))
        del self._dict[key]
        
    def undo(self):
        action, key, value = self._stack_undo.pop()
        
        if action == 'add':
            del self._dict[key]
        else:
            self._dict[key] = value
            
        self._stack_redo.append((action, key, value))
        
    def redo(self):
        action, key, value = self._stack_redo.pop()
        
        if action == 'add':
            self._dict[key] = value
        else:
            del self._dict[key]
            
        self._stack_undo.append((action, key, value))


our_dict = RedoDictionary()
our_dict.add('a', 3)
assert our_dict.get('a') == 3

our_dict.remove('a')
# assert our_dict.get('a') == 3

our_dict.undo()
assert our_dict.get('a') == 3

our_dict.redo()
# assert our_dict.get('a') == 3

our_dict.undo()
assert our_dict.get('a') == 3

our_dict.add('b', 3)
our_dict.add('b', 5)
our_dict.undo();
assert our_dict.get('b') == 3