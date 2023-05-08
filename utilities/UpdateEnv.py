
import os
import dotenv

def updateEnvVar(varName, newValue):

    """
    updates an enviroment variable

    Args:
        variable_ name (str): the name of the variable \n
        variable_value (str): the value of the vaiable \n

    Returns:
        (bool) - true \n
    """
    
    #gets .env file 
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    #updates enviroment variable
    os.environ[varName] = newValue

    #adds or Updates a key/value
    dotenv.set_key(dotenv_file, varName, os.environ[varName])

    return True