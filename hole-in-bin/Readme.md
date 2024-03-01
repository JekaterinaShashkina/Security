# Hole in bin

## Objective

This exercise is designed to test skills and understanding of binary exploitation and reverse engineering. You will need to work through a series of binary exploitation challenges using a provided virtual machine.

Audit questions https://github.com/01-edu/public/blob/master/subjects/cybersecurity/hole-in-bin/audit/README.md

1. Download the virtual machine file `hole-in-bin.ova`. Install and launch the machine in VirtualBox.
   Username: user, Password: user
2. Access the specified address mentioned in the description: `/opt/hole-in-bin`
3. In the directory, there are 12 new folders - 12 exercises.

## ex00.

The first task in the README.md file

This level is completed when you see the "You have changed the 'modified' variable" message.

Run the bin file using the command `./bin` to see what happens when it's executed.

`objdump -d bin` - This command outputs the disassembled machine code of the executable file.

Use this information to analyze how the program handles the modified variable.

![exercise 1 image 1](/img/ex00_1.png)

Open the file in the vim editor: `vim bin`. It opens as a binary file.

`:%!xxd` is a command used within vim that converts the code to hexadecimal format.

Locate the line with the variable, which is line 400 with the data `5c00`, and change the data to `0000`.

Then return to the binary file: `:%!xxd -r`, and save it to a new file: `:wq! /home/user/newfile`.

Run the file `./newfile`.

![execise 1 image 3](/img/ex00_3.png)

## ex01.

To begin, let's run the program `./bin` and view the README.md file.

![execise 2 image 1](/img/ex01_1.png)

Next, we'll use the disassembler `objdump -d bin`.

We look for points where the program might check or modify variable values.

![execise 2 image 2](/img/ex01_2.png)

We see at line `80484ab` comparison instructions (cmp) and conditional jumps (jne, which means "jump if not equal") are often used to check conditions and change the program's execution flow based on the comparison results.

We open the file in the vim `vim bin`, just like in the previous exercise, change the binary file to a more readable format `:%!xxd`, and find the variable to be changed at line 75. We change `6463 6261` to `0000 0000`.

![execise 2 image 3](/img/ex01_3.png)

Save the modified file as `newfile1`

`:%!xxd -r`

`:wq! /home/user/newfile1`.

Use the command `chmod +x newfile1` to make the file executable.

Run `./newfile1 1`.

![execise 2 image 4](/img/ex01_4.png)

## ex02.

Go to the directory `opt/hole-in-bin/ex02` for the next task.

Run the file `./bin`. The message indicates that the program requires the `GREENIE` environment variable to work.

![execise 3 image 1](/img/ex02_1.png)

Run the file with the GREENIE variable `GREENIE=x ./bin`.

![execise 3 image 2](/img/ex02_2.png)

Likely, for successful completion of this level, the GREENIE variable needs to contain a specific value.

Next, use the disassembler `objdump -d bin | less`.

![execise 3 image 3](/img/ex02_3.png)

The instruction `cmp $0xd0a0d0a,%eax` compares the content of the register %eax with the specific value 0xd0a0d0a. To successfully complete the task, it's necessary to set the GREENIE variable to a value that, after processing by the program, passes all checks, including comparison with the value 0xd0a0d0a.

Open `vim bin`, as in the previous tasks, convert everything to a more readable format `:%!xxd`.

Locate the line

![execise 3 image 4](/img/ex02_4.png)

and change the data from `3d0a` to `000a`.

Exit to binary code `:%!xxd -r` and save it to a new file `newfile2` `:wq! /home/user/newfile2`.

Modify the file to be executable `chmod +x newfile2` and check the result `./newfile2`.

![execise 3 image 5](/img/ex02_5.png)

## ex03.

Go to the directory of the next task, run the bin file `./bin`, then read what is written in the README.md file "This level is complete when you see the "code flow successfully changed" message."

