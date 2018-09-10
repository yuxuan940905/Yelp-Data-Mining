Yelp Data mining

Data source: Yelp review
API: Yelp Fusion API, Google Cloud Natural Language API

Goals and Outline:

The goal of our project is to apply clustering methods to answer the following questions that we think worthwhile to explore:
1.	What neighborhoods in a city have the best cuisine selection according to the ratings in Yelp dataset?
2.	Does some neighborhoods in a city provide more expansive cuisines than the others?
2.	In the review of a restaurant, which kind of keywords are more likely to be mentioned?
    If a restaurant wants to improve its reviews, what should they focus on? 

This project report takes the example of reviews about "Pizza" in Boston. Three main components were done 
to solve the above questions.

1.Drawing of locations of all restaurants serves pizza in Boston shown in Google Map with Google API.

2.Geographical based clustering.
  Use K-means and GMM clustering algorithm to draw the clustering figure of restaurants. This shows the ratings and price distributions of all the restaurants.
  Silhouette Score of each clustering is calculated.

3.Classify the reviews via sentiment analysis.
  Make use of Google Cloud Natural Language API to divide review into positive and 
  negative part.
  
4.Find and plot the relationship between topics and keywords.
  Use LDA(Latent Dirichlet Allocation) to process the corpus, visualize the result by 
  PyLDAVis and Wordclouds.
  
  
Environment requirements:
-	Download and install Anaconda, install Jupyter via Anaconda.
-	install the following packages:
	lda
	gensim
	PyLDAVis
	wordcloud
	bokeh
	sklearn
	TextBlob
	google.cloud
	
Running instruction:

To run the whole application, you should:
1.	run main.ipynb in the root folder
	this will show 	
			a) the plotting of all the restaurants on Google Map
			b) the K-Means and GMM clustering result for rating and price, 4 plotting in total
			c) the reviews crwaled and saved to LDA/reviews.csv
			d) key words via wordclouds.
3.	run sentiment_analysis.ipynb, this will show
			a)	the result of sentiment Analysis of positive and negative revirew and the result of the review process. 
4.	go into the directory of this project and then cd LDA in terminal( cd [path]/LDA)
	and then use command: python LDA.py
	this will show
			a)	the topics extracted from the corpus, with top frequent keywords on its right
				when click on topics, the right panel will show how much the keywords count