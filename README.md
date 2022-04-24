# Spokesbrain

## How to make it work

0. Install required dependencies.
1. Download any _binary_ vector model from [RusVectores.org](https://rusvectores.org/ru/models/) (for example, [RusCorpora combined with russian Wikipedia articles](http://vectors.nlpl.eu/repository/20/220.zip) or [russian news articles](http://vectors.nlpl.eu/repository/20/184.zip)). 
2. Unpack it and place `.bin` file into `assets` folder.
3. Ensure the valid path in `src/models/guess.py:3` file.
4. Run `uvicorn main:server --reload`.