![execise 4 image 1](/img/ex03_1.png)

Use `objdump -d bin | less`.

The function `win` is presumably the function that needs to be called to receive the "code flow successfully changed" message.

![execise 4 image 2](/img/ex03_2.png)

- The address of the win function is: 08048424.
- The address of the main function is: 08048438.

Open the binary file in the hexadecimal editor `vim` `vim bin` `:%!xxd`.

Find the location corresponding to the return address of the `main` function, which needs to be changed to the address of the `win` function. The address of the win function in hexadecimal will be represented as `2484 0408`, and main as `3384 0408`.

On line 57, change `3384` to `2484`.

![execise 4 image 3](/img/ex03_3.png)

Exit to binary code `:%!xxd -r` and save it to a new file exercise3 `:wq! /home/user/exercise3`.

Modify the file to be executable `chmod +x newfile2` and check the result `./exercise3`.

![execise 4 image 4](/img/ex03_4.png)

## ex04

The next task seems similar to the previous one.

![execise 5 image 1](/img/ex04_1.png)

Use `objdump -d bin | less`.

![execise 5 image 2](/img/ex04_2.png)

- The address of the win function is: `080483f4`.
- The address of the main function is: `08048408`.

Open the binary file in the hexadecimal editor vim `vim bin` `:%!xxd`, find the location corresponding to the return address of the `main` function, which needs to be changed to the address of the `win` function.

The address of the win function in hexadecimal will be represented as `f483 0408`, and main as `0884 0408`.

![execise 5 image 3](/img/ex04_3.png)

Change `0884 0408` to `f483 0408` on line 54.

Exit to binary code `:%!xxd -r` and save it to a new file exercise4 `:wq! /home/user/exercise3`.

Modify the file to be executable `chmod +x newfile2` and check the result `./exercise4`.

![execise 5 image 4](/img/ex04_4.png)

## ex05

The next task is as follows:

![execise 6 image 1](/img/ex05_1.png)

Continue examining the file using `objdump -d bin | less`

Find the line with the `jne` operation code in `vuln`. This can be used to change the program's execution flow.

![execise 6 image 2](/img/ex05_2.png)

Open `vim bin`, convert to hexadecimal format with `:%!xxd`.

Find `de75` on line 66 and change it to `de74`.

This change alters the behavior of this specific instruction from `jne` to `je`, modifying the logic of the conditional jump.

![execise 6 image 3](/img/ex05_3.png)

`:!xxd -r`, `:wq! /home/user/exercise05` Exit to binary code, save to file.

`chmod +x exercise05` Make the file executable.

`./exercise05` Run the file.

![execise 6 image 4](/img/ex05_4.png)

## ex06

Run the `./bin` file and read the task in README.md: "This level is completed when you see the 'that wasn't too bad now, was it?' message."

![execise 7 image 1](/img/ex06_1.png)

Use `objdump -d bin | less`, we see the `winner` and `main` functions.

- The address of the `winner` function is: 08048864
- The address of the `main` function is: 08048889

![execise 7 image 2](/img/ex06_2.png)

We open the binary file in hexadecimal editor `vim bin`.

`:%!xxd`

The address of the winner function in hexadecimal will be represented as `6488 0408`, and main as `8988 0408`.

We find `8988 0408` on line 125 and change it to `6488 0408`.

`:%!xxd -r` we exit to binary format, `:wq! /home/user/exercise06` save to file

`chmod +x exercise06` modify the file's permissions

Then execute it.

![execise 7 image 3](/img/ex06_3.png)

## ex07

Run the `./bin` and read in README.md file the new task: "This level is completed when you see the "you have modified the target" message"
![exercise 8 image 1](/img/ex07_1.png)

Open the file using `objdump -d bin | less`, searching for the `vuln` and `main` functions. In the vuln function, there is an instruction `8048492` `jne`. Changing this condition might alter the entire algorithm.

