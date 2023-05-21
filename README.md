# sTools
## Installation
To install sTools and use it in your project, follow the steps below.
1. Run the following in your terminal:
    ```
    git clone https://github.com/heewoonkim2020/stools.git stools_install/
    ```
2. Create **a folder** _for_ your project that uses **_sTools_**. Move the folders to make the file structure look like the following:
    ```
    ~ = Folder
    - = File

    ~ Projects
        ~ MyProject
            ~ stools_install
    ```
3. Then, navigate inside the ```stools_install``` folder. Find the ```src/stools``` folder and move it like the following:
    ```
    ~ = Folder
    - = File

    ~ Projects
        ~ MyProject
            ~ stools_install
            ~ stools
    ```
4. In your terminal, run:
    - For Windows: ```rmdir /s /q stools_install```
    - For Bash, Zsh, and Sh: ```rm -rf stools_install```
5. Then, inside your ```MyProject``` directory, create a ```main.py```, with this code inside:
    ```py
    # Import the module
    import stools

    stools.variables.set('NAME', 'World')

    # My program that uses stools
    stools.echo('Hello ($NAME)')
    
    stools.echo('A wonderful module, ($mname)!', mname='sTools')
    ```
6. You're done, have fun coding!