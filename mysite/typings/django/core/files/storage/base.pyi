"""
This type stub file was generated by pyright.
"""

class Storage:
    """
    A base storage class, providing some default behaviors that all other
    storage systems can inherit or override, as necessary.
    """
    def open(self, name, mode=...):
        """Retrieve the specified file from storage."""
        ...
    
    def save(self, name, content, max_length=...):
        """
        Save new content to the file specified by name. The content should be
        a proper File object or any Python file-like object, ready to be read
        from the beginning.
        """
        ...
    
    def is_name_available(self, name, max_length=...): # -> bool:
        ...
    
    def get_valid_name(self, name): # -> str:
        """
        Return a filename, based on the provided filename, that's suitable for
        use in the target storage system.
        """
        ...
    
    def get_alternative_name(self, file_root, file_ext): # -> str:
        """
        Return an alternative filename, by adding an underscore and a random 7
        character alphanumeric string (before the file extension, if one
        exists) to the filename.
        """
        ...
    
    def get_available_name(self, name, max_length=...): # -> str:
        """
        Return a filename that's free on the target storage system and
        available for new content to be written to.
        """
        ...
    
    def generate_filename(self, filename): # -> str:
        """
        Validate the filename by calling get_valid_name() and return a filename
        to be passed to the save() method.
        """
        ...
    
    def path(self, name):
        """
        Return a local filesystem path where the file can be retrieved using
        Python's built-in open() function. Storage systems that can't be
        accessed using open() should *not* implement this method.
        """
        ...
    
    def delete(self, name):
        """
        Delete the specified file from the storage system.
        """
        ...
    
    def exists(self, name):
        """
        Return True if a file referenced by the given name already exists in the
        storage system, or False if the name is available for a new file.
        """
        ...
    
    def listdir(self, path):
        """
        List the contents of the specified path. Return a 2-tuple of lists:
        the first item being directories, the second item being files.
        """
        ...
    
    def size(self, name):
        """
        Return the total size, in bytes, of the file specified by name.
        """
        ...
    
    def url(self, name):
        """
        Return an absolute URL where the file's contents can be accessed
        directly by a web browser.
        """
        ...
    
    def get_accessed_time(self, name):
        """
        Return the last accessed time (as a datetime) of the file specified by
        name. The datetime will be timezone-aware if USE_TZ=True.
        """
        ...
    
    def get_created_time(self, name):
        """
        Return the creation time (as a datetime) of the file specified by name.
        The datetime will be timezone-aware if USE_TZ=True.
        """
        ...
    
    def get_modified_time(self, name):
        """
        Return the last modified time (as a datetime) of the file specified by
        name. The datetime will be timezone-aware if USE_TZ=True.
        """
        ...
    