![exercise 8 image 2](/img/ex07_2.png)

Enter the binary file with `vim bin`, convert it to hexadecimal view `:%!xxd`.

On line 74, we find `750e c704` and change it to `740e c704`.

![execise 8 image 3](/img/ex07_3.png)

`:%!xxd -r` exit to binary code, `:wq! /home/user/exercise07` save to a new file.

`chmod +x exercise07` modify the file's permissions

![execise 8 image 4](/img/ex07_4.png)

## ex08

The next exercise resembles ex07.

![execise 8 image 1](/img/ex08_1.png)

We open the file using `objdump -d bin | less`.

![execise 8 image 2](/img/ex08_2.png)

Enter the binary file with `vim bin`, convert it to hexadecimal view `:%!xxd`.

On line 75, `0175 0ec7`, we change it to `0174 0ec7`.

![execise 8 image 3](/img/ex08_3.png)

`:%!xxd -r` exit to binary code, `:wq! /home/user/exercise08` save to a new file.

`chmod +x exercise08` modify the file's permissions

![execise 8 image 4](/img/ex08_4.png)

## ex09

Run the `./bin` file and read the task in README.md: "This level is completed when you see the 'code execution redirected!' message."

![execise 9 image 1](/img/ex09_1.png)

Use `objdump -d bin | less`, we see the `hello` and `main` functions.

- The address of the `hello` function is: 080484b4
- The address of the `main` function is: 08048514

![execise 9 image 2](/img/ex09_2.png)

![execise 9 image 3](/img/ex09_3.png)

We open the binary file in hexadecimal editor `vim bin`.

`:%!xxd`

The address of the hello function in hexadecimal will be represented as `b484 0408`, and main as `1485 0408`.

We find `1485 0408` on line 66 and change it to `b484 0408`.
![execise 9 image 4](/img/ex09_4.png)

`:%!xxd -r` we exit to binary format, `:wq! /home/user/exercise09` save to file

`chmod +x exercise09` modify the file's permissions

Then execute it.

![execise 9 image 5](/img/ex09_5.png)

## ex10

Run the `./bin` file and read the task in README.md: "This level is completed when you see the 'level passed' message."

![execise 10 image 1](/img/ex10_1.png)

Use `objdump -d bin | less`, we see the `winner` and `main` functions.

- The address of the `winner` function is: 08048464
- The address of the `main` function is: 0804848c

![execise 10 image 2](/img/ex10_2.png)

We open the binary file in hexadecimal editor `vim bin`.

`:%!xxd`

The address of the winner function in hexadecimal will be represented as `6484 0408`, and main as `8c84 0408`.

We find `8c84 0408` on line 61 and change it to `6484 0408`.

![execise 10 image 3](/img/ex10_3.png)

`:%!xxd -r` we exit to binary format, `:wq! /home/user/exercise10` save to file

`chmod +x exercise10` modify the file's permissions

Then execute it.

![execise 10 image 4](/img/ex10_4.png)

## ex11

Run the `./bin` file and read the task in README.md: "This level is completed when you see the 'and we have a winner' message."

![execise 11 image 1](/img/ex11_1.png)

Use `objdump -d bin | less`, we see the `winner` and `main` functions.

- The address of the `winner` function is: 08048494
- The address of the `main` function is: 080484b9

![execise 11 image 2](/img/ex11_2.png)

Open the binary file in hexadecimal editor `vim bin`.

`:%!xxd`

The address of the winner function in hexadecimal will be represented as `9484 0408`, and main as `b984 0408`.

We find `b984 0408` on line 64 and change it to `9484 0408`.

![execise 11 image 3](/img/ex11_3.png)

`:%!xxd -r` we exit to binary format, `:wq! /home/user/exercise11` save to file

`chmod +x exercise11` modify the file's permissions

Then execute it.

![execise 11 image 4](/img/ex11_4.png)

## Author

Catharin
