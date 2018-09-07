# bohora: better open hacks on recurring actions

Project documentation for Python package `bohora`

---

## Overview

As the name suggests, this package provides some outstanding magical tricks/methods which are very useful and frequently encountered in research, statistics and data science.

## Few Examples

- **is_palindrome()**

```r
is_palindrome("Was It A   Rat    I Saw?", remove_punctuation=True)
True
```
- **to_any_case()**
```r
to_any_case(x, case = 'screaming_snake_case')
'THIS_IS_A_STRANGE_STRING_2'
to_any_case(x, case = 'snake_case')
'this_is_a_strange_string_2'
to_any_case(x, case = 'upper_camel_case')
'ThisIsAStrangeString2'
to_any_case(x, case = 'upper_lower')
'thisISaSTRANGEstring2'
to_any_case(x, case = "parsed_case")
'this_Is_a_Strange_string_2'
to_any_case(x, case = "swap_case")
'THIS iS A sTRANGE_STRING 2'
```

- **nepalese_words_to_number()**

```r
x = "ek karod paanch hajaar paanch saya paanch" 
nepalese_words_to_number(x)
10005505
```

- **kmers_of()**

```r
x = 'Find three kmers'
kmers_of(x,3, remove_space=True)
['Fin', 'ind', 'ndt', 'dth', 'thr', 'hre', 'ree', 'eek', 'ekm', 'kme', 'mer', 'ers']
```

## Installation  

Here is the [GitHub](https://github.com/sbohora/bohora) repository for `bohora`

You can install `bohora` via GitHub

`$ git clone https://github.com/sbohora/bohora.git`

The following installation method is not currently available.

`$ pip install bohora`

## Developer

I am Som and am a statistician at [The Department of Pediatrics, The University of Oklahoma Health Sciences Center](http://ouhsc.edu/bbmc/team/). I received my MApStat and MS in Biostatistics from LSU and OUHSC, respectively. In addition to BBMC, I work as a statistician and data programmer in a number of pediatric research projects. I was trained in biostatistics and epidemiology, and has research experience in Fetal Alcohol Spectrum Disorders (FASD), HIV/AIDS clinical trials and child maltreatment prevention. I am interested in the applications of statistical computing and simulation, data analytics, dynamic reporting, automating tasks and real-time data decision making. I use mainly R, Python, SQL, and many other programming languages. 

