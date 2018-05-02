
# CUTC Challenge

This readme was written assuming a windows environment using PowerShell, but can easily be changed for Linux or MacOS.

## Team:

* Shivani Thaker

* Jude Tillekeratne

* Tejpal Sahota

# [Trello Board](https://trello.com/b/0YOTnxj2/deloitte-challenge)

# Tools used:
  
*  [MultiChain](https://www.multichain.com/)

*  [Savoir](https://github.com/DXMarkets/Savoir)

*  [Flask](http://flask.pocoo.org/)

# Install

1. Clone repo and install Flask + Savoir (if pip isn't working, make sure you've added python and pythonscripts to your path). Also move the contents of the chains folder to where your MultiChain was installed (\AppData\Roaming\MultiChain)

 ```powershell
 $ pip install flask
 $ pip install savoir
```

2. Navigate into the repo

3. Move the chains folder contents to AppData\Roaming\MultiChain

4. Add the launch scripts to your $profile.

5. Use the function launchNodes to start the 10 nodes (abc, corp1, corp2... corp9). Then use the function cutc to start the interactive explorer!

```powershell
$ launchNodes
$ cutc
```
6. If it is your first time running, issue assets by running this command. It may take some time to complete.:

```powershell
$ issueAssets
```

# Usage

To be updated

# Links

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
https://code-maven.com/using-templates-in-flask 