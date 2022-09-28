# [Working with text (CLI)]
[Getting familiar with standard input and standard output of the commands and how to redirect them.]

## Key terminology
[stdin: Standard Input, is the standard source of the data you enter. It refers by default to the the keyboard and what you type with it, and can be changed (redirected).

stdout: Standard Output, is the standard destination where the result of the entered command will be printed. It refers by default to the screen (the terminal), and can be changed (redirected).

Input Redirection: Changing the source of the input to be different from the keyboard, a file for example.

Output Redirection: Changing the destination where the result of a command will be printed to be different from the terminal, a file for example.

Pipe: Is a command in linux with the syntax '|' used to link two commands together, so that the output of the command before the | becomes the input of the command after the |.
]

## Exercise
Used the echo command to write a new sentence (line) to the new_text.txt file, and then used the grep command to filter for a line and then a word and redirected that word to a new text file (techgrounds.txt).
### Sources
[1. https://www.educative.io/answers/how-to-do-input-output-redirection-in-linux

2. https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/

3. 
]

### Overcome challenges
[I was at first using the sed tool to filter the content of the file. After consulting with my teammates I found out that I'm better off using the grep command.]

### Results
![Filtering_for_line](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/7b217c4747c90c084052079732fe90249c4f7d3a/00_includes/Linux/Filtering_for_line.png)
![stdout_redirection](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/7b217c4747c90c084052079732fe90249c4f7d3a/00_includes/Linux/stdout_Redirection.png)