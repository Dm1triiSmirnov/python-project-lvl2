# Difference Calculator

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Dm1triiSmirnov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Dm1triiSmirnov/python-project-lvl2/actions)
[![Python-CI](https://github.com/Dm1triiSmirnov/python-project-lvl2/actions/workflows/pyci.yml/badge.svg?branch=main)](https://github.com/Dm1triiSmirnov/python-project-lvl2/actions/workflows/pyci.yml)
<a href="https://codeclimate.com/github/Dm1triiSmirnov/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/21d0f1863670dd2c0671/maintainability" /></a>
<a href="https://codeclimate.com/github/Dm1triiSmirnov/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/21d0f1863670dd2c0671/test_coverage" /></a>


<br>


The Difference Calculator is a program for developing differentiation between two data structures.


<br>


### Utility features:
<ul>
<li>Support for different input formats: yaml, json
<li>Report generation in the form of plain text, stylish and json
</ul>


<br>


### Commands:
gendiff [-h] [-f FORMAT] first_file second_file

<br>

  -h, --help            show help message and exit

  -f, --format          set format of output

<br>

### Example: 
gendiff --format json filepath1.json filepath2.json

<br>

### Dependencies:
<table>
    <tr>
        <th>python</th>
        <th>^3.8</th>
    </tr>
    <tr>
        <th>argparse</th>
        <th>^1.4.0</th>
    </tr>
</table>


<br>

### MAKE file:
<ul>
<li>make install
<li>make build
<li>make package-install
</ul>


<br>


### Demonstration:

<ol>
<li>Compare flat JSON files</li>
<a href="https://asciinema.org/a/3XlmN2TOFOpyIvKrr7ACPPK2n" target="_blank"><img src="https://asciinema.org/a/3XlmN2TOFOpyIvKrr7ACPPK2n.svg" /></a>

<li>Compare flat YAML files</li>
<a href="https://asciinema.org/a/nVRUnFPaIBFaYgSrEqZRKD8In" target="_blank"><img src="https://asciinema.org/a/nVRUnFPaIBFaYgSrEqZRKD8In.svg" /></a>

<li>Compare nested JSON & YAML files (STYLISH formatter)</li>
<a href="https://asciinema.org/a/RpRXwb4sf2EFYKiwu0SeSz660" target="_blank"><img src="https://asciinema.org/a/RpRXwb4sf2EFYKiwu0SeSz660.svg" /></a>

<li>Compare nested JSON & YAML files (PLAIN formatter)</li>
<a href="https://asciinema.org/a/UKmAX37sZOvJPLH86IkE9TocE" target="_blank"><img src="https://asciinema.org/a/UKmAX37sZOvJPLH86IkE9TocE.svg" /></a>

<li>Compare nested JSON & YAML files (JSON formatter)</li>
<a href="https://asciinema.org/a/iukBgisAMLzQrGuZBYjGF8X8f" target="_blank"><img src="https://asciinema.org/a/iukBgisAMLzQrGuZBYjGF8X8f.svg" /></a>
</ol>