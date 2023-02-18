## Section 1: Motivation and Purpose/rubric={reasoning:8,writing:2}

- Our role: Music data scientist
- Target audience: Music production company
Music is much easier to spread in today’s informative society than the age of vinyl records, listeners' appetite changes dramatic and fast too. It is sometimes difficult for music companies to grasp the trends in the music market to their detriment. We need a tool to monitor the characteristics of music preferred by listeners to help music companies analyze and predict market needs. Our product can provide the main features of hit songs with respect to audio, lyrics and artist through years. Administrators in music companies can determine the orientation and style of their artists and songs based on the information we offer.

## Section 2: Description of the data/rubric={reasoning:8,writing:2}

The dataset contains Top 100 hot  trending songs per year ranked by BillBoard during the last ten years, which are based on sales (physical and digital), radio play, and online streaming in the United States. In terms of those songs:
- a. we use spotify APIs to get artists information (name, followers, genres, albums and popularity, etc) to provide a comparison of artists, which includes a comparison of all artists as a whole as well as a comparison of each artist themselves in different dimensions. 
- b. We use web scraping on Musixmatch.com to get lyrics information (lyrics text) describe word frequency, word sentiment, song length, and the trend of the number of words with ranking. 
- c. We use web scraping on Youtube.com to down the top songs video and transfer them to waveform data (.mp3 of songs)analyze and visualize those features levels: High-level including instrumentation, key, chords, melody, harmony, rhythm, genre, mood; Mid-level: pitch, beat-related descriptors, note onsets, fluctuation patterns, MFCCs; Low- level: amplitude envelope, energy, spectral centroid, spectral flux, zero-crossing rate.

## Section 3: Research questions and usage scenarios
Yuhong is a music producer and recently received a tough task from CEO Nyx to prepare a new album for a new singer Tia. Tia just parachuted into the company and has no idea in music but is Nyx’s Nephew. At the same time, agent Mackey was asked to help Tia turn into a successful artist who has at least one million followers to make money from. Or Nyx will fire them.   
So Yuhong and Mackey came to us to get the tricks about how will songs and artists become successful in music markets and what features they own.   
Mackey sees the artist data visualization, he checks that the analyzing result through years in different dimensions, [filtered] their genres, [sorted] their activity and popularity, number of albums and overall album popularity, he easily [chooses] the artists genres he wants and see how their data compares.   
Yuhong [compares] the themes of the hot songs, [looks through] the word distribution of them to know the topic listeners care about. She [filters] the keys beats and rhythms of songs to adapt Tia’s narrow sound range. Also she [observes] the melody and mix characters to find the production orientation for Tia’s album.  
They both get what they want.
