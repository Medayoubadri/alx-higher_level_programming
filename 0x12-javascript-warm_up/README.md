# 0x12. JavaScript - Warm up

## Background Context
JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

- Scripting (same as we did with Python)
- Web front-end
For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:600/1*ggLRwaAFVct202rIY_Jepw.png" alt="JavaScript meme">
</p>

## Project Tasks

0. First constant, first print
1. 3 languages
2. Arguments
3. Value of my argument
4. Create a sentence
5. An Integer
6. Loop to languages
7. I love C
8. Square
9. Add
10. Factorial
11. Second biggest!
12. Object
13. Add file
14. Const or not const
15. Call me Moby
16. Add me maybe
17. Increment object

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All files must be executable
- The length of your files will be tested using `wc`

## Setup

1. Install Node 14
I'll provide you with a downloadable version of the README.md file in a code block. You can copy this content and save it as a file named "README.md" in your project directory.

```markdown
# 0x12. JavaScript - Warm up

## Description
This project is an introduction to JavaScript programming. It covers basic concepts and scripting techniques, preparing us for more advanced JavaScript topics and web front-end development.

## Project Tasks

0. First constant, first print
1. 3 languages
2. Arguments
3. Value of my argument
4. Create a sentence
5. An Integer
6. Loop to languages
7. I love C
8. Square
9. Add
10. Factorial
11. Second biggest!
12. Object
13. Add file
14. Const or not const
15. Call me Moby
16. Add me maybe
17. Increment object

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All files must be executable
- The length of your files will be tested using `wc`

```

## Setup

1. Install Node 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```


2. Install semistandard

```bash
$ sudo npm install semistandard --global
```


3. Clone the repository

```bash
$ git clone `<repository-url>`
$ cd 0x12-javascript-warm_up
```

4. Make all script files executable

```bash
$ chmod +x *.js
```

## Usage

To run any script, use the following format:


```bash
$ ./script-name.js [arguments]
```

For example:


```bash
$ ./0-javascript_is_amazing.js
JavaScript is amazing

$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing

$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
```

To check if a file is semistandard compliant:


```bash
$ semistandard script-name.js
```
