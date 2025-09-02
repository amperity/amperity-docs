.. https://docs.amperity.com/operator/

:orphan:

==================================================
Command shell
==================================================

.. command-shell-start

You can use a command shell to interact with certain Amperity.

.. command-shell-end


.. _command-shell-basics:

Basics
==================================================

.. command-shell-basics-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Command
     - Description
   * - **Ctrl + a**
     - Move to the beginning of a line.
   * - **Ctrl + c**
     - Stop the execution of the current command. Useful if you’ve typed something that will take a while to complete, but need to stop the command.
   * - **Ctrl + e**
     - Move to the end of a line.
   * - **Ctrl + r**
     - Search through the terminal history.

       After typing Ctrl + r start typing the command that you’re looking for and previously used commands will populate based on your search.

       To cycle through commands that use the same search term just hit Ctrl + r again.
   * - **Option + b**
     - Move back a word. On Mac OS X this requires the **Use Option as Meta key** setting to be enabled at **Terminal** > **Preferences** > **Profiles** > **Keyboard**.
   * - **Option + f**
     - Move forward a word. On Mac OS X this requires the **Use Option as Meta key** setting to be enabled at **Terminal** > **Preferences** > **Profiles** > **Keyboard**.

   * - **man**
     - Display the man page for any command

       Use **man grep** to show you all the different flags and options that you can pass to grep.

       https://xkcd.com/1168/

.. command-shell-basics-end


.. _command-shell-navigate:

Navigate
==================================================

.. command-shell-navigate-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Command
     - Description
   * - **cd directory/folder**
     - This will change your current directory to the one specified. Relative and absolute paths can be used.
   * - **cd ..**
     - Move up a directory.
   * - **cd ../..**
     - Move up two directories.
   * - **pwd**
     - Display your current location in the file hierarchy.
   * - **ls**
     - Show the files and folders in the current directory.
   * - **ls -lah**
     - Show all the files, even hidden ones and their total sizes in a human readable format.
   * - **ls -rt**
     - Show files with the newest ones at the bottom of the list.

.. command-shell-navigate-end


.. _command-shell-manipulate-files:

Manipulate files
==================================================

.. command-shell-manipulate-files-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Command
     - Description
   * - **mv file1.csv file2.csv**
     - Renames file1.csv to file2.csv.
   * - **mv file1.csv folder/file1.csv**
     - Moves file1.csv to a directory named 'subfolder'.
   * - **cp file1.csv file2.csv**
     - Makes a copy of file1.csv called file2.csv without modifying the original.
   * - **cp -r**
     - Copy all of the files in a folder recursively. You cannot copy the entire contents of a folder without this flag.
   * - **rm file1.csv**
     - Remove a file. Make sure you want to delete this file. Deletion from the terminal is permanent.
   * - **touch filename.csv**
     - Create a blank file called filenames.

.. command-shell-manipulate-files-end


.. _command-shell-inspect-files:

Inspect files
==================================================

.. command-shell-inspect-files-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Command
     - Description
   * - **less BigFile.csv**
     - Stream the contents of a file to the screen one window at a time. Ideal for viewing large files since less does not require reading the entire file for display.
   * - **head BigFile.csv**
     - Display the first 10 lines of a file
   * - **head -n 100**
     - Use the -n flag to display a specific number of rows.
   * - **file filename.csv**
     - Outputs basic information about the file format.

       Examples of output (that Amperity can easily ingest).

       ASCII text, with CRLF line terminators.

       UTF-8 Unicode text, with CRLF line terminators.
   * - **wc filename.csv**
     - Count the number of words in a file.

       Use the -l flag to display the number of lines in the file. 
   * - **cat**
     - Display the entire contents of a file to stdout. Useful for piping the contents of a file into another command.

   * - **grep "searchterm" filename.csv**
     - Will search the file for "searchterm" and return any results.

       Use the -C flag in conjunction with a number to show the number of lines before and after a result Ex: -C5 will show 11 lines in total.

       Use the -E flag will to pass regex to grep rather than a simple search string.

.. command-shell-inspect-files-end


.. _command-shell-move-files:

Move files
==================================================

.. command-shell-move-files-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Command
     - Description
   * - **scp file.txt prod:/mnt/folder/file.txt**
     - Copy myfile.txt from your local machine to a remote machine.

.. command-shell-move-files-end


.. _command-shell-tmux:

tmux
==================================================

.. command-shell-tmux-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Command
     - Description
   * - **tmux new -s SessionName**
     - Start a new tmux session.
   * - **tmux a -t SessionName**
     - Connect to a previously created named tmux session.
   * - **tmux ls**
     - List all tmux sessions.
   * - **Ctrl + b, d**
     - Detach from tmux while in an active session.
   * - **Ctrl + b, ?**
     - Show all tmux options
   * - **Ctrl + [**
     - Move around the terminal with the arrow keys.

.. command-shell-tmux-end


.. _command-shell-redirect-stdout:

Redirect stdout
==================================================

.. command-shell-redirect-stdout-start

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - Command
     - Description
   * - **>**
     - After a command will take the output of that command and write it to a file. For example:

       .. code-block:: console

          $ head BigFile.csv > SmallFile.csv

       will take the first 10 lines from BigFile.csv and write them to the new file SmallFile.csv. If SmallFile.csv exists it will be overwritten. If it does not exist it will be created.
   * - **>>**
     - Can be used to concatenate results onto a file.  For example:

       .. code-block:: console

          $ head MediumFile.csv >> SmallFile.csv

       will take the first 10 lines from MediumFile.csv and append them to SmallFile.csv.

.. command-shell-redirect-stdout-end
