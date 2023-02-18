# Study-Bird-551
This is a Music Analysis Dashboard

## Dash description

The dashboard contains a sidebar and three main pages. We use python code to create this demo of Dash, and we also chose the appropriate color scheme for the chart based on our music theme. you can find code [here](./web-apps/dash.ipynb).

The sidebar is our category selector, which allow the user to select different analysis objects, including `Artist`, `Lyric` and `Audio`. In the three different main screens, we will show the user different dimensions of music analysis. We will present our music data in different chart types (bar charts, line charts, stack charts, etc.). We will show more than 2 charts per main page, and we will also add different sliders, filters, and so on in each main page depending on the data type and analysis content.

At the top of the main page, we have a slider that allows users to select the year they want to view, which we set to range from 2018 to 2022. Users select different years in the three main pages so as to view data visualization graphs for each year, for example, genres analysis, album popularity distribution of artists in 2018, lyric sentiment analysis, audio data analysis, etc. The specific chart type and content will be adjusted according to the actual data afterwards.

## Dash sketch
![sketch](sketch.png)
