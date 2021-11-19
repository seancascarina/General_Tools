
# MIT License==========================
"""
Copyright (c) 2021 Sean M. Cascarina

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
#======================================

# Known, error-inducing situations (which I have no intention to address in this script) that can result in skipped/non-copied files:
#   1) File paths with long names
#   2) Apostrophes in file paths

#======================================

import os

def main():

    starting_path = os.getcwd()
    output = open('BatchCommands_to_Copy_Python_Scripts.bat', 'w')
    error_log = open('Directories_Resulting_in_Error_During_BatchCommandGeneration.txt', 'w', encoding='utf-8')
    
    for (dir, dirname, files) in os.walk('.'):
        cwd = os.getcwd()

        try:
            if dir == '.':
                output.write('powershell -Command "New-Item -Path \'' + starting_path + '\' -Name \'\\Gathered_Files\' -ItemType \'directory\'"\n')
            else:
                output.write('powershell -Command "New-Item -Path \'' + starting_path + '\\Gathered_Files\' -Name \'' + dir[1:] + '\' -ItemType \'directory\'"\n')
        except:
            error_log.write(dir + '\n')

        for file in files:
            if file.endswith('.py'):
                print('powershell -Command "Copy-Item \'' + cwd + dir[1:] + '\\' + file + '\' -Destination \'' + starting_path + '\\Gathered_Files' + dir[1:] + '\'"' + '\n')
                
                # THE ''powershell -Command ' PREFIX IS NECESSARY TO RUN POWERSHELL CMDLETs FROM INSIDE A BATCH FILE
                if dir == '.':
                    output.write('powershell -Command "Copy-Item \'' + cwd + dir[1:] + '\\' + file + '\' -Destination \'' + starting_path + '\\Gathered_Files' + '\'"' + '\n')
                else:
                    output.write('powershell -Command "Copy-Item \'' + cwd + dir[1:] + '\\' + file + '\' -Destination \'' + starting_path + '\\Gathered_Files' + dir[1:] + '\'"' + '\n')
                
    output.close()
    error_log.close()

if __name__ == '__main__':
    main()