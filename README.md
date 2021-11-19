# General_Tools
This is a Python script that writes a batch file containing all commands necessary to re-create your directory structure and copy all Python scripts (i.e. those ending in ".py"). The batch file is specific for Windows Powershell and will not work on other operating systems. To back up all Python files in your desktop and all subdirectories, place this script on your desktop and run the commands indicated below in-sequence. Use at your own risk, per the associated license disclaimers.

## Basic Usage
$ python write_BatchFile_Gather_PythonScripts.py
$ BatchCommands_to_Copy_Python_Scripts.bat

The Python script generates the batch file (BatchCommands_to_Copy_Python_Scripts.bat) with commands to make directories and copy Python files, as well as an error log file (Directories_Resulting_in_Error_During_BatchCommandGeneration.txt) that will list any commands that could not be written to the batch file (usually due to unusual characters in directory names).

## Optional
To log all commands that were executed when running the batch file, try:
$ Start-Process -FilePath 'C:\YourPathToBatchFile\BatchCommands_to_Copy_Python_Scripts.bat' -RedirectStandardOutput 'C:\YourDesiredPathToLogFile\BatchLog.txt' -Wait -WindowStyle Hidden

This should contain all commands that ran during batch file execution, as well as errors when trying to run any of the commands. Currently, two situations are known to cause issues, which I have no intention to address in the script:
1) File paths with long names
2) Apostrophes in file paths

## License info
write_BatchFile_Gather_PythonScripts.py is subject to the terms of the MIT license.
