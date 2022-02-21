def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se encontro el archivo")
    except IsADirectoryError:
        print("Se encontro config.txt pero es un directorio, no se puede leer")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()

try:
     open("mars.jpg")
except FileNotFoundError as err:
     print("got a problem trying to read the file:", err)
     
try:
    open("config.txt")
except OSError as err:
   if err.errno == 2:
        print("Couldn't find the config.txt file!")
   elif err.errno == 13:
        print("Found config.txt but couldn't read it")