# random access memory (RAM) is volatile which loses its data when computer is turned off.
# non-volatile memory = permanent memory
# File Operation takes place in the following order.
    # Open a file
    # Read or write (perform operation)
    # Close the file
# when working with files in text mode, it is highly recommended to specify the encoding type.
# A safer way is to use a try...finally block.
# with open => This ensures that the file is closed when the block inside with is exited, We don't need to explicitly call the close() method. It is done internally.
# -------------------------------------------------------------------------
# File Modes :
# 'r'	Open a file for reading. (default)
# 'w'	Open a file for writing. Creates a new file if it does not exist or truncates/erase the file if it exists.
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
# 'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# 't'	Open in text mode. (default)
# 'b'	Open in binary mode.
# '+'	Open a file for updating (reading and writing)
# -------------------------------------------------------------------------
# File Operations :
# close()	Close an open file. It has no effect if the file is already closed.
# detach()	Separate the underlying binary buffer from the TextIOBase and return it.
# fileno()	Return an integer number (file descriptor) of the file.
# flush()	Flush the write buffer of the file stream.
# isatty()	Return True if the file stream is interactive.
# read(n)	Read atmost n characters from the file. Reads till end of file if it is negative or None.
# readable()    Returns True if the file stream can be read from.
# readline()  method to read individual lines of a file. This method reads a file till the newline, including the newline character.
# readlines()  method returns a list of lines of the entire file.
# readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
# readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
# seekable()	Returns True if the file stream supports random access.
# tell()	Returns the current file location.
# truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
# writable()	Returns True if the file stream can be written to.
# write(s)	Write string s to the file and return the number of characters written.
# writelines(lines)	Write a list of lines to the file.
# -------------------------------------------------------------------------