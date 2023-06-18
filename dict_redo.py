#!/usr/bin/env python3

class RedoDictionary():
    def __init__(self):
        self._dict = {}

        self._stack_redo = []
        self._stack_undo = []

    def set(self, key, value):
        self._stack_undo.append(('add', key, value))
        self._dict[key] = value

    def get(self, key):
        return self._dict[key]

    def delete(self, key):
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
