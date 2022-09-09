import subprocess
import os

def runCommand(command):
    command=command.split("--->>")
    print("commandlist ",command)
    os.chdir(command[0])                #whatever is coming from palette, current directory will be changed to that
    cdComm=command[1].split(" ")
    print(cdComm)
    if cdComm[0]=='cd':
        try:
            os.chdir(cdComm[1])
            print("current:",os.getcwd())
            return "cd success"
        except Exception as e:
            return str(e)
    else:
        result = subprocess.Popen(cdComm, shell=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = result.communicate()
        if error:
            return error.decode("utf-8")
        else:
            return output.decode("utf-8")