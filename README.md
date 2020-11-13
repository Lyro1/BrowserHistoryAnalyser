# Browser History Analyser

A little security tool that checks your browsing history 
and indicates if you have visited website that might be
dangerous.

## Installation

Before using the tool, you must install some Python
packages. To do so, you need to have `pip` installed.
Just go in the project folder and type the following 
command:

> We recommand that you create a virtual env in which
> you will install those packages, to avoid any conflict
> with your current system installation.

```
pip install -r requirements.txt
```

You are now good to go!

## Configuration

Before you start a scan, we recommand that you take a look
at the configuration file, which is `src/config.json`.
This files holds all the configuration of the script, so
you might want to tune it to fit your needs. Here is a 
little details about all the fields:

- `limit-entries`: can be set to `"False"` or `"True"`, 
it will determine if you want to analyse only a certain
amount of website, or if you want to scan you entire web
history.

- `max-entries`: if `limit-entries` is set to `"True"`,
this variable will define how many history entries will
be analysed.

- `max-threads`: defines how many threads can be created
by the script. More threads will be faster, but will use
more ressources. Do not hesitate to test how much your
computer can handle.

- `sources`: holds all the sources that are used by 
**Browser History Analyser**. Currently, URLHaus and
VirusTotal are the two available sources. You can enable
or disable each source, and if needed, add an API key.

## How to use it

Once you installed all the packages and customized your
configuration, you can run the script like this:

```
python main.py
```

Note that **the script will only analyse the history
of browsers that are closed**.