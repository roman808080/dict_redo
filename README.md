# Dictionary with undo/redo functionality

This repository contains a simple code that demonstrates an implementation of a dictionary with undo and redo functionality. The task was initially received during an interview.

After the interview, the solution was improved in the following two cases:
* Fixed an issue with setting a new value for an old key.
* Cleared the redo stack after set and delete actions.

The code currently does not limit the size of the stacks, which should be implemented for better efficiency.
Additionally, other cases like multithreading are not handled in this repository.