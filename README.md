# StudyBird551
**Heroku:https://study-bird-dash-app.herokuapp.com**
StudyBird551 is a analysis visualization dashboard for billboard top100 hottest songs over year.

## Description
The dashboard contains a sidebar and three main pages. We use python code to create this demo of Dash, and we also chose the appropriate color scheme for the chart based on our music theme. you can find code [here](./web-apps/dash.ipynb).

   - Artists of the songs:
      - Popularity
      - seniority
      - dedication/activity
      - genres
   - Literature of the songs
      - Theme and topic
      - Physical features
      - Sentiments.
   - Musicality of the songs
      - Vibes
      - Rhythm
      - Musical scale.

The sidebar is our category selector, which allow the user to select different analysis objects, including `Artist`, `Lyric` and `Audio`. In the three different main screens, we will show the user different dimensions of music analysis. We will present our music data in different chart types (bar charts, line charts, stack charts, etc.). We will show more than 2 charts per main page, and we will also add different sliders, filters, and so on in each main page depending on the data type and analysis content.

At the top of the main page, we have a slider that allows users to select the year they want to view, which we set to range from 2018 to 2022. Users select different years in the three main pages so as to view data visualization graphs for each year, for example, genres analysis, album popularity distribution of artists in 2018, lyric sentiment analysis, audio data analysis, etc. The specific chart type and content will be adjusted according to the actual data afterwards.

## Visuals
![image](https://user-images.githubusercontent.com/43694291/219890638-220e6808-c7b9-4977-83fe-f6d8c900a5ea.png)
![image](https://user-images.githubusercontent.com/43694291/219890683-6afd4d37-b106-418f-80ff-954632d09c20.png)
![image](https://user-images.githubusercontent.com/43694291/219890719-92f0ac39-0b69-4dd1-a4ef-0af41b548e7d.png)

## Installation

Use the package manager [tbc](https://pip.pypa.io/en/stable/) to install StudyBird551.

```bash
pip install _
```

## Usage

```python
import tbd
<!-- 
# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena') -->
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

<!-- [MIT](https://choosealicense.com/licenses/mit/) -->





