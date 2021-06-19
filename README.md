<!-- Repository git : https://github.com/ManuSquall/squalltalk -->
# SquallTalk

<!-- Description -->
![output8](/readme/output8.png)

## Context
<!-- Why am i making this -->
the goal of this python project is to create a communication between two or more device with an GUI as Tkinter.

## Tools used
<!-- Packages, external librairies, IDE, utilitaries used -->
* [VS Code](https://code.visualstudio.com/)


## How does it work
<!-- What we have to do to make it work/run -->
1- if you want to make a communication in the same desktop (localhost)

* the "hote" of all client file must have a "localhost" value
* the port number of all files (client et server) must be the same (in this case: 15555)
* I have configure the server file to have a maximum of 4 communicators or clients (4 emission thread and 4 reception thread)
* 1 emission thread and 1 reception thread for each client file
* if you want more communicator duplicate the "client_X.py" file and add as many emission and reception thread that you want communicator


* In the command line, RUN FIRSTLY THE SERVEUR.PY FILE and ONLY AFTER IT the client files, it won't work unless that, the server must be up to exhange messages
* you can run them with the command: "py serveur.py" => "py TheFile"



## Output:

<!-- What the result is supposed to be -->

![output1](/readme/output1.png)

![output2](/readme/output2.png)

![output3](/readme/output3.png)

![output4](/readme/output4.png)

![output5](/readme/output5.png)

![output6](/readme/output6.png)

![output7](/readme/output7.png)

![output8](/readme/output8.png)

![output9](/readme/output9.png)



## About Authors / Contributors

[ManuSquall](https://manusquall.azurewebsites.net/)

## License

This project is licensed under the [CC0 1.0 Universal](https://creativecommons.org/) Creative Commons License.


## Acknowledgments
<!-- inspiration, research stuff -->
* https://wiki.python.org/moin/TkInter
* https://tkdocs.com/tutorial/index.html
*


# Made with purple 💜 lust :-)
