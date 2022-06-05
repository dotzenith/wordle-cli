<h2 align="center"> ━━━━━━  ❖  ━━━━━━ </h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   
   <img src="https://img.shields.io/github/stars/dotzenith/wordle-cli?color=F8BD96&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/forks/dotzenith/wordle-cli?color=DDB6F2&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/repo-size/dotzenith/wordle-cli?color=ABE9B3&labelColor=302D41&style=for-the-badge">
   
   <img src="https://badges.pufler.dev/visits/dotzenith/wordle-cli?style=for-the-badge&color=96CDFB&logoColor=white&labelColor=302D41"/>
   <br>
</div>

<p/>

---

### ❖ Information 

  wordle-cli is, as the name suggests, wordle in the command-line. There are no fancy gui/tui elements, just a simple and minimalistic way to play wordle :)

  <img src="assets/wordle.gif" alt="wordle preview">

---

### ❖ Installation

> Install from pip
```sh
$ pip3 install wordlecli
```

> Install from source
- First, install [poetry](https://python-poetry.org/)
```sh
$ git clone https://github.com/ZenithDS/wordle-cli.git
$ cd wordle-cli
$ poetry build
$ pip3 install ./dist/wordlecli-0.2.2.tar.gz
```

### ❖ Usage 

Playing wordle in the command-line is as simple as running the following command:

```sh
$ wordle
```

But if your addiction to wordle needs more, you can also play an older wordle by specifying it's number

```sh
$ wordle 240
```

The on-screen keyboard can be turned off using the `--hard` option

```sh
$ wordle --hard
```

---

### ❖ What's New? 
0.2.2 - Updated `words.py` to be consistent with the official wordle

---

<div align="center">

   <img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=F5E0DC&labelColor=302D41&style=for-the-badge">

</div>

