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
            self._stack_undo.append(('delete', key, value))

        self._dict[key] = value

    def get(self, key):
        return self._dict[key]

    def delete(self, key):
        self._stack_undo.append((('set', key, self._dict[key])))
        del self._dict[key]

    def undo(self):
        self._reverse_action(self._stack_undo, self._stack_redo)

    def redo(self):
        self._reverse_action(self._stack_redo, self._stack_undo)

    def _reverse_action(self, input_stack, output_stack):
        action, key, old_value = input_stack.pop()

        # 1. action set and we have a key inside the dictionary tren we need to save the current value to redo and restore the old one
        # 2. action set and we do not have the key in the dictionary then we need to save delete to redo
        # 3. action delete then we need to save action set to redo

        if action == 'set' and key in self._dict:
            # Saving the current value to the redo list before we reset it
            # to the previous value

            output_stack.append(('set', key, self._dict[key]))
            self._dict[key] = old_value

        elif action == 'set' and key not in self._dict:
            # We reverse delete action, and we need to save it for redo

            output_stack.append(('delete', key, old_value))
            self._dict[key] = old_value

        else:
            # Otherwise we need to delete
            # and to add a set action to the redo list.

            output_stack.append(('set', key, old_value))
            del self._dict[key]
