import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.metrics.pairwise import cosine_similarity


def getRecommendations(test_item_name):
  
  file = pd.read_csv("Fashion-Dataset.csv")


  # print(file.shape)
  # print(file.head())

  # Considering: Title,Genre,Description,Director,Actors

  features = []

  # print(file["Genre"])
  for i in range(len(file["id"])):
    data = file["name"][i] + " " + file["size"][i] + " " + \
        file["brand"][i] + " " + file["description"][i]
    features.append(data)

  
  # print(features)
  # test_item_name = "Trench Coat"
  # test_item_name = trench coat.  Should recommend the jacket, but since there is no word 'coat' all similarities are 0.  Maybe could think about getting synonyms for words or similar words for better recommendations.
  # print("test item name", test_item_name)
  features.append(test_item_name)
  file = file.append({"name": test_item_name}, ignore_index=True)

  # print("file[name]", file["name"])

  file["features"] = features

  # print(file.head())

  tokenizer = Tokenizer()  # oov not helpful because there is no testing data
  # assign rankings to every word (1st priority:how many times word occurred, then left to right)
  tokenizer.fit_on_texts(file["features"])

  # str in matrix form (directly gives you pad sequences)
  sequences = tokenizer.texts_to_matrix(file["features"])

  # print(sequences.shape)
  # print(file["features"][0])

  # comparison of two things -- vector math gives great results - dont need to train model
  var = cosine_similarity(sequences)
  # print(var.shape)

  # want to get highest cosine similarity


  for i in range(len(file["id"])):
      item_title = file["name"][i]
      if file["name"][i] == test_item_name:
          item_id = i
          # print("i", i)
          break
  # print(item_id, file["name"][i])

  # print(var[movie_rank])

  similarities = []

  for i in range(len(var[item_id])):
      number = var[item_id][i]
      similarities.append(number)

  unsorted_similarities = similarities.copy()
  similarities.sort(reverse=True)

  # second highest similarity - excluding the similarity to itself
  # print("similarities list", similarities)
  # print(similarities[1])


  top_two = []
  for i in range(2):
      for i in range(len(similarities)):
          if unsorted_similarities[i] == similarities[len(top_two)+1]:
              item_name = file["name"][i]
              if (item_name not in top_two):
                  top_two.append(item_name)
                  # print("name", item_name)
                  break

  # print("Top Two Recommendations", top_two)
  return top_two

# getRecommendations("Trench coat")

  # get inputs from 4 people (dont influence what they pick)
  # 5 items for each person
  # have each person try (see if they get a good recommendation)
  # then do a flask server

  # suggest the top 5
  # figure out what helps someone make a decision on what someone buys next in the fashion industry

  # brand - people like similar or the same brand
  # if they buy shoes they might be shopping for something else (shirt or pants to go with it)
  # if a lot of people have it (its really popular ex. air forces)
  # color - complementary colors (ex. if they buy blue shoes, they might want a blue shirt as well)
  # similar use case items (if they buy basketball shoes, they might want basketball shorts)


  # 23rd thursday 8:30pm
  # 28th tuesday 9:00am
