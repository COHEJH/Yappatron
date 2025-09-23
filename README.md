# Yappatron
**Build and run language models, quickly and easily, with minimal depression**

Yappatron is a simple project, letting you easily build (incredibly simple) language models. Coherence sold separately.

Although, conversations may still be more interesting than talking to *real* people.

# Usage (non-linear)
Simply run:
```shell
python yappatron.py
```
You likely need to install some packages. Get yourself a time machine, and utilise pip:
```shell
pip install -r requirements.txt
```
If you feel like the command line is currently beyond your capabilities, feel free to watch this helpful tutorial I made earlier: [docs.python.org/3/howto/a-beginners-guide-to-pip](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
# Models
## Markov Chain N-Gram
A simple, lightweight model which can underperform ChatGPT with ease. Works by looking at the last N words, then picking the most likely word (in its dataset) to come next. If we have a problem, we pull the trick beloved of LLMs - hallucinate. Like crazy. Not a bug, a feature. By the time the fact-checkers come running, we'll be sipping champagne in our (taxpayer-funded) private jet, courtesy of King Trump I. 
