## reddit-wipe
reddit-wipe is a command line reddit history scrubber. 

## Features
* Properly deletes comments by editing first and then deleting
* Delete user content matching a keyword or a regex pattern
* Configurable

## Examples

Only delete comments that contain the keyword `keyword`

`reddit-wipe --exclude=submissions --keyword=keyword`

## Usage
Firstly to install, just clone and run `pip install .`

Secondly because of reddit limitations you will need a **client id** and **client secret**.
To do so you will need to add reddit-wipe under your app preferences [here](https://www.reddit.com/prefs/apps).
Click *Create another app*, give it any name and any redirect url. 

The **client id** is the first string right under the app title
The **client secret** is further down next to *secret*

Now run reddit-wipe with your desired names and enter your username, password and the client id and secret
as it asks for them.

