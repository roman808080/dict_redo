#!/usr/bin/env python3

class RedoDictionary():
    def __init__(self):
        self._dict = {}

        self._stack_redo = []
        self._stack_undo = []

    def set(self, key, value):
        if key in self._dict:
            self._stack_undo.append(('set', key, self._dict[key]))
        else:
            self._stack_undo.append(('delete', key))

        self._dict[key] = value

    def get(self, key):
        return self._dict[key]

    def delete(self, key):
        self._stack_undo.append((('set', key, self._dict[key])))
        del self._dict[key]

    def undo(self):
        action, key, old_value = self._stack_undo.pop()

        if action == 'set':
            # Saving the current value to the redo list before we reset it
            self._stack_redo.append(('set', key, self._dict[key]))
            self._dict[key] = old_value

        else:
            # Otherwise we need to delete and to add delete action to the redo list
            self._stack_redo.append(('delete', key))
            del self._dict[key]

    def redo(self):
        action, key, old_value = self._stack_redo.pop()

        if action == 'set':
            self._stack_undo.append(('set', key, self._dict[key]))
            self._dict[key] = old_value
        else:
            self._stack_undo.append(('delete', key))
            del self._dict[key]
